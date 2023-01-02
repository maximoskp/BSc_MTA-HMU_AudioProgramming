#include "MainComponent.h"

//==============================================================================
MainComponent::MainComponent()
{
    // Make sure you set the size of the component after
    // you add any child components.
    setSize (800, 600);
    
    pre_amp = 3.;
    clip_level = 0.5;
    sr = 0.;
    
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
    
    if (auto* device = deviceManager.getCurrentAudioDevice())
    {
        juce::Logger::writeToLog("Current audio device: " + device->getName().quoted());
        juce::Logger::writeToLog("Sample rate: " + juce::String(device->getCurrentSampleRate()) + " Hz");
        juce::Logger::writeToLog("Block size: " + juce::String(device->getCurrentBufferSizeSamples()) + " samples");
        juce::Array<int> availableBufferSizes = device->getAvailableBufferSizes();
        juce::Logger::writeToLog("Available buffer sizes: ");
        for (int i = 0; i < availableBufferSizes.size(); i++) {
            juce::Logger::writeToLog(juce::String(availableBufferSizes[i]));
        }
        juce::Logger::writeToLog("Bit depth: " + juce::String(device->getCurrentBitDepth()));
        juce::Logger::writeToLog("Input channel names: " + device->getInputChannelNames().joinIntoString(", "));
        juce::Logger::writeToLog("Output channel names: " + device->getOutputChannelNames().joinIntoString(", "));
    }
    else
    {
        juce::Logger::writeToLog("No audio device open");
    }
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
    sr = (float)sampleRate;
}

void MainComponent::getNextAudioBlock (const juce::AudioSourceChannelInfo& bufferToFill)
{
    // Your audio-processing code goes here!
    if (sr > 0.0) { // make sure that prepareToPlay has been called
        // prepare buffers to write to
        auto* leftBuffer = bufferToFill.buffer->getWritePointer(0, bufferToFill.startSample);
        auto* rightBuffer = bufferToFill.buffer->getWritePointer(1, bufferToFill.startSample);
        auto* mic_signal = bufferToFill.buffer->getReadPointer(0, bufferToFill.startSample);
        for (auto i = 0; i < bufferToFill.numSamples; i++) {
            float x = pre_amp * mic_signal[i];
            if (x < -.5){
                x = -.5;
            }
            if (x > .5){
                x = .5;
            }
            leftBuffer[i] = x;
            rightBuffer[i] = x;
            // DBG("mic: " + juce::String( mic_signal[i] ));
        }
    }
    else { // if not, produce no sound
        bufferToFill.clearActiveBufferRegion();
    }
    // For more details, see the help for AudioProcessor::getNextAudioBlock()

    // Right now we are not producing any data, in which case we need to clear the buffer
    // (to prevent the output of random noise)
    // bufferToFill.clearActiveBufferRegion();
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
}
