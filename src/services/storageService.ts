import { AssessmentReport, Question, IncorrectRecord } from '../types';
import { getAllQuestions, invalidateQuestionCache } from '../data/questionBank';

const DB_NAME = 'WAPCNM_MHN_DB_V2';
const DB_VERSION = 2;
const STORE_REPORTS = 'reports';
const STORE_QUESTIONS = 'questions';
const STORE_BOOKMARKS = 'bookmarks';
const STORE_INCORRECT = 'incorrect_queue';
const STORE_SETTINGS = 'settings';

export class StorageService {
  private static dbPromise: Promise<IDBDatabase> | null = null;
  private static memoryCache: {
    questions?: Question[];
    reports?: AssessmentReport[];
    bookmarks?: string[];
    incorrect?: IncorrectRecord[];
    name?: string;
  } = {};

  private static getDB(): Promise<IDBDatabase> {
    if (!this.dbPromise) {
      this.dbPromise = new Promise((resolve) => {
        if (typeof window === 'undefined' || !window.indexedDB) {
          resolve(null as any);
          return;
        }

        try {
          const request = indexedDB.open(DB_NAME, DB_VERSION);

          request.onerror = () => {
            console.warn('IndexedDB error, falling back to memory/session storage.');
            resolve(null as any);
          };

          request.onsuccess = () => {
            resolve(request.result);
          };

          request.onupgradeneeded = (event) => {
            const db = (event.target as IDBOpenDBRequest).result;
            try {
              if (!db.objectStoreNames.contains(STORE_REPORTS)) {
                db.createObjectStore(STORE_REPORTS, { keyPath: 'id' });
              }
              if (!db.objectStoreNames.contains(STORE_QUESTIONS)) {
                db.createObjectStore(STORE_QUESTIONS, { keyPath: 'id' });
              }
              if (!db.objectStoreNames.contains(STORE_BOOKMARKS)) {
                db.createObjectStore(STORE_BOOKMARKS, { keyPath: 'questionId' });
              }
              if (!db.objectStoreNames.contains(STORE_INCORRECT)) {
                db.createObjectStore(STORE_INCORRECT, { keyPath: 'questionId' });
              }
              if (!db.objectStoreNames.contains(STORE_SETTINGS)) {
                db.createObjectStore(STORE_SETTINGS, { keyPath: 'key' });
              }
            } catch (e) {
              console.error('Error upgrading IDB store:', e);
            }
          };
        } catch (e) {
          resolve(null as any);
        }
      });
    }
    return this.dbPromise;
  }

  // --- Questions ---
  public static async getQuestions(): Promise<Question[]> {
    if (this.memoryCache.questions && this.memoryCache.questions.length > 0) {
      return this.memoryCache.questions;
    }

    try {
      const db = await this.getDB();
      if (!db) {
        const fallback = getAllQuestions();
        this.memoryCache.questions = fallback;
        return fallback;
      }

      return new Promise((resolve) => {
        const transaction = db.transaction(STORE_QUESTIONS, 'readonly');
        const store = transaction.objectStore(STORE_QUESTIONS);
        const request = store.getAll();

        request.onsuccess = async () => {
          const questions = request.result as Question[];
          if (!questions || questions.length < 50) {
            const fullBank = getAllQuestions();
            // Save in background without blocking
            this.saveQuestionsInBackground(fullBank);
            this.memoryCache.questions = fullBank;
            resolve(fullBank);
          } else {
            this.memoryCache.questions = questions;
            resolve(questions);
          }
        };
        request.onerror = () => {
          const fallback = getAllQuestions();
          this.memoryCache.questions = fallback;
          resolve(fallback);
        };
      });
    } catch {
      const fallback = getAllQuestions();
      this.memoryCache.questions = fallback;
      return fallback;
    }
  }

  private static async saveQuestionsInBackground(questions: Question[]): Promise<void> {
    try {
      const db = await this.getDB();
      if (!db) return;
      const transaction = db.transaction(STORE_QUESTIONS, 'readwrite');
      const store = transaction.objectStore(STORE_QUESTIONS);
      // Put in chunks to avoid blocking
      questions.forEach(q => store.put(q));
    } catch (e) {
      console.warn('Background question save failed:', e);
    }
  }

