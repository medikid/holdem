'''
Created on Feb 1, 2013

@author: chinnu
'''
from sikuli.Sikuli import *
from os import path
#from sys import *

class PlayNowApp():
    userid = 'ragavgroups'
    pwd = 'Ragav76'
    screen_title = 'Poker | PlayNow.com'    
    app_screen = App(screen_title)
    folder_path = path.dirname(path.realpath(__file__))
    
    def __init__(self):
        self.path_exe = r'C:\Program Files (x86)\Poker PlayNow.com\poker.exe'
        self.path_image = PlayNowApp.folder_path + '\\images'
#        guide.dialog("initialized app")

    def open(self):
        if PlayNowApp.app_screen.window(0) :
            # switchApp(PlayNowApp.app_screen)
            PlayNowApp.app_screen.focus()
        else:
             type('r', KeyModifier.WIN)                        
             paste(self.path_exe)
             type(Key.ENTER)
             wait(5)
        self.maximize()
 #        guide.dialog("Opened app")

    def close(self):
        click(self.image("exit-poker-btn"))
        wait(1)
        click(self.image("yes-btn"))
#       guide.dialog("Closed app")

    def image(self, name):
        img_path = self.path_image + '\\' + name + '.png'
        return img_path
            
    def maximize(self):
       click(self.image("maximize-btn"))
#       dialog("Maximized Screen")

    def login(self):
       click(self.image("loginnow-btn"))
       wait(1)
       click(self.image("password-field"))
       type(PlayNowApp.pwd)
       wait(1)
       click(self.image("loginnow-btn"))
       wait(3)
#       dialog("Logged into app")

    def go_to_texas_holdem(self):
        click(self.image("texas-holdem-btn"))

    def go_to_practice_tables(self):
        click(self.image("practice-btn"))
        wait(2) 
        click(self.image("pokerschool-lbl"))
        wait(2)
        click(self.image("go-to-table-btn"))
        wait(2)
        self.maximize()
 #       dialog("Selected a practice table")
        
        


