// import everything necessary to make sound.
import ddf.minim.*;
import ddf.minim.ugens.*;

// STEP 1: declare
Minim minim;
AudioOutput out;

Oscil sine;

void setup()
{
  size( 512, 200);

  // initialize the minim and out objects
  minim = new Minim( this );
  out   = minim.getLineOut();
  
  // STEP 2: initialisation
  sine   = new Oscil( 100, 0.5f, Waves.SINE );
  
  // STEP 3: patch to output
  sine.patch( out );
  
  ellipseMode(CENTER);
}

// draw is run many times
void draw()
{
  // erase the window to black
  background( 0 );
  // draw using a white stroke
  stroke( 255 );
  fill(255);
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
  
  fill(230, 70, 70);
  ellipse(mouseX, mouseY, 5, 5);
  
  stroke( 255 );
  fill(255);
  text( "frequency: " + sine.frequency.getLastValue(), 5, 15 );
}

// we can change the parameters of the frequency of Oscil
// in real-time using the mouse.
void mouseMoved()
{
  float amplitude = map( mouseY, 0, height, 1.0, 0.0 );
  float frequency = map( mouseX, 0, width, 20.0, 1000.0);
  
  sine.setFrequency( frequency );
  sine.setAmplitude( amplitude );
}

void keyPressed()
{ 
  switch( key )
  {
    case '1': 
      sine.setWaveform( Waves.SINE );
      break;
     
    case '2':
      sine.setWaveform( Waves.TRIANGLE );
      break;
     
    case '3':
      sine.setWaveform( Waves.SAW );
      break;
    
    case '4':
      sine.setWaveform( Waves.SQUARE );
      break;
      
    case '5':
      sine.setWaveform( Waves.QUARTERPULSE );
      break;
     
    default: break; 
  }
}
