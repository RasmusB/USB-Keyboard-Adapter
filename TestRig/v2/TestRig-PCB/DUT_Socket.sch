EESchema Schematic File Version 4
LIBS:TestRig-PCB-cache
EELAYER 29 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 2 2
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:GND #PWR0202
U 1 1 5DB0EE50
P 4400 8150
AR Path="/5DB0CBB8/5DB0EE50" Ref="#PWR0202"  Part="1" 
AR Path="/5DB22390/5DB0EE50" Ref="#PWR?"  Part="1" 
AR Path="/5DB223CE/5DB0EE50" Ref="#PWR?"  Part="1" 
AR Path="/5DB25ADF/5DB0EE50" Ref="#PWR0302"  Part="1" 
AR Path="/5DB25B10/5DB0EE50" Ref="#PWR0402"  Part="1" 
F 0 "#PWR0202" H 4400 7900 50  0001 C CNN
F 1 "GND" H 4405 7977 50  0000 C CNN
F 2 "" H 4400 8150 50  0001 C CNN
F 3 "" H 4400 8150 50  0001 C CNN
	1    4400 8150
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP205
U 1 1 5DB17266
P 3950 7550
AR Path="/5DB0CBB8/5DB17266" Ref="TP205"  Part="1" 
AR Path="/5DB22390/5DB17266" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB17266" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB17266" Ref="TP305"  Part="1" 
AR Path="/5DB25B10/5DB17266" Ref="TP405"  Part="1" 
F 0 "TP205" H 4008 7668 50  0000 L CNN
F 1 "VBUS" H 4008 7577 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4150 7550 50  0001 C CNN
F 3 "~" H 4150 7550 50  0001 C CNN
	1    3950 7550
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP206
U 1 1 5DB177F9
P 4400 7550
AR Path="/5DB0CBB8/5DB177F9" Ref="TP206"  Part="1" 
AR Path="/5DB22390/5DB177F9" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB177F9" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB177F9" Ref="TP306"  Part="1" 
AR Path="/5DB25B10/5DB177F9" Ref="TP406"  Part="1" 
F 0 "TP206" H 4458 7668 50  0000 L CNN
F 1 "GND" H 4458 7577 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4600 7550 50  0001 C CNN
F 3 "~" H 4600 7550 50  0001 C CNN
	1    4400 7550
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP201
U 1 1 5DB199F8
P 3800 6400
AR Path="/5DB0CBB8/5DB199F8" Ref="TP201"  Part="1" 
AR Path="/5DB22390/5DB199F8" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB199F8" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB199F8" Ref="TP301"  Part="1" 
AR Path="/5DB25B10/5DB199F8" Ref="TP401"  Part="1" 
F 0 "TP201" V 3754 6588 50  0000 L CNN
F 1 "RESET" V 3845 6588 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4000 6400 50  0001 C CNN
F 3 "~" H 4000 6400 50  0001 C CNN
	1    3800 6400
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP202
U 1 1 5DB19A02
P 3800 6600
AR Path="/5DB0CBB8/5DB19A02" Ref="TP202"  Part="1" 
AR Path="/5DB22390/5DB19A02" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB19A02" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB19A02" Ref="TP302"  Part="1" 
AR Path="/5DB25B10/5DB19A02" Ref="TP402"  Part="1" 
F 0 "TP202" V 3754 6788 50  0000 L CNN
F 1 "SCK" V 3845 6788 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4000 6600 50  0001 C CNN
F 3 "~" H 4000 6600 50  0001 C CNN
	1    3800 6600
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP204
U 1 1 5DB19D21
P 3800 7000
AR Path="/5DB0CBB8/5DB19D21" Ref="TP204"  Part="1" 
AR Path="/5DB22390/5DB19D21" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB19D21" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB19D21" Ref="TP304"  Part="1" 
AR Path="/5DB25B10/5DB19D21" Ref="TP404"  Part="1" 
F 0 "TP204" V 3754 7188 50  0000 L CNN
F 1 "MISO" V 3845 7188 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4000 7000 50  0001 C CNN
F 3 "~" H 4000 7000 50  0001 C CNN
	1    3800 7000
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP203
U 1 1 5DB19D2B
P 3800 6800
AR Path="/5DB0CBB8/5DB19D2B" Ref="TP203"  Part="1" 
AR Path="/5DB22390/5DB19D2B" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB19D2B" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB19D2B" Ref="TP303"  Part="1" 
AR Path="/5DB25B10/5DB19D2B" Ref="TP403"  Part="1" 
F 0 "TP203" V 3754 6988 50  0000 L CNN
F 1 "MOSI" V 3845 6988 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4000 6800 50  0001 C CNN
F 3 "~" H 4000 6800 50  0001 C CNN
	1    3800 6800
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small R201
U 1 1 5DB1B2BD
P 3950 7700
AR Path="/5DB0CBB8/5DB1B2BD" Ref="R201"  Part="1" 
AR Path="/5DB22390/5DB1B2BD" Ref="R?"  Part="1" 
AR Path="/5DB223CE/5DB1B2BD" Ref="R?"  Part="1" 
AR Path="/5DB25ADF/5DB1B2BD" Ref="R301"  Part="1" 
AR Path="/5DB25B10/5DB1B2BD" Ref="R401"  Part="1" 
F 0 "R201" H 4009 7746 50  0000 L CNN
F 1 "10k 1%" H 4009 7655 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 3950 7700 50  0001 C CNN
F 3 "~" H 3950 7700 50  0001 C CNN
	1    3950 7700
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R202
U 1 1 5DB1C4A9
P 3950 8000
AR Path="/5DB0CBB8/5DB1C4A9" Ref="R202"  Part="1" 
AR Path="/5DB22390/5DB1C4A9" Ref="R?"  Part="1" 
AR Path="/5DB223CE/5DB1C4A9" Ref="R?"  Part="1" 
AR Path="/5DB25ADF/5DB1C4A9" Ref="R302"  Part="1" 
AR Path="/5DB25B10/5DB1C4A9" Ref="R402"  Part="1" 
F 0 "R202" H 4009 8046 50  0000 L CNN
F 1 "10k 1%" H 4009 7955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 3950 8000 50  0001 C CNN
F 3 "~" H 3950 8000 50  0001 C CNN
	1    3950 8000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 7550 3950 7600
