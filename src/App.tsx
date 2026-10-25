/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { StorageService } from './services/storageService';
import { Question, AssessmentReport, AssessmentMode, IncorrectRecord } from './types';
import { CAOSCEReport, CAOSCEMode } from './types/clinicalExams';
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
import { HelpAndPrivacy } from './components/HelpAndPrivacy';
import { ClinicalExamCenter } from './components/clinical/ClinicalExamCenter';
import { CAOSCESession } from './components/clinical/CAOSCESession';
import { CAOSCEResultDossier } from './components/clinical/CAOSCEResultDossier';
import { NGNCaseSession } from './components/clinical/NGNCaseSession';
import { PsychopharmMathSession } from './components/clinical/PsychopharmMathSession';
import { NMCNAllSpecialtiesView } from './components/specialties/NMCNAllSpecialtiesView';

export default function App() {
  const [activeTab, setActiveTab] = useState<string>('dashboard');
  const [candidateName, setCandidateName] = useState<string>('Postgraduate Candidate');
  const [questions, setQuestions] = useState<Question[]>([]);
  const [reports, setReports] = useState<AssessmentReport[]>([]);
  const [caosceReports, setCaosceReports] = useState<CAOSCEReport[]>([]);
  const [bookmarks, setBookmarks] = useState<string[]>([]);
  const [incorrectQueue, setIncorrectQueue] = useState<IncorrectRecord[]>([]);

  // Active MCQ session / view states
  const [activeSession, setActiveSession] = useState<{
    type: AssessmentMode;
    moduleName?: string;
    customQuestions?: Question[];
    customTitle?: string;
  } | null>(null);

  const [activeReport, setActiveReport] = useState<AssessmentReport | null>(null);

  // Active Clinical Exam States
  const [activeCAOSCEConfig, setActiveCAOSCEConfig] = useState<{
    mode: CAOSCEMode;
    initialStationNumber?: number;
  } | null>(null);

  const [activeCAOSCEReport, setActiveCAOSCEReport] = useState<CAOSCEReport | null>(null);
  const [activeNGNCaseId, setActiveNGNCaseId] = useState<string | null>(null);
  const [activePsychopharmProblemId, setActivePsychopharmProblemId] = useState<string | null>(null);

  const loadAppData = async () => {
    try {
      const qList = await StorageService.getQuestions();
      const rList = await StorageService.getReports();
      const cList = await StorageService.getCAOSCEReports();
      const bList = await StorageService.getBookmarks();
      const iList = await StorageService.getIncorrectQueue();
      const name = await StorageService.getCandidateName();

      setQuestions(qList);
      setReports(rList);
      setCaosceReports(cList);
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
      moduleName,
    });
    setActiveTab('active-session');
  };

  const handleStartLearning = (moduleName?: string) => {
    setActiveSession({
      type: 'learning',
      moduleName,
    });
    setActiveTab('active-session');
  };

  const handleStartMock = () => {
    setActiveSession({
      type: 'mock',
      customTitle: 'WAPCNM Mock Specialty Examination v1.0',
    });
    setActiveTab('active-session');
  };

  const handleStartTargetedPractice = (subset: Question[], title: string) => {
    setActiveSession({
      type: 'practice',
      customQuestions: subset,
      customTitle: title,
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

  // --- Clinical Examination Handlers ---
  const handleStartCAOSCE = (mode: CAOSCEMode, specificStationNumber?: number) => {
    setActiveCAOSCEConfig({
      mode,
      initialStationNumber: specificStationNumber,
    });
    setActiveTab('caosce-session');
  };

  const handleFinishCAOSCE = async (report: CAOSCEReport) => {
    await StorageService.saveCAOSCEReport(report);
    setActiveCAOSCEReport(report);
    setActiveCAOSCEConfig(null);
    setActiveTab('caosce-result');
    loadAppData();
  };

  const handleOpenCAOSCEReportById = async (reportId: string) => {
    const rep = await StorageService.getCAOSCEReportById(reportId);
    if (rep) {
      setActiveCAOSCEReport(rep);
      setActiveTab('caosce-result');
    }
  };

  const handleStartNGNCase = (caseId: string) => {
    setActiveNGNCaseId(caseId);
    setActiveTab('ngn-session');
  };

  const handleStartPsychopharmMath = (problemId?: string) => {
    setActivePsychopharmProblemId(problemId || null);
    setActiveTab('math-session');
  };

  // Filter and SHUFFLE questions for active session
  const sessionQuestions = React.useMemo<Question[]>(() => {
    if (!activeSession) return [];
    let pool: Question[];
    if (activeSession.customQuestions) {
      pool = activeSession.customQuestions;
    } else if (activeSession.moduleName) {
      pool = questions.filter((q) => q.module === activeSession.moduleName);
    } else if (activeSession.type === 'mock') {
      const mockSet: Question[] = [];
      const moduleMap: Record<string, Question[]> = {};
      questions.forEach((q) => {
        if (!moduleMap[q.module]) moduleMap[q.module] = [];
        moduleMap[q.module].push(q);
      });
      Object.keys(moduleMap).forEach((mod) => {
        const shuffledMod = shuffleArray(moduleMap[mod]);
        mockSet.push(...shuffledMod.slice(0, 5));
      });
      if (mockSet.length < 70) {
        const remaining = questions.filter((q) => !mockSet.some((m) => m.id === q.id));
        mockSet.push(...shuffleArray(remaining).slice(0, 70 - mockSet.length));
      }
      pool = mockSet.slice(0, 70);
    } else {
      pool = [...questions];
    }
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
        caosceCount={caosceReports.length}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'dashboard' && (
          <Dashboard
            candidateName={candidateName}
            questions={questions}
            reports={reports}
            bookmarks={bookmarks}
            incorrectQueue={incorrectQueue}
            caosceReports={caosceReports}
            onStartPractice={handleStartPractice}
            onStartLearning={handleStartLearning}
            onStartMock={handleStartMock}
            onNavigate={setActiveTab}
            onOpenReport={handleOpenReportById}
            onStartTargetedPractice={handleStartTargetedPractice}
          />
        )}

        {/* Clinical Examination Suites Hub */}
        {activeTab === 'clinical-exams' && (
          <ClinicalExamCenter
            candidateName={candidateName}
            caosceReports={caosceReports}
            onStartCAOSCE={handleStartCAOSCE}
            onStartNGNCase={handleStartNGNCase}
            onStartPsychopharmMath={handleStartPsychopharmMath}
            onOpenCAOSCEReport={handleOpenCAOSCEReportById}
          />
        )}

        {/* Active CAOSCE Examination Session */}
        {activeTab === 'caosce-session' && (
          <CAOSCESession
            candidateName={candidateName}
            mode={activeCAOSCEConfig?.mode || 'strict-exam'}
            initialStationNumber={activeCAOSCEConfig?.initialStationNumber}
            onFinish={handleFinishCAOSCE}
            onCancel={() => setActiveTab('clinical-exams')}
          />
        )}

        {/* CAOSCE Official Result Dossier */}
        {activeTab === 'caosce-result' && activeCAOSCEReport && (
          <CAOSCEResultDossier
            report={activeCAOSCEReport}
            onBackToCenter={() => setActiveTab('clinical-exams')}
            onRetakeCircuit={() => handleStartCAOSCE('strict-exam')}
          />
        )}

        {/* NGN Clinical Judgment Case Session */}
        {activeTab === 'ngn-session' && (
          <NGNCaseSession
            candidateName={candidateName}
            initialCaseId={activeNGNCaseId || undefined}
            onBackToCenter={() => setActiveTab('clinical-exams')}
          />
        )}

        {/* Psychopharmacology Math & Titration Session */}
        {activeTab === 'math-session' && (
          <PsychopharmMathSession
            candidateName={candidateName}
            initialProblemId={activePsychopharmProblemId || undefined}
            onBackToCenter={() => setActiveTab('clinical-exams')}
          />
        )}

        {/* NMCN Statutory Specialisations Suite (Self-Contained View) */}
        {activeTab === 'specialties' && (
          <NMCNAllSpecialtiesView
            candidateName={candidateName}
            onNavigateHome={() => setActiveTab('dashboard')}
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
          <MyReports reports={reports} onOpenReport={handleOpenReportById} />
        )}

        {activeTab === 'bookmarks' && (
          <BookmarksAndReview
            questions={questions}
            onStartTargetedPractice={handleStartTargetedPractice}
          />
        )}

        {activeTab === 'help' && <HelpAndPrivacy />}
      </main>

      <Footer onNavigate={setActiveTab} />
    </div>
  );
}
