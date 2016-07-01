#!/usr/bin/python
# ------------------------------------------------------------------------
from threading import Thread;
import time
import alsaaudio

# ------------------------------------------------------------------------
rate = 44100
pcm = alsaaudio.PCM(type=alsaaudio.PCM_PLAYBACK)
pcm.setchannels(1)
pcm.setrate(rate)
pcm.setformat(alsaaudio.PCM_FORMAT_S32_LE)

def Beep_alsa(frequency, duration=1000, amplitude=1, _TP=alsaaudio.PCM_FORMAT_S32_LE):
    
    global rate, pcm

    """
    rate = 44100
    pcm = alsaaudio.PCM(type=alsaaudio.PCM_PLAYBACK)
    pcm.setchannels(1)
    pcm.setrate(rate)
    pcm.setformat(_TP)
    """
    #print(chr(0));
    #print(chr(amplitude));

    half_period = int(rate/frequency/2)
    beep = (chr(0)+chr(amplitude))*half_period+(chr(0)*2)*half_period
    #print "L",len(beep), beep
    beep *= int(duration*rate/half_period/2000)
    #print "duration", beep

    pcm.setperiodsize(160)
    for idx in xrange(0,len(beep),320):
        frm = beep[idx:idx+320]
        if len(frm) == 320:
            pcm.write(frm) 



# ------------------------------------------------------------------------
if __name__ == '__main__':

    """    
    freq = 1;

    for TM in xrange(0, 20000):
        Beep_alsa(frequency=freq, duration=250, amplitude=1, _TP=alsaaudio.PCM_FORMAT_S32_LE);
        print("Current freq: "+str(freq));
        freq += 100;
    """


    FREQS_ARR = [100,200,300,600,200,100,800,500,600,700,300,200,900,250];
    AMPS_ARR = [1,2,3,4,5,6,7,8,9,25,50,100,150,200,225,250];

    for FREQ in FREQS_ARR:
        for AMP in AMPS_ARR:

            Beep_alsa(frequency=FREQ, duration=250, amplitude=1, _TP="NO-FORMAT");
            print(str(AMP)+" : "+str(FREQ));



    PCM_FORMATS = [

            alsaaudio.PCM_FORMAT_S8,
            alsaaudio.PCM_FORMAT_U8,
            alsaaudio.PCM_FORMAT_S16_LE,
            alsaaudio.PCM_FORMAT_S16_BE,
            alsaaudio.PCM_FORMAT_U16_LE,
            alsaaudio.PCM_FORMAT_U16_BE,
            alsaaudio.PCM_FORMAT_S24_LE,
            alsaaudio.PCM_FORMAT_S24_BE,
            alsaaudio.PCM_FORMAT_U24_LE,
            alsaaudio.PCM_FORMAT_U24_BE,
            alsaaudio.PCM_FORMAT_S32_LE,
            alsaaudio.PCM_FORMAT_S32_BE,
            alsaaudio.PCM_FORMAT_U32_LE,
            alsaaudio.PCM_FORMAT_U32_BE,
            alsaaudio.PCM_FORMAT_FLOAT_LE,
            alsaaudio.PCM_FORMAT_FLOAT_BE,
            alsaaudio.PCM_FORMAT_FLOAT64_LE,
            alsaaudio.PCM_FORMAT_FLOAT64_BE,
            alsaaudio.PCM_FORMAT_MU_LAW,
            alsaaudio.PCM_FORMAT_A_LAW,
            alsaaudio.PCM_FORMAT_IMA_ADPCM,
            alsaaudio.PCM_FORMAT_MPEG,
            alsaaudio.PCM_FORMAT_GSM
            ]

    for FREQ in FREQS_ARR:

        for AMP in AMPS_ARR:
            for PCM_FORMAT in PCM_FORMATS:

                Beep_alsa(frequency=FREQ, duration=250, amplitude=1, _TP=PCM_FORMAT);
                print(str(PCM_FORMAT)+" : "+str(AMP)+" : "+str(FREQ));


"""

PCM_FORMAT_S8               Signed 8 bit samples for each channel
PCM_FORMAT_U8               Signed 8 bit samples for each channel
PCM_FORMAT_S16_LE           Signed 16 bit samples for each channel Little Endian byte order)
PCM_FORMAT_S16_BE           Signed 16 bit samples for each channel (Big Endian byte order)
PCM_FORMAT_U16_LE           Unsigned 16 bit samples for each channel (Little Endian byte order)
PCM_FORMAT_U16_BE           Unsigned 16 bit samples for each channel (Big Endian byte order)
PCM_FORMAT_S24_LE           Signed 24 bit samples for each channel (Little Endian byte order)
PCM_FORMAT_S24_BE           Signed 24 bit samples for each channel (Big Endian byte order)}
PCM_FORMAT_U24_LE           Unsigned 24 bit samples for each channel (Little Endian byte order)
PCM_FORMAT_U24_BE           Unsigned 24 bit samples for each channel (Big Endian byte order)
PCM_FORMAT_S32_LE           Signed 32 bit samples for each channel (Little Endian byte order)
PCM_FORMAT_S32_BE           Signed 32 bit samples for each channel (Big Endian byte order)
PCM_FORMAT_U32_LE           Unsigned 32 bit samples for each channel (Little Endian byte order)
PCM_FORMAT_U32_BE           Unsigned 32 bit samples for each channel (Big Endian byte order)
PCM_FORMAT_FLOAT_LE         32 bit samples encoded as float (Little Endian byte order)
PCM_FORMAT_FLOAT_BE         32 bit samples encoded as float (Big Endian byte order)
PCM_FORMAT_FLOAT64_LE       64 bit samples encoded as float (Little Endian byte order)
PCM_FORMAT_FLOAT64_BE       64 bit samples encoded as float (Big Endian byte order)
PCM_FORMAT_MU_LAW           A logarithmic encoding (used by Sun .au files and telephony)
PCM_FORMAT_A_LAW            Another logarithmic encoding
PCM_FORMAT_IMA_ADPCM        A 4:1 compressed format defined by the Interactive Multimedia Association.
PCM_FORMAT_MPEG             MPEG encoded audio?
PCM_FORMAT_GSM              9600 bits/s constant rate encoding for speech






"""




