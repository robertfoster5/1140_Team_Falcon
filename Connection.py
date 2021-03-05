from Mailbox import Mailbox
from MailSystem import MailSystem
from Message import Message
from MessageQueue import MessageQueue
#from Teleself.phone import Teleself.phone

DISCONNECTED = 0
CONNECTED = 1
RECORDING = 2
MAILBOX_MENU = 3
MESSAGE_MENU = 4
CHANGE_PASSCODE = 5
CHANGE_GREETING = 6
INITIAL_PROMPT = "Enter mailbox number followed by #"
MAILBOX_MENU_TEXT = "Enter 1 to listen to your messages\n" + "Enter 2 to change your passcode\n" + "Enter 3 to change your greeting"
MESSAGE_MENU_TEXT = "Enter 1 to listen to the current message\n" + "Enter 2 to save the current message\n" + "Enter 3 to delete the current message\n"+ "Enter 4 to return to the main menu"

class Connection:
	system = []	
	phone = []
	state = []
	currentMailbox = ""
	accumulatedKeys = ""
	currentRecording = ""
	
	def __init__(self, s, p):
		self.system = s
		self.phone = p
		self.resetConnection()
	
	def dial(self,key):
		if self.state == CONNECTED:
			self.connect(key)
		elif self.state == RECORDING:
			self.login(key)
		elif self.state == CHANGE_PASSCODE:
			changePasscode(key)
		elif self.state == CHANGE_GREETING:
			self.changeGreeting(key)
		elif self.state == MAILBOX_MENU:
			self.mailboxMenu(key)
		elif self.state == MESSAGE_MENU:
			self.messageMenu(key)	
		
	def record(self, voice):
		if self.state == RECORDING or  self.state == CHANGE_GREETING:
			self.currentRecording += voice
	
	def hangup(self):
		if self.state == RECORDING:
			self.currentMailbox.addMessage(currentRecording)
		self.resetConnection()
	
	def resetConnection(self):
		self.currentRecording = ""
		self.accumulateKeys = ""
		self.state = CONNECTED
		self.phone.speak(INITIAL_PROMPT)
		
	def connect(self, key):
		if key == "#":
			self.currentMailbox = self.system.findMailbox(accumulatedKeys)
			if currentMailbox != None :
				self.state = RECORDING
				self.phone.speak(currentMailbox.getGreeting())
			else:
				self.self.phone.speak("Incorrect mailbox number. Try again!")
				self.accumulatedKeys = ""
		else:
			self.accumulatedKeys += key
	
	def changePasscode(self, key):
		if key == "#":
			currentMailbox.setPasscode(accumulatedKeys)
			self.state = MAILBOX_MENU
			self.phone.speak(MAILBOX_MENU_TEXT)
			self.accumulatedKeys = ""
		else:
			self.accumulatedKeys += key
			
	def changeGreeting(self, key):
		if key == "#":
			self.currentMailbox.setGreeting(currentRecording)
			self.currentRecording = ""
			self.state = MAILBOX_MENU
			self.phone.speak(MAILBOX_MENU_TEXT)
			
	def mailboxMenu(self, key):
		if key == "1":
			self.state = MESSAGE_MENU
			self.phone.speak(MESSAGE_MENU_TEXT)
		elif key == "2":
			self.state = CHANGE_PASSCODE
			self.phone.speak("ENTER new passcode followed by the # key")
		elif key == "3":
			self.state = CHANGE_GREETING
			self.phone.speak("Record your greeting, then press the # key")
	
	def messageMenu(self, key):
		if key == "1":
			output = ""
			m = self.currentMailbox.getCurrentMessage()
			if m == None:
				output += "No messages." + "\n"
			else:
				output += m.messageText + "\n"
			output += MESSAGE_MENU_TEXT
			self.phone.speak(output)
		elif key == "2":
			self.currentMailbox.saveCurrentMessage()
			self.phone.speak(MESSAGE_MENU_TEXT)
		elif key == "3":
			self.currentMailbox.removeCurrentMessage()
			self.phone.speak(MESSAGE_MENU_TEXT)
		elif key == "4":
			self.state = MAILBOX_MENU
			self.phone.speak(MAILBOX_MENU_TEXT)

	
