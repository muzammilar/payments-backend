import csv
import os
import traceback
import logging
# package
import config

class File:
    """
    A class to handle general files
    """
    
    def __init__(self):
        self.fhandle = None
        self.csvhandle = None
        self.header = None

    def open(self, f_name):
        pass
        
    def close(self):  # clear file handles.
        if self.fhandle is not None:
            self.fhandle.close()
        self.fhandle = None
        self.csvhandle = None
        self.header = None
        

class ReadFile(File):
    """
    A class to read files
    """
    
    def open(self, f_name):  # override, read specific file
        file_path  = os.path.join(config.PORJECT_ROOT, config.DIR_DATA_INPUT, f_name)
        logging.info("Openning file:" + file_path)
        try: 
            self.fhandle = open(file_path,'rb')
            self.csvhandle = csv.DictReader(self.fhandle)
            self.header = self.csvhandle.fieldnames
            if not self.header:
                raise EOFError("Empty File")
        except:
            logging.error("File Error: reading file")
            logging.exception("Exception")
            return False
        logging.info("Openning file success:" + file_path)
        return True
    

class WriteFile(File):
    """
    A class to write files
    """

    def open(self, f_name):  # override, write specific file
        file_path  = os.path.join(config.PORJECT_ROOT, config.DIR_DATA_OUTPUT, f_name)
        logging.info("Openning file:" + file_path)
        try: 
            self.fhandle = open(file_path,'wb')
            #self.csvhandle = csv.DictWriter(self.fhandle)
            #self.header = []
        except:
            logging.error("File Error: writing file creation.")
            logging.exception("Exception")
            return False
        logging.info("Openning file success:" + file_path)
        return True
        
    def writeheader(self, header):
        self.header = header
        self.csvhandle = csv.DictWriter(self.fhandle, fieldnames=header)
        self.csvhandle.writeheader()
        
    def writerow(self, dict_obj):
        self.csvhandle.writerow({k:dict_obj[k] for k in self.header})