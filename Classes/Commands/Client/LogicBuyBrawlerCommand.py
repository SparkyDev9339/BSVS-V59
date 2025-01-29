import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters

class LogicBuyBrawlerCommand(LogicCommand):
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
        fields['Unk1'] = calling_instance.readDataReference
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])

        brawlerName = Characters.getBrawlerNameByID(fields['BrawlerID'][1])
        cardID = Cards.getCardIdByName(brawlerName)

        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID
        #Messaging.sendMessage(24111, fields)

    def getCommandType(self):
        return 560
    