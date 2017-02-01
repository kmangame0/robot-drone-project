import time, socket, XboxController

s = socket.socket()
host = "192.168.1.2"
port = 12345
s.connect((host, port))
size = 1024

xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)

xboxCont.start()

while True:
	if xboxCont.LTHUMBX > 0.2:
		x1 = "r"+str(float("{0:.2f}".format(xboxCont.LTHUMBX)))
		s.send(x1)				
	elif xboxCont.LTHUMBX < -0.2:
		x1 = "l"+str(float("{0:.2f}".format(xboxCont.LTHUMBX)))
		s.send(x1)
	elif xboxCont.LTHUMBY < -0.2:
		x1 = "u"+str(float("{0:.2f}".format(xboxCont.LTHUMBY)))
		s.send(x1)
	elif xboxCont.LTHUMBY > 0.2:
		x1 = "d"+str(float("{0:.2f}".format(xboxCont.LTHUMBY)))
		s.send(x1)
	else:
		x1 = "s"
		s.send(x1)