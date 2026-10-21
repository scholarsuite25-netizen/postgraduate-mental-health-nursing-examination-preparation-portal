/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect } from 'react';
import { 
  Bookmark, 
  ChevronLeft, 
  ChevronRight, 
  CheckCircle2, 
  XCircle, 
  HelpCircle, 
  Clock, 
  Send, 
  Sparkles,
  AlertCircle
} from 'lucide-react';
import { Question, AssessmentMode, AssessmentReport } from '../types';
import { StorageService } from '../services/storageService';

interface PracticeSessionProps {
  questions: Question[];
  mode: AssessmentMode;
  moduleName?: string;
  candidateName: string;
  onFinish: (report: AssessmentReport) => void;
  onCancel: () => void;
}

export const PracticeSession: React.FC<PracticeSessionProps> = ({
  questions,
  mode,
  moduleName,
  candidateName,
  onFinish,
  onCancel
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, 'A' | 'B' | 'C' | 'D' | null>>({});
  const [revealedQuestions, setRevealedQuestions] = useState<Record<string, boolean>>({});
  const [bookmarks, setBookmarks] = useState<string[]>([]);
  const [secondsElapsed, setSecondsElapsed] = useState(0);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [confirmSubmitOpen, setConfirmSubmitOpen] = useState(false);

  // Timer
  useEffect(() => {
    const timer = setInterval(() => {
      setSecondsElapsed(prev => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  // Load bookmarks
  useEffect(() => {
    StorageService.getBookmarks().then(setBookmarks).catch(() => {});
  }, []);

  const currentQ = questions[currentIndex];
  const selectedOpt = selectedAnswers[currentQ?.id] || null;
  const isRevealed = Boolean(revealedQuestions[currentQ?.id] || selectedOpt !== null);
  const isAnswerCorrect = selectedOpt === currentQ?.correctAnswer;

  const handleSelectOption = (optId: 'A' | 'B' | 'C' | 'D') => {
    setSelectedAnswers(prev => ({
      ...prev,
      [currentQ.id]: optId
    }));

    setRevealedQuestions(prev => ({
      ...prev,
      [currentQ.id]: true
    }));

    // If incorrect, record in incorrect queue immediately for review & remediation
    if (optId !== currentQ.correctAnswer) {
      StorageService.recordIncorrectAnswer(currentQ.id, currentQ.module, optId);
    } else {
      StorageService.removeFromIncorrectQueue(currentQ.id);
    }
  };

  const handleRetryQuestion = () => {
    setSelectedAnswers(prev => {
      const next = { ...prev };
      delete next[currentQ.id];
      return next;
    });
    setRevealedQuestions(prev => {
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

  const handleFinalSubmit = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);

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
    const percentage = totalQuestions > 0 ? (correctCount / totalQuestions) * 100 : 0;
    const passMark = 70.0;
    const status = percentage >= passMark ? 'PASS' : 'FAIL';

    const reportId = `WAPCNM-REP-${Math.random().toString(36).substring(2, 9).toUpperCase()}`;

    const report: AssessmentReport = {
      id: reportId,
      candidateName,
      assessmentTitle: moduleName ? `Module Practice: ${moduleName}` : 'General MCQ Practice Session',
      mode,
      module: moduleName,
      dateTimestamp: Date.now(),
      totalQuestions,
      answeredCount,
      correctCount,
      incorrectCount,
      unansweredCount,
      percentage,
      passMark,
      status,
      timeTakenSeconds: secondsElapsed,
      questionsSnapshot: [...questions],
      candidateAnswers: { ...selectedAnswers }
    };

    try {
      await StorageService.saveReport(report);
      onFinish(report);
    } catch (err: any) {
      alert(err.message || 'Failed to save assessment report.');
      setIsSubmitting(false);
    }
  };

  const formatTime = (totalSecs: number) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  if (!currentQ) return <div>No questions available.</div>;

  const isBookmarked = bookmarks.includes(currentQ.id);
  const unansweredCount = questions.filter(q => !selectedAnswers[q.id]).length;

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Top Header Bar */}
      <div className="bg-white dark:bg-slate-900 p-4 sm:p-5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 text-xs font-semibold text-emerald-600 dark:text-emerald-400 mb-1">
            <span>{moduleName || 'General Practice'}</span>
            <span>•</span>
            <span className="uppercase px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300">
              {mode} mode
            </span>
          </div>
          <h2 className="text-base sm:text-lg font-bold text-slate-900 dark:text-white">
            Question {currentIndex + 1} of {questions.length}
          </h2>
        </div>

        <div className="flex items-center gap-3 w-full sm:w-auto justify-between sm:justify-end">
          <div className="flex items-center gap-1.5 bg-slate-100 dark:bg-slate-800 px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-700 dark:text-slate-300">
            <Clock className="w-4 h-4 text-slate-500" />
            <span>Time: {formatTime(secondsElapsed)}</span>
          </div>

          <button
            onClick={handleToggleBookmark}
            className={`p-2 rounded-lg border transition-colors flex items-center gap-1.5 text-xs font-semibold ${
              isBookmarked 
                ? 'bg-amber-50 border-amber-300 text-amber-700 dark:bg-amber-950/60 dark:border-amber-700 dark:text-amber-300' 
                : 'bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300'
            }`}
          >
            <Bookmark className={`w-4 h-4 ${isBookmarked ? 'fill-amber-500 text-amber-500' : ''}`} />
            <span className="hidden sm:inline">{isBookmarked ? 'Bookmarked' : 'Bookmark'}</span>
          </button>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
        <div 
          className="bg-emerald-600 h-full transition-all duration-300"
          style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-xs space-y-6">
        <div className="flex items-start justify-between gap-4">
          <div className="space-y-1">
            <span className="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
              Topic: {currentQ.topic} ({currentQ.difficulty})
            </span>
            <h3 className="text-lg sm:text-xl font-bold text-slate-900 dark:text-white leading-relaxed">
              {currentQ.questionText}
            </h3>
          </div>
        </div>

        {/* Options */}
        <div className="space-y-3">
          {currentQ.options.map((opt) => {
            const isSelected = selectedOpt === opt.id;
            const isCorrectOption = opt.id === currentQ.correctAnswer;
            
            let btnStyle = "border-slate-200 dark:border-slate-800 hover:border-emerald-500/50 bg-white dark:bg-slate-800/40 text-slate-800 dark:text-slate-200";

            if (isRevealed) {
              if (isCorrectOption) {
                // Correct answer is always prominently highlighted in emerald
                btnStyle = "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 ring-2 ring-emerald-500 shadow-xs";
              } else if (isSelected && !isCorrectOption) {
                // Wrong answer chosen by candidate is highlighted in rose/red
                btnStyle = "border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 ring-2 ring-rose-500 shadow-xs";
              } else {
                // Non-selected distractors are subdued
                btnStyle = "border-slate-200 dark:border-slate-800/60 bg-slate-50/50 dark:bg-slate-900/40 text-slate-500 dark:text-slate-400 opacity-70";
              }
            } else if (isSelected) {
              btnStyle = "border-emerald-600 bg-emerald-50/50 dark:bg-emerald-950/30 text-emerald-900 dark:text-emerald-200 ring-1 ring-emerald-600";
            }

            return (
              <button
                key={opt.id}
                onClick={() => handleSelectOption(opt.id)}
                className={`w-full text-left p-4 rounded-xl border transition-all flex items-start gap-3.5 cursor-pointer ${btnStyle}`}
              >
                <span className={`w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
                  isRevealed && isCorrectOption
                    ? 'bg-emerald-600 text-white'
                    : isRevealed && isSelected && !isCorrectOption
                    ? 'bg-rose-600 text-white'
                    : isSelected
                    ? 'bg-emerald-600 text-white'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                }`}>
                  {opt.id}
                </span>
                <span className="text-sm sm:text-base leading-relaxed flex-1 font-medium">
                  {opt.text}
                </span>
                {isRevealed && isCorrectOption && (
                  <div className="flex items-center gap-1.5 text-emerald-700 dark:text-emerald-300 font-bold text-xs bg-emerald-100/90 dark:bg-emerald-900/70 px-2.5 py-1 rounded-md shrink-0">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                    <span>Correct Answer</span>
                  </div>
                )}
                {isRevealed && isSelected && !isCorrectOption && (
                  <div className="flex items-center gap-1.5 text-rose-700 dark:text-rose-300 font-bold text-xs bg-rose-100/90 dark:bg-rose-900/70 px-2.5 py-1 rounded-md shrink-0">
                    <XCircle className="w-4 h-4 text-rose-600 dark:text-rose-400" />
                    <span>Your Answer (Incorrect)</span>
                  </div>
                )}
              </button>
            );
          })}
        </div>

        {/* Immediate Post-Attempt Clinical Feedback & Explanation */}
        {isRevealed && (
          <div className={`mt-6 p-6 rounded-2xl border space-y-5 animate-fadeIn ${
            !isAnswerCorrect
              ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
              : 'bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60'
          }`}>
            {/* Header Alert */}
            {!isAnswerCorrect ? (
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-rose-200 dark:border-rose-900/60">
                <div className="flex items-center gap-2.5 text-rose-800 dark:text-rose-300 font-bold text-base sm:text-lg">
                  <XCircle className="w-6 h-6 text-rose-600 shrink-0" />
                  <span>Incorrect — Review Correct Answer & Clinical Explanation</span>
                </div>
                <button
                  onClick={handleRetryQuestion}
                  className="self-start sm:self-auto text-xs font-semibold px-3 py-1.5 rounded-lg bg-rose-200/80 hover:bg-rose-300 dark:bg-rose-900/80 dark:hover:bg-rose-800 text-rose-900 dark:text-rose-100 transition-colors cursor-pointer"
                >
                  Try Again
                </button>
              </div>
            ) : (
              <div className="flex items-center gap-2.5 text-emerald-800 dark:text-emerald-300 font-bold text-base sm:text-lg pb-3 border-b border-emerald-200 dark:border-emerald-900/60">
                <CheckCircle2 className="w-6 h-6 text-emerald-600 shrink-0" />
                <span>Correct Answer! Well done.</span>
              </div>
            )}

            {/* Direct Answer Comparison */}
            <div className={`p-4 rounded-xl border text-xs sm:text-sm space-y-2 ${
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

            {/* Detailed Clinical Rationale */}
            <div className="p-4 rounded-xl bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-xs sm:text-sm text-slate-800 dark:text-slate-200 space-y-2">
              <div className="flex items-center gap-1.5 font-bold text-slate-900 dark:text-white">
                <Sparkles className="w-4 h-4 text-emerald-600" />
                <span>Detailed Clinical Rationale (Why Option {currentQ.correctAnswer} is Correct)</span>
              </div>
              <p className="leading-relaxed text-slate-700 dark:text-slate-300">
                {currentQ.explanation}
              </p>
            </div>

            {/* Option-by-Option Breakdown */}
            <div className="space-y-2 pt-1">
              <p className="text-xs font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400">
                Detailed Breakdown of All Options:
              </p>
              <div className="grid grid-cols-1 gap-2.5">
                {currentQ.options.map(opt => {
                  const isCorrect = opt.id === currentQ.correctAnswer;
                  const isCandidate = opt.id === selectedOpt;
                  const specificIncorrectExp = currentQ.incorrectExplanations?.[opt.id];

                  return (
                    <div 
                      key={opt.id}
                      className={`p-3.5 rounded-xl border text-xs sm:text-sm transition-all ${
                        isCorrect 
                          ? 'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-300 dark:border-emerald-700 text-emerald-950 dark:text-emerald-100 font-medium' 
                          : isCandidate
                          ? 'bg-rose-50 dark:bg-rose-950/50 border-rose-300 dark:border-rose-700 text-rose-950 dark:text-rose-100'
                          : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
                      }`}
                    >
                      <div className="flex items-start gap-2.5">
                        <span className={`w-6 h-6 rounded flex items-center justify-center font-bold text-xs shrink-0 mt-0.5 ${
                          isCorrect 
                            ? 'bg-emerald-600 text-white' 
                            : isCandidate
                            ? 'bg-rose-600 text-white'
                            : 'bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                        }`}>
                          {opt.id}
                        </span>
                        <div className="flex-1 space-y-1">
                          <div className="flex items-center gap-2 flex-wrap">
                            <span className="font-semibold text-slate-900 dark:text-white">{opt.text}</span>
                            {isCorrect && (
                              <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-emerald-200/80 dark:bg-emerald-800 text-emerald-900 dark:text-emerald-100">
                                Correct Answer
                              </span>
                            )}
                            {isCandidate && !isCorrect && (
                              <span className="text-[10px] font-bold uppercase px-2 py-0.5 rounded bg-rose-200/80 dark:bg-rose-800 text-rose-900 dark:text-rose-100">
                                Selected Incorrectly
                              </span>
                            )}
                          </div>
                          <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                            {isCorrect 
                              ? `✓ Correct: Accurately aligns with evidence-based mental health nursing criteria and the clinical rationale above.` 
                              : specificIncorrectExp || `✕ Incorrect: This choice does not reflect the evidence-based standard or prioritized nursing intervention for this presentation.`
                            }
                          </p>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Learning Objective & Reference */}
            {(currentQ.learningObjective || currentQ.reference) && (
              <div className="pt-3 border-t border-slate-200 dark:border-slate-800 space-y-1.5 text-xs text-slate-600 dark:text-slate-400">
                {currentQ.learningObjective && (
                  <p>
                    <strong className="text-slate-700 dark:text-slate-300">Learning Objective:</strong> {currentQ.learningObjective}
                  </p>
                )}
                {currentQ.reference && (
                  <p className="text-[11px] text-slate-500">
                    <strong className="text-slate-600 dark:text-slate-400">Reference:</strong> {currentQ.reference}
                  </p>
                )}
              </div>
            )}
          </div>
        )}
      </div>

      {/* Navigation Footer */}
      <div className="flex items-center justify-between pt-2">
        <button
          disabled={currentIndex === 0}
          onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}
          className={`flex items-center gap-1.5 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
            currentIndex === 0
              ? 'opacity-40 cursor-not-allowed bg-slate-100 dark:bg-slate-800 text-slate-400'
              : 'bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800'
          }`}
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Previous</span>
        </button>

        <div className="flex items-center gap-3">
          <button
            onClick={() => setConfirmSubmitOpen(true)}
            className="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-6 py-2.5 rounded-xl text-xs sm:text-sm flex items-center gap-2 shadow-md shadow-emerald-600/20 cursor-pointer"
          >
            <Send className="w-4 h-4" />
            <span>Finish & Submit Assessment</span>
          </button>

          {currentIndex < questions.length - 1 ? (
            <button
              onClick={() => setCurrentIndex(prev => Math.min(questions.length - 1, prev + 1))}
              className="flex items-center gap-1.5 px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold bg-slate-900 dark:bg-slate-800 text-white hover:bg-slate-800 dark:hover:bg-slate-700 cursor-pointer"
            >
              <span>Next</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          ) : null}
        </div>
      </div>

      {/* Confirmation Modal */}
      {confirmSubmitOpen && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 rounded-2xl max-w-md w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 space-y-4">
            <div className="w-12 h-12 rounded-full bg-amber-100 dark:bg-amber-950/60 text-amber-600 flex items-center justify-center mx-auto">
              <AlertCircle className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-center text-slate-900 dark:text-white">
              Ready to Submit Assessment?
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 text-center leading-relaxed">
              You have answered <strong className="text-slate-800 dark:text-slate-200">{Object.keys(selectedAnswers).length}</strong> out of <strong className="text-slate-800 dark:text-slate-200">{questions.length}</strong> questions. 
              {unansweredCount > 0 && (
                <span className="block mt-1 text-amber-600 dark:text-amber-400 font-medium">
                  Note: {unansweredCount} unanswered question(s) will be counted as incorrect.
                </span>
              )}
            </p>
            <div className="flex items-center gap-3 pt-2">
              <button
                onClick={() => setConfirmSubmitOpen(false)}
                className="flex-1 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 font-semibold text-xs hover:bg-slate-50 dark:hover:bg-slate-800 cursor-pointer"
              >
                Continue Reviewing
              </button>
              <button
                disabled={isSubmitting}
                onClick={handleFinalSubmit}
                className="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs shadow-md shadow-emerald-600/20 cursor-pointer flex items-center justify-center gap-2"
              >
                {isSubmitting ? 'Saving Report...' : 'Confirm Submission'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
