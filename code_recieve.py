import board
import busio
import digitalio
from analogio import AnalogIn
import time
import struct
from adafruit_mcp2515       import MCP2515 as CAN
from adafruit_mcp2515.canio import RemoteTransmissionRequest, Message, Match, Timer
import time
import lcd
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.


# Modify this if you have a different sized Character LCD
lcd_columns = 20
lcd_rows = 4

cs = digitalio.DigitalInOut(board.GP9)
cs.switch_to_output()
spi = busio.SPI(board.GP2, board.GP3, board.GP4)


mcp = CAN(spi, cs, baudrate = 500000, crystal_freq = 16000000, silent = False)



# Initialise I2C bus.
i2c = busio.I2C(board.GP7, board.GP6) # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Initialise the lcd class
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=4, num_cols=20)

first = False
while True:
    
    with mcp.listen(matches = [Match(0x400,mask = 0xF00)], timeout=0) as listener:
       
       
       
       
        message_count = listener.in_waiting()

       
        if message_count == 0:
           continue

        next_message = listener.receive()
        message_num = 0
        while not next_message is None:
            message_num += 1

             # Check the id to properly unpack it
            if next_message.id == 0x402:

            #unpack and print the message
                holder = struct.unpack('<8s',next_message.data)
                print(holder)
                lcd.print(holder[0].decode())
                first = True
                time.sleep(1)
                

            if next_message.id == 0x403 and first == True:

                #unpack and print the message
                holder = struct.unpack('<8s',next_message.data)
                print(holder)
                lcd.print(holder[0].decode())
                first = False
                time.sleep(1)
                lcd.clear()
                time.sleep(1)
                
                
               
            next_message = listener.receive()
          
    
