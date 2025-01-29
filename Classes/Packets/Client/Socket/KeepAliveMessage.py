from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
import time


class KeepAliveMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        return {}
    
    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(20108, fields)
        Messaging.sendMessage(49001, fields, calling_instance.player)

    def getMessageType(self):
        return 10108

    def getMessageVersion(self):
        return self.messageVersion