/*
  ==============================================================================

    SineGenerator.h
    Created: 9 Dec 2020 5:10:56pm
    Author:  user

  ==============================================================================
*/

#include <JuceHeader.h>

#pragma once

class SineGenerator {
public:
    // constructor and destructor
    SineGenerator::SineGenerator();
    SineGenerator::SineGenerator(float sr);
    SineGenerator::SineGenerator(float sr, float freq, float amp);
    SineGenerator::~SineGenerator();

    void setFrequency(float f);
    void setAmplitude(float a);
    float getNextSample();
    void setSampleRate(float s);
private:
    float sampleRate;
    float frequency;
    float amplitude;

    float current_angle;
    float current_sample_value;

    float pi = 3.14159265358979323846;
};