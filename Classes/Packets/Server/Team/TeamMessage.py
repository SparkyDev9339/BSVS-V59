from Classes.Packets.PiranhaMessage import PiranhaMessage

from Classes.ClientsManager import ClientsManager
from Database.DatabaseHandler import TeamDatabaseHandler, DatabaseHandler
import json

class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)
        
        self.writeVInt(0) # Room Type
        self.writeBoolean(True)
        self.writeVInt(3)

        self.writeLong(0, ClientsManager.rooms[playerData['RoomID']-1]['roomID']) # TeamID

        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeDataReference(15, ClientsManager.rooms[playerData['RoomID']-1]['map_id']) # Map
        
        self.writeBoolean(False) # BattlePlayerMap
        
        self.writeVInt(len(ClientsManager.rooms[playerData['RoomID']-1]['players']))  # Players Array
        for plr in ClientsManager.rooms[playerData['RoomID']-1]['players']:
            player_data = db_instance.getPlayer(plr['id'])
            brawlerID = player_data['SelectedBrawlers'][0]
            self.writeBoolean(plr['isOwner'])  # Owner
            self.writeLong(plr['id'][0], plr['id'][1]) # Player ID
            self.writeDataReference(16, player_data['SelectedBrawlers'][0]) # Brawler
            self.writeDataReference(29, player_data['SelectedSkins'][str(brawlerID)]) # Brawler Skin
            self.writeVInt(0) # ?
            self.writeVInt(player_data['OwnedBrawlers'][str(brawlerID)]['Trophies']) # Brawler Trophies
            self.writeVInt(player_data['OwnedBrawlers'][str(brawlerID)]['HighestTrophies']) # Brawler Trophies for Rank
            self.writeVInt(player_data['OwnedBrawlers'][str(brawlerID)]['PowerLevel']) # Brawler Level
            self.writeVInt(3) # Player State
            self.writeBoolean(False) # Ready
            self.writeVInt(0) # Team
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
        	
            self.writeString(player_data['Name']) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000 + player_data['Thumbnail']) # Player Thumbnail
            self.writeVInt(43000000 + player_data['Namecolor']) # Player Name Color
            self.writeVInt(-1) # Player Gradient Name Color
            self.writeDataReference(0, 0) # Starpower
            self.writeDataReference(0, 0) # Gadget
            self.writeDataReference(0, 0) # Gear
            self.writeDataReference(0, 0) # Gear
            self.writeDataReference(0, 0)
            self.writeDataReference(0, 0)
            self.writeVInt(0)
        
        self.writeVInt(0) # Invite Players
        self.writeVInt(0) # Team Join Request
        self.writeVInt(0) # Bot Slots Disabled
        for x in range(0):
            self.writeVInt(x+ 1)
        self.writeBoolean(False) # Text Chat Enabled
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0) # Modifiers
        for x in range(0):
            self.writeVInt(1) # Modifier ID
        

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion