/*
  ==============================================================================

    SineClass.h
    Created: 12 Dec 2022 3:24:54pm
    Author:  Maximos Kaliakatsos-Papakostas

  ==============================================================================
*/

#pragma once

#include <JuceHeader.h>

class SineClass{
public:
    // public variables / functions go here
    SineClass();
    SineClass(float sr);
    SineClass(float sr, float f, float a);
    ~SineClass();
    
    // setters
    void set_frequency(float f);
    void set_amplitude(float a);
    void set_sample_rate(float sr);
    // getters
    float get_next_sample();
private:
    // private variables / functions go here
    // generator variables
    float amplitude = 0.5;
    float frequency = 220.;
    // math constants
    float pi = 3.14159265358979323846; // not given by a common library
    // state variables
    float sample_rate = 44100.0;
    // unsigned int total_samples = 0; // we don't count samples any more
    float current_angle = 0.0; // we count angle difference!
};
