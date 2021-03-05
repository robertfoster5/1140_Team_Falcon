from Message import Message

class MessageQueue():

    messageList = []

    def remove(self):
        if self.size() == 0:
            return None
        else:
            return self.messageList.pop(0)

    def add(self,mes):
        self.messageList.append(mes)

    def size(self):
        return len(self.messageList)

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.messageList[0]