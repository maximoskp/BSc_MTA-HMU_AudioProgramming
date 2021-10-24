import ddf.minim.*;

import ddf.minim.analysis.*;

FFT fft;
float[][] allFFTs;
int fftHistory = 20; // poses metriseis toy fft kratame na trexei to diagramma
int fftBins;

Minim minim;
AudioInput in;

void setup(){
  size(600,600);
  minim = new Minim( this );
  in = minim.getLineIn(Minim.MONO, 512);
  in.mute();
  
  fft = new FFT(512,in.sampleRate());
  fft.window(FFT.HAMMING);
  fftBins = fft.specSize();
  
  initializeFFTmatrix();
}

void draw(){
  background(0);
  thread("computeFFT");
  
  paintMatrix(width/3.0,0,(2.0/3.0)*width,height,allFFTs,"spectrogram");
}

// =======================================================================================

void initializeFFTmatrix(){
  allFFTs = new float[fftBins][fftHistory];
  for(int i=0; i<fftBins; i++){
    for(int j=0; j<fftHistory; j++){
      allFFTs[i][j] = 0.0;
    }
  }
}

void computeFFT(){
  fft.forward(in.mix);
  for(int i=0; i<fftBins; i++){
    // metaferoyme ta prin mia thesi piso
    for(int j=0; j<(fftHistory-1); j++) allFFTs[fftBins-1-i][j] = allFFTs[fftBins-1-i][j+1];
    // ypologizoyme to kainoyrio
    allFFTs[fftBins-1-i][fftHistory-1] = fft.getBand(i);
  }
}

void paintMatrix(float xL,float yU,float xR, float yD, float[][] m, String myName){
  float xtmp, ytmp;
  float xSpace, ySpace;
  ySpace = (yD-yU)/(float)m.length;
  xSpace = (xR-xL)/(float)m[0].length;
  rectMode(CORNERS);
  // plaisio
  stroke(200);
  noFill();
  rect(xL,yU,xR,yD);
  noStroke();
  ytmp = 0.0;
  for(int i=0; i<m.length; i++){
    xtmp = 0.0;
    for(int j=0; j<m[i].length; j++){
      fill(150.0*pow(m[i][j],0.5));
//      fill(120.0*pow(m[i][j],0.2),110.0*pow(m[i][j],0.5),0.0);
      rect(xL+xtmp, yU+ytmp, xL+xtmp+xSpace, yU+ytmp+ySpace);
      xtmp += xSpace;
    }
    ytmp += ySpace;
  }
  textAlign(LEFT);
  stroke(250,210,110,110);
  fill(250,210,110,110);
  text(myName,xL+2,yU+15);
}