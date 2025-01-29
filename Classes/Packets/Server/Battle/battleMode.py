from Classes.Packets.PiranhaMessage import PiranhaMessage
import random
from Classes.BitStream import BitStream

class battleMode(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        pass
        
    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 6974

    def getMessageVersion(self):
        return self.messageVersion