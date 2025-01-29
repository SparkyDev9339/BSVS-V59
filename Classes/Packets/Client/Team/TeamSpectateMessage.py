from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Gameroom import Gameroom
from Database.DatabaseHandler import DatabaseHandler
from Classes.ClientsManager import ClientsManager

class TeamSpectateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['RoomID'] = self.readVInt()
        fields['RoomID1'] = self.readVInt()
        fields['roomType'] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        print(fields['Socket'])
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)

        for room in ClientsManager.rooms:
            if room['roomID'] == fields['RoomID1']:
                if len(room['players']) < 3 and len(room['players']) < 1:
                    for plr in room['players']:
                        if playerData['ID'] != plr['id']:
                            playerData['RoomID'] = room['roomID']
                            db_instance.updatePlayerData(playerData, calling_instance)
                            new_player = {'id': calling_instance.player.ID, 'isOwner': 0, 'state': 2}
                            room['players'].append(new_player)
                            for plr in room['players']:
                                try:
                                    fields['Socket'] = ClientsManager.PlayersList[plr['id'][1]]['Socket']
                                    Messaging.sendMessageByID(24124, fields, plr['id'][1], calling_instance.player)
                                except:
                                    Messaging.sendMessage(24124, fields, calling_instance.player)

    def getMessageType(self):
        return 14358

    def getMessageVersion(self):
        return self.messageVersion