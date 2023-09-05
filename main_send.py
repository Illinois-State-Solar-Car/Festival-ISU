import board
import busio
import digitalio
from analogio import AnalogIn
import time
import struct
from adafruit_mcp2515       import MCP2515 as CAN
from adafruit_mcp2515.canio import RemoteTransmissionRequest, Message, Match, Timer
import time






# Initalize the SPI bus on the RP2040
# NOTE: Theses pins constant for all CAN-Pico Boards... DO NOT TOUCH
cs = digitalio.DigitalInOut(board.GP9)
cs.switch_to_output()
spi = busio.SPI(board.GP2, board.GP3, board.GP4)


mcp = CAN(spi, cs, baudrate = 500000, crystal_freq = 16000000, silent = False)


string = "Tits....or Ass? "



out = [(string[i:i+8]) for i in range(0, len(string), 8)]



data=struct.pack('<8s',out[0])

print(out[0])

data2=struct.pack('<8s',out[1])
print(out[1])


while True:
    
    
    
    message = Message(id=0x402, data=data, extended=False)
    send_success = mcp.send(message)
    print(send_success)
    time.sleep(1)
    
    
    message = Message(id=0x403, data=data2, extended=False)
    send_success = mcp.send(message)
    print(send_success)
    time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    

        






              

            
            
                        
                
          
            
            
                        
                    
                
            
           
            
    
        
               

                    
            
    