Wire Wire Line
	3950 7800 3950 7850
Wire Wire Line
	3950 7850 2700 7850
Connection ~ 3950 7850
Wire Wire Line
	3950 7850 3950 7900
Text Label 2800 7850 0    50   ~ 0
DUT_VBUS
Wire Wire Line
	3950 8100 3950 8150
Wire Wire Line
	4400 7550 4400 8150
$Comp
L power:GND #PWR0201
U 1 1 5DB1E8DC
P 3950 8150
AR Path="/5DB0CBB8/5DB1E8DC" Ref="#PWR0201"  Part="1" 
AR Path="/5DB22390/5DB1E8DC" Ref="#PWR?"  Part="1" 
AR Path="/5DB223CE/5DB1E8DC" Ref="#PWR?"  Part="1" 
AR Path="/5DB25ADF/5DB1E8DC" Ref="#PWR0301"  Part="1" 
AR Path="/5DB25B10/5DB1E8DC" Ref="#PWR0401"  Part="1" 
F 0 "#PWR0201" H 3950 7900 50  0001 C CNN
F 1 "GND" H 3955 7977 50  0000 C CNN
F 2 "" H 3950 8150 50  0001 C CNN
F 3 "" H 3950 8150 50  0001 C CNN
	1    3950 8150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 6400 2700 6400
Text Label 2800 6400 0    50   ~ 0
ICSP_RESET
Wire Wire Line
	3800 6600 2700 6600
Text Label 2800 6600 0    50   ~ 0
ICSP_SCK
Wire Wire Line
	3800 6800 2700 6800
Text Label 2800 6800 0    50   ~ 0
ICSP_MOSI
Wire Wire Line
	3800 7000 2700 7000
