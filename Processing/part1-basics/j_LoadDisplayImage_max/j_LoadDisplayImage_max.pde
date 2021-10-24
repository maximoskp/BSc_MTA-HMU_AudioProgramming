/**
 * Load and Display 
 * 
 * Images can be loaded and displayed to the screen at their actual size
 * or any other size. 
 */

PImage img;  // Declare variable "a" of type PImage
float x = 100;
float y = 100;

void setup() {
  size(640, 360);
  // The image file must be in the data folder of the current sketch 
  // to load successfully
  img = loadImage("moonwalk.jpg");  // Load the image into the program
  imageMode(CENTER);
}

void draw() {
  background(200);
  // Displays the image at point (0, height/2) at half of its size
  image(img, x, y, img.width/2, img.height/2);
}

void mouseDragged(){
  x = mouseX;
  y = mouseY;
}
void mousePressed(){
  println("mouse is pressed!");
  x = mouseX;
  y = mouseY;
}
void mouseReleased(){
  println("mouse is released!");
}