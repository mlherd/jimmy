/*
 * rosserial Service Server
 */
 
#include <ros.h>
#include <rosserial_arduino/Test.h>

// Neo Pixel

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1
#define PIN            6

// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS      3

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

int delayval = 500; // delay for half a second
int flag = 0;

ros::NodeHandle  nh;
using rosserial_arduino::Test;

void callback(const Test::Request & req, Test::Response & res){
    if(String(req.input).equals("Talk")){
      flag = 1;
      res.output = "Started Talking";
    }
    if(String(req.input).equals("StopTalk")){
      flag = 0;
      res.output = "Stoped Talking";
    }
}

ros::ServiceServer<Test::Request, Test::Response> server("mouth",&callback);

void setup()
{
   pixels.begin(); // This initializes the NeoPixel library.
   nh.initNode();
   nh.advertiseService(server);
}

void loop()
{
  nh.spinOnce();
  delay(10);
  if (flag == 1){
    pixels.setPixelColor(0, pixels.Color(199,21,133));
    pixels.setPixelColor(1, pixels.Color(199,21,133));
    pixels.setPixelColor(2, pixels.Color(199,21,133));
    pixels.show();
    delay(200);
    pixels.setPixelColor(0, pixels.Color(0,0,0));
    pixels.setPixelColor(1, pixels.Color(0,0,0));
    pixels.setPixelColor(2, pixels.Color(0,0,0));
    pixels.show();
    delay(200);
  }
  else if (flag == 0){
    pixels.setPixelColor(0, pixels.Color(0,0,0));
    pixels.setPixelColor(1, pixels.Color(0,0,0));
    pixels.setPixelColor(2, pixels.Color(0,0,0));
    pixels.show();
    delay(10);
  }
}
