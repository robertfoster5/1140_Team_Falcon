from Connection import Connection

class Telephone():

    def speak(self, text):
        print(text)


    def run(self,wire):
        keypad = "123456789#"
        while(True):
            enter = input()
            if(len(enter) == 0):
                continue
            elif(enter.lower() == "h"):
                wire.hangup()
            elif(enter.lower() == "q"):
                break
            elif(len(enter) == 1 and enter in keypad):
                wire.dial(enter)
            else:
                wire.record(enter)