Text Label 2800 7000 0    50   ~ 0
ICSP_MISO
Text HLabel 2700 7850 0    50   Output ~ 0
DUT_VBUS
Text HLabel 2700 6400 0    50   Input ~ 0
ICSP_RESET
Text HLabel 2700 6600 0    50   Input ~ 0
ICSP_SCK
Text HLabel 2700 6800 0    50   Input ~ 0
ICSP_MOSI
Text HLabel 2700 7000 0    50   Output ~ 0
ICSP_MISO
$Comp
L rbv_pcb_extras:PCB_OUTLINE DUT201
U 1 1 5DB21260
P 12900 2600
AR Path="/5DB0CBB8/5DB21260" Ref="DUT201"  Part="1" 
AR Path="/5DB22390/5DB21260" Ref="DUT?"  Part="1" 
AR Path="/5DB223CE/5DB21260" Ref="DUT?"  Part="1" 
AR Path="/5DB25ADF/5DB21260" Ref="DUT301"  Part="1" 
AR Path="/5DB25B10/5DB21260" Ref="DUT401"  Part="1" 
F 0 "DUT201" H 13428 2706 60  0000 L CNN
F 1 "DUT_OUTLINE" H 13428 2600 60  0000 L CNN
F 2 "USB-Keyboard:USB_KEYBOARD_ADAPTER_V1.22_DUMMY" H 13428 2494 60  0000 L CNN
F 3 "" H 12900 2600 60  0000 C CNN
	1    12900 2600
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP207
U 1 1 5DB28AF9
P 3800 7200
AR Path="/5DB0CBB8/5DB28AF9" Ref="TP207"  Part="1" 
AR Path="/5DB22390/5DB28AF9" Ref="TP?"  Part="1" 
AR Path="/5DB223CE/5DB28AF9" Ref="TP?"  Part="1" 
AR Path="/5DB25ADF/5DB28AF9" Ref="TP?"  Part="1" 
AR Path="/5DB25B10/5DB28AF9" Ref="TP?"  Part="1" 
F 0 "TP207" V 3754 7388 50  0000 L CNN
F 1 "VTARGET" V 3845 7388 50  0000 L CNN
F 2 "Pogo:Pogo_P50_Bottom" H 4000 7200 50  0001 C CNN
F 3 "~" H 4000 7200 50  0001 C CNN
	1    3800 7200
	0    1    1    0   
$EndComp
Wire Wire Line
	3800 7200 2700 7200
Text Label 2800 7200 0    50   ~ 0
ICSP_VTARGET
Text HLabel 2700 7200 0    50   Output ~ 0
ICSP_VTARGET
$Comp
L rbv_keyboard:KEYBOARD-PSION-5MX J201
U 1 1 5DB75D08
P 11150 2100
F 0 "J201" H 11150 3350 60  0000 L CNN
F 1 "DUT_CONN" H 11200 900 60  0000 L CNN
F 2 "Connector_FFC-FPC:Hirose_FH12-22S-0.5SH_1x22-1MP_P0.50mm_Horizontal" H 11750 3400 60  0001 C CNN
F 3 "" H 11150 2900 60  0000 C CNN
	1    11150 2100
	1    0    0    -1  
$EndComp
Text Label 2700 2650 0    50   ~ 0
KB_02
Text Label 2700 2950 0    50   ~ 0
KB_03
Text Label 2700 2850 0    50   ~ 0
KB_04
Text Label 2700 2750 0    50   ~ 0
KB_05
Text Label 2700 2550 0    50   ~ 0
KB_06
Text Label 2700 2450 0    50   ~ 0
KB_07
Text Label 2700 2050 0    50   ~ 0
KB_08
Text Label 2700 2150 0    50   ~ 0
KB_09
Text Label 2700 2250 0    50   ~ 0
KB_10
Text Label 2700 2350 0    50   ~ 0
KB_11
Text Label 2700 1950 0    50   ~ 0
KB_12
Text Label 2700 1250 0    50   ~ 0
KB_13
Text Label 2700 1350 0    50   ~ 0
KB_14
Text Label 2700 1450 0    50   ~ 0
KB_15
Text Label 2700 1850 0    50   ~ 0
KB_16
Text Label 2700 1150 0    50   ~ 0
KB_17
Text Label 2700 1550 0    50   ~ 0
KB_18
Text Label 2700 1650 0    50   ~ 0
KB_19
Text Label 2700 1750 0    50   ~ 0
KB_20
$Comp
L 74xx:74LS165 U201
U 1 1 5DB980D1
P 4800 4500
F 0 "U201" H 4800 5581 50  0000 C CNN
F 1 "74LS165" H 4800 5490 50  0000 C CNN
F 2 "Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm" H 4800 4500 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS165" H 4800 4500 50  0001 C CNN
	1    4800 4500
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS165 U202
U 1 1 5DB9B0E5
P 7000 4500
F 0 "U202" H 7000 5581 50  0000 C CNN
F 1 "74LS165" H 7000 5490 50  0000 C CNN
F 2 "Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm" H 7000 4500 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS165" H 7000 4500 50  0001 C CNN
	1    7000 4500
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS165 U203
U 1 1 5DB9C001
P 9200 4500
F 0 "U203" H 9200 5581 50  0000 C CNN
F 1 "74LS165" H 9200 5490 50  0000 C CNN
F 2 "Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm" H 9200 4500 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS165" H 9200 4500 50  0001 C CNN
	1    9200 4500
	1    0    0    -1  
