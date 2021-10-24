import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import ddf.minim.*; 
import ddf.minim.analysis.*; 
import ddf.minim.effects.*; 
import ddf.minim.signals.*; 
import ddf.minim.spi.*; 
import ddf.minim.ugens.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class the_mentor extends PApplet {








float breath = 0.0f;
float breath_speed = 0.1f;
float breath_direction = +1;

float current_time;

Minim minim;
AudioOutput out;
ArrayList<Sampler> s = new ArrayList<Sampler>();
ArrayList<MoogFilter> b = new ArrayList<MoogFilter>();
ArrayList<Gain> g = new ArrayList<Gain>();
ArrayList<Pan> p = new ArrayList<Pan>();
int sample_idx = 0;

Delay d;
Sampler victory_sample;

float x, y, x_w, y_w, angle_from, angle_to;

float vol, q, c;

int col;

boolean victory = false;

public void setup(){
  
  background(0);
  minim = new Minim(this);
  out = minim.getLineOut();
  
  d = new Delay( 0.25f, 0.9f, true, true );
  victory_sample = new Sampler( "a18.mp3", 1, minim );
  victory_sample.patch(d).patch(out);
  
  for (int i=0; i<25; i++){
    //s.add( minim.loadSample("a"+str(i%25)+".mp3") );
    s.add( new Sampler( "a"+str(i%25)+".mp3", 4, minim ));
    b.add( new MoogFilter( 1500, 0.1f ) );
    b.get(i).type = MoogFilter.Type.BP;
    b.get(i).setChannelCount(2);
    g.add(new Gain(-50.0f));
    g.get(i).setChannelCount(2);
    p.add(new Pan(0.0f));
    s.get(i).patch(g.get(i)).patch(p.get(i)).patch(b.get(i)).patch(out);
  }
  
  x = random(width);
  y = random(height);
  
  current_time = millis();
  
  textSize(32);
  textAlign(CENTER, CENTER);
  
}

public void draw(){
  breath += breath_direction*breath_speed;
  if (breath > 10.0f || breath <= 0.0f) breath_direction *= -1;
  if (victory){
    fill(255,255,224, breath);
    rect(0, height/2.0f - 1, width, 2);
    rect(width/2.0f - 1, 0, 2, height);
    fill(255,0,0);
    text("You won :( ", width/2.0f,height/2.0f);
  }else{
    fill(255,0,0, breath);
    rect(0, height/2.0f - 1, width, 2);
    rect(width/2.0f - 1, 0, 2, height);
  }
  
  fill(0, 2);
  rect(0,0,width, height);
  
  if (millis() - current_time > 50 && !victory){
    x_w = random(width)/(2.0f*abs(width/2 - mouseX)+10.0f) + 1.0f;
    y_w = random(height)/(2.0f*abs(height/2 - mouseY)+10.0f) + 1.0f;
    // x += random(2)/1.0*x_w - 1.0*x_w;
    x += x_w*( (mouseX*random(200)/100.0f - width/2.0f)/(width/2.0f) );
    if (x < 0.0f) x += width;
    if (x > width) x = width-x;
    // y += random(2)/1.0*y_w - 1.0*y_w;
    y += y_w*( (mouseY*random(200)/100.0f - height/2.0f)/(height/2.0f) );
    if (y < 0.0f) y += height;
    if (y > height) y = height-y;
    angle_from = random(1000)*PI/1000.0f;
    angle_to = random(1000)*TWO_PI/1000.0f;
    
    col = (int)random(255);
    fill(col);
    arc(x, y, x_w, y_w, angle_from, angle_to);
    
    vol = 5.0f*pow((x_w + y_w)/5.0f, 0.8f ) - 50.0f;
    if (vol > -1.0f) vol = -1.0f;
    
    sample_idx = col%25;
    
    g.get(sample_idx).setValue(vol);
    p.get(sample_idx).setPan((2.0f*x-width)/width);
    b.get(sample_idx).frequency.setLastValue( 1000.0f*abs(angle_from-angle_to) );
    b.get(sample_idx).resonance.setLastValue( abs(angle_from-angle_from)/TWO_PI );
    s.get(sample_idx).trigger();
    
    current_time = millis();
    
    if (x <= width/2.0f && x+x_w >= width/2.0f && y <= height/2.0f && y+y_w >= height/2.0f){
      victory = true;
      fill(255,0,0);
      text("You won :( ", width/2.0f,height/2.0f);
      victory_sample.trigger();
    }
  }
}

public void mousePressed(){
  victory = true;
  fill(255,0,0);
  text("You won :( ", width/2.0f,height/2.0f);
  victory_sample.trigger();
}
  public void settings() {  size(900, 700); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "the_mentor" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
