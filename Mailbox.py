from MessageQueue import MessageQueue
from Message import Message

class Mailbox:
	def __init__(self, aPasscode, aGreeting):
		self.passcode = aPasscode
		self.greeting = aGreeting
		self.newMessages = MessageQueue()
		self.keptMessages = MessageQueue()
		
	def checkPasscode(self, aPasscode):
		if(self.passcode == aPasscode):
			return 1;
		else:
			return 0;
			
	def addMessage(self, aMessage):
		self.newMessages.add(aMessage)
		
	def getCurrentMessage(self):
		if self.newMessages.size() > 0:
			return self.newMessages.peek()
		elif self.keptMessages.size() > 0:
			return self.keptMessages.peek()
		else:
			return None;
	
	def removeCurrentMessage(self):
		if self.newMessages.size() > 0:
			return self.newMessages.remove()
		elif self.keptMessages.size() > 0:
			return self.keptMessages.remove()
		else:
			return None;
	
	def saveCurrentMessage(self):
		m = Message()
		m = removeCurrentMessage()
		if (m != None):
			self.keptMessages.add(m)
	
	def setGreeting(self,newGreeting):
		self.greeting = newGreeting
	
	def setPasscode(self,newPasscode):
		self.passcode = newPasscode
		