$EndComp
NoConn ~ 5300 4000
NoConn ~ 7500 4000
NoConn ~ 9700 4000
Wire Wire Line
	5300 3900 6500 3900
Wire Wire Line
	7500 3900 8700 3900
$Comp
L power:GND #PWR0101
U 1 1 5DB9FFA0
P 4800 5500
AR Path="/5DB0CBB8/5DB9FFA0" Ref="#PWR0101"  Part="1" 
AR Path="/5DB22390/5DB9FFA0" Ref="#PWR?"  Part="1" 
AR Path="/5DB223CE/5DB9FFA0" Ref="#PWR?"  Part="1" 
AR Path="/5DB25ADF/5DB9FFA0" Ref="#PWR?"  Part="1" 
AR Path="/5DB25B10/5DB9FFA0" Ref="#PWR?"  Part="1" 
F 0 "#PWR0101" H 4800 5250 50  0001 C CNN
F 1 "GND" H 4805 5327 50  0000 C CNN
F 2 "" H 4800 5500 50  0001 C CNN
F 3 "" H 4800 5500 50  0001 C CNN
	1    4800 5500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5DBA0C22
P 7000 5500
AR Path="/5DB0CBB8/5DBA0C22" Ref="#PWR0102"  Part="1" 
AR Path="/5DB22390/5DBA0C22" Ref="#PWR?"  Part="1" 
AR Path="/5DB223CE/5DBA0C22" Ref="#PWR?"  Part="1" 
AR Path="/5DB25ADF/5DBA0C22" Ref="#PWR?"  Part="1" 
AR Path="/5DB25B10/5DBA0C22" Ref="#PWR?"  Part="1" 
F 0 "#PWR0102" H 7000 5250 50  0001 C CNN
F 1 "GND" H 7005 5327 50  0000 C CNN
F 2 "" H 7000 5500 50  0001 C CNN
F 3 "" H 7000 5500 50  0001 C CNN
	1    7000 5500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 5DBA0FF0
P 9200 5500
AR Path="/5DB0CBB8/5DBA0FF0" Ref="#PWR0103"  Part="1" 
AR Path="/5DB22390/5DBA0FF0" Ref="#PWR?"  Part="1" 
AR Path="/5DB223CE/5DBA0FF0" Ref="#PWR?"  Part="1" 
AR Path="/5DB25ADF/5DBA0FF0" Ref="#PWR?"  Part="1" 
AR Path="/5DB25B10/5DBA0FF0" Ref="#PWR?"  Part="1" 
F 0 "#PWR0103" H 9200 5250 50  0001 C CNN
F 1 "GND" H 9205 5327 50  0000 C CNN
F 2 "" H 9200 5500 50  0001 C CNN
F 3 "" H 9200 5500 50  0001 C CNN
	1    9200 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 1050 7900 1050
Wire Wire Line
	2700 1150 6100 1150
Wire Wire Line
	2700 1350 6400 1350
Wire Wire Line
	2700 1450 6300 1450
Wire Wire Line
	2700 1550 8200 1550
Wire Wire Line
	2700 1650 8100 1650
Wire Wire Line
	2700 1750 8000 1750
