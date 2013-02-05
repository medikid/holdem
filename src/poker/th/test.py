'''
Created on Feb 1, 2013

@author: chinnu
'''
from sikuli.Sikuli import *
from os import path
from PlayNowApp import PlayNowApp
from PokerTable import PokerTable
from card import Card


#t = PokerTable()
#t.highlight_regions_all()


#from javax.swing import JFrame, JButton, JLabel
#
#frame = JFrame("My First Swing Gui", size=(800, 600))
#
#button = JButton("Clicke Me")
#frame.add(button)
#
#
#frame.visible = True

c=Card('a','s')
print(str(c.__hash__))