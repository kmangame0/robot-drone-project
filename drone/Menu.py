from Tkinter import *
import Autonomous
root = Tk()
ACClicked = False
MCClicked = False
RobotACClicked = False
RobotMCClicked = False


class Main():

    ACClicked = False
    MCClicked = False
    RobotACClicked = False
    RobotMCClicked = False
    
    def __init__(self):

        self.root = root
        #Drone side
        drone = Label(root, text="Drone",width=10)
        drone.grid(row=0, column=0)

        b1 = Button(root, text="Autonomous", width=10, command=lambda: self.DroneAutonomousClicked(b1,b2))
        b1.grid(row=1, column=0,padx=25)

        b2 = Button(root, text="Manual", width=10, command=lambda: self.DroneManualClicked(b1,b2))
        b2.grid(row=2, column=0)

        b3 = Button(root, text="Stop", width=10, command=lambda: self.DroneStop(b1,b2))
        b3.grid(row=3, column=0)

        #Robot side
        robot = Label(root, text="Robot",width=10)
        robot.grid(row=0, column=2)

        b4 = Button(root, text="Autonomous", width=10, command=lambda: self.RobotAutonomousClicked(b4,b5))
        b4.grid(row=1, column=2,padx=25)

        b5 = Button(root, text="Manual", width=10, command=lambda: self.RobotManualClicked(b4,b5))
        b5.grid(row=2, column=2)

        b6 = Button(root, text="Stop", width=10, command=lambda: self.RobotStop(b4,b5))
        b6.grid(row=3, column=2)

        root.title("Control Center")
        mainloop()

    #Drone Methods

    def DroneAutonomousClicked(self,b1,b2):
        global ACClicked
        global MCClicked
        MCClicked = False
        b2.configure(bg='light grey')
        if ACClicked == False:
            ACClicked = True
            b1.configure(bg='green')
            Autonomous.run()
            print "Here"
            #Video2.videoProcessing()
        else:
            #Video2.stop = True
            ACClicked = False
            b1.configure(bg='light grey')
        
    def DroneManualClicked(self,b1,b2):
        global ACClicked
        global MCClicked
        ACClicked = False
        Video2.stop = True
        b1.configure(bg='light grey')
        if MCClicked == False:
            MCClicked = True
            b2.configure(bg='green')
        else:
            MCClicked = False
            b2.configure(bg='light grey')
        
    def DroneStop(self,b1,b2):
        global ACClicked
        global MCClicked
        Video2.stop = True
        b1.configure(bg='light grey')
        b2.configure(bg='light grey')
        ACClicked = False
        MCClicked = False

    #Robot Methods
    def RobotAutonomousClicked(self,b4,b5):
        global RobotACClicked
        global RobotMCClicked
        RobotMCClicked = False
        b5.configure(bg='light grey')
        if RobotACClicked == False:
            RobotACClicked = True
            b4.configure(bg='green')
        else:
            RobotACClicked = False
            b4.configure(bg='light grey')
        
    def RobotManualClicked(self,b4,b5):
        global RobotACClicked
        global RobotMCClicked
        RobotACClicked = False
        b4.configure(bg='light grey')
        if RobotMCClicked == False:
            RobotMCClicked = True
            b5.configure(bg='green')
        else:
            RobotMCClicked = False
            b5.configure(bg='light grey')
        
    def RobotStop(self,b4,b5):
        global RobotACClicked
        global RobotMCClicked
        b4.configure(bg='light grey')
        b5.configure(bg='light grey')
        RobotACClicked = False
        RobotMCClicked = False
        
Main()
