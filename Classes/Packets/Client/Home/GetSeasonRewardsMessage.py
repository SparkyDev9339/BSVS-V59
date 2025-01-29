from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.BattleLogPlayerEntry import BattleLogPlayerEntry


class GetSeasonRewardsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['RewardID'] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(22033, fields)

    def getMessageType(self):
        return 12938

    def getMessageVersion(self):
        return self.messageVersion