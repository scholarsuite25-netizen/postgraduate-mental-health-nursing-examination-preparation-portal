/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { StorageService } from './services/storageService';
import { Question, AssessmentReport, AssessmentMode, IncorrectRecord } from './types';
import { shuffleArray } from './utils/shuffle';
import { DisclaimerBanner } from './components/DisclaimerBanner';
import { QuoteOfTheDay } from './components/QuoteOfTheDay';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { Dashboard } from './components/Dashboard';
import { ModulesView } from './components/ModulesView';
import { PracticeSession } from './components/PracticeSession';
import { MockExamSession } from './components/MockExamSession';
import { AssessmentResult } from './components/AssessmentResult';
import { MyReports } from './components/MyReports';
import { BookmarksAndReview } from './components/BookmarksAndReview';
import { QuestionBankManager } from './components/QuestionBankManager';
import { HelpAndPrivacy } from './components/HelpAndPrivacy';

export default function App() {
  const [activeTab, setActiveTab] = useState<string>('dashboard');
  const [candidateName, setCandidateName] = useState<string>('Postgraduate Candidate');
  const [questions, setQuestions] = useState<Question[]>([]);
  const [reports, setReports] = useState<AssessmentReport[]>([]);
  const [bookmarks, setBookmarks] = useState<string[]>([]);
  const [incorrectQueue, setIncorrectQueue] = useState<IncorrectRecord[]>([]);
  
  // Active session / view states
  const [activeSession, setActiveSession] = useState<{
    type: AssessmentMode;
    moduleName?: string;
    customQuestions?: Question[];
    customTitle?: string;
  } | null>(null);

  const [activeReport, setActiveReport] = useState<AssessmentReport | null>(null);

  const loadAppData = async () => {
    try {
      const qList = await StorageService.getQuestions();
      const rList = await StorageService.getReports();
      const bList = await StorageService.getBookmarks();
      const iList = await StorageService.getIncorrectQueue();
      const name = await StorageService.getCandidateName();

      setQuestions(qList);
      setReports(rList);
      setBookmarks(bList);
      setIncorrectQueue(iList);
      setCandidateName(name);
    } catch (err) {
      console.error('Failed to load application data', err);
    }
  };

  useEffect(() => {
    loadAppData();
  }, []);

  const handleStartPractice = (moduleName?: string) => {
    setActiveSession({
      type: 'practice',
      moduleName
    });
    setActiveTab('active-session');
  };

  const handleStartLearning = (moduleName?: string) => {
    setActiveSession({
      type: 'learning',
      moduleName
    });
    setActiveTab('active-session');
  };

  const handleStartMock = () => {
    setActiveSession({
      type: 'mock',
      customTitle: 'WAPCNM Mock Specialty Examination v1.0'
    });
    setActiveTab('active-session');
  };

  const handleStartTargetedPractice = (subset: Question[], title: string) => {
    setActiveSession({
      type: 'practice',
      customQuestions: subset,
      customTitle: title
    });
    setActiveTab('active-session');
  };

  const handleFinishAssessment = (report: AssessmentReport) => {
    setActiveReport(report);
    setActiveSession(null);
    setActiveTab('result');
    loadAppData();
  };

  const handleOpenReportById = async (reportId: string) => {
    const rep = await StorageService.getReportById(reportId);
    if (rep) {
      setActiveReport(rep);
      setActiveTab('result');
    }
  };

  // Filter and SHUFFLE questions for active session.
  // shuffleArray returns a new array each render of the active-session tab,
  // but React's useMemo (keyed on activeSession) keeps it stable within a session.
  const sessionQuestions = React.useMemo<Question[]>(() => {
    if (!activeSession) return [];
    let pool: Question[];
    if (activeSession.customQuestions) {
      pool = activeSession.customQuestions;
    } else if (activeSession.moduleName) {
      pool = questions.filter(q => q.module === activeSession.moduleName);
    } else if (activeSession.type === 'mock') {
      // WAPCNM Mock Examination: sample a realistic 70-question examination (5 from each of the 14 modules)
      const mockSet: Question[] = [];
      const moduleMap: Record<string, Question[]> = {};
      questions.forEach(q => {
        if (!moduleMap[q.module]) moduleMap[q.module] = [];
        moduleMap[q.module].push(q);
      });
      Object.keys(moduleMap).forEach(mod => {
        const shuffledMod = shuffleArray(moduleMap[mod]);
        mockSet.push(...shuffledMod.slice(0, 5));
      });
      if (mockSet.length < 70) {
        const remaining = questions.filter(q => !mockSet.some(m => m.id === q.id));
        mockSet.push(...shuffleArray(remaining).slice(0, 70 - mockSet.length));
      }
      pool = mockSet.slice(0, 70);
    } else {
      pool = [...questions];
    }
    // Shuffle so every new session presents questions in a fresh random order
    return shuffleArray(pool);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeSession, questions]);

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col font-sans">
      <DisclaimerBanner />
      <QuoteOfTheDay />
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        candidateName={candidateName}
        setCandidateName={setCandidateName}
        questionCount={questions.length}
        reportCount={reports.length}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'dashboard' && (
          <Dashboard
            candidateName={candidateName}
            questions={questions}
            reports={reports}
            bookmarks={bookmarks}
            incorrectQueue={incorrectQueue}
            onStartPractice={handleStartPractice}
            onStartLearning={handleStartLearning}
            onStartMock={handleStartMock}
            onNavigate={setActiveTab}
            onOpenReport={handleOpenReportById}
            onStartTargetedPractice={handleStartTargetedPractice}
          />
        )}

        {activeTab === 'modules' && (
          <ModulesView
            questions={questions}
            onStartPractice={handleStartPractice}
            onStartLearning={handleStartLearning}
            onStartMock={handleStartMock}
          />
        )}

        {activeTab === 'active-session' && activeSession?.type === 'mock' && (
          <MockExamSession
            questions={sessionQuestions.length > 0 ? sessionQuestions : questions}
            candidateName={candidateName}
            timeLimitMinutes={60}
            onFinish={handleFinishAssessment}
            onCancel={() => setActiveTab('dashboard')}
          />
        )}

        {activeTab === 'active-session' && activeSession?.type !== 'mock' && (
          <PracticeSession
            questions={sessionQuestions.length > 0 ? sessionQuestions : questions}
            mode={activeSession?.type || 'practice'}
            moduleName={activeSession?.moduleName || activeSession?.customTitle}
            candidateName={candidateName}
            onFinish={handleFinishAssessment}
            onCancel={() => setActiveTab('dashboard')}
          />
        )}

        {activeTab === 'result' && activeReport && (
          <AssessmentResult
            report={activeReport}
            onBackToDashboard={() => setActiveTab('dashboard')}
            onViewReports={() => setActiveTab('reports')}
          />
        )}

        {activeTab === 'reports' && (
          <MyReports
            reports={reports}
            onOpenReport={handleOpenReportById}
          />
        )}

        {activeTab === 'bookmarks' && (
          <BookmarksAndReview
            questions={questions}
            onStartTargetedPractice={handleStartTargetedPractice}
          />
        )}

        {activeTab === 'admin' && (
          <QuestionBankManager
            questions={questions}
            onQuestionsUpdated={loadAppData}
          />
        )}

        {activeTab === 'help' && (
          <HelpAndPrivacy />
        )}
      </main>

      <Footer onNavigate={setActiveTab} />
    </div>
  );
}
