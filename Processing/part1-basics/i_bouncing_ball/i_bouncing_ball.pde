// declare variables
float ell_x = 0.0;
float ell_y = 200.0;
float ell_size = 50.0;

float direction_x = 1.0;
float direction_y = 1.0;

float red_component = 100.0;

void setup() {
  // initialise screen
  size(1000, 600);
  // initialise variables
  ell_x = 100.0;
  ell_y = 200.0;
  ell_size = 50.0;
  ellipseMode(CENTER);
}

void draw() {
  // draw background
  background(30);
  // draw ellangle
  fill(red_component, 150, 150);
  ellipse(ell_x, ell_y, ell_size, ell_size);
  ell_x = ell_x + direction_x*20;
  ell_y = ell_y + direction_y*17;
  if (ell_x > width - ell_size/2.0 || ell_x < ell_size/2.0){
    direction_x  = -1.0*direction_x;
    red_component = random(255);
  }
  if (ell_y > height - ell_size/2.0 || ell_y < ell_size/2.0){
    direction_y  = -1.0*direction_y;
    red_component = random(255);
  }
  if (ell_size < 150.0){
    ell_size = ell_size + 2;
  }
  // increase x coordinate -> move right
  //ell_x = ell_x > width + ell_size/2.0 ? ell_x = -ell_size/2.0 : ell_x+5;
}