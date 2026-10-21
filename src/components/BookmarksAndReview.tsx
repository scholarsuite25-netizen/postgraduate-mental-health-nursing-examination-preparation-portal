/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { Bookmark, AlertCircle, Trash2, Play, CheckCircle2, BookOpen } from 'lucide-react';
import { Question, IncorrectRecord } from '../types';
import { StorageService } from '../services/storageService';

interface BookmarksAndReviewProps {
  questions: Question[];
  onStartTargetedPractice: (subset: Question[], title: string) => void;
}

export const BookmarksAndReview: React.FC<BookmarksAndReviewProps> = ({
  questions,
  onStartTargetedPractice
}) => {
  const [activeSubTab, setActiveSubTab] = useState<'bookmarks' | 'incorrect'>('bookmarks');
  const [bookmarkIds, setBookmarkIds] = useState<string[]>([]);
  const [incorrectQueue, setIncorrectQueue] = useState<IncorrectRecord[]>([]);

  const loadData = async () => {
    const bms = await StorageService.getBookmarks();
    const inc = await StorageService.getIncorrectQueue();
    setBookmarkIds(bms);
    setIncorrectQueue(inc);
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleRemoveBookmark = async (qId: string) => {
    await StorageService.toggleBookmark(qId);
    loadData();
  };

  const handleRemoveIncorrect = async (qId: string) => {
    await StorageService.removeFromIncorrectQueue(qId);
    loadData();
  };

  const bookmarkedQuestions = questions.filter(q => bookmarkIds.includes(q.id));
  const incorrectQuestions = questions.filter(q => incorrectQueue.some(i => i.questionId === q.id));

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Header & Tabs */}
      <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
            Bookmarks & Targeted Revision
          </h2>
          <p className="text-slate-500 dark:text-slate-400 text-xs sm:text-sm mt-1">
            Review your saved questions and strengthen weak areas from previous assessment attempts.
          </p>
        </div>

        <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-800 p-1 rounded-xl">
          <button
            onClick={() => setActiveSubTab('bookmarks')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              activeSubTab === 'bookmarks'
                ? 'bg-white dark:bg-slate-900 text-slate-900 dark:text-white shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
            }`}
          >
            <Bookmark className="w-4 h-4 text-amber-500 fill-amber-500" />
            <span>Bookmarks ({bookmarkedQuestions.length})</span>
          </button>
          <button
            onClick={() => setActiveSubTab('incorrect')}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              activeSubTab === 'incorrect'
                ? 'bg-white dark:bg-slate-900 text-slate-900 dark:text-white shadow-xs'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
            }`}
          >
            <AlertCircle className="w-4 h-4 text-rose-500" />
            <span>Incorrect Queue ({incorrectQuestions.length})</span>
          </button>
        </div>
      </div>

      {/* Bookmarks Section */}
      {activeSubTab === 'bookmarks' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-bold text-slate-900 dark:text-white text-base">
              Bookmarked Questions
            </h3>
            {bookmarkedQuestions.length > 0 && (
              <button
                onClick={() => onStartTargetedPractice(bookmarkedQuestions, 'Bookmarked Questions Practice')}
                className="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-md cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Practice Bookmarks</span>
              </button>
            )}
          </div>

          {bookmarkedQuestions.length === 0 ? (
            <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-12 text-center space-y-3">
              <Bookmark className="w-12 h-12 text-amber-500 mx-auto opacity-80" />
              <h4 className="text-base font-bold text-slate-800 dark:text-slate-200">No Bookmarked Questions Yet</h4>
              <p className="text-xs text-slate-500 dark:text-slate-400 max-w-sm mx-auto">
                Click the bookmark icon during practice or mock examinations to save questions for later review.
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              {bookmarkedQuestions.map((q, idx) => (
                <div key={q.id} className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold px-2 py-0.5 rounded bg-amber-50 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300">
                      {q.module}
                    </span>
                    <button
                      onClick={() => handleRemoveBookmark(q.id)}
                      className="text-slate-400 hover:text-rose-600 transition-colors p-1"
                      title="Remove bookmark"
                    >
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                  <h4 className="font-bold text-slate-900 dark:text-white text-base">
                    {q.questionText}
                  </h4>
                  <div className="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-700 text-xs text-slate-700 dark:text-slate-300">
                    <strong>Correct Answer ({q.correctAnswer}):</strong> {q.options.find(o => o.id === q.correctAnswer)?.text}
                    <p className="mt-1 text-slate-500">{q.explanation}</p>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Incorrect Queue Section */}
      {activeSubTab === 'incorrect' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-bold text-slate-900 dark:text-white text-base">
              Incorrect Answers Review Queue
            </h3>
            {incorrectQuestions.length > 0 && (
              <button
                onClick={() => onStartTargetedPractice(incorrectQuestions, 'Targeted Revision: Missed Questions')}
                className="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-md cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Practice Missed Questions</span>
              </button>
            )}
          </div>

          {incorrectQuestions.length === 0 ? (
            <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-12 text-center space-y-3">
              <CheckCircle2 className="w-12 h-12 text-emerald-500 mx-auto opacity-80" />
              <h4 className="text-base font-bold text-slate-800 dark:text-slate-200">No Missed Questions in Queue</h4>
              <p className="text-xs text-slate-500 dark:text-slate-400 max-w-sm mx-auto">
                Fantastic work! Any questions answered incorrectly during assessments will automatically appear here for targeted revision.
              </p>
            </div>
          ) : (
            <div className="space-y-4">
              {incorrectQuestions.map((q) => {
                const record = incorrectQueue.find(i => i.questionId === q.id);
                return (
                  <div key={q.id} className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-3">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold px-2 py-0.5 rounded bg-rose-50 dark:bg-rose-950/60 text-rose-700 dark:text-rose-300">
                          Failed {record?.timesFailed || 1} time(s)
                        </span>
                        <span className="text-xs text-slate-400">{q.module}</span>
                      </div>
                      <button
                        onClick={() => handleRemoveIncorrect(q.id)}
                        className="text-slate-400 hover:text-emerald-600 transition-colors p-1 text-xs font-semibold flex items-center gap-1"
                        title="Mark as mastered and remove"
                      >
                        <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                        <span>Mastered</span>
                      </button>
                    </div>
                    <h4 className="font-bold text-slate-900 dark:text-white text-base">
                      {q.questionText}
                    </h4>
                    <div className="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-700 text-xs text-slate-700 dark:text-slate-300">
                      <strong>Correct Answer ({q.correctAnswer}):</strong> {q.options.find(o => o.id === q.correctAnswer)?.text}
                      <p className="mt-1 text-slate-500">{q.explanation}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
