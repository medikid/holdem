'''
Created on 2013-02-02

@author: chinnu
'''
from javax.swing import JFrame, JPanel, JButton, JToggleButton, Timer, JLabel, JMenuBar, JMenu, JMenuItem, ImageIcon, JScrollPane
from java.awt import FlowLayout, GridLayout, Toolkit
from java.awt.BorderLayout import SOUTH, NORTH
from java.awt.image import BufferedImage
from javax.imageio import ImageIO
from java.io import File
from threading import Thread
from sikuli.Sikuli import *
from PlayNowApp import PlayNowApp
from PokerTable import PokerTable

class PokerApp:
    def __init__(self):
        self._frame = JFrame("PokerApp", size=(600,400), defaultCloseOperation=JFrame.EXIT_ON_CLOSE)

    def minimizeFrame(self, true_false):
        if true_false == True:
            self._frame.state = JFrame.ICONIFIED
        else:
            self._frame.MAXIMIZED_BOTH
#            self._frame.state = JFrame.NORMAL

    def launchPlayNowApp(self, action):
            
            self.playNowApp = PlayNowApp()
            self.pokerTable = PokerTable()
            if (action=="open") :
                self.playNowApp.open()
                self.msg.text += "Play now app opened"
            elif action=="playNowLogin":
                self.playNowApp.login()
                self.msg.text += "Logged into PlayNow app"
            elif action=="texasHoldem":
                self.playNowApp.go_to_texas_holdem()
            elif action=="practiceTable":
                self.playNowApp.go_to_practice_tables()
                self.minimizeFrame(False)
            elif action=="joinTable":
                self.pokerTable.join_table()
            elif action=="highlightObservations":
                self.pokerTable.highlight_regions_all()
            elif action=="leaveTable":
                self.pokerTable.leave_table()
            elif action=="playNowClose":
                self.playNowApp.close()
            else:
                self.minimizeFrame(True)
                self.playNowApp.open()
                self.msg.text += "Play now app opened"
                self.playNowApp.login()
                self.msg.text += "Logged into PlayNow app"
                self.playNowApp.go_to_texas_holdem()
                self.playNowApp.go_to_practice_tables()
                self.minimizeFrame(False)
                self.pokerTable.join_table()
                


    def getScreenSize(self):
        return Toolkit.getDefaultToolkit().getScreenSize()

    def setFrameLocation(self, side):
            screenSize = self.getScreenSize()
            if side == 'Right':
                self._frame.setSize( int(screenSize.width * 0.31), int(screenSize.height * 0.95) )
                self._frame.setLocation( int(screenSize.width * 0.69), 0 )
            

    def playNowApp_startThread(self, action):
            self.setFrameLocation("Right")
            Thread(name="AppLaunch", target=self.launchPlayNowApp, args=(action,) ).start()
            
            

    def setMenuBar(self):
        menuBar = JMenuBar()
        
        menuApp = JMenu("Apps")
        menuApp.setMnemonic('A')
        
        menuSettings = JMenu("Settings")
        menuSettings.setMnemonic('S')
        
        #set submenus
        menuPlayNow = JMenu("PlayNow" )
        
        menuPlayNowOpen = JMenuItem("Open", actionPerformed = (lambda x, param="open": self.playNowApp_startThread(param)) )
        menuPlayNow.add(menuPlayNowOpen)
        
        menuPlayNowLogin = JMenuItem("Login", actionPerformed = lambda x, action="playNowLogin": self.playNowApp_startThread(action) )
        menuPlayNow.add(menuPlayNowLogin)
        
        menuPlayNowClose = JMenuItem("Close", actionPerformed = lambda x, action="playNowClose": self.playNowApp_startThread(action) )
        menuPlayNow.add(menuPlayNowClose)
        
        menuPokerTable = JMenu("PokerTable")
        menuPokerTableJoin = JMenuItem("Find Practice Table", actionPerformed = lambda x, action="practiceTable": self.playNowApp_startThread(action) )
        menuPokerTable.add(menuPokerTableJoin)
        
        menuPokerTableJoin = JMenuItem("Join Table", actionPerformed = lambda x, action="joinTable": self.playNowApp_startThread(action) )
        menuPokerTable.add(menuPokerTableJoin)
        
        menuPokerTableAddChips = JMenuItem("Add Chips", actionPerformed = lambda x, action="addChips": self.playNowApp_startThread(action) )
        menuPokerTable.add(menuPokerTableAddChips)
        
        menuPokerTableSitOut = JMenuItem("Sit Out", actionPerformed = lambda x, action="sitOut": self.playNowApp_startThread(action) )
        menuPokerTable.add(menuPokerTableSitOut)
        
        menuPokerTableLeaveTable = JMenuItem("Leave Table", actionPerformed = lambda x, action="leaveTable": self.playNowApp_startThread(action) )
        menuPokerTable.add(menuPokerTableLeaveTable)
        
        menuPokerAppExit = JMenuItem("Exit")
        
        menuApp.add(menuPlayNow)
        menuApp.add(menuPokerTable)
        menuApp.addSeparator()
        menuApp.add(menuPokerAppExit)
        
        menuBar.add(menuApp)
        menuBar.add(menuSettings)
        
        self._frame.setJMenuBar(menuBar)

    def startGui(self):
        
#        self.gridPanel = JPanel(GridLayout(self.numRows, self.numCols))
#        self.cellButtons = self._doForAllCells(self._createCellButton)
#        self.grid = self._doForAllCells(lambda r,c: False)
#        frame.add(self.gridPanel)
#        buttonPanel = JPanel(FlowLayout())
#        stepButton = JButton("Step", actionPerformed=self._step)
#        runButton = JToggleButton("Run", actionPerformed=self._run)
#        buttonPanel.add(stepButton)
#        buttonPanel.add(runButton)
#        frame.add(buttonPanel, SOUTH)
#        frame.pack()
#        frame.locationRelativeTo = None
        self.setMenuBar()
        
        image_path = "D:\\wamp\\www\\holdem\\src\\poker\\th\\images\\As.png"
        myPicture = ImageIcon(image_path)
        myPictureLabel = JLabel("Pocket: ", myPicture, JLabel.LEFT)
        
        cardPanel = JPanel()
        cardPanel.setLayout(None)
        cardPanel.add(myPictureLabel)
        myPictureLabel.setBounds(10,10,36,52);
        
        self._frame.getContentPane().add(cardPanel)

        
        self.msg=JLabel("Hello")
        self._frame.add(self.msg, NORTH)
        self._frame.locationRelativeTo = None
        self._frame.visible = True


pk=PokerApp()
pk.startGui()
#p = PlayNowApp()
#p.open()
#p.login()
#p.go_to_texas_holdem()
#p.go_to_practice_tables()
#t = PokerTable()
#t.join_table()  
#            t.highlight_regions_all()
#            t.leave_table()
#            p.close()
