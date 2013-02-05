'''
Created on 2013-02-03

@author: chinnu
'''
from card import Card
from hand import Hand
from lookupTables import LookupTables

class Evaluator:
        EvaluatorPercentile = 0
        
        def evaluate_percentile(self, Hand):
            hand = Hand.pocket
            """
            Using lookup table, return percentile of your hand with two cards
            """
            if len(hand) != 2:
                raise self.HandLengthException("Only 2-card hands are supported by the Two evaluator")
            
            if hand[0].suiteRank == hand[1].suiteRank:
                if hand[0].cardRank < hand[1].cardRank:
                    self.EvaluatorPercentile = LookupTables.Two.suited_ranks_to_percentile[hand[0].cardRank][hand[1].cardRank]
                else:
                    self.EvaluatorPercentile = LookupTables.Two.suited_ranks_to_percentile[hand[1].cardRank][hand[0].cardRank]
            else:
                self.EvaluatorPercentile = LookupTables.Two.unsuited_ranks_to_percentile[hand[0].cardRank][hand[1].cardRank]
            
#            self.evaluator_percentile = staticmethod(evaluate_percentile)

h= Hand('texasHoldem')
h.setPocket_th( Card(10, 's'), Card(5, 'd'))
h.setFlop_th(Card('Q', 's'), Card('K', 'h'), Card('5', 'c'))
h.setTurn_th(Card('8', 'd'))
h.setRiver_th(Card('k', 'c'))

#e = HandEvaluator.Two.evaluate_percentile(h.pocket)
e = Evaluator.evaluate_percentile(h)
print(str(h.EvaluatorPercentile))