Wire Wire Line
	2700 1850 6200 1850
Wire Wire Line
	2700 2050 4000 2050
Wire Wire Line
	2700 2150 3900 2150
Wire Wire Line
	2700 2450 4100 2450
Wire Wire Line
	2700 2550 4200 2550
Wire Wire Line
	2700 2650 3800 2650
Wire Wire Line
	2700 2750 3500 2750
Wire Wire Line
	2700 2850 3600 2850
Wire Wire Line
	2700 2950 3700 2950
Text Label 2700 1050 0    50   ~ 0
KB_21
Wire Wire Line
	4300 4000 4200 4000
Wire Wire Line
	4300 4100 4100 4100
Wire Wire Line
	4300 4200 4000 4200
Wire Wire Line
	4300 4300 3900 4300
Wire Wire Line
	4300 4400 3800 4400
Wire Wire Line
	4300 4500 3700 4500
Wire Wire Line
	4300 4600 3600 4600
Wire Wire Line
	4300 4700 3500 4700
Wire Wire Line
	6500 4000 6400 4000
Wire Wire Line
	6500 4100 6300 4100
Wire Wire Line
	6500 4200 6200 4200
Wire Wire Line
	6500 4300 6100 4300
Wire Wire Line
	6500 4400 6000 4400
Wire Wire Line
	6500 4500 5900 4500
Wire Wire Line
	6500 4600 5800 4600
Wire Wire Line
	6500 4700 5700 4700
Wire Wire Line
	8700 4400 8200 4400
Wire Wire Line
	8700 4500 8100 4500
Wire Wire Line
	8700 4600 8000 4600
Wire Wire Line
	8700 4700 7900 4700
Wire Wire Line
	3800 4400 3800 2650
Connection ~ 3800 2650
Wire Wire Line
	3800 2650 10950 2650
Wire Wire Line
	3700 4500 3700 2950
Connection ~ 3700 2950
Wire Wire Line
	3700 2950 10950 2950
Wire Wire Line
	3600 2850 3600 4600
Connection ~ 3600 2850
Wire Wire Line
	3600 2850 10950 2850
Wire Wire Line
	3500 4700 3500 2750
Connection ~ 3500 2750
Wire Wire Line
	3500 2750 10950 2750
NoConn ~ 8700 4000
NoConn ~ 8700 4100
NoConn ~ 8700 4200
NoConn ~ 8700 4300
Wire Wire Line
	4200 2550 4200 4000
Connection ~ 4200 2550
Wire Wire Line
	4200 2550 10950 2550
Wire Wire Line
	4100 4100 4100 2450
Connection ~ 4100 2450
Wire Wire Line
	4100 2450 10950 2450
Wire Wire Line
	4000 4200 4000 2050
Connection ~ 4000 2050
Wire Wire Line
	4000 2050 10950 2050
Wire Wire Line
	3900 4300 3900 2150
Connection ~ 3900 2150
Wire Wire Line
	3900 2150 10950 2150
Wire Wire Line
	2700 1250 5700 1250
Wire Wire Line
	2700 1950 5800 1950
Wire Wire Line
	2700 2350 5900 2350
Wire Wire Line
	2700 2250 6000 2250
Wire Wire Line
	6000 4400 6000 2250
Connection ~ 6000 2250
Wire Wire Line
	6000 2250 10950 2250
Wire Wire Line
	5900 4500 5900 2350
Connection ~ 5900 2350
Wire Wire Line
	5900 2350 10950 2350
Wire Wire Line
	5800 4600 5800 1950
Connection ~ 5800 1950
Wire Wire Line
	5800 1950 10950 1950
Wire Wire Line
	5700 4700 5700 1250
Connection ~ 5700 1250
Wire Wire Line
	5700 1250 10950 1250
Wire Wire Line
	6400 4000 6400 1350
Connection ~ 6400 1350
Wire Wire Line
	6400 1350 10950 1350
Wire Wire Line
	6300 4100 6300 1450
Connection ~ 6300 1450
Wire Wire Line
	6300 1450 10950 1450
Wire Wire Line
	6200 4200 6200 1850
