// initialise variable
float x;

void setup(){
  size(600,300);
  x = 0.0;
  background(40);
}

void draw(){
  //background(40);
  increase_x(); // calling function increase_x()
  if (x > 100.0){
    textSize(32);
    fill(random(255), 100.0, 100.0);
    text("hi! - ", random(width), random(height)); 
    println("bang - " + x);
    x = 0.0;
  }
}

void increase_x(){
  x += 1.3; // same as: x = x + 1.3;
}

//void mousePressed(){
//  background(40);
//}
