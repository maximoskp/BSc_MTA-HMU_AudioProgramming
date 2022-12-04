/*
  ==============================================================================

    Synth.h
    Created: 16 Dec 2020 3:56:18pm
    Author:  user

  ==============================================================================
*/

#pragma once

#include <JuceHeader.h>
#include "SineGenerator.h"

class Synth {
public:
    // constructor and destructor
    Synth();
    Synth(float sr);
    Synth(float sr, float freq, float amp);
    Synth(float sr, int wavtype, float freq, float amp);
    Synth(float sr, int wavtype, int numHarmonics, float freq, float amp);
    Synth(float sr, int wavtype, int numHarmonics);
    Synth(int wavtype);
    ~Synth();

    void setFrequency(float f);
    void setAmplitude(float a);
    float getNextSample();
    void setSampleRate(float s);
    void setWaveformType(int t);
    void setMaxHarmonicsNumber(int t);
    // juce::OwnedArray<SineGenerator> harmonics;
private:
    float sampleRate;
    float frequency;
    float amplitude;

    float current_sample_value;
    bool suppressing_output;

    int waveformType;
    int maxHarmonicsNumber;

    juce::OwnedArray<SineGenerator> harmonics;

    void constructHarmonics();
    void readjustHarmonics();
};
