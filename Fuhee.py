import wiringpi as pi
import time
import subprocess
from subprocess import Popen
import socket
import sys
from sc1602 import sc1602

RS = 23
E  = 24
D4 = 22
D5 = 27
D6 = 17
D7 = 4
SPI_CH = 0
READ_CH = 0
state = 0

pi.wiringPiSetupGpio()
pi.wiringPiSPISetup(SPI_CH, 1000000 )
lcd = sc1602( RS, E, D4, D5, D6, D7 )
lcd.set_cursol( 0 )
lcd.set_blink( 0 )
lcd.clear( )
lcd.move_home( )
lcd.lcd_byte( 0x40, 0 )
lcd.lcd_byte( 0x00, 1 )
lcd.lcd_byte( 0x41, 0 )
lcd.lcd_byte( 0x1F, 1 )
lcd.lcd_byte( 0x42, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x43, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x44, 0 )
lcd.lcd_byte( 0x16, 1 )
lcd.lcd_byte( 0x45, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x46, 0 )
lcd.lcd_byte( 0x12, 1 )
lcd.lcd_byte( 0x47, 0 )
lcd.lcd_byte( 0x10, 1 )

lcd.lcd_byte( 0x48, 0 )
lcd.lcd_byte( 0x00, 1 )
lcd.lcd_byte( 0x49, 0 )
lcd.lcd_byte( 0x1F, 1 )
lcd.lcd_byte( 0x4A, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x4B, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x4C, 0 )
lcd.lcd_byte( 0x0D, 1 )
lcd.lcd_byte( 0x4D, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x4E, 0 )
lcd.lcd_byte( 0x09, 1 )
lcd.lcd_byte( 0x4F, 0 )
lcd.lcd_byte( 0x01, 1 )

lcd.lcd_byte( 0x50, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x51, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x52, 0 )
lcd.lcd_byte( 0x13, 1 )
lcd.lcd_byte( 0x53, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x54, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x55, 0 )
lcd.lcd_byte( 0x10, 1 )
lcd.lcd_byte( 0x56, 0 )
lcd.lcd_byte( 0x1F, 1 )
lcd.lcd_byte( 0x57, 0 )
lcd.lcd_byte( 0x00, 1 )

lcd.lcd_byte( 0x58, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x59, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x5A, 0 )
lcd.lcd_byte( 0x19, 1 )
lcd.lcd_byte( 0x5B, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x5C, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x5D, 0 )
lcd.lcd_byte( 0x01, 1 )
lcd.lcd_byte( 0x5E, 0 )
lcd.lcd_byte( 0x1F, 1 )
lcd.lcd_byte( 0x5F, 0 )
lcd.lcd_byte( 0x00, 1 )

lcd.clear( )
lcd.move(7, 0x00 )
lcd.lcd_byte( 0x00, 1 )
lcd.lcd_byte( 0x01, 1 )
lcd.move(7, 0x01 )
lcd.lcd_byte( 0x02, 1 )
lcd.lcd_byte( 0x03, 1 )


