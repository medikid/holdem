'''
Created on 2013-02-03

@author: chinnu
'''
from card import Card
#from handEvaluator import HandEvaluator

class Hand():
    EvaluatorPercentile = 0
    
    def __init__(self, poker_type):
        if poker_type == 'texasHoldem':
            self.count=0
            self.confidence = 0
            self.pocket = []
            self.community = []
            self.pool = []
            
    
    def setPocketCard(self, card):
        self.pocket.append(card)
        self.pool.append(card)
        self.count += 1
    
    def setCommunityCard(self, card):
        self.community.append(card)
        self.pool.append(card)
        self.count += 1
    
    def setPocket_th(self, card1, card2):
        self.setPocketCard(card1)
        self.setPocketCard(card2)
    
    def setFlop_th(self, card1, card2, card3):
        self.setCommunityCard(card1)
        self.setCommunityCard(card2)
        self.setCommunityCard(card3)
    
    def setTurn_th(self, card4):
        self.setCommunityCard(card4)
    
    def setRiver_th(self, card5):
        self.setCommunityCard(card5)
    
    def getPool(self):
        self.pool = "" 
    
    def sortPool(self):
        self.poolSorted = sorted(self.pool, key=lambda card: card.cardRank, reverse=True)



#h= Hand('texasHoldem')
#h.setPocket_th( Card(10, 's'), Card(5, 'd'))
#h.setFlop_th(Card('Q', 's'), Card('K', 'h'), Card('5', 'c'))
#h.setTurn_th(Card('8', 'd'))
#h.setRiver_th(Card('k', 'c'))
#
##e = HandEvaluator.Two.evaluate_percentile(h.pocket)
#print(h.pocket[0])
