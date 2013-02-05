'''
Created on 2013-02-03

@author: chinnu
'''
from os import path
from sikuli.Sikuli import *
from re import *

class Card:
    SUITE_TO_SUITERANK = {
        "s" : 1,
        "h" : 2,
        "d" : 3,
        "c" : 4
    }
    
    NUM_TO_CARDRANK = {
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10": 10,
        "J" : 11,
        "Q" : 12,
        "K" : 13,
        "A" : 14
    }
    
    SUITERANK_TO_SUITE = dict([(v, k) for k, v in SUITE_TO_SUITERANK.iteritems()])
    CARDRANK_TO_NUM = dict([(v, k) for k, v in NUM_TO_CARDRANK.iteritems()])
    
    REPR_RE = compile(r'\((.*?)\)')
    
    def __init__(self, num, suite):
        self.num = str(num).upper()
        self.suite = str(suite).lower()
        self.setCardRank()
        self.setSuiteRank()
        self.setCardImage()
    
    def __repr__(self):
        return str(self.num).upper() + str(self.suite).lower()
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.cardRank == other.cardRank and self.suiteRank == other.suiteRank)
    
    def __hash__(self):
        return hash((self.cardRank, self.suiteRank))
    
    def setCardRank(self):
        self.cardRank = Card.NUM_TO_CARDRANK[self.num]
    
    def setSuiteRank(self):        
        self.suiteRank = Card.SUITE_TO_SUITERANK[self.suite]
    
    def setCardImage(self):
        folder_path = path.dirname(path.realpath(__file__))
        image_path = folder_path + '\\images' + '\\cards' + '\\gifs'
        self.cardImage = image_path + '\\' + str(self.num).lower() + str(self.suite).lower() + '.png'

#c = Card('j', 's')
#print("Card is "+ c.value +" and rank is "+ str(c.cardRank) +" and image is "+ c.cardImage )