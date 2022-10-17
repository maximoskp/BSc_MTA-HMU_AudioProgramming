// import everything necessary to make sound.
import ddf.minim.*;
import ddf.minim.ugens.*;

// STEP 1: declare
Minim minim;
AudioOutput out;

Delay myDelay;
Oscil square;

void setup()
{
  size( 512, 200, P3D );

  // initialize the minim and out objects
  minim = new Minim( this );
  out   = minim.getLineOut();
  
  // STEP 2: initialisation
  myDelay = new Delay( 0.3, 0.7, true, true );
  square   = new Oscil( 100, 0.5f, Waves.SQUARE );
  
  // STEP 3: patch to output
  square.patch( myDelay ).patch( out );
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
  
  text( "frequency: " + square.frequency.getLastValue(), 5, 15 );
}

// we can change the parameters of the frequency modulation Oscil
// in real-time using the mouse.
void mouseMoved()
{
  float amplitude = map( mouseY, 0, height, 1.0, 0.0 );
  float frequency = map( mouseX, 0, width, 20.0, 1000.0);
  
  square.setFrequency( frequency );
  square.setAmplitude( amplitude );
}
