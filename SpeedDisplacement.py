import time
import ps_drone
import numpy as np
import matplotlib.pyplot as pit

drone = ps_drone.Drone()       
drone.startup()
drone.reset()

time.sleep(1)
drone.takeoff()
time.sleep(12)
drone.land()