while True:
    buffer = 0x6800 |  (0x1800 * READ_CH ) 
    buffer = buffer.to_bytes( 2, byteorder='big' )

    pi.wiringPiSPIDataRW( SPI_CH, buffer )
    value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff

    if (value > 500) and (state == 1):
        print ("Bright")
        lcd.lcd_byte( 0x40, 0 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x41, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x42, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x43, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x44, 0 )
        lcd.lcd_byte( 0x16, 1 )
        lcd.lcd_byte( 0x45, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x46, 0 )
        lcd.lcd_byte( 0x12, 1 )
        lcd.lcd_byte( 0x47, 0 )
        lcd.lcd_byte( 0x10, 1 )
        
        lcd.lcd_byte( 0x48, 0 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x49, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x4A, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x4B, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x4C, 0 )
        lcd.lcd_byte( 0x0D, 1 )
        lcd.lcd_byte( 0x4D, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x4E, 0 )
        lcd.lcd_byte( 0x09, 1 )
        lcd.lcd_byte( 0x4F, 0 )
        lcd.lcd_byte( 0x01, 1 )
        
        lcd.lcd_byte( 0x50, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x51, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x52, 0 )
        lcd.lcd_byte( 0x13, 1 )
        lcd.lcd_byte( 0x53, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x54, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x55, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x56, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x57, 0 )
        lcd.lcd_byte( 0x00, 1 )
        
        lcd.lcd_byte( 0x58, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x59, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x5A, 0 )
        lcd.lcd_byte( 0x19, 1 )
        lcd.lcd_byte( 0x5B, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x5C, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x5D, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x5E, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x5F, 0 )
        lcd.lcd_byte( 0x00, 1 )
        
        lcd.clear( )
        lcd.move(7, 0x00 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.move(7, 0x01 )
        lcd.lcd_byte( 0x02, 1 )
        lcd.lcd_byte( 0x03, 1 )
        
        state = 0
    elif(value < 500):
        print ("Dark")
        lcd.lcd_byte( 0x40, 0 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x41, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x42, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x43, 0 )
        lcd.lcd_byte( 0x14, 1 )
        lcd.lcd_byte( 0x44, 0 )
        lcd.lcd_byte( 0x12, 1 )
        lcd.lcd_byte( 0x45, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x46, 0 )
        lcd.lcd_byte( 0x12, 1 )
        lcd.lcd_byte( 0x47, 0 )
        lcd.lcd_byte( 0x12, 1 )
        
        lcd.lcd_byte( 0x48, 0 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x49, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x4A, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x4B, 0 )
        lcd.lcd_byte( 0x05, 1 )
        lcd.lcd_byte( 0x4C, 0 )
        lcd.lcd_byte( 0x09, 1 )
        lcd.lcd_byte( 0x4D, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x4E, 0 )
        lcd.lcd_byte( 0x09, 1 )
        lcd.lcd_byte( 0x4F, 0 )
        lcd.lcd_byte( 0x09, 1 )
        
        lcd.lcd_byte( 0x50, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x51, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x52, 0 )
        lcd.lcd_byte( 0x12, 1 )
        lcd.lcd_byte( 0x53, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x54, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x55, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x56, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x57, 0 )
        lcd.lcd_byte( 0x00, 1 )
        
        lcd.lcd_byte( 0x58, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x59, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x5A, 0 )
        lcd.lcd_byte( 0x09, 1 )
        lcd.lcd_byte( 0x5B, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x5C, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x5D, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x5E, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x5F, 0 )
        lcd.lcd_byte( 0x00, 1 )
        
        lcd.lcd_byte( 0x60, 0 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x61, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x62, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x63, 0 )
        lcd.lcd_byte( 0x14, 1 )
        lcd.lcd_byte( 0x64, 0 )
        lcd.lcd_byte( 0x12, 1 )
        lcd.lcd_byte( 0x65, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x66, 0 )
        lcd.lcd_byte( 0x12, 1 )
        lcd.lcd_byte( 0x67, 0 )
        lcd.lcd_byte( 0x12, 1 )
        
        lcd.lcd_byte( 0x68, 0 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x69, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x6A, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x6B, 0 )
        lcd.lcd_byte( 0x05, 1 )
        lcd.lcd_byte( 0x6C, 0 )
        lcd.lcd_byte( 0x09, 1 )
        lcd.lcd_byte( 0x6D, 0 )
        lcd.lcd_byte( 0x11, 1 )
        lcd.lcd_byte( 0x6E, 0 )
        lcd.lcd_byte( 0x09, 1 )
        lcd.lcd_byte( 0x6F, 0 )
        lcd.lcd_byte( 0x09, 1 )
        
        lcd.lcd_byte( 0x70, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x71, 0 )
        lcd.lcd_byte( 0x17, 1 )
        lcd.lcd_byte( 0x72, 0 )
        lcd.lcd_byte( 0x14, 1 )
        lcd.lcd_byte( 0x73, 0 )
        lcd.lcd_byte( 0x17, 1 )
        lcd.lcd_byte( 0x74, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x75, 0 )
        lcd.lcd_byte( 0x10, 1 )
        lcd.lcd_byte( 0x76, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x77, 0 )
        lcd.lcd_byte( 0x00, 1 )
        
        lcd.lcd_byte( 0x78, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x79, 0 )
        lcd.lcd_byte( 0x1D, 1 )
        lcd.lcd_byte( 0x7A, 0 )
        lcd.lcd_byte( 0x05, 1 )
        lcd.lcd_byte( 0x7B, 0 )
        lcd.lcd_byte( 0x1D, 1 )
        lcd.lcd_byte( 0x7C, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x7D, 0 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.lcd_byte( 0x7E, 0 )
        lcd.lcd_byte( 0x1F, 1 )
        lcd.lcd_byte( 0x7F, 0 )
        lcd.lcd_byte( 0x00, 1 )
        
        lcd.lcd_byte( 0x80, 0 )
        
        cmd = "aplay fuhee.wav"
        proc = Popen( cmd .strip().split(" ") )
        lcd.clear( )
        lcd.move(7, 0x00 )
        lcd.lcd_byte( 0x00, 1 )
        lcd.lcd_byte( 0x01, 1 )
        lcd.move(7, 0x01 )
        lcd.lcd_byte( 0x02, 1 )
        lcd.lcd_byte( 0x03, 1 )
        time.sleep(0.1)
        lcd.clear( )
        lcd.move(7, 0x00 )
        lcd.lcd_byte( 0x04, 1 )
        lcd.lcd_byte( 0x05, 1 )
        lcd.move(7, 0x01 )
        lcd.lcd_byte( 0x06, 1 )
        lcd.lcd_byte( 0x07, 1 )
        time.sleep(0.3)
        state = 1

    time.sleep(0.4)
