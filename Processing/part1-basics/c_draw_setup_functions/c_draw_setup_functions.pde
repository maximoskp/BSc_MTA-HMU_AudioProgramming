// declare variables
float rect_x;
float rect_y;
float rect_size;

void setup() {
  // initialise screen
  size(800, 400);
  // initialise variables
  rect_x = 0.0;
  rect_y = 200.0;
  rect_size = 50.0;
  rectMode(CENTER);
  //frameRate(80);
}

void draw() {
  // draw background
  background(30);
  // draw rectangle
  rect(rect_x, rect_y, rect_size, rect_size);
  rect_x = increase_coordinate( rect_x , mouseX/10 );
}

void mouseDragged(){
  println("you've pressed on: " + mouseX + " - " + mouseY);
}

void keyPressed(){
  println("a key was pressed: " + int(key) );
  if (int(key) == 97){
    println("good!");
  }
}

float increase_coordinate(float coord, float incr_step){
  coord = coord + incr_step;
  if (coord > width + rect_size/2.0){
    coord = -rect_size/2.0;
  }
  return coord;
}