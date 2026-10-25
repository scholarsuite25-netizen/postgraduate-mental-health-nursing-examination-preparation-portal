/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useCallback } from 'react';
import { 
  Clock, 
  ChevronLeft, 
  ChevronRight, 
  Send, 
  Bookmark, 
  AlertTriangle, 
  ShieldCheck,
  Sparkles,
  CheckCircle2,
  XCircle,
  HelpCircle
} from 'lucide-react';
import { Question, AssessmentReport } from '../types';
import { StorageService } from '../services/storageService';

interface MockExamSessionProps {
  questions: Question[];
  candidateName: string;
  timeLimitMinutes?: number;
  onFinish: (report: AssessmentReport) => void;
  onCancel: () => void;
}

export const MockExamSession: React.FC<MockExamSessionProps> = ({
  questions,
  candidateName,
  timeLimitMinutes = 60,
  onFinish,
  onCancel
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, 'A' | 'B' | 'C' | 'D' | null>>({});
  const [bookmarks, setBookmarks] = useState<string[]>([]);
  const [timeLeftSeconds, setTimeLeftSeconds] = useState(timeLimitMinutes * 60);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [confirmSubmitOpen, setConfirmSubmitOpen] = useState(false);
  const [autoSubmitted, setAutoSubmitted] = useState(false);
  const [tutorialSupportMode, setTutorialSupportMode] = useState<boolean>(true);

  const performSubmission = useCallback(async () => {
    if (isSubmitting || autoSubmitted) return;
    setIsSubmitting(true);
    setAutoSubmitted(true);

    let correctCount = 0;
    let incorrectCount = 0;
    let unansweredCount = 0;

    questions.forEach(q => {
      const ans = selectedAnswers[q.id];
      if (!ans) {
        unansweredCount++;
        StorageService.recordIncorrectAnswer(q.id, q.module, null);
      } else if (ans === q.correctAnswer) {
        correctCount++;
        StorageService.removeFromIncorrectQueue(q.id);
      } else {
        incorrectCount++;
        StorageService.recordIncorrectAnswer(q.id, q.module, ans);
      }
    });

    const totalQuestions = questions.length;
    const answeredCount = totalQuestions - unansweredCount;
    // Unrounded score formula: (Correct / Total Scored) * 100
    const percentage = totalQuestions > 0 ? (correctCount / totalQuestions) * 100 : 0;
    const passMark = 70.0;
    const status = percentage >= passMark ? 'PASS' : 'FAIL';

    const reportId = `WAPCNM-MOCK-${Math.random().toString(36).substring(2, 9).toUpperCase()}`;
    const timeTaken = (timeLimitMinutes * 60) - timeLeftSeconds;

    const report: AssessmentReport = {
      id: reportId,
      candidateName,
      assessmentTitle: 'WAPCNM Mock Specialty Examination v1.0',
      mode: 'mock',
      dateTimestamp: Date.now(),
      totalQuestions,
      answeredCount,
      correctCount,
      incorrectCount,
      unansweredCount,
      percentage,
      passMark,
      status,
      timeTakenSeconds: timeTaken > 0 ? timeTaken : 1,
      questionsSnapshot: [...questions],
      candidateAnswers: { ...selectedAnswers }
    };

    try {
      await StorageService.saveReport(report);
      onFinish(report);
    } catch (err: any) {
      alert(err.message || 'Failed to save mock examination report.');
      setIsSubmitting(false);
    }
  }, [isSubmitting, autoSubmitted, questions, selectedAnswers, candidateName, timeLimitMinutes, timeLeftSeconds, onFinish]);

  // Timer countdown
  useEffect(() => {
    const timer = setInterval(() => {
      setTimeLeftSeconds(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          performSubmission();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [performSubmission]);

  useEffect(() => {
    StorageService.getBookmarks().then(setBookmarks).catch(() => {});
  }, []);

  const currentQ = questions[currentIndex];
  const selectedOpt = selectedAnswers[currentQ?.id] || null;
  const isAnswerCorrect = selectedOpt === currentQ?.correctAnswer;

  const handleSelectOption = (optId: 'A' | 'B' | 'C' | 'D') => {
    setSelectedAnswers(prev => ({
      ...prev,
      [currentQ.id]: optId
    }));

    if (optId !== currentQ.correctAnswer) {
      StorageService.recordIncorrectAnswer(currentQ.id, currentQ.module, optId);
    } else {
      StorageService.removeFromIncorrectQueue(currentQ.id);
    }
  };

  const handleRetryOption = () => {
    setSelectedAnswers(prev => {
      const next = { ...prev };
      delete next[currentQ.id];
      return next;
    });
  };

  const handleToggleBookmark = async () => {
    await StorageService.toggleBookmark(currentQ.id);
    const updated = await StorageService.getBookmarks();
    setBookmarks(updated);
  };

  const formatTimer = (totalSecs: number) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  const unansweredCount = questions.filter(q => !selectedAnswers[q.id]).length;
  const isBookmarked = bookmarks.includes(currentQ?.id);

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Mock Exam Top Header */}
      <div className="bg-slate-900 text-white p-5 rounded-2xl shadow-lg flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 text-xs font-semibold text-emerald-400 mb-1">
            <ShieldCheck className="w-4 h-4" />
            <span>WAPCNM Official Mock Examination Protocol</span>
          </div>
          <h2 className="text-lg font-bold">
            Postgraduate Mental Health Nursing Mock Assessment
          </h2>
        </div>

        <div className="flex flex-wrap items-center gap-3">
          <button
            onClick={() => setTutorialSupportMode(prev => !prev)}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer ${
              tutorialSupportMode
                ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-400/50 shadow-sm ring-1 ring-emerald-400/50'
                : 'bg-slate-800 text-slate-400 border border-slate-700 hover:text-white'
            }`}
            title="Toggle immediate answer validation and explanations"
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>Tutorial Support: {tutorialSupportMode ? 'ACTIVE (Instant Feedback)' : 'OFF (Silent Exam)'}</span>
          </button>

          <div className={`flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold shadow-xs ${
            timeLeftSeconds < 300 
              ? 'bg-rose-600 text-white animate-pulse ring-2 ring-rose-400' 
              : 'bg-slate-800 text-emerald-400 border border-slate-700'
          }`}>
            <Clock className="w-4 h-4" />
            <span>{formatTimer(timeLeftSeconds)} {timeLeftSeconds < 300 ? '(URGENT)' : ''}</span>
          </div>

          <button
            onClick={() => setConfirmSubmitOpen(true)}
            className="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-2 rounded-xl text-xs sm:text-sm shadow-md cursor-pointer"
          >
            Submit Exam
          </button>
        </div>
      </div>

      {/* Under 5 minutes warning banner */}
      {timeLeftSeconds < 300 && (
        <div className="bg-rose-50 dark:bg-rose-950/60 border border-rose-300 dark:border-rose-800 text-rose-800 dark:text-rose-200 px-4 py-3 rounded-xl text-xs font-semibold flex items-center gap-2 animate-bounce">
          <AlertTriangle className="w-4 h-4 text-rose-600 shrink-0" />
          <span>Warning: Less than 5 minutes remaining! Review your answers and submit before time expires.</span>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Main Question Area */}
        <div className="lg:col-span-3 space-y-6">
          <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-xs space-y-6">
            <div className="flex items-start justify-between gap-4">
              <div>
                <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                  Question {currentIndex + 1} of {questions.length} • {currentQ.module}
                </span>
                <h3 className="text-lg sm:text-xl font-bold text-slate-900 dark:text-white mt-1 leading-relaxed">
                  {currentQ.questionText}
                </h3>
              </div>
              <button
                onClick={handleToggleBookmark}
                className={`p-2 rounded-lg border transition-colors ${
                  isBookmarked 
                    ? 'bg-amber-50 border-amber-300 text-amber-700' 
                    : 'bg-slate-50 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-600'
                }`}
              >
                <Bookmark className={`w-4 h-4 ${isBookmarked ? 'fill-amber-500 text-amber-500' : ''}`} />
              </button>
            </div>

            {/* Options */}
            <div className="space-y-3">
              {currentQ.options.map((opt) => {
                const isSelected = selectedOpt === opt.id;
                const isCorrectOption = opt.id === currentQ.correctAnswer;

                let btnStyle = "border-slate-200 dark:border-slate-800 hover:border-emerald-500/50 bg-white dark:bg-slate-800/40 text-slate-800 dark:text-slate-200";

                if (tutorialSupportMode && selectedOpt !== null) {
                  if (isCorrectOption) {
                    btnStyle = "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 ring-2 ring-emerald-500 shadow-xs";
                  } else if (isSelected && !isCorrectOption) {
                    btnStyle = "border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 ring-2 ring-rose-500 shadow-xs";
                  } else {
                    btnStyle = "border-slate-200 dark:border-slate-800/60 bg-slate-50/50 dark:bg-slate-900/40 text-slate-500 dark:text-slate-400 opacity-70";
                  }
                } else if (isSelected) {
                  btnStyle = "border-emerald-600 bg-emerald-50/50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 ring-1 ring-emerald-600";
                }

                return (
                  <button
                    key={opt.id}
                    onClick={() => handleSelectOption(opt.id)}
                    className={`w-full text-left p-4 rounded-xl border transition-all flex items-start gap-3.5 cursor-pointer ${btnStyle}`}
                  >
                    <span className={`w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
                      tutorialSupportMode && selectedOpt !== null && isCorrectOption
                        ? 'bg-emerald-600 text-white'
                        : tutorialSupportMode && selectedOpt !== null && isSelected && !isCorrectOption
                        ? 'bg-rose-600 text-white'
                        : isSelected
                        ? 'bg-emerald-600 text-white'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                    }`}>
                      {opt.id}
                    </span>
                    <span className="text-sm sm:text-base leading-relaxed flex-1">
                      {opt.text}
                    </span>
                    {tutorialSupportMode && selectedOpt !== null && isCorrectOption && (
                      <div className="flex items-center gap-1.5 text-emerald-700 dark:text-emerald-300 font-bold text-xs bg-emerald-100/90 dark:bg-emerald-900/70 px-2.5 py-1 rounded-md shrink-0">
                        <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                        <span>Correct Answer</span>
                      </div>
                    )}
                    {tutorialSupportMode && selectedOpt !== null && isSelected && !isCorrectOption && (
                      <div className="flex items-center gap-1.5 text-rose-700 dark:text-rose-300 font-bold text-xs bg-rose-100/90 dark:bg-rose-900/70 px-2.5 py-1 rounded-md shrink-0">
                        <XCircle className="w-4 h-4 text-rose-600 dark:text-rose-400" />
                        <span>Your Answer (Incorrect)</span>
                      </div>
                    )}
                  </button>
                );
              })}
            </div>

            {/* Immediate Tutorial Support Box */}
            {tutorialSupportMode && selectedOpt !== null && (
              <div className={`p-5 rounded-2xl border space-y-4 animate-fadeIn ${
                !isAnswerCorrect
                  ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
                  : 'bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60'
              }`}>
                {/* Header Alert */}
                {!isAnswerCorrect ? (
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-rose-200 dark:border-rose-900/60">
                    <div className="flex items-center gap-2.5 text-rose-800 dark:text-rose-300 font-bold text-sm sm:text-base">
                      <XCircle className="w-5 h-5 text-rose-600 shrink-0" />
                      <span>Incorrect Choice — Review Correct Answer & Clinical Explanation</span>
                    </div>
                    <button
                      onClick={handleRetryOption}
                      className="self-start sm:self-auto text-xs font-semibold px-3 py-1.5 rounded-lg bg-rose-200/80 hover:bg-rose-300 dark:bg-rose-900/80 dark:hover:bg-rose-800 text-rose-900 dark:text-rose-100 transition-colors cursor-pointer"
                    >
                      Try Again
                    </button>
                  </div>
                ) : (
                  <div className="flex items-center gap-2.5 text-emerald-800 dark:text-emerald-300 font-bold text-sm sm:text-base pb-3 border-b border-emerald-200 dark:border-emerald-900/60">
                    <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
                    <span>Correct Answer! Well done.</span>
                  </div>
                )}

                {/* Direct Comparison */}
                <div className={`p-3.5 rounded-xl border text-xs sm:text-sm space-y-1.5 ${
                  !isAnswerCorrect 
                    ? 'bg-white dark:bg-slate-900 border-rose-200 dark:border-rose-900/60' 
                    : 'bg-white dark:bg-slate-900 border-emerald-200 dark:border-emerald-900/60'
                }`}>
                  <div className="flex items-start gap-2">
                    <span className="font-bold text-emerald-700 dark:text-emerald-400 shrink-0">
                      ✓ Correct Answer:
                    </span>
                    <span className="font-semibold text-slate-900 dark:text-white">
                      Option {currentQ.correctAnswer} — {currentQ.options.find(o => o.id === currentQ.correctAnswer)?.text}
                    </span>
                  </div>
                  {!isAnswerCorrect && selectedOpt && (
                    <div className="flex items-start gap-2 text-rose-700 dark:text-rose-400">
                      <span className="font-bold shrink-0">✕ Your Choice:</span>
                      <span>
                        Option {selectedOpt} — {currentQ.options.find(o => o.id === selectedOpt)?.text}
                      </span>
                    </div>
                  )}
                </div>

                {/* Explanation */}
                <div className="p-4 rounded-xl bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-xs sm:text-sm text-slate-800 dark:text-slate-200 space-y-1.5">
                  <div className="flex items-center gap-1.5 font-bold text-slate-900 dark:text-white">
                    <Sparkles className="w-4 h-4 text-emerald-600" />
                    <span>Tutorial Support Rationale (Why Option {currentQ.correctAnswer} is Correct)</span>
                  </div>
                  <p className="leading-relaxed text-slate-700 dark:text-slate-300">
                    {currentQ.explanation}
                  </p>
                </div>
              </div>
            )}
          </div>

          {/* Navigation */}
          <div className="flex items-center justify-between">
            <button
              disabled={currentIndex === 0}
              onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}
              className={`flex items-center gap-1.5 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                currentIndex === 0
                  ? 'opacity-40 cursor-not-allowed bg-slate-100 dark:bg-slate-800 text-slate-400'
                  : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-50'
              }`}
            >
              <ChevronLeft className="w-4 h-4" />
              <span>Previous</span>
            </button>

            {currentIndex < questions.length - 1 && (
              <button
                onClick={() => setCurrentIndex(prev => Math.min(questions.length - 1, prev + 1))}
                className="flex items-center gap-1.5 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-900 dark:bg-slate-800 text-white hover:bg-slate-800 cursor-pointer"
              >
                <span>Next</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            )}
          </div>
        </div>

        {/* Question Palette Sidebar */}
        <div className="space-y-4">
          <div className="bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-4">
            <h4 className="font-bold text-slate-900 dark:text-white text-sm">Question Palette</h4>
            <div className="grid grid-cols-5 gap-2 max-h-96 overflow-y-auto p-1">
              {questions.map((q, idx) => {
                const ans = selectedAnswers[q.id];
                const isAnswered = ans !== undefined && ans !== null;
                const isCurrent = idx === currentIndex;
                const isCorrect = ans === q.correctAnswer;

                let paletteColor = 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-200';
                if (isAnswered) {
                  if (tutorialSupportMode) {
                    paletteColor = isCorrect
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'bg-rose-600 text-white shadow-xs';
                  } else {
                    paletteColor = 'bg-emerald-600 text-white shadow-xs';
                  }
                }

                return (
                  <button
                    key={q.id}
                    onClick={() => setCurrentIndex(idx)}
                    className={`h-9 rounded-lg font-bold text-xs flex items-center justify-center transition-all cursor-pointer ${
                      isCurrent
                        ? 'ring-2 ring-emerald-600 ring-offset-2 dark:ring-offset-slate-900'
                        : ''
                    } ${paletteColor}`}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>

            <div className="pt-3 border-t border-slate-100 dark:border-slate-800 space-y-2 text-xs text-slate-500">
              <div className="flex items-center justify-between">
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-emerald-600 inline-block" /> Answered</span>
                <span className="font-bold text-slate-800 dark:text-slate-200">
                  {Object.values(selectedAnswers).filter(Boolean).length}
                </span>
              </div>
              <div className="flex items-center justify-between">
                <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-slate-200 dark:bg-slate-700 inline-block" /> Unanswered</span>
                <span className="font-bold text-slate-800 dark:text-slate-200">{unansweredCount}</span>
              </div>
            </div>

            <button
              onClick={() => setConfirmSubmitOpen(true)}
              className="w-full bg-emerald-600 hover:bg-emerald-500 text-white font-semibold py-2.5 rounded-xl text-xs shadow-md transition-colors cursor-pointer mt-2"
            >
              Finish & Submit Exam
            </button>
          </div>
        </div>
      </div>

      {/* Confirmation Modal */}
      {confirmSubmitOpen && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 rounded-2xl max-w-md w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 space-y-4">
            <div className="w-12 h-12 rounded-full bg-amber-100 dark:bg-amber-950/60 text-amber-600 flex items-center justify-center mx-auto">
              <AlertTriangle className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-center text-slate-900 dark:text-white">
              Submit Mock Examination?
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 text-center leading-relaxed">
              You have answered <strong className="text-slate-800 dark:text-slate-200">{questions.length - unansweredCount}</strong> out of <strong className="text-slate-800 dark:text-slate-200">{questions.length}</strong> questions. 
              {unansweredCount > 0 && (
                <span className="block mt-1 text-amber-600 dark:text-amber-400 font-medium">
                  Unanswered questions will be counted as incorrect. Pass threshold is fixed at 70%.
                </span>
              )}
            </p>
            <div className="flex items-center gap-3 pt-2">
              <button
                onClick={() => setConfirmSubmitOpen(false)}
                className="flex-1 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 font-semibold text-xs hover:bg-slate-50 cursor-pointer"
              >
                Return to Exam
              </button>
              <button
                disabled={isSubmitting}
                onClick={performSubmission}
                className="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs shadow-md cursor-pointer flex items-center justify-center"
              >
                {isSubmitting ? 'Submitting...' : 'Confirm Submit'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
