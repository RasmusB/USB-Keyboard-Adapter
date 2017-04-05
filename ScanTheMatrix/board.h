/*
 board.h
 
 List all the pins that are connected to your keyboard. 
 */
 

#define NPINS 20    // Number of pins connected to the keyboard.

// This is a list of all pins that are connected to the keyboard.
int Pin [NPINS] = {
  0,
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10,
  12,
  13,
  18,
  19,
  20,
  21,
  22,
  23,
  30
};

// This is the name of the keyboard signal that each
// pin is connected to. Make sure to include unused
// pins in this list as well!
// This list MUST be in numerical pin order.
char* pinName[] = {
  "COL_11", // PIN0
  "COL_10", // PIN1
  "COL_12", // PIN2
  "COL_09", // PIN3
  "COL_07", // PIN4
  "ROW_03", // PIN5
  "COL_05", // PIN6
  "ROW_07", // PIN7
  "COL_04", // PIN8
  "COL_03", // PIN9
  "COL_02", // PIN10
  "-",      // PIN11 (LED)
  "COL_06", // PIN12
  "ROW_04", // PIN13
  "-",      // PIN14 - MISO
  "-",      // PIN15 - SCK
  "-",      // PIN16 - MOSI
  "-",      // PIN17 - SS
  "ROW_05", // PIN18
  "COL_01", // PIN19
  "ROW_02", // PIN20
  "ROW_06", // PIN21
  "ROW_01", // PIN22
  "ROW_08", // PIN23
  "-",      // PIN24
  "-",      // PIN25
  "-",      // PIN26
  "-",      // PIN27
  "-",      // PIN28
  "-",      // PIN29
  "COL_08"  // PIN30
};
