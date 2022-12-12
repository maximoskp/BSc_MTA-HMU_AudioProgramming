#pragma once

#include <JuceHeader.h>
// __added__ vvv
// import class header
#include "Synth.h"
// __added ^^^

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
    std::unique_ptr<Synth> s; // modern approach
    // Synth* s; // old school
    float sample_rate;
    float current_sample_value;

    // UI
    juce::Slider amp_slider;
    juce::Slider freq_slider;
    juce::ComboBox typeMenu;
    // __added ^^^

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (MainComponent)
};
