Human h;

void setup(){
  size(900,700);
  h = new Human("Tom", "male", 100., 200.);
  //frameRate(4);
}

void draw(){
  background(40);
  h.draw_myself();
  //h.change_my_image();
}

void mouseDragged(){
  h.move_myself(mouseX, mouseY);
  // println( h.x + " - " + h.y );
}
void mousePressed(){
  h.move_myself(mouseX, mouseY);
  // println( h.x + " - " + h.y );
}

class Human{
  float x, y;
  PImage my_image;
  String my_name;
  //String my_gender;
  // constructor
  Human(String name, String gender, float x_position, float y_position){
    my_name = name;
    //my_gender = gender;
    x = x_position;
    y = y_position;
    if (gender.equals("male")){
      my_image = loadImage("./figs/gentleman_image.png");
    }else{
      my_image = loadImage("./figs/lady_image.png");
    }
  }
  void draw_myself(){
    image(my_image, x, y, 70.0, 100.0);
  }
  void move_myself(float x_in, float y_in){
    x = x_in;
    y = y_in;
  }
  //void change_my_image(){
  //  if( my_gender.equals("male") ){
  //    my_gender = "female";
  //    my_image = loadImage("./figs/lady_image.png");
  //  }else{
  //    my_gender = "male";
  //    my_image = loadImage("./figs/gentleman_image.png");
  //  }
  //}
}
