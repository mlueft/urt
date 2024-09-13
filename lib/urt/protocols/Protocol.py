import time, serial

from lib.Property import Property

from . import IProtocol
from ..ports.Serial import Serial
from ..ENUMS import COMMANDS
from ..ENUMS import MODULATIONS
from ..Exceptions import CommandNotSupportedException
from ..Exceptions import ModulationNotSupported

class Protocol(IProtocol):


	def __init__(self):
	
		self.__port = self.createPort()

		self._modulations = self.createModulations()
		self._commands    = self.createCommands()
		self._pilottones  = self.createPilottones()

		self.model        = Property(True)
		self.manufacturer = Property(True)
		
		self.smeter       = Property(True)
		self.dCentering   = Property(True)
		self.dcsCode      = Property(True)
		self.squelch      = Property(True)

		self.power       = Property(True)
		self.split       = Property(True)
		self.swr         = Property(True)
		self.ptt         = Property(True)

		self.frequency    = Property(True)
		self.modulation   = Property(True)
		
		self.sendDelay    = 0.2

	# ==========================================
	# CONNECTION
	# ==========================================

	def createPort(self):
		result = Serial()
		result.setProperty("baudrate", 4800 )
		result.setProperty("parity", serial.PARITY_NONE )
		result.setProperty("stopbit", serial.STOPBITS_TWO )
		result.setProperty("bytesize", serial.EIGHTBITS )
		result.setProperty("xonxoff", False )
		result.setProperty("rtscts", False )
		result.setProperty("dsrdtr", False )
		return result

	@property
	def port(self):
		return self.__port
	
	@port.setter
	def port(self,value):
		if self.__port.isConnected:
			self.__port.disconnect()

		self.__port = value

	# ==========================================
	# DEVICE
	# ==========================================

	def _decodeAnswer(self, command,data):
		raise Exception("_decodeAnswer() not implemented in protocol class!")

	def main(self):
		
		if self.__port:
			self.__port.main()
		
	def createModulations(self):
		raise Exception("getModes() not implemented in protocol class!")
	
	def createCommands(self):
		raise Exception("createCommands() not implemented in protocol class!")
	
	def createPilottones(self):
		raise Exception("createPilottones () not implemented in protocol class!")

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
		raise Exception("prepairParameters() not implemented in protocol class!")
	
	def prepairData(self,command, parameters):
		raise Exception("prepairData() not implemented in protocol class!")

	def assumeCommandSupport(self,command):
		if self.isCommandSupported(command) == False:
			raise CommandNotSupportedException("Command not supported!")

	def encodeCommand(self,command):
		
		if command == COMMANDS.LOCK_ON: 
			return self._commands.LOCK_ON
		
		if command == COMMANDS.LOCK_OFF: 
			return self._commands.LOCK_OFF
		
		if command == COMMANDS.LOCK_TOGGLE:
			return self._commands.LOCK_TOGGLE
		
		if command == COMMANDS.SPLIT_ON:
			return self._commands.SPLIT_ON
		
		if command == COMMANDS.SPLIT_OFF:
			return self._commands.SPLIT_OFF
		
		if command == COMMANDS.SPLIT_TOGGLE:
			return self._commands.SPLIT_TOGGLE
		
		if command == COMMANDS.SET_FREQUENCY:
			return self._commands.SET_FREQUENCY
		
		if command == COMMANDS.SET_MODULATION:
			return self._commands.SET_MODULATION
		
		if command == COMMANDS.READ_RX_STATE:
			return self._commands.READ_RX_STATE
		
		if command == COMMANDS.READ_TX_STATE:
			return self._commands.READ_TX_STATE

		if command == COMMANDS.READ_FREQ_MODE:
			return self._commands.READ_FREQ_MODE

		if command == COMMANDS.PTT_ON:
			return self._commands.PTT_ON

		if command == COMMANDS.PTT_OFF:
			return self._commands.PTT_OFF

		return None

	def decodeCommand(self,command):
		
		if command == self._commands.LOCK_ON: 
			return COMMANDS.LOCK_ON
		
		if command == self._commands.LOCK_OFF: 
			return COMMANDS.LOCK_OFF
		
		if command == self._commands.LOCK_TOGGLE:
			return COMMANDS.LOCK_TOGGLE
		
		if command == self._commands.SPLIT_ON:
			return COMMANDS.SPLIT_ON
		
		if command == self._commands.SPLIT_OFF:
			return COMMANDS.SPLIT_OFF
		
		if command == self._commands.SPLIT_TOGGLE:
			return COMMANDS.SPLIT_TOGGLE
		
		if command == self._commands.SET_FREQUENCY:
			return COMMANDS.SET_FREQUENCY
		
		if command == self._commands.SET_MODULATION:
			return COMMANDS.SET_MODULATION
		
		if command == self._commands.READ_RX_STATE:
			return COMMANDS.READ_RX_STATE
		
		if command == self._commands.READ_TX_STATE:
			return COMMANDS.READ_TX_STATE

		if command == self._commands.READ_FREQ_MODE:
			return COMMANDS.READ_FREQ_MODE

		if command == self._commands.PTT_ON:
			return COMMANDS.PTT_ON

		if command == self._commands.PTT_OFF:
			return COMMANDS.PTT_OFF
		
		return None

	def encodeModulation(self,modulation):
		if modulation == MODULATIONS.LSB: 
			return self._modulations.LSB
		
		if modulation == MODULATIONS.USB: 
			return self._modulations.USB
		
		if modulation == MODULATIONS.CW: 
			return self._modulations.CW
		
		if modulation == MODULATIONS.CWR: 
			return self._modulations.CWR
		
		if modulation == MODULATIONS.AM: 
			return self._modulations.AM
		
		if modulation == MODULATIONS.FM: 
			return self._modulations.FM
		
		if modulation == MODULATIONS.DIG: 
			return self._modulations.DIG
		
		if modulation == MODULATIONS.PKT: 
			return self._modulations.PKT
		
		if modulation == MODULATIONS.FMN: 
			return self._modulations.FMN
		
		if modulation == MODULATIONS.FMW: 
			return self._modulations.FMW
		
		return None
	
	def decodeModulation(self,modulation):
		#print(modulation)
		if modulation == self._modulations.LSB: 
			return MODULATIONS.LSB
		
		if modulation == self._modulations.USB: 
			return MODULATIONS.USB
		
		if modulation == self._modulations.CW: 
			return MODULATIONS.CW
		
		if modulation == self._modulations.CWR: 
			return MODULATIONS.CWR
		
		if modulation == self._modulations.AM: 
			return MODULATIONS.AM
		
		if modulation == self._modulations.FM: 
			return MODULATIONS.FM
		
		if modulation == self._modulations.DIG: 
			return MODULATIONS.DIG
		
		if modulation == self._modulations.PKT: 
			return MODULATIONS.PKT
		
		if modulation == self._modulations.FMN: 
			return MODULATIONS.FMN
		
		if modulation == self._modulations.FMW: 
			return MODULATIONS.FMW
		
		return None

	def assumeModulationSupport(self,modulation):
		if self.isModulationSupported(modulation) == False:
			raise ModulationNotSupported("Modulation not supported!")

	## Sends data to the device.
	#
	#  @param commandlist   A list with commands send to the device.
	#                       [
	#                         [ENUM-Value, data package ],
	#                         [COMMANDS.SET_FREQUENCY, [000,110,200,010,01]]
	#                       ]
	#                       The data package is send unchanged.
	def write(self,commandlist):
		result = 0
		for cmd,data in commandlist:
			result += self.__port.write(data)
			time.sleep(self.sendDelay)
		return result

	def isCommandSupported(self,command):
		return self.encodeCommand(command) != None
	
	def isModulationSupported(self,modulation):
		return self.encodeModulation(modulation) != None
