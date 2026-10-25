/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { CAOSCE_STATIONS } from '../../data/caosceStations';
import { NGN_CASE_STUDIES } from '../../data/ngnCaseStudies';
import { PSYCHOPHARM_MATH_PROBLEMS } from '../../data/psychopharmMath';
import { CAOSCEReport, CAOSCEMode } from '../../types/clinicalExams';

interface ClinicalExamCenterProps {
  candidateName: string;
  caosceReports: CAOSCEReport[];
  onStartCAOSCE: (mode: CAOSCEMode, specificStationNumber?: number) => void;
  onStartNGNCase: (caseId: string) => void;
  onStartPsychopharmMath: (problemId?: string) => void;
  onOpenCAOSCEReport: (reportId: string) => void;
}

export const ClinicalExamCenter: React.FC<ClinicalExamCenterProps> = ({
  candidateName,
  caosceReports,
  onStartCAOSCE,
  onStartNGNCase,
  onStartPsychopharmMath,
  onOpenCAOSCEReport,
}) => {
  const [activeTab, setActiveTab] = useState<'caosce' | 'ngn' | 'math' | 'history'>('caosce');
  const [selectedMode, setSelectedMode] = useState<CAOSCEMode>('strict-exam');

  const latestReport = caosceReports.length > 0 ? caosceReports[0] : null;

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Hero Header */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-indigo-900 via-slate-900 to-teal-950 p-8 text-white shadow-xl border border-indigo-500/20">
        <div className="relative z-10 max-w-4xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 mb-4">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            Postgraduate Fellowship Accreditation Standard (WAPCNM Faculty of Mental Health & Psychiatric Nursing)
          </div>
          <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight text-white mb-3">
            Postgraduate Mental Health Clinical Examination Suites
          </h1>
          <p className="text-slate-300 text-base md:text-lg leading-relaxed">
            High-fidelity simulated clinical assessments designed for postgraduate psychiatric nurse specialists.
            Evaluate psychomotor de-escalation, rapid tranquilization, high-lethality suicide prevention, psychopharmacologic emergencies, and statutory mental health law.
          </p>

          <div className="mt-6 flex flex-wrap gap-4 text-xs md:text-sm text-slate-300">
            <div className="flex items-center gap-2 bg-white/10 px-3 py-1.5 rounded-lg backdrop-blur-sm">
              <span className="font-bold text-emerald-400">70% Pass Mark</span> Fellowship Criterion
            </div>
            <div className="flex items-center gap-2 bg-white/10 px-3 py-1.5 rounded-lg backdrop-blur-sm">
              <span className="font-bold text-amber-400">Red Flag Policy</span> Fatal Patient Safety Referrals
            </div>
            <div className="flex items-center gap-2 bg-white/10 px-3 py-1.5 rounded-lg backdrop-blur-sm">
              <span className="font-bold text-cyan-400">Clock-Lockstep</span> 120-Min Synchronized Circuit
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Modality Tabs */}
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-4">
        <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-900 p-1.5 rounded-xl border border-slate-200 dark:border-slate-800">
          <button
            onClick={() => setActiveTab('caosce')}
            className={`px-4 py-2 rounded-lg text-sm font-semibold transition-all ${
              activeTab === 'caosce'
                ? 'bg-indigo-600 text-white shadow-md'
                : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            🎯 6-Station CAOSCE Circuit
          </button>
          <button
            onClick={() => setActiveTab('ngn')}
            className={`px-4 py-2 rounded-lg text-sm font-semibold transition-all ${
              activeTab === 'ngn'
                ? 'bg-indigo-600 text-white shadow-md'
                : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            📋 NGN Clinical Judgment Cases
          </button>
          <button
            onClick={() => setActiveTab('math')}
            className={`px-4 py-2 rounded-lg text-sm font-semibold transition-all ${
              activeTab === 'math'
                ? 'bg-indigo-600 text-white shadow-md'
                : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            💊 Psychopharm Titration & Math
          </button>
          <button
            onClick={() => setActiveTab('history')}
            className={`px-4 py-2 rounded-lg text-sm font-semibold transition-all ${
              activeTab === 'history'
                ? 'bg-indigo-600 text-white shadow-md'
                : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            📜 Clinical Records ({caosceReports.length})
          </button>
        </div>

        {activeTab === 'caosce' && (
          <div className="flex items-center gap-3">
            <span className="text-xs font-medium text-slate-500 dark:text-slate-400">Execution Mode:</span>
            <div className="inline-flex rounded-lg border border-slate-300 dark:border-slate-700 p-1 bg-white dark:bg-slate-900 text-xs font-semibold">
              <button
                onClick={() => setSelectedMode('strict-exam')}
                className={`px-3 py-1.5 rounded-md transition-colors ${
                  selectedMode === 'strict-exam'
                    ? 'bg-amber-600 text-white'
                    : 'text-slate-600 dark:text-slate-300 hover:text-slate-900'
                }`}
                title="Strict 20m/station lockstep timer with acoustic warning bells and fatal error referral"
              >
                ⏱️ Strict Exam Circuit (120m)
              </button>
              <button
                onClick={() => setSelectedMode('self-paced')}
                className={`px-3 py-1.5 rounded-md transition-colors ${
                  selectedMode === 'self-paced'
                    ? 'bg-teal-600 text-white'
                    : 'text-slate-600 dark:text-slate-300 hover:text-slate-900'
                }`}
                title="Untimed clinical exploration with instant step rationales and retries"
              >
                🌱 Self-Paced Training
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Tab 1: 6-Station CAOSCE Circuit */}
      {activeTab === 'caosce' && (
        <div className="space-y-6">
          <div className="bg-amber-50 dark:bg-amber-950/30 border border-amber-300 dark:border-amber-700/50 rounded-xl p-5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div className="space-y-1">
              <h3 className="font-bold text-amber-900 dark:text-amber-200 flex items-center gap-2">
                <span>⚠️</span> Non-Negotiable Patient Safety Policy ("Red Flag" Criteria)
              </h3>
              <p className="text-sm text-amber-800 dark:text-amber-300/90 leading-relaxed">
                In postgraduate psychiatric licensure, clinical knowledge without patient safety constitutes malpractice.
                Committing or omitting any predefined <strong>Red Flag</strong> (e.g. attempting to wrestle a weapon from an agitated psychotic patient, failing to enforce lethal means restriction, or infusing dextrose before parenteral thiamine) automatically caps the station practical mark at <strong>49% (Station Referral)</strong>.
              </p>
            </div>
            <button
              onClick={() => onStartCAOSCE(selectedMode)}
              className="whitespace-nowrap px-6 py-3 rounded-xl font-bold text-sm bg-gradient-to-r from-amber-600 to-indigo-600 text-white hover:from-amber-500 hover:to-indigo-500 shadow-lg shadow-amber-900/20 transition-all hover:scale-[1.02] flex items-center gap-2"
            >
              <span>🚀</span> Start Full 6-Station Circuit ({selectedMode === 'strict-exam' ? '120 Mins' : 'Self-Paced'})
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {CAOSCE_STATIONS.map((station) => (
              <div
                key={station.id}
                className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 flex flex-col justify-between hover:border-indigo-500 dark:hover:border-indigo-500 transition-all shadow-sm hover:shadow-md group"
              >
                <div>
                  <div className="flex items-center justify-between text-xs font-semibold mb-2">
                    <span className="px-2.5 py-1 rounded-md bg-indigo-50 dark:bg-indigo-950/50 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800">
                      Station {station.stationNumber} of 6
                    </span>
                    <span className="text-slate-500 dark:text-slate-400">
                      20 Mins (10m + 10m)
                    </span>
                  </div>

                  <h3 className="font-bold text-lg text-slate-900 dark:text-white group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors">
                    {station.title}
                  </h3>
                  <p className="text-xs font-medium text-slate-500 dark:text-slate-400 mt-0.5 mb-3">
                    {station.specialtyDomain}
                  </p>

                  <div className="bg-slate-50 dark:bg-slate-950/50 p-3 rounded-lg border border-slate-100 dark:border-slate-800/80 mb-4">
                    <div className="text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                      Standardized Patient: {station.patientProfile.name}, {station.patientProfile.age}y/o
                    </div>
                    <p className="text-xs text-slate-600 dark:text-slate-400 line-clamp-3 leading-relaxed">
                      {station.doorBriefing}
                    </p>
                  </div>

                  <div className="space-y-1.5 text-xs text-slate-600 dark:text-slate-400">
                    <div className="flex items-center gap-1.5">
                      <span className="text-emerald-500 font-bold">✓</span>
                      <span>10-Step Psychomotor Checklist (100 Pts)</span>
                    </div>
                    <div className="flex items-center gap-1.5">
                      <span className="text-amber-500 font-bold">⚡</span>
                      <span>
                        {station.checklist.filter((c) => c.isCriticalFail).length} Red Flag Safety Checkpoints
                      </span>
                    </div>
                    <div className="flex items-center gap-1.5">
                      <span className="text-indigo-500 font-bold">📝</span>
                      <span>10 Station-Linked Scenario MCQs (100 Pts)</span>
                    </div>
                  </div>
                </div>

                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <button
                    onClick={() => onStartCAOSCE('self-paced', station.stationNumber)}
                    className="text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-indigo-600 dark:hover:text-indigo-400"
                  >
                    Targeted Station Practice
                  </button>
                  <button
                    onClick={() => onStartCAOSCE(selectedMode, station.stationNumber)}
                    className="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-indigo-50 dark:bg-indigo-900/40 text-indigo-700 dark:text-indigo-300 hover:bg-indigo-600 hover:text-white transition-colors"
                  >
                    Launch Station →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Tab 2: NGN Clinical Judgment Cases */}
      {activeTab === 'ngn' && (
        <div className="space-y-6">
          <div className="bg-indigo-50 dark:bg-indigo-950/30 border border-indigo-200 dark:border-indigo-800/50 rounded-xl p-5">
            <h3 className="font-bold text-indigo-900 dark:text-indigo-200 flex items-center gap-2 mb-1">
              <span>📋</span> Next Generation NCLEX (NGN) Clinical Judgment Measurement Model
            </h3>
            <p className="text-sm text-indigo-800 dark:text-indigo-300/90 leading-relaxed">
              Step beyond isolated rote questions into progressive, unfolding clinical situations.
              Navigate the 6 cognitive layers defined by the NCSBN: <em>Recognize Cues</em>, <em>Analyze Cues</em>, <em>Prioritize Hypotheses</em>, <em>Generate Solutions</em>, <em>Take Action</em>, and <em>Evaluate Outcomes</em>.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {NGN_CASE_STUDIES.map((study) => (
              <div
                key={study.id}
                className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition-shadow"
              >
                <div>
                  <span className="inline-block px-2.5 py-1 rounded-md text-xs font-semibold bg-purple-50 dark:bg-purple-950/50 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800 mb-3">
                    6-Stage Unfolding Case Study
                  </span>
                  <h3 className="text-xl font-bold text-slate-900 dark:text-white mb-1">
                    {study.title}
                  </h3>
                  <p className="text-xs font-medium text-slate-500 dark:text-slate-400 mb-3">
                    {study.subtitle}
                  </p>
                  <p className="text-sm text-slate-600 dark:text-slate-300 leading-relaxed mb-4">
                    {study.clinicalSummary}
                  </p>

                  <div className="bg-slate-50 dark:bg-slate-950/50 p-3 rounded-lg border border-slate-100 dark:border-slate-800 text-xs space-y-1">
                    <div><strong>Patient:</strong> {study.patientDemographics.name}, {study.patientDemographics.age}y/o ({study.patientDemographics.gender})</div>
                    <div><strong>Diagnosis:</strong> {study.patientDemographics.admissionDiagnosis}</div>
                  </div>
                </div>

                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <span className="text-xs text-slate-500">6 Cognitive Assessment Stages</span>
                  <button
                    onClick={() => onStartNGNCase(study.id)}
                    className="px-4 py-2 rounded-lg text-xs font-bold bg-indigo-600 text-white hover:bg-indigo-500 transition-colors shadow-sm"
                  >
                    Open Case Study →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Tab 3: Psychopharmacology Titration & Math Lab */}
      {activeTab === 'math' && (
        <div className="space-y-6">
          <div className="bg-teal-50 dark:bg-teal-950/30 border border-teal-200 dark:border-teal-800/50 rounded-xl p-5">
            <h3 className="font-bold text-teal-900 dark:text-teal-200 flex items-center gap-2 mb-1">
              <span>💊</span> Advanced Neuropsychiatric Pharmacology & Clinical Mathematics
            </h3>
            <p className="text-sm text-teal-800 dark:text-teal-300/90 leading-relaxed">
              Calculate critical clinical boundaries in high-risk psychopharmacology: Cockcroft-Gault creatinine clearance for lithium titration, Clozapine Absolute Neutrophil Count (ANC) REMS thresholds, long-acting depot conversions, and Bazett QTc interval prolongation formulas.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {PSYCHOPHARM_MATH_PROBLEMS.map((problem) => (
              <div
                key={problem.id}
                className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition-shadow"
              >
                <div>
                  <span className="inline-block px-2.5 py-1 rounded-md text-xs font-semibold bg-teal-50 dark:bg-teal-950/50 text-teal-700 dark:text-teal-300 border border-teal-200 dark:border-teal-800 mb-3">
                    {problem.category}
                  </span>
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white mb-2">
                    {problem.title}
                  </h3>
                  <p className="text-xs text-slate-600 dark:text-slate-300 line-clamp-3 leading-relaxed mb-4">
                    {problem.clinicalScenario}
                  </p>

                  <div className="bg-slate-50 dark:bg-slate-950/50 p-3 rounded-lg border border-slate-100 dark:border-slate-800 text-xs text-slate-700 dark:text-slate-300">
                    <span className="font-semibold text-teal-600 dark:text-teal-400">Clinical Focus:</span>{' '}
                    {problem.clinicalSignificance}
                  </div>
                </div>

                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <span className="text-xs text-slate-500">Formulas & Step-by-Step Proof</span>
                  <button
                    onClick={() => onStartPsychopharmMath(problem.id)}
                    className="px-4 py-2 rounded-lg text-xs font-bold bg-teal-600 text-white hover:bg-teal-500 transition-colors shadow-sm"
                  >
                    Solve Problem →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Tab 4: Clinical Exam History */}
      {activeTab === 'history' && (
        <div className="space-y-6">
          <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 shadow-sm">
            <h3 className="font-bold text-lg text-slate-900 dark:text-white mb-2">
              Official Postgraduate Clinical Examination Dossiers
            </h3>
            <p className="text-sm text-slate-600 dark:text-slate-400 mb-6">
              Review your completed CAOSCE circuits, station-by-station breakdowns, and official statutory remedial directives.
            </p>

            {caosceReports.length === 0 ? (
              <div className="text-center py-12 border-2 border-dashed border-slate-200 dark:border-slate-800 rounded-xl">
                <span className="text-4xl mb-3 block">📜</span>
                <h4 className="font-bold text-slate-800 dark:text-slate-200 text-base mb-1">
                  No Clinical Examination Records Found
                </h4>
                <p className="text-xs text-slate-500 max-w-md mx-auto mb-4">
                  Complete the 6-Station CAOSCE Circuit to generate your official WAPCNM / NMCN clinical examination result dossier.
                </p>
                <button
                  onClick={() => onStartCAOSCE('strict-exam')}
                  className="px-4 py-2 rounded-lg text-xs font-bold bg-indigo-600 text-white hover:bg-indigo-500"
                >
                  Start First CAOSCE Circuit
                </button>
              </div>
            ) : (
              <div className="divide-y divide-slate-100 dark:divide-slate-800">
                {caosceReports.map((report) => (
                  <div key={report.id} className="py-4 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                    <div>
                      <div className="flex items-center gap-2 mb-1">
                        <span className="font-bold text-slate-900 dark:text-white text-sm">
                          {report.examinationTitle}
                        </span>
                        <span
                          className={`px-2 py-0.5 rounded text-[11px] font-bold ${
                            report.overallStatus === 'DISTINCTION'
                              ? 'bg-purple-100 text-purple-800 dark:bg-purple-950/60 dark:text-purple-300'
                              : report.overallStatus === 'PASS'
                              ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300'
                              : 'bg-rose-100 text-rose-800 dark:bg-rose-950/60 dark:text-rose-300'
                          }`}
                        >
                          {report.overallStatus}
                        </span>
                      </div>
                      <div className="text-xs text-slate-500 flex items-center gap-3">
                        <span>{new Date(report.dateTimestamp).toLocaleString()}</span>
                        <span>•</span>
                        <span>Score: <strong>{report.overallCompositePercentage.toFixed(1)}%</strong></span>
                        <span>•</span>
                        <span>Mode: {report.mode === 'strict-exam' ? 'Strict 120m Circuit' : 'Self-Paced Training'}</span>
                        {report.totalCriticalFails > 0 && (
                          <span className="text-rose-600 dark:text-rose-400 font-semibold">
                            ⚠️ {report.totalCriticalFails} Red Flag Violation(s)
                          </span>
                        )}
                      </div>
                    </div>

                    <button
                      onClick={() => onOpenCAOSCEReport(report.id)}
                      className="px-4 py-2 rounded-lg text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-indigo-600 hover:text-white transition-colors"
                    >
                      View Official Dossier →
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
