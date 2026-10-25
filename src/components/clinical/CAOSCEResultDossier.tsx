/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { CAOSCEReport } from '../../types/clinicalExams';
import { CAOSCE_STATIONS } from '../../data/caosceStations';

interface CAOSCEResultDossierProps {
  report: CAOSCEReport;
  onBackToCenter: () => void;
  onRetakeCircuit: () => void;
}

export const CAOSCEResultDossier: React.FC<CAOSCEResultDossierProps> = ({
  report,
  onBackToCenter,
  onRetakeCircuit,
}) => {
  const isPassed = report.overallStatus === 'PASS' || report.overallStatus === 'DISTINCTION';
  const hasSafetyViolations = report.totalCriticalFails > 0;

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="space-y-8 animate-fadeIn max-w-5xl mx-auto pb-16">
      {/* Top Action Bar (hidden on print) */}
      <div className="flex items-center justify-between gap-4 print:hidden">
        <button
          onClick={onBackToCenter}
          className="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors"
        >
          ← Return to Clinical Exam Center
        </button>

        <div className="flex items-center gap-3">
          <button
            onClick={onRetakeCircuit}
            className="px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold bg-indigo-50 dark:bg-indigo-950/50 text-indigo-700 dark:text-indigo-300 border border-indigo-300 dark:border-indigo-800 hover:bg-indigo-600 hover:text-white transition-colors"
          >
            🔄 Retake Examination
          </button>
          <button
            onClick={handlePrint}
            className="px-5 py-2 rounded-xl text-xs sm:text-sm font-bold bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition-colors flex items-center gap-2"
          >
            <span>🖨️</span> Print Official Dossier
          </button>
        </div>
      </div>

      {/* Official Examination Result Dossier Sheet */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-10 shadow-xl space-y-8 print:border-none print:shadow-none print:p-0">
        {/* Statutory Header */}
        <div className="text-center space-y-2 border-b border-slate-200 dark:border-slate-800 pb-6">
          <div className="text-xs uppercase tracking-widest font-bold text-indigo-600 dark:text-indigo-400">
            West African Postgraduate College of Nurses & Midwives (WAPCNM)
          </div>
          <h1 className="text-2xl sm:text-3xl font-black text-slate-900 dark:text-white tracking-tight">
            OFFICIAL CLINICAL EXAMINATION RESULT DOSSIER
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 max-w-2xl mx-auto">
            Autonomous Computer-Assisted Objective Structured Clinical Examination (CAOSCE)
            <br />
            Postgraduate Mental Health & Psychiatric Nursing Specialty Fellowship Licensure
          </p>
        </div>

        {/* Candidate & Assessment Metadata */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-950/50 border border-slate-100 dark:border-slate-800 text-xs">
          <div>
            <span className="text-slate-400 block mb-0.5">Candidate Name:</span>
            <strong className="text-slate-900 dark:text-white text-sm">{report.candidateName}</strong>
          </div>
          <div>
            <span className="text-slate-400 block mb-0.5">Dossier Serial:</span>
            <strong className="font-mono text-slate-900 dark:text-white">{report.id}</strong>
          </div>
          <div>
            <span className="text-slate-400 block mb-0.5">Examination Date:</span>
            <strong className="text-slate-900 dark:text-white">
              {new Date(report.dateTimestamp).toLocaleDateString(undefined, {
                dateStyle: 'medium',
              })}
            </strong>
          </div>
          <div>
            <span className="text-slate-400 block mb-0.5">Circuit Execution:</span>
            <strong className="text-slate-900 dark:text-white">
              {report.mode === 'strict-exam' ? 'Strict 120m Circuit' : 'Self-Paced Training'}
            </strong>
          </div>
        </div>

        {/* Big Outcome Banner */}
        <div
          className={`p-6 rounded-2xl border text-center space-y-2 ${
            report.overallStatus === 'DISTINCTION'
              ? 'bg-purple-50 dark:bg-purple-950/40 border-purple-300 dark:border-purple-800 text-purple-900 dark:text-purple-200'
              : report.overallStatus === 'PASS'
              ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200'
              : report.overallStatus === 'REFERRAL (SAFETY VIOLATION)'
              ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-400 dark:border-rose-800 text-rose-950 dark:text-rose-200'
              : 'bg-slate-100 dark:bg-slate-800 border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-200'
          }`}
        >
          <span className="text-xs uppercase font-extrabold tracking-widest block opacity-75">
            Examination Board Determination
          </span>
          <div className="text-3xl sm:text-4xl font-black tracking-tight">
            {report.overallStatus}
          </div>
          <div className="text-sm font-semibold opacity-90">
            Composite Fellowship Score: <strong>{report.overallCompositePercentage.toFixed(1)}%</strong>{' '}
            (Benchmark Pass Mark: 70.0% | Distinction: 85.0%)
          </div>
        </div>

        {/* Safety Alert Box (if critical fails triggered) */}
        {hasSafetyViolations && (
          <div className="p-5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-300 dark:border-rose-900 text-rose-900 dark:text-rose-200 space-y-3">
            <div className="flex items-center gap-2 font-bold text-sm sm:text-base text-rose-700 dark:text-rose-300">
              <span className="text-xl">⚠️</span>
              <span>PATIENT SAFETY "RED FLAG" VIOLATIONS DETECTED ({report.totalCriticalFails})</span>
            </div>
            <p className="text-xs sm:text-sm leading-relaxed text-rose-800 dark:text-rose-300/90">
              In accordance with statutory NMCN / WAPCNM regulations, candidates committing or omitting defined critical fail checkpoints receive an automatic station practical score cap of <strong>49% (Station Referral)</strong>, regardless of total points accumulated.
            </p>
            <div className="space-y-2 pt-1">
              {report.remedialDirectives.map((dir, idx) => (
                <div
                  key={idx}
                  className="bg-white/80 dark:bg-slate-900/80 p-3 rounded-lg border border-rose-200 dark:border-rose-900/60 text-xs font-medium text-rose-950 dark:text-rose-200"
                >
                  {dir}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Station-by-Station Breakdown Table */}
        <div className="space-y-3">
          <h3 className="font-bold text-base text-slate-900 dark:text-white uppercase tracking-wider text-xs">
            Station-by-Station Evaluation Matrix
          </h3>
          <div className="overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800">
            <table className="w-full text-left text-xs sm:text-sm">
              <thead className="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 uppercase tracking-wider text-[11px] font-bold">
                <tr>
                  <th className="py-3 px-4">Station</th>
                  <th className="py-3 px-4">Domain Specialization</th>
                  <th className="py-3 px-4 text-center">Practical (100 Pts)</th>
                  <th className="py-3 px-4 text-center">MCQs (10 Qs)</th>
                  <th className="py-3 px-4 text-center">Composite %</th>
                  <th className="py-3 px-4 text-center">Red Flag Status</th>
                  <th className="py-3 px-4 text-right">Result</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100 dark:divide-slate-800 text-slate-800 dark:text-slate-200">
                {report.stationSubmissions.map((sub) => {
                  const stationMeta = CAOSCE_STATIONS.find((s) => s.id === sub.stationId);
                  return (
                    <tr
                      key={sub.stationId}
                      className={
                        sub.criticalFailTriggered
                          ? 'bg-rose-50/40 dark:bg-rose-950/20'
                          : 'hover:bg-slate-50 dark:hover:bg-slate-800/40'
                      }
                    >
                      <td className="py-3 px-4 font-bold">Station {sub.stationNumber}</td>
                      <td className="py-3 px-4">
                        <div className="font-semibold">{stationMeta?.title}</div>
                        <div className="text-[11px] text-slate-400">{stationMeta?.specialtyDomain}</div>
                      </td>
                      <td className="py-3 px-4 text-center font-mono">
                        {sub.practicalScore} pts
                        {sub.criticalFailTriggered && (
                          <span className="block text-[10px] text-rose-500 font-bold">Capped 49%</span>
                        )}
                      </td>
                      <td className="py-3 px-4 text-center font-mono">
                        {sub.mcqScore} / {sub.mcqMaxScore} ({sub.mcqPercentage.toFixed(0)}%)
                      </td>
                      <td className="py-3 px-4 text-center font-bold font-mono">
                        {sub.stationCompositePercentage.toFixed(1)}%
                      </td>
                      <td className="py-3 px-4 text-center">
                        {sub.criticalFailTriggered ? (
                          <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300">
                            ⚡ VIOLATED
                          </span>
                        ) : (
                          <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">
                            ✓ ZERO ERRORS
                          </span>
                        )}
                      </td>
                      <td className="py-3 px-4 text-right font-bold">
                        {sub.isStationPassed ? (
                          <span className="text-emerald-600 dark:text-emerald-400">PASSED</span>
                        ) : (
                          <span className="text-rose-600 dark:text-rose-400">REFERRED</span>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>

        {/* Detailed Station-by-Station Review */}
        <div className="space-y-6 pt-4 border-t border-slate-200 dark:border-slate-800">
          <h3 className="font-bold text-base text-slate-900 dark:text-white uppercase tracking-wider text-xs">
            Comprehensive Psychomotor Checklist Review
          </h3>

          <div className="space-y-6">
            {report.stationSubmissions.map((sub) => {
              const stationMeta = CAOSCE_STATIONS.find((s) => s.id === sub.stationId);
              if (!stationMeta) return null;

              return (
                <div
                  key={sub.stationId}
                  className="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/30 space-y-3"
                >
                  <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200 dark:border-slate-800 pb-2">
                    <span className="font-bold text-sm text-slate-900 dark:text-white">
                      Station {sub.stationNumber}: {stationMeta.title}
                    </span>
                    <span className="text-xs text-slate-500 font-mono">
                      Station Score: {sub.stationCompositePercentage.toFixed(1)}% |{' '}
                      {sub.isStationPassed ? 'PASSED' : 'REFERRED'}
                    </span>
                  </div>

                  <div className="space-y-2">
                    {stationMeta.checklist.map((item) => {
                      const wasSelected = !!sub.checklistSelections[item.id];
                      const isMissedRedFlag = item.isCriticalFail && !wasSelected;

                      return (
                        <div
                          key={item.id}
                          className={`p-2.5 rounded-lg border text-xs flex items-start gap-2.5 ${
                            isMissedRedFlag
                              ? 'bg-rose-50 dark:bg-rose-950/40 border-rose-300 dark:border-rose-900 text-rose-900 dark:text-rose-200'
                              : wasSelected
                              ? 'bg-emerald-50/50 dark:bg-emerald-950/20 border-emerald-200 dark:border-emerald-900/50 text-slate-800 dark:text-slate-200'
                              : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400'
                          }`}
                        >
                          <span className="font-bold text-sm shrink-0">
                            {wasSelected ? '✅' : isMissedRedFlag ? '🚨' : '⬜'}
                          </span>
                          <div className="flex-1 space-y-0.5">
                            <div className="flex items-center justify-between">
                              <span className="font-semibold">
                                Step {item.stepNumber}: {item.category}
                              </span>
                              {item.isCriticalFail && (
                                <span className="text-[10px] font-bold text-rose-600 dark:text-rose-400">
                                  CRITICAL RED FLAG
                                </span>
                              )}
                            </div>
                            <p className="leading-snug">{item.instruction}</p>
                            <p className="text-[11px] text-slate-500 dark:text-slate-400 italic pt-0.5">
                              Rationale: {item.rationale}
                            </p>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Regulatory Sign-off Footer */}
        <div className="pt-8 border-t border-slate-200 dark:border-slate-800 text-xs text-slate-500 text-center space-y-2">
          <p>
            Autonomous CAOSCE Clinical Simulation Engine certified under WAPCNM Postgraduate Examination Guidelines (Faculty of Mental Health & Psychiatric Nursing).
          </p>
          <div className="font-mono text-[11px]">
            Security Verification Hash: {report.id} • Verified Candidate: {report.candidateName}
          </div>
        </div>
      </div>
    </div>
  );
};
