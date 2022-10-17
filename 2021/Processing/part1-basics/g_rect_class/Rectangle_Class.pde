class Rectangle_Class{
  
  float world_x;
  float world_y;
  
  float my_X_size;
  float my_Y_size;
  
  float my_X_position;
  float my_Y_position;
  
  float myR;
  float myG;
  float myB;
  
  Rectangle_Class(float world_X_size, float world_Y_size){
    world_x = world_X_size;
    world_y = world_Y_size;
    
    my_X_size = 10.0 + random(90);
    my_Y_size = 10.0 + random(90);
    
    my_X_position = random(world_x);
    my_Y_position = random(world_y);
    
    myR = random(255);
    myG = random(255);
    myB = random(255);
    
    //println("Hello!");
  }
  
  void draw_myself(){
    rectMode(CENTER);
    fill(myR, myG, myB);
    //stroke(255);
    rect(my_X_position, my_Y_position, my_X_size, my_Y_size);
  }
  
  void check_if_clicked(float x, float y){
    if (x >= my_X_position-my_X_size/2.0 && x <= my_X_position+my_X_size/2.0 && 
          y >= my_Y_position-my_Y_size/2.0 && y <= my_Y_position+my_Y_size/2.0){
      println("ouch!");
      
      my_X_size = 10.0 + random(90);
      my_Y_size = 10.0 + random(90);
      
      my_X_position = random(world_x);
      my_Y_position = random(world_y);
      
    }
  }
  
}
