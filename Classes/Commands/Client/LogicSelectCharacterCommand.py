import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.ClientsManager import ClientsManager
from Database.DatabaseHandler import DatabaseHandler

class LogicSelectCharacterCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields['BrawlerID'] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data['SelectedBrawlers'][0] = fields['BrawlerID'][1]
        db_instance.updatePlayerData(player_data, calling_instance)

        for plr in ClientsManager.rooms[player_data['RoomID']-1]['players']:
            if plr['id'] == calling_instance.player.ID:
                print('[LogicSelectCharacterCommand::execute] Messaging.sendMessage using')
                player_data['RoomID'] = 0
                db_instance.updatePlayerData(player_data, calling_instance)
                fields["Socket"] = calling_instance.client
                Messaging.sendMessage(24124, fields, calling_instance.player)
            else:
                print('[LogicSelectCharacterCommand::execute] Messaging.sendMessageByID using')
                fields['Socket'] = ClientsManager.PlayersList[plr['id'][1]]['Socket']
                Messaging.sendMessageByID(24124, fields, plr['id'][1], calling_instance.player)

    def getCommandType(self):
        return 525