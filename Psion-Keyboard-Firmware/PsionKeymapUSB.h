/*
 PsionKeymapUSB.h
 
 Maps the keys to USB scancodes
 Note that the "Fn" and "Menu" keys are
 mapped to AltGr and Alt respectively.
 This is to make some kind of Plug 'n Play
 possible.
 
 */

#define KEY_A          0x04
#define KEY_B          0x05
#define KEY_C          0x06
#define KEY_D          0x07
#define KEY_E          0x08
#define KEY_F          0x09
#define KEY_G          0x0A
#define KEY_H          0x0B
#define KEY_I          0x0C
#define KEY_J          0x0D
#define KEY_K          0x0E
#define KEY_L          0x0F
#define KEY_M          0x10
#define KEY_N          0x11
#define KEY_O          0x12
#define KEY_P          0x13
#define KEY_Q          0x14
#define KEY_R          0x15
#define KEY_S          0x16
#define KEY_T          0x17
#define KEY_U          0x18
#define KEY_V          0x19
#define KEY_W          0x1A
#define KEY_X          0x1B
#define KEY_Y          0x1C
#define KEY_Z          0x1D

#define KEY_1          0x1E
#define KEY_2          0x1F
#define KEY_3          0x20
#define KEY_4          0x21
#define KEY_5          0x22
#define KEY_6          0x23
#define KEY_7          0x24
#define KEY_8          0x25
#define KEY_9          0x26
#define KEY_0          0x27

#define KEY_ENTER      0x28
#define KEY_ESC        0x29
#define KEY_BACKSPACE  0x2A
#define KEY_TAB        0x2B
#define KEY_SPACE      0x2C
#define KEY_APOSTROPHE 0x35
#define KEY_COMMA      0x36
#define KEY_PERIOD     0x37
#define KEY_RIGHT      0x4F
#define KEY_LEFT       0x50
#define KEY_DOWN       0x51
#define KEY_UP         0x52
#define KEY_CTRL       0xE0
#define KEY_LSHIFT     0xE1
#define KEY_MENU       0xE2  // Mapped as AltGr
#define KEY_RSHIFT     0xE5
#define KEY_FN         0xE6  // Mapped as Alt

static int keyScancode [NROWS] [NCOLS] = {
  { 0       ,KEY_SPACE ,KEY_UP ,KEY_COMMA ,KEY_LEFT      ,KEY_RIGHT      ,KEY_LSHIFT ,0          ,0        ,0      ,0        ,0       },
  { KEY_1   ,KEY_2     ,KEY_3  ,KEY_4     ,KEY_5         ,KEY_6          ,0          ,0          ,0        ,0      ,0        ,0       },
  { KEY_7   ,KEY_8     ,KEY_9  ,KEY_0     ,KEY_BACKSPACE ,KEY_APOSTROPHE ,0          ,0          ,0        ,0      ,0        ,0       },
  { KEY_Q   ,KEY_W     ,KEY_E  ,KEY_R     ,KEY_T         ,KEY_Y          ,0          ,0          ,0        ,0      ,0        ,KEY_ESC },
  { KEY_U   ,KEY_I     ,KEY_O  ,KEY_P     ,KEY_L         ,KEY_ENTER      ,0          ,0          ,0        ,0      ,KEY_MENU ,0       },
  { KEY_TAB ,KEY_A     ,KEY_S  ,KEY_D     ,KEY_F         ,KEY_G          ,0          ,0          ,KEY_CTRL ,0      ,0        ,0       },
  { KEY_H   ,KEY_J     ,KEY_K  ,KEY_M     ,KEY_PERIOD    ,KEY_DOWN       ,0          ,0          ,0        ,KEY_FN ,0        ,0       },
  { KEY_Z   ,KEY_X     ,KEY_C  ,KEY_V     ,KEY_B         ,KEY_N          ,0          ,KEY_RSHIFT ,0        ,0      ,0        ,0       }
};
