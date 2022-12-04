/*
  ==============================================================================

    Synth.cpp
    Created: 16 Dec 2020 3:56:18pm
    Author:  user

  ==============================================================================
*/

#include "Synth.h"

Synth::Synth() {
    sampleRate = 44100.;
    frequency = 220.;
    amplitude = 0.5;

    waveformType = 0; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = 30;
    suppressing_output = false;
    constructHarmonics();
}
Synth::Synth(float sr) {
    sampleRate = sr;
    frequency = 220.;
    amplitude = 0.5;

    waveformType = 0; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = 30;
    suppressing_output = false;
    constructHarmonics();
}
Synth::Synth(float sr, float freq, float amp) {
    sampleRate = sr;
    frequency = freq;
    amplitude = amp;

    waveformType = 0; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = 30;
    suppressing_output = false;
    constructHarmonics();
}
Synth::Synth(float sr, int wavtype, float freq, float amp) {
    sampleRate = sr;
    frequency = freq;
    amplitude = amp;

    waveformType = wavtype; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = 30;
    suppressing_output = false;
    constructHarmonics();
}
Synth::Synth(float sr, int wavtype, int numHarmonics, float freq, float amp) {
    sampleRate = sr;
    frequency = freq;
    amplitude = amp;

    waveformType = wavtype; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = numHarmonics;
    suppressing_output = false;
    constructHarmonics();
}
Synth::Synth(float sr, int wavtype, int numHarmonics) {
    sampleRate = sr;
    frequency = 220.;
    amplitude = 0.5;

    waveformType = wavtype; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = numHarmonics;
    suppressing_output = false;
    constructHarmonics();
}
Synth::Synth(int wavtype) {
    sampleRate = 44100.;
    frequency = 220.;
    amplitude = 0.5;

    waveformType = wavtype; // 0:sine, 1:square, 2:saw, 3:triangle
    maxHarmonicsNumber = 30;
    suppressing_output = false;
    constructHarmonics();
}
Synth::~Synth() {
    // ownedarrays handle memory dealocation on their own
}

void Synth::setFrequency(float f) {
    frequency = f;
    readjustHarmonics();
}
void Synth::setAmplitude(float a) {
    amplitude = a;
    readjustHarmonics();
}
float Synth::getNextSample() {
    current_sample_value = 0.0;
    for (int i = 0; i < harmonics.size() && !suppressing_output && harmonics[i]->getFrequency() <= sampleRate/2.; i++) {
        current_sample_value += harmonics[i]->getNextSample();
    }
    return current_sample_value;
}
void Synth::setSampleRate(float s) {
    sampleRate = s;
    constructHarmonics();
}
void Synth::setWaveformType(int t) {
    waveformType = t;
    constructHarmonics();
}
void Synth::setMaxHarmonicsNumber(int t) {
    maxHarmonicsNumber = t;
    constructHarmonics();
}

void Synth::constructHarmonics() {
    suppressing_output = true;
    harmonics.clear();
    // make code more compact
    int harmonics_incr = waveformType == 2 ? 1 : 2;
    int harmonics_limit = waveformType == 0 ? 1 : maxHarmonicsNumber;
    float harmonics_exponent = waveformType == 3 ? 2 : 1;
    float harmonics_tringle_phase_sign = waveformType == 3 ? -1 : 1;
    float tmp_freq;
    float tmp_amp;
    for (int i = 1; i <= harmonics_limit; i+=harmonics_incr) {
        tmp_freq = (float)i * frequency;
        tmp_amp = (std::powf(-1.0,(harmonics_exponent-1.)*((float)i-1.)/2.))*amplitude/std::powf((float)i,harmonics_exponent);
        harmonics.add(new SineGenerator(sampleRate, tmp_freq, tmp_amp));
    }
    suppressing_output = false;
}

void Synth::readjustHarmonics() {
    // make code more compact
    int harmonics_incr = waveformType == 2 ? 1 : 2;
    int harmonics_limit = waveformType == 0 ? 1 : maxHarmonicsNumber;
    float harmonics_exponent = waveformType == 3 ? 2 : 1;
    float harmonics_tringle_phase_sign = waveformType == 3 ? -1 : 1;
    float tmp_freq;
    float tmp_amp;
    float tmp_harmonic_idx = 1.0;
    for (int i = 0; i < harmonics.size(); i++) {
        tmp_freq = tmp_harmonic_idx * frequency;
        tmp_amp = (std::powf(-1.0, (harmonics_exponent-1.)*(tmp_harmonic_idx - 1.) / 2.)) * amplitude / std::powf(tmp_harmonic_idx, harmonics_exponent);
        harmonics[i]->setFrequency(tmp_freq);
        harmonics[i]->setAmplitude(tmp_amp);
        tmp_harmonic_idx += harmonics_incr;
    }
}
