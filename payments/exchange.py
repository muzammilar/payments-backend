import os
import traceback
import logging
# package
import config
from fhandler import ReadFile

def load_rates():
    logging.info("Loading rates.")
    global rates  # it's going to be a constant once it's loaded.
    rates = {}
    read_file = ReadFile()
    success = read_file.open(config.FILE_EXCHANGE)
    if not success:
        print "Total Money made (in USD):", 0
        return success
        
    # load the rates
    for rate_dict in read_file.csvhandle:
        logging.info("Reading rate:" + str(rate_dict))
        try:
            rates[rate_dict[read_file.header[0]]] = float(rate_dict[read_file.header[1]])
        except:
            logging.warning("File Error: Reading rate.")
            logging.exception("Exception") 
            success = False
    read_file.close()
    return success