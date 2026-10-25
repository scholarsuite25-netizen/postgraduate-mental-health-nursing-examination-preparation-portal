/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

// Web Audio API offline acoustic chime generator
class AudioChimeService {
  private audioCtx: AudioContext | null = null;
  private isMuted: boolean = false;

  constructor() {
    const saved = localStorage.getItem('WAPCNM_CAOSCE_MUTED');
    if (saved !== null) {
      this.isMuted = saved === 'true';
    }
  }

  private getAudioContext(): AudioContext | null {
    if (typeof window === 'undefined') return null;
    if (!this.audioCtx) {
      const AudioCtxClass = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      if (AudioCtxClass) {
        this.audioCtx = new AudioCtxClass();
      }
    }
    if (this.audioCtx && this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
    return this.audioCtx;
  }

  public getMuteState(): boolean {
    return this.isMuted;
  }

  public setMuteState(muted: boolean): void {
    this.isMuted = muted;
    localStorage.setItem('WAPCNM_CAOSCE_MUTED', String(muted));
  }

  public toggleMute(): boolean {
    this.setMuteState(!this.isMuted);
    return this.isMuted;
  }

  /**
   * Warning Bell: Single resonant 750 Hz chime with exponential decay.
   * Plays at 2 minutes remaining in each phase.
   */
  public playWarningBell(): void {
    if (this.isMuted) return;
    try {
      const ctx = this.getAudioContext();
      if (!ctx) return;

      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(750, ctx.currentTime);

      gain.gain.setValueAtTime(0.3, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 1.2);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(ctx.currentTime);
      osc.stop(ctx.currentTime + 1.25);
    } catch (e) {
      console.warn('Audio chime warning bell suppressed:', e);
    }
  }

  /**
   * Rotation Bell: Double resonant 1000 Hz chime (two acoustic chimes).
   * Plays at station rotation / 30-second transition bell.
   */
  public playRotationBell(): void {
    if (this.isMuted) return;
    try {
      const ctx = this.getAudioContext();
      if (!ctx) return;

      const playPulse = (delay: number) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = 'sine';
        osc.frequency.setValueAtTime(1000, ctx.currentTime + delay);

        gain.gain.setValueAtTime(0.35, ctx.currentTime + delay);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + delay + 0.8);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(ctx.currentTime + delay);
        osc.stop(ctx.currentTime + delay + 0.85);
      };

      playPulse(0);
      playPulse(0.35); // Second chime 350ms later
    } catch (e) {
      console.warn('Audio chime rotation bell suppressed:', e);
    }
  }
}

export const AudioChimes = new AudioChimeService();
