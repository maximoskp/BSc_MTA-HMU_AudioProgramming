import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress dest;
OscMessage msg = new OscMessage("/values");

void setup() {
  size(640, 480);
  // start oscP5, listening for incoming messages at port 9000
  oscP5 = new OscP5(this,9000);
  // send to port 12000
  dest = new NetAddress("127.0.0.1",5005);
  
}

void draw() {
  background(0);
  fill(255);
  ellipse(mouseX, mouseY, 10, 10);
  sendOsc();
}

void sendOsc() {
  msg.clear();
  msg.setAddrPattern("/values");
  msg.add((float)mouseX); 
  msg.add((float)mouseY);
  oscP5.send(msg, dest);
}
