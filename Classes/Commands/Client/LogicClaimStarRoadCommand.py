import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters

class LogicClaimStarRoadCommand(LogicCommand):
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

        brawlerName = Characters.getBrawlerNameByID(fields['BrawlerID'][1])
        cardID = Cards.getCardIdByName(brawlerName)

        all_brawlers = []
        rare = [1, 2, 3, 6, 8, 10, 13, 24]
        super_rare = [7, 9, 18, 19, 22, 25, 27, 34, 61, 4]
        epic = [14, 15, 16, 20, 26, 29, 30, 36, 39, 43, 45, 46, 48, 50, 51, 53, 58, 60, 65, 68, 69, 77, 79, 82]
        mythic = [11, 17, 21, 35, 31, 32, 37, 41, 42, 44, 47, 49, 54, 55, 57, 59, 62, 64, 66, 67, 71, 72, 73, 74, 75, 78, 81, 83, 84]
        legendary = [5, 12, 23, 28, 38, 40, 52, 63, 70, 76, 80, 85]

        if fields['BrawlerID'][1] in rare:
            CreditsNeeded = 160
        if fields['BrawlerID'][1] in super_rare:
            CreditsNeeded = 430
        if fields['BrawlerID'][1] in epic:
            CreditsNeeded = 925
        if fields['BrawlerID'][1] in mythic:
            CreditsNeeded = 1900
        if fields['BrawlerID'][1] in legendary:
            CreditsNeeded = 3800

        brawler = {'CardID': cardID, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}

        player_data['RareTokens'] = player_data['RareTokens'] - CreditsNeeded

        player_data['OwnedBrawlers'][fields['BrawlerID'][1]] = brawler

        ja = fields["BrawlerID"][1]

        if ja != 0:
            player_data["UnlockingBrawler"] = player_data["UnlockingBrawler"] + 1
        if ja == 85:
            player_data["UnlockingBrawler"] = 0
        if player_data["UnlockingBrawler"] == 32:
            player_data["UnlockingBrawler"] = player_data["UnlockingBrawler"] + 2
        if player_data["UnlockingBrawler"] == 55:
            player_data["UnlockingBrawler"] = player_data["UnlockingBrawler"] + 2

        """if ja == 8:
            player_data["UnlockingBrawler"] = 1
        if ja == 1:
            player_data["UnlockingBrawler"] = 2
        if ja == 2:
            player_data["UnlockingBrawler"] = 3
        if ja == 3:
            player_data["UnlockingBrawler"] = 4
        if ja == 4:
            player_data["UnlockingBrawler"] = 6
        if ja == 6:
            player_data["UnlockingBrawler"] = 7
        if ja == 7:
            player_data["UnlockingBrawler"] = 9
        if ja == 9:
            player_data["UnlockingBrawler"] = 10
        if ja == 10:
            player_data["UnlockingBrawler"] = 11
        if ja == 11:
            player_data["UnlockingBrawler"] = 12
        if ja == 12:
            player_data["UnlockingBrawler"] = 13
        if ja == 13:
            player_data["UnlockingBrawler"] = 14
        if ja == 14:
            player_data["UnlockingBrawler"] = 15
        if ja == 15:
            player_data["UnlockingBrawler"] = 16
        if ja == 16:
            player_data["UnlockingBrawler"] = 17
        if ja == 17:
            player_data["UnlockingBrawler"] = 18
        if ja == 18:
            player_data["UnlockingBrawler"] = 19
        if ja == 19:
            player_data["UnlockingBrawler"] = 20
        if ja == 20:
            player_data["UnlockingBrawler"] = 21
        if ja == 21:
            player_data["UnlockingBrawler"] = 22
        if ja == 22:
            player_data["UnlockingBrawler"] = 23
        if ja == 23:
            player_data["UnlockingBrawler"] = 24
        if ja == 24:
            player_data["UnlockingBrawler"] = 25
        if ja == 25:
            player_data["UnlockingBrawler"] = 26
        if ja == 26:
            player_data["UnlockingBrawler"] = 27
        if ja == 27:
            player_data["UnlockingBrawler"] = 28
        if ja == 28:
            player_data["UnlockingBrawler"] = 29
        if ja == 29:
            player_data["UnlockingBrawler"] = 30
        if ja == 30:
            player_data["UnlockingBrawler"] = 31
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32
        if ja == 31:
            player_data["UnlockingBrawler"] = 32"""
        db_instance.updatePlayerData(player_data, calling_instance)

        db_instance.updatePlayerData(player_data, calling_instance)

        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 227}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields)

    def getCommandType(self):
        return 562
    