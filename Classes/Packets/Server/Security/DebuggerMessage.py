from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
import random

class DebuggerMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        MessageCount = fields['MessageCount']
        Message = fields['Message']
        for MessageIndex in range(MessageCount):
            self.writeString(Message)
            self.writeInt(random.randint(100, 500))
            self.writeVInt(random.randint(0,1000))
        
    def decode(self):
        fields = {}
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20500

    def getMessageVersion(self):
        return self.messageVersion