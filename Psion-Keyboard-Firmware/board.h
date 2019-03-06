/*
 board.h
 
 This is how the pins are connected to the keyboard
 
 */

// This disables the RX and TX LEDs that are not on this PCB
#undef TXLED0
#undef RXLED0
#undef TXLED1
#undef RXLED1
#undef TX_RX_LED_INIT

#undef LED_BUILTIN_RX
#undef LED_BUILTIN_TX

#define TXLED0 0
#define RXLED0 0 
#define TXLED1 0
#define RXLED1 0
#define TX_RX_LED_INIT 0


#define LED_BUILTIN_RX 0
#define LED_BUILTIN_TX 0


// Standard LED is moved to pin 11
#undef LED_BUILTIN
#define LED_BUILTIN 11
 
// See the keyboard schematic for row/col mapping
#define NROWS 8
#define NCOLS 12

#define ROW_01  22
#define ROW_02  20
#define ROW_03  5
#define ROW_04  13
#define ROW_05  18
#define ROW_06  21
#define ROW_07  7
#define ROW_08  23

#define COL_1   19
#define COL_2   10
#define COL_3   9
#define COL_4   8
#define COL_5   6
#define COL_6   12
#define COL_7   4
#define COL_8   30
#define COL_9   3
#define COL_10  1
#define COL_11  0
#define COL_12  2

int Rows [NROWS] = {
  ROW_01,
  ROW_02,
  ROW_03,
  ROW_04,
  ROW_05,
  ROW_06,
  ROW_07,
  ROW_08
};

int Cols [NCOLS] = {
  COL_1,
  COL_2,
  COL_3,
  COL_4,
  COL_5,
  COL_6,
  COL_7,
  COL_8,
  COL_9,
  COL_10,
  COL_11,
  COL_12
};
