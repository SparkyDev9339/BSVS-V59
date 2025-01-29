from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class LatencyTestResultMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1)

        self.writeVInt(0) # R (Server Type(Number?))
        self.writeVInt(0) # Ping
        self.writeVInt(0) # Q
        self.writeVInt(0) # C
        self.writeBoolean(True) # Unk
        self.writeInt(1)
        self.writeInt(2)
        self.writeString(" tg:archbrawl")
        self.writeString(" tg:archbrawl")
        self.writeString(" tg:archbrawl")
        
        
    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 49001

    def getMessageVersion(self):
        return self.messageVersion