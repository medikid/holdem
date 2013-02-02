'''
Created on Feb 1, 2013

@author: chinnu
'''
from sikuli.Sikuli import *
from PlayNowApp import PlayNowApp

class PokerTable(PlayNowApp):
    region_chair_1 = Region(1169, 38, 143, 322)
    region_chair_2 = Region(1300, 201, 279, 205)
    region_chair_3 = Region(1312, 395, 305, 234)
    region_chair_4 = Region(1230, 533, 215, 299)
    region_chair_5 = Region(1001, 553, 164, 297)
    region_chair_6 = Region(755, 572, 163, 280)
    region_chair_7 = Region(478, 541, 187, 292)
    region_chair_8 = Region(298, 431, 282, 198)
    region_chair_9 = Region(322, 207, 292, 196)
    region_chair_10 = Region(590,82,169,269)
    region_community_cards = Region(712,308,479,132)
    region_community_card_1 = Region(713,308,89,131)
    region_community_card_2 = Region(809,310,90,129)
    region_community_card_3 = Region(906,310,90,129)
    region_community_card_4 = Region(1003,310,90,128)
    region_community_card_5 = Region(1099,309,91,130)
    
    def __init__(self):
        PlayNowApp.__init__(self)
        self.table_id = ''
        self.table_title = ''
        self.capacity = ''
        
        
    def __del__(self):
        print("table is being destroyed")
        
    def find_empty_chairs(self):
            return
            
    def join_table(self):
       click(self.image("join-table-btn"))
       self.add_chips(200)
       
    def leave_table(self):
        self.open_table_menu(self)
        click(self.image("menu-leave-table-btn"))
        click(self.image("yes-btn"))
       
    def add_chips(self, chips_amount):
        click(self.image("menu-cashier-btn"))
        click(self.image("add-chips-btn"))
        click(self.image("ok-btn"))
    
    def open_table_menu(self):
        click(self.image("menu-open-btn"))
    
    def close_table_menu(self):
        click(self.image("menu-open-btn"))
    
    def select_table_menu(self, menu_selection):
            click(self.image(menu_selection))
                
    def highlight_regions_all(self):
        PokerTable.region_chair_1.highlight()
        PokerTable.region_chair_2.highlight()
        PokerTable.region_chair_3.highlight()
        PokerTable.region_chair_4.highlight()
        PokerTable.region_chair_5.highlight()
        PokerTable.region_chair_6.highlight()
        PokerTable.region_chair_7.highlight()
        PokerTable.region_chair_8.highlight()
        PokerTable.region_chair_9.highlight()
        PokerTable.region_chair_10.highlight()
        PokerTable.region_community_cards.highlight()
        PokerTable.region_community_card_1.highlight()
        PokerTable.region_community_card_2.highlight()
        PokerTable.region_community_card_3.highlight()
        PokerTable.region_community_card_4.highlight()
        PokerTable.region_community_card_5.highlight()



#p = PlayNowApp()
#p.open()
#p.login()
#p.go_to_texas_holdem()
#p.go_to_practice_tables()
#t = PokerTable()
#t.join_table()  
#t.highlight_regions_all()
#t.leave_table()
#p.close()
