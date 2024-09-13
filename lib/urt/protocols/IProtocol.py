
class IProtocol():

	def __init__(self):
		pass

	def initialize(self):
		pass

	# ==========================================
	# PORT
	# ==========================================

	def createPort(self):
		raise Exception("createPort() not implemented in protocol class!")

	@property
	def port(self):
		pass
	
	@port.setter
	def port(self,value):
		pass

	# ==========================================
	# DEVICE
	# ==========================================

	def _decodeAnswer(self, command,data):
		pass

	def _getAnswerSize(self,command):
		pass

	def main(self):
		pass
		
	def createModulations(self):
		pass
	
	def createCommands(self):
		pass
	
	def createPilottones(self):
		pass

	## Prepairs data to be send to the device.
	#  This function returns a list of commands to send.
	#  [
	#     [command, data package],
	#     ...
	#  ]
	#  This allows to send other commands before the 
	#  actual command.
	# Example: FT-817 FMW is just allowed in a certain
	#          frequency range. So we can change frequency
	#          before switching to FMW.
	def prepairParameters(command,data = None):
		pass
	
	def prepairData(self,command, parameters):
		pass

	def assumeCommandSupport(self,command):
		pass

	def encodeCommand(self,command):
		pass

	def decodeCommand(self,command):
		pass

	def encodeModulation(self,modulation):
		pass
	
	def decodeModulation(self,modulation):
		pass

	def assumeModulationSupport(self,modulation):
		pass

	## Sends data to the device.
	#
	#  @param commandlist   A list with commands send to the device.
	#                       [
	#                         [ENUM-Value, data package ],
	#                         [Commands.SET_FREQUENCY, [000,110,200,010,01]]
	#                       ]
	#                       The data package is send unchanged.
	def write(self,commandlist):
		pass

	def isCommandSupported(self,command):
		pass
	
	def isModulationSupported(self,modulation):
		pass
