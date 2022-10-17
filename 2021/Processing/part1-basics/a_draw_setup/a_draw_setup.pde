// declare variables
float rect_x;

void setup() {
  // initialise screen
  size(800, 400);
  // initialise variables
  rect_x = 400.0;

  //rectMode(CENTER);
  frameRate(60);
  background(55);
}

void draw() {
  // draw background
  //background(55);
  // draw rectangle
  fill(55, 55, 55, 10);
  rect(0, 0, width, height);
  fill(255, 0, 0);
  stroke(0, 255, 0);
  rect(rect_x, 200, 50, 50);
  rect_x += 2;
  if (rect_x > width) {
    rect_x = -50.0;
  }
}

void mouseClicked() {
  println("Mouse Clicked! - " + mouseX + " - " + mouseY);
}

void mousePressed() {
  println("Mouse Pressed! - " + mouseX + " - " + mouseY);
}

void mouseDragged() {
  println("Mouse Dragged! - " + mouseX + " - " + mouseY);
}

void keyPressed() {
  println("Key Pressed! - " + key);
}