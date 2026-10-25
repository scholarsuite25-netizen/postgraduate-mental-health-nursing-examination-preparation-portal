/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { NGN_CASE_STUDIES } from '../../data/ngnCaseStudies';
import { NGNCaseStudy, NGNCaseStage } from '../../types/clinicalExams';

interface NGNCaseSessionProps {
  initialCaseId?: string;
  candidateName: string;
  onBackToCenter: () => void;
}

export const NGNCaseSession: React.FC<NGNCaseSessionProps> = ({
  initialCaseId,
  candidateName,
  onBackToCenter,
}) => {
  const [selectedCaseId, setSelectedCaseId] = useState<string>(
    initialCaseId || NGN_CASE_STUDIES[0].id
  );
  const currentCase: NGNCaseStudy =
    NGN_CASE_STUDIES.find((c) => c.id === selectedCaseId) || NGN_CASE_STUDIES[0];

  const [currentStageIndex, setCurrentStageIndex] = useState<number>(0);
  const currentStage: NGNCaseStage = currentCase.stages[currentStageIndex];

  // Selected answers: stage index -> option id
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, string>>({});
  const [isCaseCompleted, setIsCaseCompleted] = useState<boolean>(false);

  const handleSelectOption = (optionId: string) => {
    if (selectedAnswers[currentStageIndex]) return; // locked once answered
    setSelectedAnswers((prev) => ({
      ...prev,
      [currentStageIndex]: optionId,
    }));
  };

  const handleNextStage = () => {
    if (currentStageIndex < currentCase.stages.length - 1) {
      setCurrentStageIndex((prev) => prev + 1);
    } else {
      setIsCaseCompleted(true);
    }
  };

  const handleRestartCase = () => {
    setSelectedAnswers({});
    setCurrentStageIndex(0);
    setIsCaseCompleted(false);
  };

  // Calculate score
  const correctCount = currentCase.stages.reduce((acc, stage, idx) => {
    const chosen = selectedAnswers[idx];
    const correctOpt = stage.options.find((o) => o.isCorrect);
    return acc + (chosen && correctOpt && chosen === correctOpt.id ? 1 : 0);
  }, 0);
  const percentage = (correctCount / currentCase.stages.length) * 100;

  return (
    <div className="space-y-6 animate-fadeIn max-w-4xl mx-auto pb-16">
      {/* Top Header */}
      <div className="flex items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <button
          onClick={onBackToCenter}
          className="text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-indigo-600 dark:hover:text-indigo-400"
        >
          ← Back to Clinical Exam Center
        </button>

        <div className="flex items-center gap-2">
          <select
            value={selectedCaseId}
            onChange={(e) => {
              setSelectedCaseId(e.target.value);
              setSelectedAnswers({});
              setCurrentStageIndex(0);
              setIsCaseCompleted(false);
            }}
            className="text-xs bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-3 py-1.5 font-semibold text-slate-800 dark:text-slate-200"
          >
            {NGN_CASE_STUDIES.map((c) => (
              <option key={c.id} value={c.id}>
                {c.title}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Case Overview Card */}
      <div className="bg-gradient-to-r from-purple-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-6 shadow-xl border border-purple-500/30 space-y-2">
        <span className="text-[11px] font-bold uppercase tracking-widest text-purple-300 block">
          NCSBN Clinical Judgment Measurement Model (NGN)
        </span>
        <h2 className="text-xl sm:text-2xl font-black text-white">{currentCase.title}</h2>
        <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
          {currentCase.clinicalSummary}
        </p>
        <div className="flex items-center gap-4 pt-2 text-xs text-purple-200">
          <span>Patient: <strong>{currentCase.patientDemographics.name}</strong>, {currentCase.patientDemographics.age}y/o</span>
          <span>•</span>
          <span>Diagnosis: <strong>{currentCase.patientDemographics.admissionDiagnosis}</strong></span>
        </div>
      </div>

      {/* Cognitive Layer Stepper */}
      <div className="grid grid-cols-6 gap-2">
        {currentCase.stages.map((stage, idx) => {
          const isCurrent = idx === currentStageIndex;
          const isAnswered = !!selectedAnswers[idx];
          const correctOpt = stage.options.find((o) => o.isCorrect);
          const wasCorrect = isAnswered && selectedAnswers[idx] === correctOpt?.id;

          return (
            <button
              key={idx}
              onClick={() => setCurrentStageIndex(idx)}
              className={`p-2 rounded-xl text-center border transition-all text-[11px] ${
                isCurrent
                  ? 'bg-indigo-600 text-white font-bold border-indigo-600 shadow-md ring-2 ring-indigo-400/40'
                  : isAnswered
                  ? wasCorrect
                    ? 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800'
                    : 'bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-300 dark:border-rose-800'
                  : 'bg-white dark:bg-slate-900 text-slate-500 dark:text-slate-400 border-slate-200 dark:border-slate-800'
              }`}
            >
              <div className="font-bold">Stage {idx + 1}</div>
              <div className="truncate text-[10px] hidden sm:block">{stage.cognitiveLevel}</div>
            </button>
          );
        })}
      </div>

      {/* Main Stage Display (or Case Completed Screen) */}
      {isCaseCompleted ? (
        <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-8 text-center space-y-6 shadow-xl">
          <div className="w-16 h-16 rounded-full bg-indigo-500/20 text-indigo-500 flex items-center justify-center text-3xl mx-auto">
            🎓
          </div>
          <div className="space-y-1">
            <h3 className="text-2xl font-bold text-slate-900 dark:text-white">
              Case Study Completed!
            </h3>
            <p className="text-xs sm:text-sm text-slate-500">
              You navigated all 6 NCSBN Cognitive Levels for {currentCase.patientDemographics.name}.
            </p>
          </div>

          <div className="inline-block p-6 rounded-2xl bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800">
            <div className="text-4xl font-extrabold font-mono text-indigo-600 dark:text-indigo-400 mb-1">
              {percentage.toFixed(0)}%
            </div>
            <div className="text-xs font-semibold text-slate-600 dark:text-slate-400">
              {correctCount} of {currentCase.stages.length} Clinical Judgment Decisions Correct
            </div>
          </div>

          <div className="flex items-center justify-center gap-4">
            <button
              onClick={handleRestartCase}
              className="px-5 py-2.5 rounded-xl font-semibold text-xs bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-200"
            >
              🔄 Replay Case
            </button>
            <button
              onClick={onBackToCenter}
              className="px-6 py-2.5 rounded-xl font-bold text-xs bg-indigo-600 text-white hover:bg-indigo-500"
            >
              Return to Clinical Hub →
            </button>
          </div>
        </div>
      ) : (
        <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-sm space-y-6">
          {/* Stage Header */}
          <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
            <div className="space-y-0.5">
              <span className="text-[11px] font-bold text-indigo-600 dark:text-indigo-400 uppercase tracking-wider">
                Stage {currentStage.stageNumber} of 6 • Cognitive Level:
              </span>
              <h3 className="text-lg font-bold text-slate-900 dark:text-white">
                {currentStage.cognitiveLevel}
              </h3>
            </div>
            <span className="px-3 py-1 rounded-full text-xs font-bold bg-indigo-50 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800">
              Postgraduate Standard
            </span>
          </div>

          {/* Clinical Progress Note */}
          <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-950/60 border border-slate-200 dark:border-slate-800/80 space-y-2">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center gap-1.5">
              <span>📋</span> Medical Record / Nursing Progress Note
            </div>
            <p className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-sans">
              {currentStage.clinicalProgressNote}
            </p>
          </div>

          {/* Diagnostic & Lab Findings (if present) */}
          {currentStage.diagnosticOrLabData && (
            <div className="p-4 rounded-xl bg-slate-950 text-emerald-400 border border-emerald-900/40 font-mono text-xs space-y-2">
              <div className="text-[10px] uppercase tracking-widest text-emerald-500 font-bold">
                Electronic Health Record (EHR) Telemetry & Lab Data
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px]">
                {Object.entries(currentStage.diagnosticOrLabData).map(([key, val]) => (
                  <div key={key} className="flex justify-between border-b border-emerald-950 pb-1">
                    <span className="text-slate-400">{key}:</span>
                    <strong className="text-white">{val}</strong>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Question Prompt */}
          <div className="space-y-3 pt-2">
            <h4 className="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-snug">
              {currentStage.questionPrompt}
            </h4>

            {/* Options */}
            <div className="space-y-2.5">
              {currentStage.options.map((opt) => {
                const isSelected = selectedAnswers[currentStageIndex] === opt.id;
                const hasAnswered = !!selectedAnswers[currentStageIndex];
                const isCorrect = opt.isCorrect;

                let optionStyle =
                  'bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-200 border-slate-200 dark:border-slate-800 hover:border-indigo-400';

                if (hasAnswered) {
                  if (opt.isCorrect) {
                    optionStyle =
                      'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-semibold ring-1 ring-emerald-500';
                  } else if (isSelected && !opt.isCorrect) {
                    optionStyle =
                      'bg-rose-50 dark:bg-rose-950/50 border-rose-500 text-rose-900 dark:text-rose-200 font-medium ring-1 ring-rose-500';
                  } else {
                    optionStyle =
                      'bg-white dark:bg-slate-900 text-slate-400 border-slate-200 dark:border-slate-800 opacity-60';
                  }
                }

                return (
                  <button
                    key={opt.id}
                    onClick={() => handleSelectOption(opt.id)}
                    disabled={hasAnswered}
                    className={`w-full text-left p-3.5 rounded-xl border text-xs sm:text-sm transition-all flex items-start gap-3 ${optionStyle}`}
                  >
                    <span
                      className={`w-6 h-6 rounded-full flex items-center justify-center font-bold text-xs shrink-0 ${
                        hasAnswered && opt.isCorrect
                          ? 'bg-emerald-600 text-white'
                          : hasAnswered && isSelected && !opt.isCorrect
                          ? 'bg-rose-600 text-white'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                      }`}
                    >
                      {opt.id}
                    </span>
                    <span className="leading-snug flex-1">{opt.text}</span>
                    {hasAnswered && opt.isCorrect && (
                      <span className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 shrink-0">
                        ✓ Correct Decision
                      </span>
                    )}
                    {hasAnswered && isSelected && !opt.isCorrect && (
                      <span className="text-[10px] font-bold text-rose-600 dark:text-rose-400 shrink-0">
                        ✕ Selected (Suboptimal)
                      </span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>

          {/* Tutorial Support & Immediate Post-Attempt Clinical Explanation Box */}
          {selectedAnswers[currentStageIndex] && (() => {
            const chosenId = selectedAnswers[currentStageIndex];
            const correctOpt = currentStage.options.find(o => o.isCorrect);
            const chosenOpt = currentStage.options.find(o => o.id === chosenId);
            const isStageCorrect = chosenId === correctOpt?.id;

            return (
              <div className={`p-5 rounded-2xl border text-xs sm:text-sm space-y-3 animate-fadeIn ${
                !isStageCorrect
                  ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
                  : 'bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60'
              }`}>
                <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-200/60 dark:border-slate-800/60">
                  <div className="flex items-center gap-2 font-bold">
                    {!isStageCorrect ? (
                      <span className="text-rose-700 dark:text-rose-300 flex items-center gap-1.5 font-bold">
                        <span>✕</span> Suboptimal Clinical Judgment — Tutorial Support Active
                      </span>
                    ) : (
                      <span className="text-emerald-700 dark:text-emerald-300 flex items-center gap-1.5 font-bold">
                        <span>✓</span> Priority Clinical Judgment Validated! Well done.
                      </span>
                    )}
                  </div>
                  {!isStageCorrect && (
                    <button
                      onClick={() => {
                        setSelectedAnswers(prev => {
                          const next = { ...prev };
                          delete next[currentStageIndex];
                          return next;
                        });
                      }}
                      className="text-[11px] font-bold px-2.5 py-1 rounded bg-rose-200/80 hover:bg-rose-300 dark:bg-rose-900/80 dark:hover:bg-rose-800 text-rose-900 dark:text-rose-100 transition-colors cursor-pointer"
                    >
                      Try Again
                    </button>
                  )}
                </div>

                {/* Direct Comparison */}
                <div className="space-y-1 text-xs">
                  <div className="flex items-start gap-1.5 font-semibold text-emerald-800 dark:text-emerald-300">
                    <span className="font-bold shrink-0">✓ Validated Priority Action:</span>
                    <span>
                      Option {correctOpt?.id} — {correctOpt?.text}
                    </span>
                  </div>
                  {!isStageCorrect && chosenOpt && (
                    <div className="flex items-start gap-1.5 text-rose-700 dark:text-rose-400">
                      <span className="font-bold shrink-0">✕ Your Decision:</span>
                      <span>
                        Option {chosenOpt.id} — {chosenOpt.text}
                      </span>
                    </div>
                  )}
                </div>

                {/* Clinical Judgment Rationale */}
                <div className="p-3.5 rounded-xl bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-slate-800 dark:text-slate-200 space-y-1.5">
                  <div className="font-bold flex items-center gap-1.5 text-slate-900 dark:text-white text-xs">
                    <span>💡</span> NCSBN Clinical Judgment Rationale ({currentStage.cognitiveLevel}):
                  </div>
                  <p className="leading-relaxed text-xs text-slate-700 dark:text-slate-300">
                    {currentStage.clinicalRationale}
                  </p>
                </div>
              </div>
            );
          })()}

          {/* Action Bar */}
          <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
            <span className="text-xs text-slate-500">
              {selectedAnswers[currentStageIndex]
                ? 'Decision verified'
                : 'Select the optimal clinical action above'}
            </span>

            {selectedAnswers[currentStageIndex] && (
              <button
                onClick={handleNextStage}
                className="px-6 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition-colors flex items-center gap-1.5"
              >
                {currentStageIndex < currentCase.stages.length - 1
                  ? `Proceed to Stage ${currentStageIndex + 2} →`
                  : 'Complete Case Study →'}
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
