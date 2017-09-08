import os

##############################################################################
# Generic Definitions
##############################################################################
PORJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = 'payment_backend.log'
OUTPUT_HEADER = ["id"]

##############################################################################
# Data Info
##############################################################################

# Input
DIR_DATA_INPUT = "input"  # This directory is the relative path of the data. You 
                # can specify a folder here or use '.' for root.
FILE_DATA = "videos.csv"  # data/videos file 
FILE_EXCHANGE = "exchange_rates.csv"  # exchange rates file

# Output
DIR_DATA_OUTPUT = "output"  # This directory is the relative path of the data. You 
                # can specify a folder here or use '.' for root.
FILE_VALID = "valid.csv"
FILE_INVALID = "invalid.csv"


##############################################################################
# Videos file
##############################################################################
PRICE_FIELD = "unit_price_in_usd"
PURCHASES_FIELD = "total_purchases"
FIELD_TYPES = {PRICE_FIELD:float, "id":int, 
               "total_likes":int, PURCHASES_FIELD:int}
