#pragma once

#include <JuceHeader.h>
#include "SineClass.h"

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
    float sample_rate = 0.0;
    // UI
    juce::Slider amp_slider;
    juce::Slider freq_slider;

    // functions - they do not need to be public
    void changeAmp();
    void changeFreq();
    
    void adjustHarmonics();
    
    float frequency = 100;
    float amplitude = 0.5;
    
    int num_harmonics = 30;
    juce::OwnedArray<SineClass> harmonics;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MainComponent)
};
