import traceback
import logging
#package 
import exchange
import functions
import config

class Rules:
    """
    A meta-class to handle all rules.
    """
    # everything here will be a class variable. 
    # doesn't make sense to create things.
    # I only used class method since the program asked me to.

    rules = []  # rules is a list of list where 
                # [[rule1 OR rule2 OR ...] AND [rule3 OR rule4] AND ...]
    
    @classmethod
    def initiate_rules(cls):
        # define all the rules here        
        cls.rules.append([Rule("title", len, functions.lt, 30)])
        cls.rules.append([Rule("total_likes", None, functions.gt, 10)])
        cls.rules.append([Rule("total_purchases", None, functions.gt, 200)])
        cls.rules.append([
                Rule("EUR", None, functions.lt, 20),
                Rule("CAD", None, functions.lt, 25),            
            ]
        )        
        # sort the rules in reverse importance order
        #rules.sort(key=lambda x:x.precedence, reverse=True)
        
    @classmethod
    def apply(cls, obj):
        # use this function to check the rules
        try:
            for rule_set in cls.rules:
                if not cls.check_rule_set(rule_set, obj):
                    return False
            return True
        except:
            traceback.print_exc()
            print "Failed to check field. Invalidating."
            return False
            
    @staticmethod
    def check_rule_set(rule_set, obj):
        for rule in rule_set:
            if rule.applies(obj):
                return True
        return False
    

class Rule:
    """
    Once a rule is defined it can be modified so only 1 private variable
    A class to handle all the functionalities of a single rule
    file_name: specifies the output file for the rule if we ever specify precedence 
        In the future there can be multiple file names instead of valid/invalid
        It can be used to sub categorize valid files.
    field_name: specifies the field name that we have to compare.
        the country currencies are specified by their three letter code.
        They should be uppercase. Other names are from the field in videos.csv
    pre_proc_operation: specifies any operation on the field to be perform,
        e.g. len to find the length of the field.
    rule: speficies the operation, eg. gt, lt, eq, ge, le. These operations are
        specified in the functions file.
    value: the value you have to compare the rule with
    rule_name: if you want to name a specified rule.
    """

    def __init__(self, field_name, pre_proc_operation, rule, value, 
                file_name="", importance=0, rule_name=""):
        self.field_name = field_name
        self.pre_proc_operation = pre_proc_operation
        self.rule = rule
        self.value = value
        self.file_name = file_name
        self.precedence = importance 
        self.__currency_rule = False   #python verson of private variable
        self.rule_name = rule_name
        if self.field_name in exchange.rates:
            self.__currency_rule = True        
            

    def __str__(self):  #maybe redefine this function use rule_name
        return self.field_name + ", " + str(value)

            
    def applies(self, obj):
        # checks if a single rule applies or not
        compare_field = self.field_name

        if self.pre_proc_operation is not None:  # eg. find the length
            field_value = self.pre_proc_operation(obj[compare_field])
        elif self.__currency_rule: 
            field_value = obj[config.PRICE_FIELD] * exchange.rates[compare_field]
        else:
            field_value = obj[compare_field]
    
        return self.rule(field_value, self.value)
        