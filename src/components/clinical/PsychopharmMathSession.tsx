/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { PSYCHOPHARM_MATH_PROBLEMS } from '../../data/psychopharmMath';
import { PsychopharmMathProblem } from '../../types/clinicalExams';

interface PsychopharmMathSessionProps {
  initialProblemId?: string;
  candidateName: string;
  onBackToCenter: () => void;
}

export const PsychopharmMathSession: React.FC<PsychopharmMathSessionProps> = ({
  initialProblemId,
  candidateName,
  onBackToCenter,
}) => {
  const [selectedProblemId, setSelectedProblemId] = useState<string>(
    initialProblemId || PSYCHOPHARM_MATH_PROBLEMS[0].id
  );
  const currentProblem: PsychopharmMathProblem =
    PSYCHOPHARM_MATH_PROBLEMS.find((p) => p.id === selectedProblemId) ||
    PSYCHOPHARM_MATH_PROBLEMS[0];

  const [selectedOptionId, setSelectedOptionId] = useState<'A' | 'B' | 'C' | 'D' | null>(null);
  const [showFormula, setShowFormula] = useState<boolean>(false);
  const [scratchpadText, setScratchpadText] = useState<string>('');

  const handleSelectOption = (optId: 'A' | 'B' | 'C' | 'D') => {
    setSelectedOptionId(optId);
  };

  const handleNextProblem = () => {
    const currentIndex = PSYCHOPHARM_MATH_PROBLEMS.findIndex((p) => p.id === currentProblem.id);
    const nextIndex = (currentIndex + 1) % PSYCHOPHARM_MATH_PROBLEMS.length;
    setSelectedProblemId(PSYCHOPHARM_MATH_PROBLEMS[nextIndex].id);
    setSelectedOptionId(null);
    setShowFormula(false);
    setScratchpadText('');
  };

  return (
    <div className="space-y-6 animate-fadeIn max-w-4xl mx-auto pb-16">
      {/* Top Header */}
      <div className="flex items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <button
          onClick={onBackToCenter}
          className="text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-teal-600 dark:hover:text-teal-400"
        >
          ← Back to Clinical Exam Center
        </button>

        <select
          value={selectedProblemId}
          onChange={(e) => {
            setSelectedProblemId(e.target.value);
            setSelectedOptionId(null);
            setShowFormula(false);
            setScratchpadText('');
          }}
          className="text-xs bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-3 py-1.5 font-semibold text-slate-800 dark:text-slate-200"
        >
          {PSYCHOPHARM_MATH_PROBLEMS.map((p) => (
            <option key={p.id} value={p.id}>
              {p.category}: {p.title}
            </option>
          ))}
        </select>
      </div>

      {/* Main Problem Card */}
      <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-sm space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-3">
          <div>
            <span className="text-[11px] font-bold uppercase tracking-widest text-teal-600 dark:text-teal-400">
              {currentProblem.category}
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white mt-0.5">
              {currentProblem.title}
            </h2>
          </div>
          <span className="px-3 py-1 rounded-full text-xs font-bold bg-teal-50 dark:bg-teal-950/60 text-teal-700 dark:text-teal-300 border border-teal-200 dark:border-teal-800">
            Clinical Dosage Calculation
          </span>
        </div>

        {/* Clinical Scenario */}
        <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-950/60 border border-slate-200 dark:border-slate-800/80 space-y-2">
          <div className="text-xs font-bold uppercase tracking-wider text-slate-500">
            Clinical Case Scenario
          </div>
          <p className="text-xs sm:text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-sans">
            {currentProblem.clinicalScenario}
          </p>
        </div>

        {/* Clinical Parameters Grid */}
        <div className="bg-slate-950 text-teal-400 p-4 rounded-xl border border-teal-900/40 font-mono text-xs space-y-2">
          <div className="text-[10px] uppercase tracking-widest text-teal-500 font-bold">
            Given Clinical Parameters & Laboratory Values
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px]">
            {Object.entries(currentProblem.parameters).map(([key, val]) => (
              <div key={key} className="flex justify-between border-b border-teal-950 pb-1">
                <span className="text-slate-400">{key}:</span>
                <strong className="text-white">{val}</strong>
              </div>
            ))}
          </div>
        </div>

        {/* Question Prompt */}
        <div className="space-y-3">
          <h3 className="text-sm sm:text-base font-bold text-slate-900 dark:text-white leading-snug">
            {currentProblem.questionPrompt}
          </h3>

          {/* Formula Hint Button */}
          {currentProblem.formulaHint && (
            <div>
              <button
                onClick={() => setShowFormula(!showFormula)}
                className="text-xs font-semibold text-teal-600 dark:text-teal-400 hover:underline flex items-center gap-1.5"
              >
                <span>📐</span> {showFormula ? 'Hide Formula Reference' : 'View Formula Reference & Hint'}
              </button>
              {showFormula && (
                <div className="mt-2 p-3 rounded-lg bg-teal-50 dark:bg-teal-950/40 border border-teal-200 dark:border-teal-800 font-mono text-xs text-teal-900 dark:text-teal-200 whitespace-pre-line animate-fadeIn">
                  {currentProblem.formulaHint}
                </div>
              )}
            </div>
          )}

          {/* Options */}
          <div className="space-y-2.5 pt-2">
            {currentProblem.options.map((opt) => {
              const isSelected = selectedOptionId === opt.id;
              const hasAnswered = selectedOptionId !== null;

              let style =
                'bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-200 border-slate-200 dark:border-slate-800 hover:border-teal-500';

              if (hasAnswered) {
                if (opt.isCorrect) {
                  style =
                    'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-semibold';
                } else if (isSelected && !opt.isCorrect) {
                  style =
                    'bg-rose-50 dark:bg-rose-950/50 border-rose-500 text-rose-900 dark:text-rose-200';
                } else {
                  style =
                    'bg-white dark:bg-slate-900 text-slate-400 border-slate-200 dark:border-slate-800 opacity-60';
                }
              }

              return (
                <button
                  key={opt.id}
                  onClick={() => handleSelectOption(opt.id)}
                  disabled={hasAnswered}
                  className={`w-full text-left p-3.5 rounded-xl border text-xs sm:text-sm transition-all flex items-start gap-3 ${style}`}
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
                </button>
              );
            })}
          </div>
        </div>

        {/* Scratchpad (Collapsible) */}
        <div className="pt-2">
          <details className="group">
            <summary className="text-xs font-semibold text-slate-500 hover:text-slate-800 dark:hover:text-slate-300 cursor-pointer list-none flex items-center gap-1.5">
              <span>📝</span>
              <span className="underline">Candidate Scratchpad / Calculation Notes</span>
            </summary>
            <div className="mt-2">
              <textarea
                value={scratchpadText}
                onChange={(e) => setScratchpadText(e.target.value)}
                placeholder="Type your intermediate calculations or notes here..."
                rows={3}
                className="w-full text-xs font-mono p-3 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-1 focus:ring-teal-500"
              />
            </div>
          </details>
        </div>

        {/* Step-by-Step Solution Breakdown (Revealed once answered) */}
        {selectedOptionId !== null && (() => {
          const correctOpt = currentProblem.options.find((o) => o.isCorrect);
          const chosenOpt = currentProblem.options.find((o) => o.id === selectedOptionId);
          const isProblemCorrect = selectedOptionId === correctOpt?.id;

          return (
            <div
              className={`p-5 rounded-2xl border space-y-4 animate-fadeIn ${
                !isProblemCorrect
                  ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
                  : 'bg-teal-50/70 dark:bg-teal-950/40 border-teal-200 dark:border-teal-900/60'
              }`}
            >
              <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-200/60 dark:border-slate-800/60">
                <div className="flex items-center gap-2 font-bold text-xs sm:text-sm">
                  {!isProblemCorrect ? (
                    <span className="text-rose-700 dark:text-rose-300 flex items-center gap-1.5 font-bold">
                      <span>✕</span> Incorrect Dosage Calculation — Tutorial Support Active
                    </span>
                  ) : (
                    <span className="text-teal-700 dark:text-teal-300 flex items-center gap-1.5 font-bold">
                      <span>✓</span> Accurate Mathematical Derivation! Well done.
                    </span>
                  )}
                </div>
                {!isProblemCorrect && (
                  <button
                    onClick={() => {
                      setSelectedOptionId(null);
                    }}
                    className="text-[11px] font-bold px-2.5 py-1 rounded bg-rose-200/80 hover:bg-rose-300 dark:bg-rose-900/80 dark:hover:bg-rose-800 text-rose-900 dark:text-rose-100 transition-colors cursor-pointer"
                  >
                    Try Again
                  </button>
                )}
              </div>

              {/* Direct Comparison */}
              <div className="space-y-1 text-xs">
                <div className="flex items-start gap-1.5 font-semibold text-teal-900 dark:text-teal-200">
                  <span className="font-bold shrink-0">✓ Validated Correct Result:</span>
                  <span>
                    Option {correctOpt?.id} — {correctOpt?.text}
                  </span>
                </div>
                {!isProblemCorrect && chosenOpt && (
                  <div className="flex items-start gap-1.5 text-rose-700 dark:text-rose-400">
                    <span className="font-bold shrink-0">✕ Your Calculated Value:</span>
                    <span>
                      Option {chosenOpt.id} — {chosenOpt.text}
                    </span>
                  </div>
                )}
              </div>

              {/* Step-by-Step Derivation */}
              <div className="p-4 rounded-xl bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 space-y-2">
                <div className="font-bold text-xs text-slate-900 dark:text-white flex items-center gap-2 uppercase tracking-wide">
                  <span>📐</span> Step-by-Step Mathematical Derivation & Proof:
                </div>
                <div className="space-y-1 text-xs text-slate-800 dark:text-slate-200 font-mono">
                  {currentProblem.stepByStepSolution.map((step, idx) => (
                    <div key={idx} className="leading-relaxed">
                      {step}
                    </div>
                  ))}
                </div>
              </div>

              <div className="p-3 rounded-lg bg-teal-100/60 dark:bg-teal-900/40 border border-teal-200/80 dark:border-teal-800 text-xs text-teal-950 dark:text-teal-200">
                <strong>Clinical Significance:</strong> {currentProblem.clinicalSignificance}
              </div>
            </div>
          );
        })()}

        {/* Footer Navigation */}
        <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
          <button
            onClick={() => {
              setSelectedOptionId(null);
              setShowFormula(false);
              setScratchpadText('');
            }}
            className="text-xs font-semibold text-slate-500 hover:text-slate-800 dark:hover:text-slate-200"
          >
            Clear / Retry Problem
          </button>

          <button
            onClick={handleNextProblem}
            className="px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-teal-600 hover:bg-teal-500 text-white shadow-md transition-colors flex items-center gap-1.5"
          >
            Next Calculation Problem →
          </button>
        </div>
      </div>
    </div>
  );
};
