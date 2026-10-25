/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { NMCN_SPECIALTIES } from '../../data/nmcnSpecialtiesData';
import { NMCNSpecialty, NMCNSpecialtySubmission } from '../../types/nmcnSpecialties';
import { ChecklistItem } from '../../types/clinicalExams';

interface NMCNAllSpecialtiesViewProps {
  candidateName: string;
  onNavigateHome: () => void;
}

export const NMCNAllSpecialtiesView: React.FC<NMCNAllSpecialtiesViewProps> = ({
  candidateName,
  onNavigateHome,
}) => {
  const [selectedSpecialtyIndex, setSelectedSpecialtyIndex] = useState<number>(0);
  const currentSpecialty: NMCNSpecialty = NMCN_SPECIALTIES[selectedSpecialtyIndex];
  const station = currentSpecialty.station;

  // Active user selections for current station
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});
  const [mcqAnswers, setMcqAnswers] = useState<Record<string, 'A' | 'B' | 'C' | 'D' | null>>({});
  const [activeSubTab, setActiveSubTab] = useState<'blueprint' | 'practical' | 'mcq' | 'result'>('blueprint');

  // Change specialty handler
  const handleSelectSpecialty = (index: number) => {
    setSelectedSpecialtyIndex(index);
    setCheckedItems({});
    setMcqAnswers({});
    setActiveSubTab('blueprint');
  };

  const handleToggleChecklist = (item: ChecklistItem) => {
    setCheckedItems((prev) => ({
      ...prev,
      [item.id]: !prev[item.id],
    }));
  };

  const handleSelectMCQ = (mcqId: string, optId: 'A' | 'B' | 'C' | 'D') => {
    setMcqAnswers((prev) => ({
      ...prev,
      [mcqId]: optId,
    }));
  };

  // Calculate live score
  const rawPractical = station.checklist.reduce((acc, item) => {
    return acc + (checkedItems[item.id] ? item.points : 0);
  }, 0);

  const missedRedFlags = station.checklist.filter(
    (item) => item.isCriticalFail && !checkedItems[item.id]
  );
  const hasRedFlag = missedRedFlags.length > 0;

  let practicalPct = (rawPractical / 100) * 100;
  if (hasRedFlag && practicalPct > 49) {
    practicalPct = 49.0; // Capped by statutory red flag rule
  }

  let mcqCorrect = 0;
  station.mcqs.forEach((q) => {
    if (mcqAnswers[q.id] === q.correctAnswer) {
      mcqCorrect++;
    }
  });
  const mcqPct = (mcqCorrect / station.mcqs.length) * 100;

  const compositePct = (practicalPct + mcqPct) / 2;
  const isPassed = compositePct >= 50.0 && !hasRedFlag;
  const isDistinction = compositePct >= 75.0 && !hasRedFlag;

  return (
    <div className="space-y-8 animate-fadeIn max-w-6xl mx-auto pb-16">
      {/* Return to WAPCNM Flagship Bar */}
      <div className="flex flex-wrap items-center justify-between gap-4 bg-slate-900 text-white p-4 rounded-2xl border border-slate-800 shadow-lg">
        <div className="flex items-center gap-3">
          <span className="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
          <span className="text-xs font-semibold text-slate-300">
            You are browsing the <strong>NMCN Statutory Professional Licensure & Global Specialisations</strong> page.
          </span>
        </div>
        <button
          onClick={onNavigateHome}
          className="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition-all flex items-center gap-2"
        >
          <span>←</span> Return to WAPCNM Mental Health Flagship
        </button>
      </div>

      {/* Header Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-slate-900 via-blue-950 to-indigo-950 p-6 sm:p-8 text-white shadow-xl border border-blue-500/20">
        <div className="max-w-4xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-blue-500/20 text-blue-300 border border-blue-500/30">
            <span>📜</span> Statutory Authority: Nursing & Midwifery Council of Nigeria (Act Cap N143 LFN 2004)
          </div>
          <h1 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
            NMCN Professional Nursing Specialisations & Global Licensure
          </h1>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Statutory council curricula and clinical examination standards across the 5 core post-basic specialisations. Evaluated against the official council benchmark: <strong>50.0% Pass Mark</strong>, <strong>75.0% Distinction</strong>, and non-negotiable <strong>Red Flag patient safety policies</strong>.
          </p>
        </div>
      </div>

      {/* Specialty Selector Tabs */}
      <div className="flex flex-wrap gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
        {NMCN_SPECIALTIES.map((spec, idx) => {
          const isSelected = idx === selectedSpecialtyIndex;
          const icons = ['🩺', '👶', '🧸', '💉', '🚑'];
          return (
            <button
              key={spec.id}
              onClick={() => handleSelectSpecialty(idx)}
              className={`px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition-all flex items-center gap-2 cursor-pointer ${
                isSelected
                  ? 'bg-blue-600 text-white shadow-md shadow-blue-600/30 ring-2 ring-blue-400/40'
                  : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 hover:border-blue-400'
              }`}
            >
              <span>{icons[idx]}</span>
              <span>{spec.title}</span>
            </button>
          );
        })}
      </div>

      {/* Sub-Tabs: Blueprint / Practical Simulation / MCQs / Evaluation */}
      <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-900 p-1.5 rounded-xl border border-slate-200 dark:border-slate-800 w-fit text-xs font-semibold">
        <button
          onClick={() => setActiveSubTab('blueprint')}
          className={`px-4 py-2 rounded-lg transition-colors ${
            activeSubTab === 'blueprint'
              ? 'bg-blue-600 text-white'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
          }`}
        >
          📋 Statutory Blueprint
        </button>
        <button
          onClick={() => setActiveSubTab('practical')}
          className={`px-4 py-2 rounded-lg transition-colors ${
            activeSubTab === 'practical'
              ? 'bg-blue-600 text-white'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
          }`}
        >
          🩺 Practical Simulation (10 Steps)
        </button>
        <button
          onClick={() => setActiveSubTab('mcq')}
          className={`px-4 py-2 rounded-lg transition-colors ${
            activeSubTab === 'mcq'
              ? 'bg-blue-600 text-white'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
          }`}
        >
          📝 Licensure MCQs (10 Qs)
        </button>
        <button
          onClick={() => setActiveSubTab('result')}
          className={`px-4 py-2 rounded-lg transition-colors ${
            activeSubTab === 'result'
              ? 'bg-blue-600 text-white'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
          }`}
        >
          📊 Council Evaluation ({compositePct.toFixed(0)}%)
        </button>
      </div>

      {/* SubTab 1: Statutory Blueprint */}
      {activeSubTab === 'blueprint' && (
        <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 space-y-6 shadow-sm">
          <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
            <div>
              <span className="text-xs font-mono font-bold text-blue-600 dark:text-blue-400">
                {currentSpecialty.code}
              </span>
              <h2 className="text-xl font-bold text-slate-900 dark:text-white">
                {currentSpecialty.regulatoryTitle}
              </h2>
            </div>
            <span className="px-3 py-1 rounded-full text-xs font-bold bg-blue-50 dark:bg-blue-950 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
              Pass Mark: 50.0%
            </span>
          </div>

          <p className="text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
            {currentSpecialty.description}
          </p>

          <div className="space-y-3">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-500">
              Statutory Competency Domains (NMCN Directives)
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {currentSpecialty.competencyDomains.map((dom, i) => (
                <div
                  key={i}
                  className="p-3 rounded-xl bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 text-xs font-semibold text-slate-800 dark:text-slate-200 flex items-center gap-2.5"
                >
                  <span className="w-5 h-5 rounded-full bg-blue-100 dark:bg-blue-900/60 text-blue-600 dark:text-blue-400 flex items-center justify-center font-bold text-[10px]">
                    {i + 1}
                  </span>
                  <span>{dom}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex justify-end">
            <button
              onClick={() => setActiveSubTab('practical')}
              className="px-6 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-blue-600 hover:bg-blue-500 text-white shadow-md transition-colors"
            >
              Enter Practical Clinical Simulation →
            </button>
          </div>
        </div>
      )}

      {/* SubTab 2: Practical Clinical Simulation */}
      {activeSubTab === 'practical' && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Left Column: Dossier & Vitals (5 cols) */}
          <div className="lg:col-span-5 space-y-5">
            {/* Door Briefing */}
            <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 shadow-sm space-y-3">
              <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-blue-600 dark:text-blue-400">
                  Door Briefing
                </span>
                <span className="text-xs text-slate-400">{station.patientProfile.setting}</span>
              </div>
              <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
                {station.doorBriefing}
              </p>
            </div>

            {/* Patient Telemetry & Dossier */}
            <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 shadow-sm space-y-4">
              <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">
                  Standardized Patient Dossier
                </span>
                <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                  {station.patientProfile.name}, {station.patientProfile.age}
                </span>
              </div>

              {/* Vitals Box */}
              <div className="bg-slate-950 text-emerald-400 p-3.5 rounded-xl border border-emerald-900/40 font-mono text-xs space-y-2">
                <div className="text-[10px] text-emerald-500 uppercase tracking-widest font-bold flex items-center justify-between">
                  <span>Entrance Vital Signs</span>
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                </div>
                <div className="grid grid-cols-2 gap-2 text-[11px]">
                  <div>BP: <strong className="text-white">{station.entryVitals.bloodPressure}</strong></div>
                  <div>HR: <strong className="text-white">{station.entryVitals.heartRate}</strong></div>
                  <div>RR: <strong className="text-white">{station.entryVitals.respiratoryRate}</strong></div>
                  <div>Temp: <strong className="text-white">{station.entryVitals.temperature}</strong></div>
                  <div className="col-span-2">SpO2: <strong className="text-white">{station.entryVitals.oxygenSaturation}</strong></div>
                </div>
                {station.entryVitals.painOrDistressScore && (
                  <div className="pt-1.5 border-t border-emerald-900/60 text-amber-300 text-[11px]">
                    Status: {station.entryVitals.painOrDistressScore}
                  </div>
                )}
              </div>

              {/* Equipment Tray */}
              <div>
                <span className="text-xs font-bold text-slate-700 dark:text-slate-300 block mb-1.5">
                  Required Equipment & Drug Tray:
                </span>
                <div className="flex flex-wrap gap-1.5">
                  {station.equipmentTray.map((eq, i) => (
                    <span
                      key={i}
                      className="px-2 py-0.5 rounded text-[11px] bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700"
                    >
                      {eq}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Right Column: 10-Step Practical Checklist (7 cols) */}
          <div className="lg:col-span-7 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 shadow-sm space-y-5">
            <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
              <div>
                <h3 className="font-bold text-lg text-slate-900 dark:text-white">
                  10-Step Psychomotor Checklist
                </h3>
                <p className="text-xs text-slate-500">
                  Select each clinical action as you execute the simulated procedure.
                </p>
              </div>
              <div className="text-right">
                <span className="text-xs text-slate-400">Score:</span>
                <div className="text-lg font-bold font-mono text-blue-600 dark:text-blue-400">
                  {rawPractical} / 100 Pts
                </div>
              </div>
            </div>

            {/* Red Flag Notice */}
            <div className="p-3 rounded-lg bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/50 text-xs text-rose-800 dark:text-rose-300 flex items-start gap-2">
              <span className="text-base">🚨</span>
              <div className="leading-relaxed">
                <strong>Statutory Fatal Error Policy:</strong> Omitting any step flagged with{' '}
                <span className="font-bold text-rose-600">⚡ RED FLAG</span> caps practical points at 49% and causes immediate station referral.
              </div>
            </div>

            {/* Checklist Items */}
            <div className="space-y-3">
              {station.checklist.map((item) => {
                const isChecked = !!checkedItems[item.id];
                return (
                  <div
                    key={item.id}
                    onClick={() => handleToggleChecklist(item)}
                    className={`p-3.5 rounded-xl border transition-all cursor-pointer select-none ${
                      isChecked
                        ? 'bg-blue-50/60 dark:bg-blue-950/40 border-blue-500/60 shadow-sm'
                        : 'bg-slate-50 dark:bg-slate-950/40 border-slate-200 dark:border-slate-800 hover:border-slate-300'
                    }`}
                  >
                    <div className="flex items-start gap-3">
                      <input
                        type="checkbox"
                        checked={isChecked}
                        onChange={() => {}} // parent onClick
                        className="mt-1 w-4 h-4 rounded text-blue-600 focus:ring-blue-500 border-slate-300"
                      />
                      <div className="flex-1 space-y-1">
                        <div className="flex items-center justify-between text-xs">
                          <span className="font-bold text-slate-700 dark:text-slate-300">
                            Step {item.stepNumber}: {item.category}
                          </span>
                          <div className="flex items-center gap-2">
                            {item.isCriticalFail && (
                              <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300 border border-rose-300 dark:border-rose-800">
                                ⚡ RED FLAG
                              </span>
                            )}
                            <span className="font-mono font-bold text-blue-600 dark:text-blue-400">
                              +{item.points} pts
                            </span>
                          </div>
                        </div>
                        <p className="text-xs sm:text-sm font-medium text-slate-900 dark:text-slate-100 leading-snug">
                          {item.instruction}
                        </p>
                        <p className="text-xs text-slate-500 dark:text-slate-400 italic pt-0.5">
                          Rationale: {item.rationale}
                        </p>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Footer */}
            <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
              <span className="text-xs text-slate-500">
                {Object.values(checkedItems).filter(Boolean).length} of 10 steps completed
              </span>
              <button
                onClick={() => setActiveSubTab('mcq')}
                className="px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-blue-600 hover:bg-blue-500 text-white shadow-md transition-colors"
              >
                Proceed to Licensure MCQs →
              </button>
            </div>
          </div>
        </div>
      )}

      {/* SubTab 3: Licensure MCQs */}
      {activeSubTab === 'mcq' && (
        <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 space-y-6 shadow-sm">
          <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
            <div>
              <h3 className="font-bold text-lg text-slate-900 dark:text-white">
                10 Scenario-Linked Professional Licensure MCQs
              </h3>
              <p className="text-xs text-slate-500">
                Calibrated to the NMCN Examination Committee standards and clinical rationale benchmarks.
              </p>
            </div>
            <div className="text-right">
              <span className="text-xs text-slate-400">Answered:</span>
              <div className="text-base font-bold font-mono text-blue-600 dark:text-blue-400">
                {Object.values(mcqAnswers).filter(Boolean).length} / 10
              </div>
            </div>
          </div>

          <div className="space-y-6">
            {station.mcqs.map((q, qIndex) => (
              <div
                key={q.id}
                className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/30 space-y-3"
              >
                <div className="flex items-center justify-between text-xs">
                  <span className="font-bold text-blue-600 dark:text-blue-400">
                    Question {qIndex + 1} of 10
                  </span>
                  <span className="text-slate-400 text-[11px]">{q.learningDomain}</span>
                </div>

                <p className="text-xs sm:text-sm font-semibold text-slate-900 dark:text-slate-100 leading-snug">
                  {q.questionText}
                </p>

                <div className="space-y-2 pt-1">
                  {q.options.map((opt) => {
                    const isSelected = mcqAnswers[q.id] === opt.id;
                    const hasAnswered = mcqAnswers[q.id] !== undefined && mcqAnswers[q.id] !== null;
                    const isCorrect = mcqAnswers[q.id] === q.correctAnswer;
                    const isCorrectOpt = opt.id === q.correctAnswer;

                    let optionStyle = 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:border-blue-400';

                    if (hasAnswered) {
                      if (isCorrectOpt) {
                        optionStyle = 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 border-emerald-500 font-semibold ring-1 ring-emerald-500';
                      } else if (isSelected && !isCorrect) {
                        optionStyle = 'bg-rose-50 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 border-rose-500 font-medium ring-1 ring-rose-500';
                      } else {
                        optionStyle = 'bg-white dark:bg-slate-900 text-slate-400 dark:text-slate-500 border-slate-200 dark:border-slate-800 opacity-60';
                      }
                    }

                    return (
                      <button
                        key={opt.id}
                        onClick={() => handleSelectMCQ(q.id, opt.id)}
                        className={`w-full text-left p-3 rounded-lg border text-xs sm:text-sm transition-all flex items-start gap-2.5 ${optionStyle}`}
                      >
                        <span
                          className={`w-5 h-5 rounded-full flex items-center justify-center font-bold text-xs shrink-0 ${
                            hasAnswered && isCorrectOpt
                              ? 'bg-emerald-600 text-white'
                              : hasAnswered && isSelected && !isCorrect
                              ? 'bg-rose-600 text-white'
                              : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                          }`}
                        >
                          {opt.id}
                        </span>
                        <span className="leading-snug flex-1">{opt.text}</span>
                        {hasAnswered && isCorrectOpt && (
                          <span className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 shrink-0">
                            ✓ Statutory Correct
                          </span>
                        )}
                        {hasAnswered && isSelected && !isCorrect && (
                          <span className="text-[10px] font-bold text-rose-600 dark:text-rose-400 shrink-0">
                            ✕ Your Choice
                          </span>
                        )}
                      </button>
                    );
                  })}
                </div>

                {mcqAnswers[q.id] && (() => {
                  const chosenId = mcqAnswers[q.id];
                  const isCorrect = chosenId === q.correctAnswer;
                  const correctOpt = q.options.find((o) => o.id === q.correctAnswer);
                  const chosenOpt = q.options.find((o) => o.id === chosenId);

                  return (
                    <div
                      className={`mt-3 p-4 rounded-xl border text-xs sm:text-sm space-y-2.5 animate-fadeIn ${
                        !isCorrect
                          ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
                          : 'bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60'
                      }`}
                    >
                      <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-200/60 dark:border-slate-800/60">
                        <div className="flex items-center gap-2 font-bold">
                          {!isCorrect ? (
                            <span className="text-rose-700 dark:text-rose-300 flex items-center gap-1.5 font-bold">
                              <span>✕</span> Incorrect Answer Supplied — Tutorial Support Active
                            </span>
                          ) : (
                            <span className="text-emerald-700 dark:text-emerald-300 flex items-center gap-1.5 font-bold">
                              <span>✓</span> Correct Statutory Answer! Well done.
                            </span>
                          )}
                        </div>
                        {!isCorrect && (
                          <button
                            onClick={() => {
                              setMcqAnswers((prev) => {
                                const next = { ...prev };
                                delete next[q.id];
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
                          <span className="font-bold shrink-0">✓ Statutory Correct Answer:</span>
                          <span>
                            Option {q.correctAnswer} — {correctOpt?.text}
                          </span>
                        </div>
                        {!isCorrect && chosenOpt && (
                          <div className="flex items-start gap-1.5 text-rose-700 dark:text-rose-400">
                            <span className="font-bold shrink-0">✕ Your Choice:</span>
                            <span>
                              Option {chosenOpt.id} — {chosenOpt.text}
                            </span>
                          </div>
                        )}
                      </div>

                      {/* Rationale */}
                      <div className="p-3 rounded-lg bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 space-y-1">
                        <strong className="text-slate-900 dark:text-white block font-bold text-xs uppercase tracking-wide">
                          NMCN Licensure Clinical Explanation:
                        </strong>
                        <p className="leading-relaxed text-xs">
                          {q.explanation}
                        </p>
                      </div>
                    </div>
                  );
                })()}
              </div>
            ))}
          </div>

          <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex justify-end">
            <button
              onClick={() => setActiveSubTab('result')}
              className="px-6 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-blue-600 hover:bg-blue-500 text-white shadow-md transition-colors"
            >
              View Statutory Determination →
            </button>
          </div>
        </div>
      )}

      {/* SubTab 4: Statutory Council Determination Result */}
      {activeSubTab === 'result' && (
        <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 space-y-6 shadow-sm">
          <div className="text-center space-y-1 border-b border-slate-100 dark:border-slate-800 pb-4">
            <span className="text-xs uppercase font-bold tracking-widest text-blue-600 dark:text-blue-400">
              Statutory Evaluation Result
            </span>
            <h2 className="text-2xl font-black text-slate-900 dark:text-white">
              {currentSpecialty.regulatoryTitle}
            </h2>
            <p className="text-xs text-slate-500">Candidate: {candidateName}</p>
          </div>

          {/* Outcome Banner */}
          <div
            className={`p-6 rounded-2xl border text-center space-y-2 ${
              isDistinction
                ? 'bg-purple-50 dark:bg-purple-950/40 border-purple-300 dark:border-purple-800 text-purple-900 dark:text-purple-200'
                : isPassed
                ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200'
                : 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-200'
            }`}
          >
            <span className="text-xs uppercase font-extrabold tracking-widest block opacity-75">
              NMCN Licensure Grade
            </span>
            <div className="text-3xl font-black">
              {isDistinction
                ? 'STATUTORY DISTINCTION (≥ 75%)'
                : isPassed
                ? 'STATUTORY PASS (≥ 50%)'
                : hasRedFlag
                ? 'STATION REFERRED (RED FLAG SAFETY VIOLATION)'
                : 'FAILED (BELOW 50% BENCHMARK)'}
            </div>
            <div className="text-sm font-semibold opacity-90">
              Composite Specialty Score: <strong>{compositePct.toFixed(1)}%</strong> (Practical: {practicalPct.toFixed(0)}% | MCQs: {mcqPct.toFixed(0)}%)
            </div>
          </div>

          {/* Safety Violations Notice */}
          {hasRedFlag && (
            <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-300 dark:border-rose-900 text-rose-900 dark:text-rose-200 space-y-2 text-xs">
              <div className="font-bold text-sm text-rose-700 dark:text-rose-300 flex items-center gap-1.5">
                <span>⚠️</span> Critical Red Flag Safety Violation:
              </div>
              <ul className="list-disc list-inside space-y-1">
                {missedRedFlags.map((item) => (
                  <li key={item.id}>
                    <strong>Step {item.stepNumber}:</strong> {item.instruction} ({item.criticalFailReason || item.rationale})
                  </li>
                ))}
              </ul>
              <p className="text-[11px] text-rose-700 dark:text-rose-400 pt-1">
                Note: In accordance with statutory council policy, committing or omitting a critical fail step automatically caps the practical mark at 49%, requiring station remedial training.
              </p>
            </div>
          )}

          {/* Score Matrix Table */}
          <div className="overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <table className="w-full text-left">
              <thead className="bg-slate-100 dark:bg-slate-800 font-bold text-slate-700 dark:text-slate-300">
                <tr>
                  <th className="py-2.5 px-4">Evaluation Dimension</th>
                  <th className="py-2.5 px-4 text-center">Score Earned</th>
                  <th className="py-2.5 px-4 text-center">Pass Threshold</th>
                  <th className="py-2.5 px-4 text-right">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 dark:divide-slate-800 text-slate-800 dark:text-slate-200">
                <tr>
                  <td className="py-2.5 px-4 font-semibold">Practical Psychomotor Checklist</td>
                  <td className="py-2.5 px-4 text-center font-mono">
                    {rawPractical} pts {hasRedFlag && <span className="text-rose-500">(Capped 49%)</span>}
                  </td>
                  <td className="py-2.5 px-4 text-center font-mono">50 pts (50%)</td>
                  <td className="py-2.5 px-4 text-right font-bold">
                    {practicalPct >= 50 ? <span className="text-emerald-600">PASS</span> : <span className="text-rose-600">REFERRAL</span>}
                  </td>
                </tr>
                <tr>
                  <td className="py-2.5 px-4 font-semibold">10 Scenario-Linked Licensure MCQs</td>
                  <td className="py-2.5 px-4 text-center font-mono">{mcqCorrect} / 10 ({mcqPct.toFixed(0)}%)</td>
                  <td className="py-2.5 px-4 text-center font-mono">5 / 10 (50%)</td>
                  <td className="py-2.5 px-4 text-right font-bold">
                    {mcqPct >= 50 ? <span className="text-emerald-600">PASS</span> : <span className="text-rose-600">FAIL</span>}
                  </td>
                </tr>
                <tr className="bg-slate-50 dark:bg-slate-950/60 font-bold">
                  <td className="py-2.5 px-4">Composite Specialty Licensure Mark</td>
                  <td className="py-2.5 px-4 text-center font-mono text-blue-600 dark:text-blue-400">{compositePct.toFixed(1)}%</td>
                  <td className="py-2.5 px-4 text-center font-mono">50.0%</td>
                  <td className="py-2.5 px-4 text-right">
                    {isPassed ? <span className="text-emerald-600">COUNCIL PASS</span> : <span className="text-rose-600">REFERRAL</span>}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
            <button
              onClick={() => {
                setCheckedItems({});
                setMcqAnswers({});
                setActiveSubTab('practical');
              }}
              className="text-xs font-semibold text-slate-500 hover:text-slate-800 dark:hover:text-slate-200"
            >
              🔄 Reset Station & Retake
            </button>

            <button
              onClick={onNavigateHome}
              className="px-6 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition-colors"
            >
              Return to WAPCNM Mental Health Flagship →
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
