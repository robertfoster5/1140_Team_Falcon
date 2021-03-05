from MailSystem import MailSystem
from Telephone import Telephone
from Connection import Connection

MAILBOX_COUNT = 20

class MailSystemTester:
	system = MailSystem(MAILBOX_COUNT)
	p = Telephone()
	c = Connection(system, p)
	p.run(c)
	
