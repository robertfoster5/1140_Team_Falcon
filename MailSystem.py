from Mailbox import Mailbox

class MailSystem:
	def __init__(self, mailboxCount):
		self.mailboxes = []
		i = 0
		while i < mailboxCount:
			passcode = "" + str(i + 1)
			greeting = "You have reached mailbox " + str(i + 1) + ". \nPlease leave a message now."
			self.mailboxes.append(Mailbox(passcode, greeting))
			i = i + 1
			 
	def findMailbox(ext):
		i = ext[0:len(ext)-2]
		if 1 <= i and i <= self.mailboxes.size():
			return self.mailboxes[i-1]
		else:
			return None