Connection ~ 6200 1850
Wire Wire Line
	6200 1850 10950 1850
Wire Wire Line
	6100 4300 6100 1150
Connection ~ 6100 1150
Wire Wire Line
	6100 1150 10950 1150
Wire Wire Line
	8200 4400 8200 1550
Connection ~ 8200 1550
Wire Wire Line
	8200 1550 10950 1550
Wire Wire Line
	8100 4500 8100 1650
Connection ~ 8100 1650
Wire Wire Line
	8100 1650 10950 1650
Wire Wire Line
	8000 4600 8000 1750
Connection ~ 8000 1750
Wire Wire Line
	8000 1750 10950 1750
Wire Wire Line
	7900 4700 7900 1050
Connection ~ 7900 1050
Wire Wire Line
	7900 1050 10950 1050
Wire Wire Line
	8700 5200 8600 5200
Wire Wire Line
	8600 5200 8600 6100
Wire Wire Line
	8600 6100 6400 6100
Wire Wire Line
	6500 5200 6400 5200
Wire Wire Line
	6400 5200 6400 6100
Connection ~ 6400 6100
Wire Wire Line
	6400 6100 4200 6100
Wire Wire Line
	4300 5200 4200 5200
Wire Wire Line
	4200 5200 4200 6100
Connection ~ 4200 6100
Wire Wire Line
	4200 6100 2700 6100
Wire Wire Line
	8700 5100 8500 5100
Wire Wire Line
	8500 5100 8500 6000
Wire Wire Line
	8500 6000 6300 6000
Wire Wire Line
	8700 4900 8300 4900
Wire Wire Line
	8300 4900 8300 5900
Wire Wire Line
	8300 5900 6100 5900
Wire Wire Line
	6500 5100 6300 5100
Wire Wire Line
	6300 5100 6300 6000
Connection ~ 6300 6000
Wire Wire Line
	6300 6000 4100 6000
Wire Wire Line
	4300 5100 4100 5100
Wire Wire Line
	4100 5100 4100 6000
Connection ~ 4100 6000
Wire Wire Line
	4100 6000 2700 6000
Wire Wire Line
	4300 4900 3900 4900
Wire Wire Line
	3900 4900 3900 5900
Connection ~ 3900 5900
Wire Wire Line
	3900 5900 2700 5900
Wire Wire Line
	6500 4900 6100 4900
Wire Wire Line
	6100 4900 6100 5900
Connection ~ 6100 5900
Wire Wire Line
	6100 5900 3900 5900
Wire Wire Line
	9700 3900 9800 3900
Wire Wire Line
	9800 3900 9800 6200
Wire Wire Line
	9800 6200 2700 6200
Wire Wire Line
	4300 3900 2700 3900
Text HLabel 2700 3900 0    50   Input ~ 0
SR_DI
Text HLabel 2700 5900 0    50   Input ~ 0
~SR_PL
Text HLabel 2700 6000 0    50   Input ~ 0
SR_CP
Text HLabel 2700 6100 0    50   Input ~ 0
~SR_CE
Text HLabel 2700 6200 0    50   Input ~ 0
SR_DO
$Comp
L power:+5V #PWR?
U 1 1 5DC32B5B
P 9200 3600
F 0 "#PWR?" H 9200 3450 50  0001 C CNN
F 1 "+5V" H 9215 3773 50  0000 C CNN
F 2 "" H 9200 3600 50  0001 C CNN
F 3 "" H 9200 3600 50  0001 C CNN
	1    9200 3600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5DC335F4
P 7000 3600
F 0 "#PWR?" H 7000 3450 50  0001 C CNN
F 1 "+5V" H 7015 3773 50  0000 C CNN
F 2 "" H 7000 3600 50  0001 C CNN
F 3 "" H 7000 3600 50  0001 C CNN
	1    7000 3600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5DC339DE
P 4800 3600
F 0 "#PWR?" H 4800 3450 50  0001 C CNN
F 1 "+5V" H 4815 3773 50  0000 C CNN
F 2 "" H 4800 3600 50  0001 C CNN
F 3 "" H 4800 3600 50  0001 C CNN
	1    4800 3600
	1    0    0    -1  
$EndComp
$EndSCHEMATC