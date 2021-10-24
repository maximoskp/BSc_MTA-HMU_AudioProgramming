float x = 100.0, y = 100.0, col = 50.0;

float current_time = 0;

void setup(){
  size(400,400);
  background(0);
}

void draw(){
  //background(0);
  
  if (millis() >= current_time+500){
    current_time = millis();
    x = random(width);
    y = random(height);
    col = 200 + random(55);
    fill(col, 100);
    stroke(230);
    rect(x,y, 20,20);
  }
}
