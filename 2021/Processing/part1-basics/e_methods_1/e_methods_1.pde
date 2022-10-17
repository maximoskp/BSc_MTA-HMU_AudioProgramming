// initialise variable
float x, y;

void setup(){
  size(600,300);
  x = 0.0;
  y = 0.0;
  background(40);
}

void draw(){
  // background(40);
  y = increase_variable(x, 1.3);
  x = increase_variable(y, 2.3);
  if (x > 100.0 && y > 100.0){
    // println("bang! - " + x + ", " + y);
    fill(120, 100);
    stroke(200);
    rect(x,y, 30, 30);
    x = random(50);
    y = random(70);
  }
  fill(255,0,0);
  ellipse( mouseX, mouseY, 10,10 );
}

float increase_variable(float t, float incr){
  t += incr;
  return t;
}

void mouseClicked(){
  println("mouseClicked!");
}
void mousePressed(){
  println("mousePressed!");
  fill(255,255,0);
  ellipse( mouseX, mouseY, 20,20 );
}
void mouseReleased(){
  println("mouseReleased!");
  fill(0, 255,255);
  ellipse( mouseX, mouseY, 20,20 );
}
void mouseDragged(){
  fill(255, 255,255);
  ellipse( mouseX, mouseY, 10,10 );
}