  public static async addCustomQuestion(question: Question): Promise<void> {
    if (this.memoryCache.questions) {
      this.memoryCache.questions.unshift(question);
    }
    // Invalidate the static question bank cache so getAllQuestions() picks up custom questions
    invalidateQuestionCache();
    try {
      const db = await this.getDB();
      if (!db) return;
      const transaction = db.transaction(STORE_QUESTIONS, 'readwrite');
      const store = transaction.objectStore(STORE_QUESTIONS);
      store.put(question);
    } catch (e) {
      console.warn('Failed to save custom question:', e);
    }
  }

  // --- Reports ---
  public static async saveReport(report: AssessmentReport): Promise<void> {
    if (!this.memoryCache.reports) {
      this.memoryCache.reports = [];
    }
    this.memoryCache.reports.unshift(report);

    try {
      const db = await this.getDB();
      if (!db) {
        localStorage.setItem('wapcnm_fallback_reports', JSON.stringify(this.memoryCache.reports));
        return;
      }
      return new Promise((resolve, reject) => {
        const transaction = db.transaction(STORE_REPORTS, 'readwrite');
        const store = transaction.objectStore(STORE_REPORTS);
        const request = store.put(report);

        request.onsuccess = () => resolve();
        request.onerror = () => {
          // Fallback to localStorage if IDB fails
          try {
            localStorage.setItem('wapcnm_fallback_reports', JSON.stringify(this.memoryCache.reports));
            resolve();
          } catch (err) {
            reject(new Error('Failed to save report to browser storage.'));
          }
        };
      });
    } catch (err) {
      try {
        localStorage.setItem('wapcnm_fallback_reports', JSON.stringify(this.memoryCache.reports));
      } catch {}
    }
  }

  public static async getReports(): Promise<AssessmentReport[]> {
    if (this.memoryCache.reports && this.memoryCache.reports.length > 0) {
      return this.memoryCache.reports;
    }

    try {
      const db = await this.getDB();
      if (!db) {
        const saved = localStorage.getItem('wapcnm_fallback_reports');
        const parsed = saved ? JSON.parse(saved) : [];
        this.memoryCache.reports = parsed;
        return parsed;
      }

      return new Promise((resolve) => {
        const transaction = db.transaction(STORE_REPORTS, 'readonly');
        const store = transaction.objectStore(STORE_REPORTS);
        const request = store.getAll();

        request.onsuccess = () => {
          let reports = (request.result as AssessmentReport[]) || [];
          if (reports.length === 0) {
            const saved = localStorage.getItem('wapcnm_fallback_reports');
            if (saved) {
              reports = JSON.parse(saved);
            }
          }
          reports.sort((a, b) => b.dateTimestamp - a.dateTimestamp);
          this.memoryCache.reports = reports;
          resolve(reports);
        };
        request.onerror = () => {
          const saved = localStorage.getItem('wapcnm_fallback_reports');
          const parsed = saved ? JSON.parse(saved) : [];
          this.memoryCache.reports = parsed;
          resolve(parsed);
        };
      });
    } catch {
      return [];
    }
  }

  public static async getReportById(id: string): Promise<AssessmentReport | null> {
    const reports = await this.getReports();
    return reports.find(r => r.id === id) || null;
  }

  // --- Bookmarks ---
  public static async getBookmarks(): Promise<string[]> {
    if (this.memoryCache.bookmarks) return this.memoryCache.bookmarks;

    try {
      const db = await this.getDB();
      if (!db) {
        const saved = localStorage.getItem('wapcnm_fallback_bookmarks');
        const parsed = saved ? JSON.parse(saved) : [];
        this.memoryCache.bookmarks = parsed;
        return parsed;
      }

      return new Promise((resolve) => {
        const transaction = db.transaction(STORE_BOOKMARKS, 'readonly');
        const store = transaction.objectStore(STORE_BOOKMARKS);
        const request = store.getAll();

        request.onsuccess = () => {
          const items = (request.result as { questionId: string }[]) || [];
          const ids = items.map(i => i.questionId);
          this.memoryCache.bookmarks = ids;
          resolve(ids);
        };
        request.onerror = () => resolve([]);
      });
    } catch {
      return [];
    }
  }

