import sys
import traceback
import logging
# package
import config
from rules import Rules
import exchange
from fhandler import ReadFile
from fhandler import WriteFile
from stats import Stats

def main():

    # read exchange rates file
    logging.info("Reading Exchange Rates.")
    if not exchange.load_rates():
        logging.error("Couldn't read the exchange_rates.csv")
        sys.exit(1)
    logging.info("Exchange Rates Read.")

    # read the rules file
    logging.info("Reading Rules.")
    try:
        Rules.initiate_rules()
    except:
        logging.error("Couldn't read the rules")
        sys.exit(1)
    logging.info("Rules Read.")
                
    read_file_video = load_videos_file()
        
    # open write files
    write_file_valid =  open_write_file(config.FILE_VALID, 
                                        read_file_video.header)
    write_file_invalid =  open_write_file(config.FILE_INVALID,
                                        read_file_video.header)

    statistics = Stats()
    # load the file, parse and assign a file.
    for video_dict in read_file_video.csvhandle:
        logging.info("Parsing Object:" + str(video_dict))
        try:
            change_field_data_types(video_dict)
            if Rules.apply(video_dict):
                write_file_valid.writerow(video_dict)
                statistics.add_money(video_dict)
            else:
                write_file_invalid.writerow(video_dict)
        except:
            logging.warning("Problem reading row from input")
            logging.exception("Exception")
    print "Total Money made (in USD):", statistics.get_money_made()
    

def open_write_file(f_name, header):
    write_file = WriteFile()
    success = write_file.open(f_name)
    if not success:
        print "Total Money made (in USD):", 0
        sys.exit(1)
    #write_file.writeheader(header)
    write_file.writeheader(config.OUTPUT_HEADER)
    return write_file                

    
def load_videos_file():
    read_file = ReadFile()
    success = read_file.open(config.FILE_DATA)
    if not success:
        print "Total Money made (in USD):", 0
        sys.exit(1)
    return read_file
    
    
def change_field_data_types(video_dict):
    for k in config.FIELD_TYPES:
        video_dict[k] = config.FIELD_TYPES[k](video_dict[k])  # int(video_dict[k]) or float