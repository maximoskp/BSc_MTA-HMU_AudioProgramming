float starting_x;
float starting_y;

boolean drawing = false;

void setup() {
  size(500, 500);
  noStroke();
}

void draw() {
  background(126);
  
  if (drawing){
    fill(255);
    rect(starting_x, starting_y, -(starting_x-mouseX), -(starting_y-mouseY));
  }
}

void mousePressed(){
  drawing = true;
  starting_x = mouseX;
  starting_y = mouseY;
}

void mouseReleased(){
  drawing = false;
}