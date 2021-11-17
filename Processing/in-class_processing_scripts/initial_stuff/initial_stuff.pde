// global variables - visible in the scope of all functions
int n = 5;
float x;

void setup(){
  size(900, 300);
  background(80);
  float y = 3.4; // y is declared with the scope of setup - it will not be visible in draw or any other function
  x = 13.8;
  println("n = " + n);
  println("in setup x = " + x);
  println("y = " + y);
}

void draw(){
  background(80);
  println(" --------------------- ");
  x += 0.1;
  for(int i=0 ;i<10000; i++){
    // print("i = " + i);
    fill( random(255), 70, 70, 100 );
    ellipse( random(width) , random(height) , 5, 5 );
  }
  //println("in draw x = " + x);
  n += 0.01; // will not produce error but will not change - it will be keeping the integer part all the time
  //println("in draw n = " + n);
  println("frameRate: " + frameRate);
  //println("in draw y = " + y); // -> produces error, not visible in y
  stroke(30,170,170);
  fill(180, 70, 40);
  // noFill();
  rect( x, 100 , 200, 50 );
}
