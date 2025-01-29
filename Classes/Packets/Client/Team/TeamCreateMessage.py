from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Gameroom import Gameroom
from Database.DatabaseHandler import DatabaseHandler
from Classes.ClientsManager import ClientsManager

class TeamCreateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['mapSlot'] = self.readVInt()
        fields['mapID'] = self.readVInt()
        fields['roomType'] = self.readVInt()
        fields['Unk4'] = self.readBoolean()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)

        roomID = len(ClientsManager.rooms) + 1
        playerData['RoomID'] = roomID
        db_instance.updatePlayerData(playerData, calling_instance)
        Gameroom.create(calling_instance, roomID, fields['roomType'], 7, calling_instance.player.ID)
        Messaging.sendMessage(24124, fields, calling_instance.player)

    def getMessageType(self):
        return 12541

    def getMessageVersion(self):
        return self.messageVersion