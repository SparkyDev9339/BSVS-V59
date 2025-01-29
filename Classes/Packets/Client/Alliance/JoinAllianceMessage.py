from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json

class JoinAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AllianceID"] = self.readLong()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])
        State = 0
        Kicked = None
        for x in clubData["ChatData"]:
        	if x['StreamType'] == 3:
        		if x['PlayerID'] == player_data["ID"]:
        			State = x['State']
        	elif x['StreamType'] == 4:
        		if x['EventType'] == 1:
        			if x['Target']['ID'] == player_data["ID"]:
        				Kicked = True
        if len(clubData["Members"]) < 30:
        	if clubData["TrophiesRequired"] > player_data["Trophies"]:
        		fields["Socket"] = calling_instance.client
        		fields["ResponseID"] = 45
        		Messaging.sendMessage(24333, fields)
        	elif State == 3:
        		fields["Socket"] = calling_instance.client
        		fields["ResponseID"] = 46
        		Messaging.sendMessage(24333, fields)
        	elif Kicked == True:
        		fields["Socket"] = calling_instance.client
        		fields["ResponseID"] = 46
        		Messaging.sendMessage(24333, fields)
        	else:
        		player_data["AllianceID"] = fields["AllianceID"]
        		clubData["Members"][str(calling_instance.player.ID[1])] = {'HighID': calling_instance.player.ID[0], 'LowID': calling_instance.player.ID[1], 'Role': 1, 'Trophies': calling_instance.player.Trophies}
        		db_instance.updatePlayerData(player_data, calling_instance)
        		clubdb_instance.updateClubData(clubData, fields["AllianceID"][1])
        		LastMessageID = len(clubData["ChatData"])
        		Role = clubData["Members"][str(player_data["ID"][1])]["Role"]
        		message = {
        		'StreamType': 4,
        		'StreamID': [0, LastMessageID + 1],
        		'PlayerID': calling_instance.player.ID,
        		'PlayerName': calling_instance.player.Name,
        		'PlayerRole': Role,
        		'EventType': 3,
        		'Target': {'ID': calling_instance.player.ID, 'Name': calling_instance.player.Name}
        		}
        		clubData["ChatData"].append(message)
        		clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        		allSockets = ClientsManager.GetAll()
        		for x in clubData["Members"]:
        			if int(x) in allSockets:
        				fields["Socket"] = allSockets[int(x)]["Socket"]
        				Messaging.sendMessage(24312, fields, calling_instance.player)
        		
        		fields["Socket"] = calling_instance.client
        		fields["ResponseID"] = 40
        		Messaging.sendMessage(24333, fields)
        		fields["HasClub"] = True
        		Messaging.sendMessage(24399, fields, calling_instance.player)
        		Messaging.sendMessage(24311, fields, calling_instance.player)
        		Messaging.sendMessage(22161, fields, calling_instance.player)
        else:
        	fields["Socket"] = calling_instance.client
        	fields["ResponseID"] = 42
        	Messaging.sendMessage(24333, fields)
        

    def getMessageType(self):
        return 14305

    def getMessageVersion(self):
        return self.messageVersion