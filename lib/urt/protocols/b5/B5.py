from .. import Protocol

from lib.Property import EventManager


class B5(Protocol):
	
	def __init__(self):
		super().__init__()

		self.__expectedCommandAnswer = []

	# ==========================================
	# DEVICE
	# ==========================================

	def _decodeAnswer(self, command,data):
		raise Exception("_decodeAnswer() not implemented in protocol class!")

	def _getAnswerSize(self,command):
		raise Exception("_getAnswerSize() not implemented in protocol class!")

	def main(self):
		
		super().main()
		
		# Read answer if waiting for
		if len(self.__expectedCommandAnswer) > 0:
			size = self._getAnswerSize( self.__expectedCommandAnswer[-1] )
			# Read answer if available
			if self.port.available >= size:
				data = self.port.read(size)
				# Get command for answer
				command = self.__expectedCommandAnswer.pop()
				# decode the answer
				self._decodeAnswer(command,data)

	def write(self,commandlist):
		
		for cmd,data in commandlist:
			self.__expectedCommandAnswer.insert(0,cmd)
		
		return super().write(commandlist)