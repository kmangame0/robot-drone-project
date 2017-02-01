import time, sys
import ps drone
#Imports the PS-Drone-API
drone = ps drone.Drone()
drone.startup()
#Initials the PS-Drone-API
#Connects to the drone and starts subprocesses
drone.reset()
#Sets drone’s LEDs to green when red
while (drone.getBattery()[0]==-1): time.sleep(0.1)
#Reset completed ?
print ̈Battery: ̈+str(drone.getBattery()[0])+ ̈%  ̈+str(drone.getBattery()[1]) ̈
drone.useDemoMode(False)
#Give me everything...fast
drone.getNDpackage([ ̈demo ̈, ̈pressure raw ̈, ̈altitude ̈, ̈magneto ̈, ̈wifi ̈])
time.sleep(0.5)
#Give it some time to fully awake
##### Mainprogram #####
NDC =
drone.NavDataCount
end =
False
while not end:
while drone.NavDataCount==NDC: time.sleep(0.001) #Wait for NavData
if drone.getKey():
end = True
NDC = drone.NavDataCount
print ̈----------- ̈
print ̈Aptitude[X,Y,Z] :
 ̈+str(drone.NavData[ ̈demo ̈][2])
print ̈Altitude / sensor / pressure :  ̈+str(drone.NavData[ ̈altitude ̈][3])\
+ ̈ /  ̈+str(drone.State[21])+ ̈ /  ̈\
+str(drone.NavData[ ̈pressure raw ̈][0])
print ̈Megnetometer[X,Y,Z] :
 ̈+str(drone.NavData[ ̈magneto ̈][0])
print ̈Wifi link quality :
 ̈+str(drone.NavData[ ̈wifi ̈])