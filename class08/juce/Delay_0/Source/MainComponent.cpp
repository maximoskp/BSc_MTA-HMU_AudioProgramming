#include "MainComponent.h"

//==============================================================================
MainComponent::MainComponent()
{
    // Make sure you set the size of the component after
    // you add any child components.
    setSize (800, 600);

    // Some platforms require permissions to open input channels so request that here
    if (juce::RuntimePermissions::isRequired (juce::RuntimePermissions::recordAudio)
        && ! juce::RuntimePermissions::isGranted (juce::RuntimePermissions::recordAudio))
    {
        juce::RuntimePermissions::request (juce::RuntimePermissions::recordAudio,
                                           [&] (bool granted) { setAudioChannels (granted ? 2 : 0, 2); });
    }
    else
    {
        // Specify the number of input and output channels that we want to open
        setAudioChannels (2, 2);
    }
    // initialise circular buffer to zeros
    for(int i=0; i<max_delay_samples; i++){
        circular_buffer[i] = 0.;
    }
    
    // initialise UI
    addAndMakeVisible(dry_slider);
    dry_slider.setRange(0., 1., 0.01);
    dry_slider.setValue(0.0);
    dry_slider.onValueChange = [this] { changeDry(); };
    
    addAndMakeVisible(wet_slider);
    wet_slider.setRange(0., 1., 0.01);
    wet_slider.setValue(0.5);
    wet_slider.onValueChange = [this] { changeWet(); };
    
    addAndMakeVisible(time_slider);
    time_slider.setRange(0., 5., 0.01);
    time_slider.setValue(0.25);
    time_slider.onValueChange = [this] { changeTime(); };
    
    addAndMakeVisible(feedback_slider);
    feedback_slider.setRange(0., 1., 0.01);
    feedback_slider.setValue(0.5);
    feedback_slider.onValueChange = [this] { changeFeedback(); };
}

MainComponent::~MainComponent()
{
    // This shuts down the audio device and clears the audio source.
    shutdownAudio();
}

//==============================================================================
void MainComponent::prepareToPlay (int samplesPerBlockExpected, double sampleRate)
{
    // This function will be called when the audio device is started, or when
    // its settings (i.e. sample rate, block size, etc) are changed.

    // You can use this function to initialise any resources you might need,
    // but be careful - it will be called on the audio thread, not the GUI thread.

    // For more details, see the help for AudioProcessor::prepareToPlay()
    sample_rate = (int)sampleRate;
}

void MainComponent::getNextAudioBlock (const juce::AudioSourceChannelInfo& bufferToFill)
{
    // Your audio-processing code goes here!
    delay_samples = (int)floorf(delay_time*(float)sample_rate);
    auto* micBuffer = bufferToFill.buffer->getReadPointer(0, bufferToFill.startSample);
    auto* leftSpeakerBuffer  = bufferToFill.buffer->getWritePointer (0, bufferToFill.startSample);
    auto* rightSpeakerBuffer = bufferToFill.buffer->getWritePointer (1, bufferToFill.startSample);
    for (auto i = 0; i < bufferToFill.numSamples; i++){
        // write to circular buffer
        read_pointer = write_pointer - delay_samples < 0 ? max_delay_samples + write_pointer - delay_samples : write_pointer - delay_samples ;
        circular_buffer[ write_pointer ] = micBuffer[i] + feedback*circular_buffer[ read_pointer ];
        write_pointer++;
        write_pointer = write_pointer%max_delay_samples;
        leftSpeakerBuffer[i]  = dry*micBuffer[i] + wet*circular_buffer[ read_pointer ];
        rightSpeakerBuffer[i] = dry*micBuffer[i] + wet*circular_buffer[ read_pointer ];
    }
}

void MainComponent::releaseResources()
{
    // This will be called when the audio device stops, or when it is being
    // restarted due to a setting change.

    // For more details, see the help for AudioProcessor::releaseResources()
}

//==============================================================================
void MainComponent::paint (juce::Graphics& g)
{
    // (Our component is opaque, so we must completely fill the background with a solid colour)
    g.fillAll (getLookAndFeel().findColour (juce::ResizableWindow::backgroundColourId));

    // You can add your drawing code here!
}

void MainComponent::resized()
{
    // This is called when the MainContentComponent is resized.
    // If you add any child components, this is where you should
    // update their positions.
    
    wet_slider.setBounds(getWidth()/4. + 10, 100, 3.*getWidth()/4. - 20, 30);
    dry_slider.setBounds(getWidth()/4. + 10, 200, 3.*getWidth()/4. - 20, 30);
    time_slider.setBounds(getWidth()/4. + 10, 300, 3.*getWidth()/4. - 20, 30);
    feedback_slider.setBounds(getWidth()/4. + 10, 400, 3.*getWidth()/4. - 20, 30);
}

void MainComponent::changeDry(){
    dry = dry_slider.getValue();
}
void MainComponent::changeWet(){
    wet = wet_slider.getValue();
}
void MainComponent::changeTime(){
    delay_time = time_slider.getValue();
}
void MainComponent::changeFeedback(){
    feedback = feedback_slider.getValue();
}
