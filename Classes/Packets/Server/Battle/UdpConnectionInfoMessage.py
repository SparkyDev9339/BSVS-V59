from io import BytesIO

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class UdpConnectionInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(9449) # Server Port
        self.writeString("192.168.43.147") # Server IP
        self.writeInt(0)
        self.writeByte(0)
        self.writeInt(0)
        self.writeByte(0)

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24112

    def getMessageVersion(self):
        return self.messageVersion