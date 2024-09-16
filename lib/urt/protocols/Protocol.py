import time, serial

from lib.Property import Property

from . import IProtocol
from ..ports.Serial import Serial
from ..enums import COMMAND
from ..enums import MODULATION
from ..Exceptions import CommandNotSupportedException
from ..Exceptions import ModulationNotSupported

class Protocol(IProtocol):


	def __init__(self):
		super().__init__()
		self.__port = self.createPort()

		self._modulations = self.createModulations()
		self._commands    = self.createCommands()
		self._pilottones  = self.createPilottones()

		self.model        = Property(True,self)
		self.manufacturer = Property(True,self)
		
		self.smeter       = Property(True,self)
		self.dCentering   = Property(True,self)
		self.dcsCode      = Property(True,self)
		self.squelch      = Property(True,self)

		self.power       = Property(True,self)
		self.split       = Property(True,self)
		self.swr         = Property(True,self)
		self.ptt         = Property(True,self)

		self.frequency    = Property(True,self)
		self.modulation   = Property(True,self)
		
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

	def createModulations(self):
		raise Exception("getModes() not implemented in protocol class!")
	
	def createCommands(self):
		raise Exception("createCommands() not implemented in protocol class!")
	
	def createPilottones(self):
		raise Exception("createPilottones () not implemented in protocol class!")

	def main(self):
		super().main()
		
		if self.__port:
			self.__port.main()

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
		
		if command == COMMAND.LOCK_ON: 
			return self._commands.LOCK_ON
		
		if command == COMMAND.LOCK_OFF: 
			return self._commands.LOCK_OFF
		
		if command == COMMAND.LOCK_TOGGLE:
			return self._commands.LOCK_TOGGLE
		
		if command == COMMAND.SPLIT_ON:
			return self._commands.SPLIT_ON
		
		if command == COMMAND.SPLIT_OFF:
			return self._commands.SPLIT_OFF
		
		if command == COMMAND.SPLIT_TOGGLE:
			return self._commands.SPLIT_TOGGLE
		
		if command == COMMAND.SET_FREQUENCY:
			return self._commands.SET_FREQUENCY
		
		if command == COMMAND.SET_MODULATION:
			return self._commands.SET_MODULATION
		
		if command == COMMAND.READ_RX_STATE:
			return self._commands.READ_RX_STATE
		
		if command == COMMAND.READ_TX_STATE:
			return self._commands.READ_TX_STATE

		if command == COMMAND.READ_FREQ_MODE:
			return self._commands.READ_FREQ_MODE

		if command == COMMAND.PTT_ON:
			return self._commands.PTT_ON

		if command == COMMAND.PTT_OFF:
			return self._commands.PTT_OFF

		return None

	def decodeCommand(self,command):
		
		if command == self._commands.LOCK_ON: 
			return COMMAND.LOCK_ON
		
		if command == self._commands.LOCK_OFF: 
			return COMMAND.LOCK_OFF
		
		if command == self._commands.LOCK_TOGGLE:
			return COMMAND.LOCK_TOGGLE
		
		if command == self._commands.SPLIT_ON:
			return COMMAND.SPLIT_ON
		
		if command == self._commands.SPLIT_OFF:
			return COMMAND.SPLIT_OFF
		
		if command == self._commands.SPLIT_TOGGLE:
			return COMMAND.SPLIT_TOGGLE
		
		if command == self._commands.SET_FREQUENCY:
			return COMMAND.SET_FREQUENCY
		
		if command == self._commands.SET_MODULATION:
			return COMMAND.SET_MODULATION
		
		if command == self._commands.READ_RX_STATE:
			return COMMAND.READ_RX_STATE
		
		if command == self._commands.READ_TX_STATE:
			return COMMAND.READ_TX_STATE

		if command == self._commands.READ_FREQ_MODE:
			return COMMAND.READ_FREQ_MODE

		if command == self._commands.PTT_ON:
			return COMMAND.PTT_ON

		if command == self._commands.PTT_OFF:
			return COMMAND.PTT_OFF
		
		return None

	def encodeModulation(self,modulation):
		if modulation == MODULATION.LSB: 
			return self._modulations.LSB
		
		if modulation == MODULATION.USB: 
			return self._modulations.USB
		
		if modulation == MODULATION.CW: 
			return self._modulations.CW
		
		if modulation == MODULATION.CWR: 
			return self._modulations.CWR
		
		if modulation == MODULATION.AM: 
			return self._modulations.AM
		
		if modulation == MODULATION.FM: 
			return self._modulations.FM
		
		if modulation == MODULATION.DIG: 
			return self._modulations.DIG
		
		if modulation == MODULATION.PKT: 
			return self._modulations.PKT
		
		if modulation == MODULATION.FMN: 
			return self._modulations.FMN
		
		if modulation == MODULATION.FMW: 
			return self._modulations.FMW
		
		return None
	
	def decodeModulation(self,modulation):
		#print(modulation)
		if modulation == self._modulations.LSB: 
			return MODULATION.LSB
		
		if modulation == self._modulations.USB: 
			return MODULATION.USB
		
		if modulation == self._modulations.CW: 
			return MODULATION.CW
		
		if modulation == self._modulations.CWR: 
			return MODULATION.CWR
		
		if modulation == self._modulations.AM: 
			return MODULATION.AM
		
		if modulation == self._modulations.FM: 
			return MODULATION.FM
		
		if modulation == self._modulations.DIG: 
			return MODULATION.DIG
		
		if modulation == self._modulations.PKT: 
			return MODULATION.PKT
		
		if modulation == self._modulations.FMN: 
			return MODULATION.FMN
		
		if modulation == self._modulations.FMW: 
			return MODULATION.FMW
		
		return None

	def assumeModulationSupport(self,modulation):
		if self.isModulationSupported(modulation) == False:
			raise ModulationNotSupported("Modulation not supported!")

	## Sends data to the device.
	#
	#  @param commandlist   A list with commands send to the device.
	#                       [
	#                         [ENUM-Value, data package ],
	#                         [COMMAND.SET_FREQUENCY, [000,110,200,010,01]]
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
