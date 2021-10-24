// import everything necessary to make sound.
import ddf.minim.*;
import ddf.minim.ugens.*;

// STEP 1: declare
Minim minim;
AudioOutput out;
Delay myDelay;
MoogFilter moog;

Oscil fm;

void setup()
{
  size( 512, 200, P3D );

  // initialize the minim and out objects
  minim = new Minim( this );
  out   = minim.getLineOut();
  
  // STEP 2: initialisation
  myDelay = new Delay( 0.3, 0.7, true, true );
  moog    = new MoogFilter( 1200, 0.5 );
  moog.type = MoogFilter.Type.BP;
  
  Oscil wave = new Oscil( 200, 0.8, Waves.SINE );
  fm   = new Oscil( 10, 2, Waves.SINE );
  fm.offset.setLastValue( 200 );
  fm.patch( wave.frequency );
  
  // STEP 3: patch to output
  wave.patch( moog ).patch( myDelay ).patch( out );
}

// draw is run many times
void draw()
{
  // erase the window to black
  background( 0 );
  // draw using a white stroke
  stroke( 255 );
  // draw the waveforms
  for( int i = 0; i < out.bufferSize() - 1; i++ )
  {
    // find the x position of each buffer value
    float x1  =  map( i, 0, out.bufferSize(), 0, width );
    float x2  =  map( i+1, 0, out.bufferSize(), 0, width );
    // draw a line from one buffer position to the next for both channels
    line( x1, 50 + out.left.get(i)*50, x2, 50 + out.left.get(i+1)*50);
    line( x1, 150 + out.right.get(i)*50, x2, 150 + out.right.get(i+1)*50);
  }  
  
  text( "Modulation frequency: " + fm.frequency.getLastValue(), 5, 15 );
  text( "Modulation amplitude: " + fm.amplitude.getLastValue(), 5, 30 );
}

// we can change the parameters of the frequency modulation Oscil
// in real-time using the mouse.
void mouseMoved()
{
  float modulateAmount = map( mouseY, 0, height, 2200, 10 );
  //float modulateFrequency = map( mouseX, 0, width, 0.1, 100 );
  float modulateFrequency = map( mouseX, 0, width, 10, 1000);
  
  fm.setFrequency( modulateFrequency );
  fm.setAmplitude( modulateAmount );
}

void keyPressed(){
  int keyNum = int(key) - 48;
  println("keyNum: " + keyNum);
  if (keyNum > 0 && keyNum < 10){
    moog.frequency.setLastValue(100*keyNum);
  }
}