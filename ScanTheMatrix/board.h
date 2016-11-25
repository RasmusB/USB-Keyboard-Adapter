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
  11,
  12,
  13,
  18,
  19,
  20,
  21,
  22,
  23
};

// This is the name of the keyboard signal that each
// pin is connected to. Make sure to include unused
// pins in this list as well!
// This list must be sorted in numerical order.
char* pinName[] = {
  "COL_10", // PIN0
  "COL_8",  // PIN1
  "COL_11", // PIN2
  "COL_12", // PIN3
  "COL_7",  // PIN4
  "ROW_03", // PIN5
  "COL_4",  // PIN6
  "ROW_01", // PIN7
  "COL_5",  // PIN8
  "COL_6",  // PIN9
  "COL_2",  // PIN10
  "COL_9",  // PIN11
  "COL_3",  // PIN12
  "ROW_04", // PIN13
  "-",       // PIN14 - unused
  "-",       // PIN15 - unused
  "-",       // PIN16 - unused
  "-",       // PIN17 - unused
  "ROW_05", // PIN18
  "COL_1",  // PIN19
  "ROW_02", // PIN20
  "ROW_06", // PIN21
  "ROW_08", // PIN22
  "ROW_07"  // PIN23
};
