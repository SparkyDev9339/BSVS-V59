from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class SeasonRewardsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(fields['RewardID']) # RewardID

        self.writeVInt(0)

    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22033
    
    def getMessageVersion(self):
        return self.messageVersion