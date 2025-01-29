from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from time import time

from Database.DatabaseHandler import DatabaseHandler
import json

class LogicViewInboxNotificationCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Index"] = calling_instance.readVInt()
        fields["Unk1"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])

        using = 1

        CsvID = 0
        CsvID1 = 0
        RewardID = 0
        RewardCount = 1
        if using:
            Notification = player_data['NotificationFactory']
            for notif in player_data['NotificationFactory']:
                if Notification[notif]['Index'] == fields['Index']:
                    notifIndex = notif
            if Notification[notifIndex]['ID'] == 89:
                RewardID = 8
                RewardCount = Notification[notifIndex]['ResourceCount']
                player_data['Gems'] = player_data['Gems'] + RewardCount
            if Notification[notifIndex]['ID'] == 64:
                if Notification[notifIndex]['ResourceID'] == 1:
                    RewardID = 7
                if Notification[notifIndex]['ResourceID'] == 3:
                    RewardID = 1
                    CsvID = 29
                    CsvID1 = Notification[notifIndex]['SkinID']
                if Notification[notifIndex]['ResourceID'] == 4:
                    RewardID = 9
                    CsvID = 16
                    CsvID1 = Notification[notifIndex]['BrawlerID']
                if Notification[notifIndex]['ResourceID'] == 16:
                    RewardID = 8
                if Notification[notifIndex]['ResourceID'] == 38:
                    RewardID = 22
                    
                if Notification[notifIndex]['ResourceID'] == 45:
                    RewardID = 25
                RewardCount = Notification[notifIndex]['ResourceCount']
            if Notification[notifIndex]['ID'] == 72:
                RewardID = 9
                CsvID = 52
                CsvID1 = Notification[notifIndex]['SkinID']
            if Notification[notifIndex]['ID'] == 93:
                RewardID = 1
                CsvID = 16
                CsvID1 = Notification[notifIndex]['BrawlerID']
            if Notification[notifIndex]['ID'] == 94:
                RewardID = 9
                CsvID = 29
                CsvID1 = Notification[notifIndex]['SkinID']
                #player_data["OwnedSkins"].append(CsvID1)
            player_data['RewardTrackType'] = 0
            player_data['BrawlPassSeason'] = 0
            player_data['RewardForRank'] = 0

            player_data['NotificationFactory'][notifIndex]['Read'] = True

            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': RewardCount, 'DataRef': [CsvID, CsvID1], 'RewardID': RewardID}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)

            db_instance.updatePlayerData(player_data, calling_instance)

        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID 
        Messaging.sendMessage(24111, fields)
        

    def getCommandType(self):
        return 528