/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useRef } from 'react';
import { CAOSCE_STATIONS } from '../../data/caosceStations';
import {
  CAOSCEStation,
  CAOSCEMode,
  StationCandidateSubmission,
  CAOSCEReport,
  ChecklistItem,
} from '../../types/clinicalExams';
import { AudioChimes } from '../../utils/audioChimes';

interface CAOSCESessionProps {
  candidateName: string;
  mode: CAOSCEMode;
  initialStationNumber?: number; // 1 to 6, or undefined for full circuit
  onFinish: (report: CAOSCEReport) => void;
  onCancel: () => void;
}

export const CAOSCESession: React.FC<CAOSCESessionProps> = ({
  candidateName,
  mode,
  initialStationNumber,
  onFinish,
  onCancel,
}) => {
  // If specific station requested, circuit has 1 station; otherwise full 6
  const stationPool = initialStationNumber
    ? CAOSCE_STATIONS.filter((s) => s.stationNumber === initialStationNumber)
    : CAOSCE_STATIONS;

  const [currentStationIndex, setCurrentStationIndex] = useState<number>(0);
  const currentStation: CAOSCEStation = stationPool[currentStationIndex] || stationPool[0];

  // Phase: 'practical' (10 mins) -> 'mcq' (10 mins) -> 'transition' (30s)
  const [currentPhase, setCurrentPhase] = useState<'practical' | 'mcq' | 'transition'>('practical');

  // Timers (in seconds). Strict mode: 600s each phase. Self-paced: counts up or toggleable
  const [secondsRemaining, setSecondsRemaining] = useState<number>(600);
  const [isPaused, setIsPaused] = useState<boolean>(false);
  const [isMuted, setIsMuted] = useState<boolean>(AudioChimes.getMuteState());

  // Submissions per station
  const [submissions, setSubmissions] = useState<Record<string, StationCandidateSubmission>>({});

  // Active inputs for current station
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});
  const [mcqAnswers, setMcqAnswers] = useState<Record<string, 'A' | 'B' | 'C' | 'D' | null>>({});

  // Self-paced mode features
  const [showRationales, setShowRationales] = useState<boolean>(false);
  const [twoMinuteWarningFired, setTwoMinuteWarningFired] = useState<boolean>(false);

  // Transition countdown
  const [transitionSeconds, setTransitionSeconds] = useState<number>(15);

  const timerRef = useRef<NodeJS.Timeout | null>(null);

  // Initialize or reset station state
  useEffect(() => {
    setCheckedItems({});
    setMcqAnswers({});
    setCurrentPhase('practical');
    setSecondsRemaining(600);
    setTwoMinuteWarningFired(false);
  }, [currentStationIndex]);

  // Main countdown timer effect
  useEffect(() => {
    if (mode === 'self-paced' && isPaused) return;

    timerRef.current = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          handleTimeExpired();
          return 0;
        }

        // 2-minute warning bell (120s)
        if (prev === 121 && !twoMinuteWarningFired) {
          setTwoMinuteWarningFired(true);
          AudioChimes.playWarningBell();
        }

        return prev - 1;
      });
    }, 1000);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [currentPhase, mode, isPaused, twoMinuteWarningFired]);

  // Handle phase transitions when timer expires or candidate advances
  const handleTimeExpired = () => {
    if (currentPhase === 'practical') {
      AudioChimes.playWarningBell();
      setCurrentPhase('mcq');
      setSecondsRemaining(600);
      setTwoMinuteWarningFired(false);
    } else if (currentPhase === 'mcq') {
      AudioChimes.playRotationBell();
      saveCurrentStationSubmission();
      if (currentStationIndex < stationPool.length - 1) {
        setCurrentPhase('transition');
        setTransitionSeconds(15);
      } else {
        handleFinalCircuitSubmission();
      }
    }
  };

  // Transition timer
  useEffect(() => {
    if (currentPhase !== 'transition') return;
    const interval = setInterval(() => {
      setTransitionSeconds((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          handleNextStation();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [currentPhase]);

  const handleNextStation = () => {
    if (currentStationIndex < stationPool.length - 1) {
      setCurrentStationIndex((prev) => prev + 1);
    } else {
      handleFinalCircuitSubmission();
    }
  };

  // Checkbox toggle
  const handleToggleChecklist = (item: ChecklistItem) => {
    setCheckedItems((prev) => ({
      ...prev,
      [item.id]: !prev[item.id],
    }));
  };

  // MCQ selection
  const handleSelectMCQ = (mcqId: string, optionId: 'A' | 'B' | 'C' | 'D') => {
    setMcqAnswers((prev) => ({
      ...prev,
      [mcqId]: optionId,
    }));
  };

  // Save current station submission
  const saveCurrentStationSubmission = (): StationCandidateSubmission => {
    const rawPractical = currentStation.checklist.reduce((acc, item) => {
      return acc + (checkedItems[item.id] ? item.points : 0);
    }, 0);

    // Identify violated or omitted critical fail steps
    const violatedCriticalItems = currentStation.checklist.filter(
      (item) => item.isCriticalFail && !checkedItems[item.id]
    );
    const criticalFailTriggered = violatedCriticalItems.length > 0;

    // Practical percentage: capped at 49% if critical fail triggered
    let practicalPct = (rawPractical / 100) * 100;
    if (criticalFailTriggered && practicalPct > 49) {
      practicalPct = 49.0;
    }

    // MCQ scoring
    let mcqCorrect = 0;
    currentStation.mcqs.forEach((q) => {
      if (mcqAnswers[q.id] === q.correctAnswer) {
        mcqCorrect++;
      }
    });
    const mcqPct = (mcqCorrect / currentStation.mcqs.length) * 100;

    // Composite: 50% practical + 50% MCQ
    const compositePct = (practicalPct + mcqPct) / 2;
    const passed = compositePct >= 70.0 && !criticalFailTriggered;

    const sub: StationCandidateSubmission = {
      stationId: currentStation.id,
      stationNumber: currentStation.stationNumber,
      checklistSelections: checkedItems,
      mcqAnswers,
      practicalScore: rawPractical,
      practicalMaxScore: 100,
      mcqScore: mcqCorrect,
      mcqMaxScore: currentStation.mcqs.length,
      criticalFailTriggered,
      criticalFailItems: violatedCriticalItems,
      practicalPercentage: practicalPct,
      mcqPercentage: mcqPct,
      stationCompositePercentage: compositePct,
      isStationPassed: passed,
      timeSpentPracticalSeconds: 600 - (currentPhase === 'practical' ? secondsRemaining : 0),
      timeSpentMcqSeconds: 600 - (currentPhase === 'mcq' ? secondsRemaining : 0),
    };

    setSubmissions((prev) => ({
      ...prev,
      [currentStation.id]: sub,
    }));

    return sub;
  };

  // Final submission of all stations
  const handleFinalCircuitSubmission = () => {
    const lastSub = saveCurrentStationSubmission();
    const allSubs: StationCandidateSubmission[] = [];

    stationPool.forEach((st) => {
      if (st.id === currentStation.id) {
        allSubs.push(lastSub);
      } else if (submissions[st.id]) {
        allSubs.push(submissions[st.id]);
      } else {
        // Unattempted station
        allSubs.push({
          stationId: st.id,
          stationNumber: st.stationNumber,
          checklistSelections: {},
          mcqAnswers: {},
          practicalScore: 0,
          practicalMaxScore: 100,
          mcqScore: 0,
          mcqMaxScore: st.mcqs.length,
          criticalFailTriggered: true,
          criticalFailItems: st.checklist.filter((c) => c.isCriticalFail),
          practicalPercentage: 0,
          mcqPercentage: 0,
          stationCompositePercentage: 0,
          isStationPassed: false,
          timeSpentPracticalSeconds: 0,
          timeSpentMcqSeconds: 0,
        });
      }
    });

    // Calculate overall statistics
    const totalCritFails = allSubs.reduce((acc, s) => acc + (s.criticalFailTriggered ? 1 : 0), 0);
    const totalPracticalEarned = allSubs.reduce((acc, s) => acc + s.practicalScore, 0);
    const totalPracticalAvail = allSubs.length * 100;
    const totalMcqEarned = allSubs.reduce((acc, s) => acc + s.mcqScore, 0);
    const totalMcqAvail = allSubs.length * 10;

    const avgComposite =
      allSubs.reduce((acc, s) => acc + s.stationCompositePercentage, 0) / allSubs.length;

    let overallStatus: CAOSCEReport['overallStatus'] = 'FAIL (BELOW BENCHMARK)';
    if (totalCritFails > 0) {
      overallStatus = 'REFERRAL (SAFETY VIOLATION)';
    } else if (avgComposite >= 85.0) {
      overallStatus = 'DISTINCTION';
    } else if (avgComposite >= 70.0) {
      overallStatus = 'PASS';
    }

    // Generate remedial clinical directives
    const directives: string[] = [];
    allSubs.forEach((sub) => {
      if (sub.criticalFailTriggered) {
        const st = CAOSCE_STATIONS.find((s) => s.id === sub.stationId);
        sub.criticalFailItems.forEach((item) => {
          directives.push(
            `[Station ${sub.stationNumber}: ${st?.title}] Critical Patient Safety Violation: "${item.instruction}". Reason: ${item.criticalFailReason || item.rationale}`
          );
        });
      }
    });

    const report: CAOSCEReport = {
      id: `CAOSCE-REP-${Date.now().toString(36).toUpperCase()}`,
      candidateName,
      examinationTitle: initialStationNumber
        ? `WAPCNM Specialty Clinical Station ${initialStationNumber} Evaluation`
        : 'WAPCNM Autonomous 6-Station Postgraduate Mental Health CAOSCE Circuit',
      dateTimestamp: Date.now(),
      mode,
      passMarkPercentage: 70.0,
      distinctionMarkPercentage: 85.0,
      overallCompositePercentage: avgComposite,
      overallStatus,
      totalCriticalFails: totalCritFails,
      stationSubmissions: allSubs,
      totalPracticalPointsEarned: totalPracticalEarned,
      totalPracticalPointsAvailable: totalPracticalAvail,
      totalMcqCorrect: totalMcqEarned,
      totalMcqAvailable: totalMcqAvail,
      totalTimeSeconds: 120 * 60,
      remedialDirectives: directives,
    };

    onFinish(report);
  };

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const handleToggleMute = () => {
    const newMuted = AudioChimes.toggleMute();
    setIsMuted(newMuted);
  };

  // Station Transition Interstitial Screen
  if (currentPhase === 'transition') {
    return (
      <div className="min-h-[600px] flex items-center justify-center animate-fadeIn">
        <div className="max-w-md w-full bg-slate-900 text-white rounded-2xl p-8 border border-slate-800 text-center shadow-2xl space-y-6">
          <div className="w-16 h-16 rounded-full bg-indigo-500/20 text-indigo-400 border border-indigo-500/30 flex items-center justify-center text-3xl mx-auto animate-pulse">
            🔔
          </div>
          <div className="space-y-2">
            <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">
              Station Rotation Bell
            </span>
            <h2 className="text-2xl font-bold">Prepare for Station {currentStationIndex + 2}</h2>
            <p className="text-xs text-slate-400">
              Station {currentStationIndex + 1} locked. Rotate to the next clinical station and read the incoming door briefing.
            </p>
          </div>
          <div className="text-5xl font-mono font-extrabold text-amber-400">
            {transitionSeconds}s
          </div>
          <button
            onClick={handleNextStation}
            className="w-full py-3 rounded-xl font-bold text-sm bg-indigo-600 hover:bg-indigo-500 text-white transition-colors"
          >
            Advance Immediately →
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6 animate-fadeIn pb-12">
      {/* Circuit Header Bar */}
      <div className="bg-slate-900 text-white rounded-2xl p-4 sm:p-6 border border-slate-800 shadow-xl flex flex-wrap items-center justify-between gap-4 sticky top-4 z-30 backdrop-blur-md bg-slate-900/95">
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded text-[11px] font-bold bg-indigo-500/30 text-indigo-300 border border-indigo-500/40">
              STATION {currentStation.stationNumber} OF {stationPool.length}
            </span>
            <span className="text-xs text-slate-400">
              Candidate: <strong>{candidateName}</strong>
            </span>
          </div>
          <h2 className="text-lg sm:text-xl font-bold tracking-tight text-white flex items-center gap-2">
            {currentStation.title}
          </h2>
        </div>

        {/* Phase Indicators & Timer */}
        <div className="flex items-center gap-3 sm:gap-4">
          <div className="flex items-center gap-1.5 bg-slate-800/80 p-1 rounded-xl border border-slate-700/60 text-xs font-semibold">
            <div
              className={`px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 ${
                currentPhase === 'practical'
                  ? 'bg-amber-600 text-white font-bold'
                  : 'text-slate-400'
              }`}
            >
              <span>🩺</span> Phase 1: Practical (10m)
            </div>
            <div
              className={`px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 ${
                currentPhase === 'mcq'
                  ? 'bg-indigo-600 text-white font-bold'
                  : 'text-slate-400'
              }`}
            >
              <span>📝</span> Phase 2: MCQs (10m)
            </div>
          </div>

          {/* Clock Timer */}
          <div
            className={`flex items-center gap-2 px-4 py-2 rounded-xl font-mono text-base sm:text-lg font-bold border transition-colors ${
              secondsRemaining <= 120
                ? 'bg-rose-950/80 text-rose-300 border-rose-500/50 animate-pulse'
                : 'bg-slate-800 text-amber-400 border-slate-700'
            }`}
          >
            <span>⏱️</span>
            <span>{formatTimer(secondsRemaining)}</span>
          </div>

          {/* Audio Mute & Pause */}
          <button
            onClick={handleToggleMute}
            className={`p-2 rounded-xl border text-sm transition-colors ${
              isMuted
                ? 'bg-slate-800 border-slate-700 text-slate-400 hover:text-white'
                : 'bg-emerald-950/40 border-emerald-500/40 text-emerald-300'
            }`}
            title={isMuted ? 'Sound Muted' : 'Sound Enabled (750Hz / 1000Hz Chimes)'}
          >
            {isMuted ? '🔇' : '🔔'}
          </button>

          {mode === 'self-paced' && (
            <button
              onClick={() => setIsPaused(!isPaused)}
              className="px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 border border-slate-700 text-slate-300 hover:text-white"
            >
              {isPaused ? '▶️ Resume' : '⏸️ Pause'}
            </button>
          )}

          <button
            onClick={onCancel}
            className="text-xs text-rose-400 hover:text-rose-300 px-3 py-2 rounded-xl border border-rose-900/50 hover:bg-rose-950/30"
          >
            Exit Exam
          </button>
        </div>
      </div>

      {/* 2-Minute Warning Banner */}
      {secondsRemaining <= 120 && (
        <div className="bg-amber-500/10 border-2 border-amber-500/60 rounded-xl p-3 text-amber-300 flex items-center justify-between text-xs sm:text-sm font-semibold animate-pulse">
          <div className="flex items-center gap-2">
            <span className="text-lg">⚠️</span>
            <span>WARNING BELL FIRED: 2 Minutes remaining in {currentPhase.toUpperCase()} phase! Finalize your clinical actions.</span>
          </div>
          <span className="font-mono text-xs">{secondsRemaining}s</span>
        </div>
      )}

      {/* Main Examination Grid: Left Dossier / Right Interactive Station */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Left Column: Dossier & Patient Telemetry (5 cols) */}
        <div className="lg:col-span-5 space-y-6">
          {/* Door Briefing Card */}
          <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 shadow-sm space-y-3">
            <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400">
                Door Briefing & Setting
              </span>
              <span className="text-xs text-slate-400">{currentStation.patientProfile.setting}</span>
            </div>
            <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
              {currentStation.doorBriefing}
            </p>
            <div className="bg-slate-50 dark:bg-slate-950/60 p-3 rounded-lg border border-slate-100 dark:border-slate-800/80">
              <div className="text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                Candidate Directives:
              </div>
              <ul className="list-disc list-inside space-y-1 text-xs text-slate-600 dark:text-slate-400">
                {currentStation.candidateInstructions.slice(0, 4).map((inst, i) => (
                  <li key={i}>{inst}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* Patient Dossier & Entrance Vitals */}
          <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 shadow-sm space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
              <span className="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">
                Patient Clinical Dossier
              </span>
              <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                {currentStation.patientProfile.name}, {currentStation.patientProfile.age}y/o ({currentStation.patientProfile.gender})
              </span>
            </div>

            {/* Vitals Telemetry Box */}
            <div className="bg-slate-950 text-emerald-400 p-3.5 rounded-xl border border-emerald-900/40 font-mono text-xs space-y-2">
              <div className="text-[10px] text-emerald-500 uppercase tracking-widest font-bold flex items-center justify-between">
                <span>Vital Signs Telemetry</span>
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
              </div>
              <div className="grid grid-cols-2 gap-2 text-[11px]">
                <div>BP: <strong className="text-white">{currentStation.entryVitals.bloodPressure}</strong></div>
                <div>HR: <strong className="text-white">{currentStation.entryVitals.heartRate}</strong></div>
                <div>RR: <strong className="text-white">{currentStation.entryVitals.respiratoryRate}</strong></div>
                <div>Temp: <strong className="text-white">{currentStation.entryVitals.temperature}</strong></div>
                <div className="col-span-2">SpO2: <strong className="text-white">{currentStation.entryVitals.oxygenSaturation}</strong></div>
              </div>
              {currentStation.entryVitals.painOrDistressScore && (
                <div className="pt-1.5 border-t border-emerald-900/60 text-amber-300 text-[11px]">
                  Clinical Distress: {currentStation.entryVitals.painOrDistressScore}
                </div>
              )}
            </div>

            {/* Patient History */}
            <div className="space-y-2 text-xs text-slate-600 dark:text-slate-300">
              <div>
                <strong className="text-slate-900 dark:text-white">Chief Complaint:</strong>{' '}
                {currentStation.patientProfile.chiefComplaint}
              </div>
              <div>
                <strong className="text-slate-900 dark:text-white">History of Illness:</strong>{' '}
                {currentStation.patientProfile.historyOfPresentIllness}
              </div>
              <div>
                <strong className="text-slate-900 dark:text-white">Current Meds:</strong>{' '}
                {currentStation.patientProfile.currentMedications.join(', ')}
              </div>
              <div>
                <strong className="text-slate-900 dark:text-white">Allergies:</strong>{' '}
                {currentStation.patientProfile.allergies.join(', ')}
              </div>
            </div>

            {/* Equipment Tray */}
            <div className="pt-2 border-t border-slate-100 dark:border-slate-800">
              <span className="text-xs font-bold text-slate-700 dark:text-slate-300 block mb-1.5">
                Standard Equipment & Drug Tray:
              </span>
              <div className="flex flex-wrap gap-1.5">
                {currentStation.equipmentTray.map((eq, i) => (
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

        {/* Right Column: Active Interactive Station Execution (7 cols) */}
        <div className="lg:col-span-7 space-y-6">
          {/* Phase 1: Practical 10-Step Checklist */}
          {currentPhase === 'practical' && (
            <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 shadow-sm space-y-5">
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-3">
                <div>
                  <h3 className="font-bold text-lg text-slate-900 dark:text-white flex items-center gap-2">
                    <span>🩺</span> Phase 1: Psychomotor Action Checklist
                  </h3>
                  <p className="text-xs text-slate-500">
                    Execute the 10 sequential clinical steps. Select each step as you complete the action.
                  </p>
                </div>
                <div className="text-right">
                  <div className="text-xs text-slate-400">Score Earned:</div>
                  <div className="text-xl font-bold font-mono text-indigo-600 dark:text-indigo-400">
                    {currentStation.checklist.reduce(
                      (acc, item) => acc + (checkedItems[item.id] ? item.points : 0),
                      0
                    )}{' '}
                    / 100 Pts
                  </div>
                </div>
              </div>

              {/* Red Flag Notice */}
              <div className="bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/50 rounded-lg p-3 text-xs text-rose-800 dark:text-rose-300 flex items-start gap-2">
                <span className="text-base">🚨</span>
                <div className="leading-relaxed">
                  <strong>Critical Red Flag Safety Checkpoints Active:</strong> Omitting or violating any step marked with <span className="font-bold text-rose-600">⚡ RED FLAG</span> triggers an immediate Station Referral (practical score capped at 49%).
                </div>
              </div>

              {/* Checklist Items */}
              <div className="space-y-3">
                {currentStation.checklist.map((item) => {
                  const isChecked = !!checkedItems[item.id];
                  return (
                    <div
                      key={item.id}
                      onClick={() => handleToggleChecklist(item)}
                      className={`p-3.5 rounded-xl border transition-all cursor-pointer select-none ${
                        isChecked
                          ? 'bg-indigo-50/60 dark:bg-indigo-950/40 border-indigo-500/60 shadow-sm'
                          : 'bg-slate-50 dark:bg-slate-950/40 border-slate-200 dark:border-slate-800 hover:border-slate-300'
                      }`}
                    >
                      <div className="flex items-start gap-3">
                        <input
                          type="checkbox"
                          checked={isChecked}
                          onChange={() => {}} // handled by parent onClick
                          className="mt-1 w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500 border-slate-300"
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
                              <span className="font-mono font-bold text-indigo-600 dark:text-indigo-400">
                                +{item.points} pts
                              </span>
                            </div>
                          </div>

                          <p className="text-xs sm:text-sm font-medium text-slate-900 dark:text-slate-100 leading-snug">
                            {item.instruction}
                          </p>

                          {mode === 'self-paced' && (
                            <p className="text-xs text-slate-500 dark:text-slate-400 pt-1 italic">
                              Rationale: {item.rationale}
                            </p>
                          )}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Action Bar */}
              <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                <span className="text-xs text-slate-500">
                  {Object.values(checkedItems).filter(Boolean).length} of 10 steps completed
                </span>
                <button
                  onClick={() => {
                    AudioChimes.playWarningBell();
                    setCurrentPhase('mcq');
                    setSecondsRemaining(600);
                  }}
                  className="px-5 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition-colors flex items-center gap-2"
                >
                  Proceed to Phase 2 (10 MCQs) →
                </button>
              </div>
            </div>
          )}

          {/* Phase 2: 10 Station-Linked MCQs */}
          {currentPhase === 'mcq' && (
            <div className="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-6 shadow-sm space-y-6">
              <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-3">
                <div>
                  <h3 className="font-bold text-lg text-slate-900 dark:text-white flex items-center gap-2">
                    <span>📝</span> Phase 2: Station-Linked Scenario MCQs
                  </h3>
                  <p className="text-xs text-slate-500">
                    Phase 1 locked. Answer 10 scenario-specific clinical questions (60 seconds recommended per question).
                  </p>
                </div>
                <div className="text-right">
                  <span className="text-xs text-slate-400">Answered:</span>
                  <div className="text-base font-bold font-mono text-indigo-600 dark:text-indigo-400">
                    {Object.values(mcqAnswers).filter(Boolean).length} / 10
                  </div>
                </div>
              </div>

              {/* MCQs List */}
              <div className="space-y-6">
                {currentStation.mcqs.map((q, qIndex) => (
                  <div
                    key={q.id}
                    className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/30 space-y-3"
                  >
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-indigo-600 dark:text-indigo-400">
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

                        let optionStyle = 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:border-indigo-400';

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
                                ✓ Correct
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

                    {/* Immediate Post-Attempt Clinical Tutorial Support */}
                    {mcqAnswers[q.id] !== undefined && mcqAnswers[q.id] !== null && (
                      <div className={`mt-3 p-4 rounded-xl border text-xs sm:text-sm space-y-2.5 animate-fadeIn ${
                        mcqAnswers[q.id] !== q.correctAnswer 
                          ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
                          : 'bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60'
                      }`}>
                        <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-200/60 dark:border-slate-800/60">
                          <div className="flex items-center gap-2 font-bold">
                            {mcqAnswers[q.id] !== q.correctAnswer ? (
                              <span className="text-rose-700 dark:text-rose-300 flex items-center gap-1.5 font-bold">
                                <span>✕</span> Incorrect Answer Supplied — Tutorial Support Active
                              </span>
                            ) : (
                              <span className="text-emerald-700 dark:text-emerald-300 flex items-center gap-1.5 font-bold">
                                <span>✓</span> Correct Clinical Decision! Well done.
                              </span>
                            )}
                          </div>
                          {mcqAnswers[q.id] !== q.correctAnswer && (
                            <button
                              onClick={() => {
                                setMcqAnswers(prev => {
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
                        <div className="space-y-1">
                          <div className="flex items-start gap-1.5 font-semibold text-emerald-800 dark:text-emerald-300">
                            <span className="font-bold shrink-0">✓ Validated Correct Answer:</span>
                            <span>
                              Option {q.correctAnswer} — {q.options.find(o => o.id === q.correctAnswer)?.text}
                            </span>
                          </div>
                          {mcqAnswers[q.id] !== q.correctAnswer && (
                            <div className="flex items-start gap-1.5 text-rose-700 dark:text-rose-400">
                              <span className="font-bold shrink-0">✕ Your Choice:</span>
                              <span>
                                Option {mcqAnswers[q.id]} — {q.options.find(o => o.id === mcqAnswers[q.id])?.text}
                              </span>
                            </div>
                          )}
                        </div>

                        {/* Clinical Rationale */}
                        <div className="p-3 rounded-lg bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 space-y-1">
                          <strong className="text-slate-900 dark:text-white block font-bold text-xs uppercase tracking-wide">
                            Station Clinical Rationale:
                          </strong>
                          <p className="leading-relaxed text-xs">
                            {q.explanation}
                          </p>
                        </div>
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {/* Station Completion Bar */}
              <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                <button
                  onClick={() => setCurrentPhase('practical')}
                  className="text-xs font-semibold text-slate-500 hover:text-slate-800 dark:hover:text-slate-200"
                >
                  ← Review Practical Steps
                </button>

                <button
                  onClick={() => {
                    AudioChimes.playRotationBell();
                    saveCurrentStationSubmission();
                    if (currentStationIndex < stationPool.length - 1) {
                      setCurrentPhase('transition');
                      setTransitionSeconds(15);
                    } else {
                      handleFinalCircuitSubmission();
                    }
                  }}
                  className="px-6 py-2.5 rounded-xl font-bold text-xs sm:text-sm bg-gradient-to-r from-emerald-600 to-indigo-600 text-white hover:from-emerald-500 hover:to-indigo-500 shadow-md transition-all"
                >
                  {currentStationIndex < stationPool.length - 1
                    ? `Complete Station ${currentStation.stationNumber} & Rotate →`
                    : 'Submit Final CAOSCE Examination →'}
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
