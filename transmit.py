import time
import sys
import RPi.GPIO as GPIO

a1_on  =  '1110101011101010101010001'
a1_off =  '1110101011101010101010111'

b1_on =  '1011101011101010101010001'#freezer
b1_off = '1011101011101010101010111'
b2_on =  '1011101010111010101010001'
b2_off = '1011101010111010101010111'
b3_on =  '1011101010101110101010001'#pompa air
b3_off = '1011101010101110101010111'

c1_on =  '1010111011101010101010001'#pompa hidroponik
c1_off = '1010111011101010101010111'
c2_on =  '1010111010111010101010001'
c2_off = '1010111010111010101010111'
c3_on =  '1010111010101110101010001'#lampu atas
c3_off = '1010111010101110101010111'

d3_on =  '1010101110101110101010001'
d3_off = '1010101110101110101010111'

one_delay = 0.0005
short_delay = 0.0008
long_delay = 0.0011
zero_delay = 0.0002
extended_delay = 0.01

NUM_ATTEMPTS = 50
TRANSMIT_PIN = 21

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
          #      print "1",
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(one_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            elif i == '0':
         #       print "0",
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(zero_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        #print "#"
        time.sleep(extended_delay)
    GPIO.cleanup()


if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')

