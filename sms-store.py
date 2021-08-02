# unread_messages = [] # not used
SMSStore = [] # creating empty list to store messages

class SMSMessage(object):
    '''
    Class for sms inbox with various methods for execution
    '''
    def __init__(self, messageText, fromNumber):
        
        self.hasBeenRead = False
        self.messageText = messageText
        if fromNumber is None:
            fromNumber = []
        else:
            self.fromNumber = fromNumber

    # I excluded below method since I did not use it, but kept it for reusability
    '''
    # defining method to change boolean value of whether a specific message has been read or not
    def MarkAsRead(self, q):
        
        SMSStore[q][0] = True
    '''

    # defining method to add messages to the inbox              
    def add_sms(self):
       
        message_new = [self.hasBeenRead, self.messageText, self.fromNumber]
        return SMSStore.append(message_new)

    # I excluded below method since I did not use it, but kept it for reusability
    '''     
    # defining method for adding unread messages to another list (if so required)   
    #def add_unread(self):

    #    message_unread = [self.hasBeenRead, self.messageText, self.fromNumber]
    #    return unread_messages.append(message_unread)
    '''
    # defining method to get count of messages in inbox
    def get_count(self):
        
        return len(SMSStore), len(unread_messages)
    
    # defining method to get specific message from the inbox and changing its state to True since it will be read
    def get_message(self, q):
        
        print(SMSStore[q])
        SMSStore[q][0] = True  # changing to true if message has been read (same as the get_hasBeenRead method below, I just chnaged the way I wanted it occurs)
    
    # I excluded below method since I did not use it, but kept it for reusability
    '''
    # defining a method to get status of message
    #def get_hasBeenRead(self):
        
    #    self.hasBeenRead = True
    '''
    # method to get unread messages should user want to see list of messages per ling
    def get_unread_messages(self, store):
        
        counter = 0
        print("Below list of unread messages (marked as False for hasBeenRead)\n")
    
        for i in store:
            
            if store[counter][0] == False:
                print("Message: " + store[counter][1] + "From: " + store[counter][2])
            
            counter += 1

    # defining method for removing messages from inbox should it be required
    def remove(self, i):
        return SMSStore.remove(i)

'''
Adding some messages for the exercise below (could also have thrown this in the while loop for user to add him/herself but decided to keep it here for purposes of this exercise)
'''

# adding first message object
message_1 = SMSMessage("How are you", "012 650 3311").add_sms()
# adding second message object 
message_2 = SMSMessage("This is great", "011 345 4433").add_sms()
# adding third message object
message_3 = SMSMessage("Lovely", "061 345 5890").add_sms() 
# adding fourth message object
message_4 = SMSMessage("Mmm yeah", "062 321 118").add_sms() 

'''
Running the loop for user choices
'''

userChoice = ""

while userChoice != "quit":

    userChoice = input("What would you like to do - read/send/quit? ")
    
    if userChoice == "read":

        i = int(input("Please enter index of the message you want to read "))
        
        messageText = "null"
        fromNumber = "null"
        hasBeenRead = "null"

        Object1 = SMSMessage(messageText, fromNumber)
        
        Object1.get_message(i)

        read_unread_messages = input("Would you like to read unread message? yes/no ")
    
        if read_unread_messages == "yes":
        
            Object1.get_unread_messages(SMSStore)

        else:
        
            print("Message/s have been read")
        
    elif userChoice == "send":       

        messageText = input("Please type your message ")
        fromNumber = input("Please type number send from ")
        Object = SMSMessage(messageText, fromNumber)
        Object.add_sms()

        print(str(Object.get_count()) + " is now the new length of the list")

    elif userChoice == "quit":
            
        print("Goodbye")

    else:
        
        print("Oops - incorrect input")

print(SMSStore) #printing SMSStore just to show how messages which has been read were changed to true and that new messages are also added if a user should select "send"
