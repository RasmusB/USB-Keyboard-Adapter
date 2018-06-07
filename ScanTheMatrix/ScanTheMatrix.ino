/*
ScanTheMatrix

 This is a sketch for scanning and .

 */

#include "board.h"
#define LED_PIN 11


void setup() {

  Serial.begin(9600);
  //while (!Serial);

  // All pins in high-Z (inactive) mode
  // Pin state should be initialized to LOW
  for (int i = 0; i < NPINS; i++) {
    pinMode(Pin[i], INPUT);
  }
  pinMode(LED_PIN, OUTPUT);
}



void loop() {

  if ( Serial.available() ) {
    Serial.println("Pin mapping:");
    for (int i = 0; i <= 30; i++) {
      Serial.print(i);
      Serial.print(": ");
      Serial.println(pinName[i]);
    }
    while (Serial.available() ) Serial.read();
    Serial.println("--------");
  }

  for (int i = 0; i < NPINS; i++) {      // "Sense" pin

    pinMode(Pin[i], INPUT_PULLUP);

    for (int j = 0; j < NPINS; j++) {    // "Select" pin

      // Pin collision! Abort and try next.
      if (i == j) {
        continue;
      }

      if ( digitalRead(Pin[i]) == LOW ) {
        Serial.print("Error on pin ");
        Serial.println(Pin[i]);
      } else {
        pinMode(Pin[j], OUTPUT);
        digitalWrite(Pin[j], LOW);

        if ( digitalRead(Pin[i]) == LOW && Pin[i] > Pin[j] ) {
          Serial.print("Found connection, pins ");

          Serial.print(Pin[i]);
          Serial.print(" (");
          Serial.print(pinName[Pin[i]]);

          Serial.print(") and ");

          Serial.print(Pin[j]);
          Serial.print(" (");
          Serial.print(pinName[Pin[j]]);
          Serial.println(")");

          digitalWrite(LED_PIN, HIGH);
          
          while (digitalRead(Pin[i]) == LOW);
          
          /*
          while( !Serial.available() );
          while( Serial.available() ) Serial.read() ;
          */
        }

        digitalWrite(Pin[j], LOW);
        pinMode(Pin[j], INPUT);

        digitalWrite(LED_PIN, LOW);

      }      
    }
    
     pinMode(Pin[i], INPUT);
  }
}
