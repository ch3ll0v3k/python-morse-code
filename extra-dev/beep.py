#!/usr/bin/python
# ------------------------------------------------------------------------
from threading import Thread;
import time

# ------------------------------------------------------------------------
def Beep_dev_au(frequency, duration, amplitude=10):

    sample = 8000
    half_period = int(sample/frequency/2)
    beep = chr(amplitude)*half_period+chr(0)*half_period
    beep *= int(duration*frequency/1000)
    audio = file('/dev/audio', 'wb')
    audio.write(beep)
    time.sleep(2);
    audio.close()



# ------------------------------------------------------------------------
if __name__ == '__main__':
    
    Beep_dev_au(3000, 3, 10);



