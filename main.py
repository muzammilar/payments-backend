#!/usr/bin/env python2

import sys
import argparse
import logging
import traceback

import payments
import config

def main(args, parser):
    loglevel = args.log
    try:
        numeric_level = getattr(logging, loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level.')        
    except:
        parser.print_help()
        sys.exit(1)

    logging.basicConfig(filename=args.logfile, level=numeric_level)
    payments.main()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default='INFO', help='INFO, WARNING, ERROR')
    parser.add_argument('--logfile', default=config.LOG_FILE)
    args = parser.parse_args()
    main(args, parser)
