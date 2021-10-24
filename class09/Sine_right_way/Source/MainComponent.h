#pragma once

#include <JuceHeader.h>

//==============================================================================
/*
    This component lives inside our window, and this is where you should put all
    your controls and content.
*/
class MainComponent  : public juce::AudioAppComponent
{
public:
    //==============================================================================
    MainComponent();
    ~MainComponent() override;

    //==============================================================================
    void prepareToPlay (int samplesPerBlockExpected, double sampleRate) override;
    void getNextAudioBlock (const juce::AudioSourceChannelInfo& bufferToFill) override;
    void releaseResources() override;

    //==============================================================================
    void paint (juce::Graphics& g) override;
    void resized() override;

private:
    //==============================================================================
    // Your private member variables go here...

    // __added__ vvv
    // generator variables
    float amplitude = 0.5;
    float frequency = 220.;
    // math constants
    float pi = 3.14159265358979323846; // not given by a common library
    // state variables
    float sample_rate = 0.0;
    // unsigned int total_samples = 0; // we don't count samples any more
    float current_angle = 0.0; // we count angle difference!
    float time_fraction = 0.0;

    // UI
    juce::Slider amp_slider;
    juce::Slider freq_slider;

    // functions - they do not need to be public
    void changeAmp();
    void changeFreq();
    // __added__ ^^^

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MainComponent)
};
