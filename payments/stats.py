import config

class Stats:
    """
    A class to handle all the stats.
    """
    
    def __init__(self):
        self.__money_made = 0
        self.__total_likes = 0
        self.__total_purchase = 0
        
    def add_money(self, data_dict):
        price = data_dict[config.PRICE_FIELD]
        purchases = data_dict[config.PURCHASES_FIELD]
        self.__money_made += price * purchases    
    
    def get_money_made(self):
        return self.__money_made