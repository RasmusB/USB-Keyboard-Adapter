/*
 Psion-Keyboard-Firmware
 
 This is firmware for turning a Psion Series 5/5mx or Ericsson MC 128
 keyboard into a USB keyboard. The firmare is intended to run on a 
 ATmega32U4.
 
 */

#include "board.h"
#include "PsionKeymapUSB.h"

#define SERIAL_ENABLED 0
#define KEYBOARD_ENABLED 1

int keypressArrayCurrent [NROWS] [NCOLS];
int keypressArrayPrevious [NROWS] [NCOLS];

void setup() {
  
  if (SERIAL_ENABLED) Serial.begin(9600);
  
  Keyboard.begin();  
  
  // Scanlines in high-Z (inactive) mode
  // Pin state should be initialized to LOW
  for (int i = 0; i < NROWS; i++) {
    pinMode(Rows[i], INPUT);
  }
  
  // Columns as inputs
  // Internal pull-up enabled
  for (int i = 0; i < NCOLS; i++) {
    pinMode(Cols[i], INPUT_PULLUP);
  }
  
  /*
  // Prevoius state = no keys pressed
  for ( int i=0; i < NROWS; i++ ) {
    for ( int j=0; j < NCOLS; j++ ) {
      keypressArrayPrevious[i][j] = 1;
    }
  } 
 */ 
}

void loop() {
  
  int nKeysPressed = scanKeyboard(keypressArrayCurrent);
  
  /*
  Serial.print(nKeysPressed);
  Serial.println(" keys pressed");
  */
  
  sendKeys(keypressArrayCurrent, keypressArrayPrevious);
  
  memcpy(keypressArrayPrevious, keypressArrayCurrent, sizeof(keypressArrayCurrent));
  
  //delay(1000);

}

int scanKeyboard ( int keyArray [] [NCOLS] ) {

  int nKeysPressed = 0;
  
  for (int row = 0; row < NROWS; row++) {
    //Serial.print("Scanning row ");
    //Serial.println(row);
    
    // Select a pin to sink current
    pinMode(Rows[row], OUTPUT);
    digitalWrite(Rows[row], LOW);
    //delay(100);
    
    for (int col = 0; col < NCOLS; col++) {
      //Serial.print("Scanning col. ");
      //Serial.println(col);
      
      // Ignore any unmapped buttons
      if (keyScancode[row][col] != 0) {
        
        // =1 for every button NOT pressed (pull-ups enabled)
        // =0 for every button PRESSED (signal shorted to row pin)
        // This value is inverted when saved
        
        if ( digitalRead(Cols[col]) != HIGH ) {
          keyArray [row] [col] = 1;
          nKeysPressed++;

        } else {
          keyArray [row] [col] = 0;
        }
      }
    }
    
    // Return pin to high-Z (inactive) mode 
    digitalWrite(Rows[row], HIGH);
    pinMode(Rows[row], INPUT);
    
  }
  
  return nKeysPressed;
}

void sendKeys ( int pressedArray [] [NCOLS], int previousArray [] [NCOLS] ) {

  for ( int row = 0; row < NROWS; row++ ) {
    for ( int col = 0; col < NCOLS; col++ ) {
      
      // Ignore any unmapped buttons
      if (keyScancode[row][col] != 0) {
        
        if ( pressedArray[row][col] > previousArray[row][col] ) {
            
              if (SERIAL_ENABLED) {
                Serial.print(keyScancode[row][col], HEX);
                Serial.println(" pressed");
              };
            
            Keyboard.press_sc(keyScancode[row][col]);
        } 
        else if ( pressedArray[row][col] < previousArray[row][col] ) {
            
            if (SERIAL_ENABLED) {
              Serial.print(keyScancode[row][col], HEX);
              Serial.println(" released");
            };
            
            Keyboard.release_sc(keyScancode[row][col]);
            
        }
      }
    }  
  }
  
}
