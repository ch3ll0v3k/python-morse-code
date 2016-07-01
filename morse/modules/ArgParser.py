#!/usr/bin/python
import sys, time
from optparse import OptionParser 


# #############################################################################################
class ArgParser(object):

    # ==========================================================================
    def __init__( self, _version ):

        # --------------------------------------------------------------
        self._USAGE = " %prog -t <text> -r [44100] -f [440] -s [200] -g [1] -l [false]"

        self.PARSER = OptionParser( 
            usage=self._USAGE, version="%prog "+_version, description="Description:"+
            "Simple python script to send morse code"
        );

        self.PARSER.set_defaults( verbose=True );

        self.PARSER.add_option( '-t', '--text', action="store", 
            type="string", metavar="SOS", dest="text", default="sos", 
            help="Text data to send default:[SOS]"
        );

        self.PARSER.add_option( '-r', '--sample-rate', action="store", 
            type="int", metavar="44100", dest="rate", default="44100", 
            help=" Sample rate default:[44100]"
        );

        self.PARSER.add_option( '-f', '--freq', action="store", 
            type="int", metavar="440", dest="freq", default="440", 
            help=" Freq in Hertz default:[440]"
        );

        self.PARSER.add_option( '-s', '--speed', action="store", 
            type="int", metavar="200", dest="speed", default="200", 
            help="Transmission speed in Milli-Seconds fr one [DOT] default:[200] "
        );

        self.PARSER.add_option( '-g', '--gain', action="store", 
            type="int", metavar="1", dest="gain", default="1", 
            help=" Gain default:[1]"
        );

        self.PARSER.add_option( '-l', '--loop', action="store_true", 
            dest="loop", default=False, 
            help=" Loop default:[False]"
        );

        self.OPTS, self.ARGS = self.PARSER.parse_args();
        # --------------------------------------------------------------
        # print(self.OPTS);
        # {'min_sdk': 15, 'target_sdk': 19, 'verbose': True, 'package': 'org.ch3ll0v3k', 'compile': False, 'name': 'TestApp'}

        # --------------------------------------------------------------

    # ==========================================================================
    def PRINT_HELP(self):

        # --------------------------------------------------------------
        print("---------------------------------------------------");
        self.PARSER.print_help();
        # --------------------------------------------------------------

    # ==========================================================================

# #############################################################################################
