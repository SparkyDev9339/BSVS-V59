from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.BattleLogPlayerEntry import BattleLogPlayerEntry


class GetPlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["BattleInfoBoolean"] = self.readBoolean()
        if fields["BattleInfoBoolean"]:
            fields["unk1"] = self.readVInt()
            fields["AnotherID"] = self.readLong()
            fields["unk2"] = self.readVInt()
            for i in self.readVInt():
                fields["CsvID"] = self.readDataReference()
                fields["unk3"] = self.readVInt()
                fields["unk4"] = self.readVInt()
                fields["unk5"] = self.readVInt()
            fields["unk6"] = self.readVInt()
            fields["PlayerName"] = self.readString()
            fields["unk7"] = self.readVInt()
            fields["Thumbnail"] = self.readVInt()
            fields["NameColor"] = self.readVInt()
            fields["unk10"] = self.readVInt()
        fields["unk11"] = self.readVInt()
        fields["PlayerID"] = self.readLong()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24113, fields)

    def getMessageType(self):
        return 15081

    def getMessageVersion(self):
        return self.messageVersion