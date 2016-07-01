#### Simple python script to send morse code

```
./sendMorseCode --help

Usage:  sendMorseCode -t <text> -r [44100] -f [440] -s [200] -g [1] -l [false]

Description:Simple python script to send morse code

Options:
    --version                       show program's version number and exit
    -h,       --help                show this help message and exit
    -t SOS,   --text=SOS            Text data to send default:[SOS]
    -r 44100, --sample-rate=44100   Sample rate default:[44100]
    -f 440,   --freq=440            Freq in Hertz default:[440]
    -s 200,   --speed=200           Transmission speed in Milli-Seconds for one [DOT] default:[200]
    -g 1,     --gain=1              Gain default:[1]
    -l,       --loop                For repeat forever!
```


#### Example

##### Sending S.O.S. With location LAT:[cord] LON:[cord]
```
./sendMorseCode -t "sos lat 3 42423 lon 43 4434" -g 4 -s 130 --loop

```
