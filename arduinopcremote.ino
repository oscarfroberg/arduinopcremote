#include <IRremote.h> // Copyright 2009 Ken Shirriff http://www.arcfn.com/2009/08/multi-protocol-infrared-remote-library.html

int RECV_PIN = 11;
int RELAY_PIN = 8;
int RELAY_STATUS = 0;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn(); // Start the receiver
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, DEC);
    if ((results.value) == 16753245) {
      if (RELAY_STATUS == 0) {
        digitalWrite(RELAY_PIN, HIGH);
        RELAY_STATUS = 1;
        Serial.println("F"); // power off
      }
      else if (RELAY_STATUS == 1) {
        digitalWrite(RELAY_PIN, LOW);
        RELAY_STATUS = 0;
        Serial.println("O"); // power on
      } 
    }
  
  switch (results.value) {
    case 16761405:
      Serial.println("M"); // play-pause
      break;
    case 16769565:
      Serial.println("M"); // mute
      break;
    case 16754775:
      Serial.println("u"); // software vol up
      break;
    case 16769055:
      Serial.println("d"); // software vol down
      break;
    case 16750695:
      Serial.println("U"); // master vol up
      break;
    case 16738455:
      Serial.println("D"); // master vol down
      break;
    case 16720605:
      Serial.println("P"); // previous song
      break;
    case 16712445:
      Serial.println("N"); // next song
      break;
    case 16724175:
      Serial.println("s"); // start music player
      break;
    case 16756815:
      Serial.println("q"); // quit media and music player
      break;
    case 16736925:
      Serial.println("f"); // fullscreen
      break;
    case 16728765:
      Serial.println("b"); // vlc back 3 seconds
  }
  irrecv.resume(); // Receive the next value
  }
}
