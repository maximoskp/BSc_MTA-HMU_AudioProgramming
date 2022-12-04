#include "MainComponent.h"

//==============================================================================
MainComponent::MainComponent()
{
    // Make sure you set the size of the component after
    // you add any child components.
    setSize (800, 600);
    // __added__ vvv
    s = std::make_unique<Synth>(2); // 0:sine, 1:square, 2:saw, 3:triangle // modern approach
    // s = new Synth(1);// old school
    // __added__ ^^^

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

    // __added__ vvv
    // initialise UI
    addAndMakeVisible(amp_slider);
    amp_slider.setRange(0., 1., 0.01);
    amp_slider.setValue(0.5);
    amp_slider.onValueChange = [this] { s->setAmplitude(amp_slider.getValue()); };

    addAndMakeVisible(freq_slider);
    freq_slider.setRange(20., 1000., 1.);
    freq_slider.setValue(220.);
    freq_slider.onValueChange = [this] {
        s->setFrequency(freq_slider.getValue());
    };

    // add items to the combo-box
    addAndMakeVisible(typeMenu);
    typeMenu.addItem("Sine", 1);
    typeMenu.addItem("Square", 2);
    typeMenu.addItem("Sawtooth", 3);
    typeMenu.addItem("Triangle", 4);

    typeMenu.onChange = [this] {
        s->setWaveformType(typeMenu.getSelectedId()-1);
    };
    typeMenu.setSelectedId(1);
    // __added__ ^^^
}

MainComponent::~MainComponent()
{
    // This shuts down the audio device and clears the audio source.
    shutdownAudio();
    // delete s;// old school
}

//==============================================================================
void MainComponent::prepareToPlay (int samplesPerBlockExpected, double sampleRate)
{
    // This function will be called when the audio device is started, or when
    // its settings (i.e. sample rate, block size, etc) are changed.

    // You can use this function to initialise any resources you might need,
    // but be careful - it will be called on the audio thread, not the GUI thread.

    // For more details, see the help for AudioProcessor::prepareToPlay()
    sample_rate = sampleRate;
    s->setSampleRate(sample_rate);
}

void MainComponent::getNextAudioBlock (const juce::AudioSourceChannelInfo& bufferToFill)
{
    // Your audio-processing code goes here!
    // __added__ vvv
    if (sample_rate > 0.0) { // make sure that prepareToPlay has been called
        // prepare buffers to write to
        auto* leftBuffer = bufferToFill.buffer->getWritePointer(0, bufferToFill.startSample);
        auto* rightBuffer = bufferToFill.buffer->getWritePointer(1, bufferToFill.startSample);
        for (auto i = 0; i < bufferToFill.numSamples; i++) {
            // taking sample values directly from object
            current_sample_value = s->getNextSample();
            leftBuffer[i] = current_sample_value;
            rightBuffer[i] = current_sample_value;
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
    // __added__ vvv
    // normally, we place UI size-related code here, since here their dimensions
    // might need to change
    amp_slider.setBounds(getWidth() / 4. + 10, 100, 3. * getWidth() / 4. - 20, 30);
    freq_slider.setBounds(getWidth() / 4. + 10, 200, 3. * getWidth() / 4. - 20, 30);
    typeMenu.setBounds(getWidth() / 4. + 10, 400, 3. * getWidth() / 4. - 20, 40);
    // __added__ ^^^
}
