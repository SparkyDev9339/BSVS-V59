from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Gameroom import Gameroom
from Database.DatabaseHandler import DatabaseHandler
from Classes.ClientsManager import ClientsManager

class TeamLeaveMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)

        for plr in ClientsManager.rooms[playerData['RoomID']-1]['players']:
            if plr['id'] == calling_instance.player.ID:
                playerData['RoomID'] = 0
                db_instance.updatePlayerData(playerData, calling_instance)
                fields["Socket"] = calling_instance.client
                Messaging.sendMessage(24125, fields, calling_instance.player)
            else:
                fields['Socket'] = ClientsManager.PlayersList[plr['id'][1]]['Socket']
                Messaging.sendMessageByID(24125, fields, plr['id'][1], calling_instance.player)

    def getMessageType(self):
        return 14353

    def getMessageVersion(self):
        return self.messageVersion