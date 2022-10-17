ArrayList<Rectangle_Class> r;

void setup(){
  size(600,400);
  r = new ArrayList<Rectangle_Class>();
  for (int i=0; i<10; i++){
    r.add(new Rectangle_Class(width, height));
  }
  
}

void draw(){
  background(0);
  for (int i=0; i<10; i++){
    r.get(i).draw_myself();
  }
  fill(255,200);
  ellipse(mouseX, mouseY, 10,10);
}

void mouseClicked(){
  for (int i=0; i<10; i++){
    r.get(i).check_if_clicked(mouseX, mouseY);
  }
}

void mouseDragged(){
  fill(255, 70,79,200);
  ellipse(mouseX, mouseY, 15,15);
}
void mousePressed(){
  fill(255, 70,79,200);
  ellipse(mouseX, mouseY, 15,15);
}