  public static async toggleBookmark(questionId: string): Promise<boolean> {
    const bookmarks = await this.getBookmarks();
    const isBookmarked = bookmarks.includes(questionId);
    const updated = isBookmarked ? bookmarks.filter(id => id !== questionId) : [...bookmarks, questionId];
    this.memoryCache.bookmarks = updated;

    try {
      localStorage.setItem('wapcnm_fallback_bookmarks', JSON.stringify(updated));
      const db = await this.getDB();
      if (db) {
        const transaction = db.transaction(STORE_BOOKMARKS, 'readwrite');
        const store = transaction.objectStore(STORE_BOOKMARKS);
        if (isBookmarked) {
          store.delete(questionId);
        } else {
          store.put({ questionId, dateAdded: Date.now() });
        }
      }
    } catch (e) {
      console.warn('Bookmark update warning:', e);
    }

    return !isBookmarked;
  }

  // --- Incorrect Answers Queue ---
  public static async getIncorrectQueue(): Promise<IncorrectRecord[]> {
    if (this.memoryCache.incorrect) return this.memoryCache.incorrect;

    try {
      const db = await this.getDB();
      if (!db) {
        const saved = localStorage.getItem('wapcnm_fallback_incorrect');
        const parsed = saved ? JSON.parse(saved) : [];
        this.memoryCache.incorrect = parsed;
        return parsed;
      }

      return new Promise((resolve) => {
        const transaction = db.transaction(STORE_INCORRECT, 'readonly');
        const store = transaction.objectStore(STORE_INCORRECT);
        const request = store.getAll();

        request.onsuccess = () => {
          const items = (request.result as IncorrectRecord[]) || [];
          this.memoryCache.incorrect = items;
          resolve(items);
        };
        request.onerror = () => resolve([]);
      });
    } catch {
      return [];
    }
  }

  public static async recordIncorrectAnswer(questionId: string, module: string, selected: 'A' | 'B' | 'C' | 'D' | null): Promise<void> {
    try {
      const queue = await this.getIncorrectQueue();
      const existing = queue.find(q => q.questionId === questionId);
      const updated = queue.filter(q => q.questionId !== questionId);

      const record: IncorrectRecord = {
        questionId,
        module,
        lastAttemptDate: Date.now(),
        lastSelected: selected,
        timesFailed: existing ? existing.timesFailed + 1 : 1
      };

      updated.unshift(record);
      this.memoryCache.incorrect = updated;
      localStorage.setItem('wapcnm_fallback_incorrect', JSON.stringify(updated));

      const db = await this.getDB();
      if (db) {
        const transaction = db.transaction(STORE_INCORRECT, 'readwrite');
        const store = transaction.objectStore(STORE_INCORRECT);
        store.put(record);
      }
    } catch (err) {
      console.warn('Failed to record incorrect answer', err);
    }
  }

  public static async removeFromIncorrectQueue(questionId: string): Promise<void> {
    try {
      const queue = await this.getIncorrectQueue();
      const updated = queue.filter(q => q.questionId !== questionId);
      this.memoryCache.incorrect = updated;
      localStorage.setItem('wapcnm_fallback_incorrect', JSON.stringify(updated));

      const db = await this.getDB();
      if (db) {
        const transaction = db.transaction(STORE_INCORRECT, 'readwrite');
        const store = transaction.objectStore(STORE_INCORRECT);
        store.delete(questionId);
      }
    } catch (err) {
      console.warn('Failed to remove from incorrect queue', err);
    }
  }

  // --- Settings ---
  public static async getCandidateName(): Promise<string> {
    if (this.memoryCache.name) return this.memoryCache.name;
    try {
      const saved = localStorage.getItem('wapcnm_candidate_name');
      if (saved) {
        this.memoryCache.name = saved;
        return saved;
      }
      const db = await this.getDB();
      if (!db) return 'Postgraduate Candidate';

      return new Promise((resolve) => {
        const transaction = db.transaction(STORE_SETTINGS, 'readonly');
        const store = transaction.objectStore(STORE_SETTINGS);
        const request = store.get('candidateName');

        request.onsuccess = () => {
          const name = request.result?.value || 'Postgraduate Candidate';
          this.memoryCache.name = name;
          resolve(name);
        };
        request.onerror = () => resolve('Postgraduate Candidate');
      });
    } catch {
      return 'Postgraduate Candidate';
    }
  }

  public static async setCandidateName(name: string): Promise<void> {
    this.memoryCache.name = name;
    try {
      localStorage.setItem('wapcnm_candidate_name', name);
      const db = await this.getDB();
      if (db) {
        const transaction = db.transaction(STORE_SETTINGS, 'readwrite');
        const store = transaction.objectStore(STORE_SETTINGS);
        store.put({ key: 'candidateName', value: name });
      }
    } catch (err) {
      console.warn('Failed to save candidate name', err);
    }
  }
}
