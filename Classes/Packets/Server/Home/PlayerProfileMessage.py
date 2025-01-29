from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.PlayerProfile import PlayerProfile
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        playerData = db_instance.getPlayer(fields["PlayerID"])

        self.writeVLong(fields["PlayerID"][0], fields["PlayerID"][1])
        self.writeDataReference(16, playerData['favoriteBrawler']) # FavoriteBrawler

        self.writeVInt(len(playerData['OwnedBrawlers']))
        for brawler in playerData['OwnedBrawlers']:
            print(brawler)
            self.writeDataReference(16, brawler)
            self.writeDataReference(0)
            self.writeVInt(playerData['OwnedBrawlers'][brawler]['Trophies']) # Trophies
            self.writeVInt(playerData['OwnedBrawlers'][brawler]['HighestTrophies']) # Highest Trophies
            self.writeVInt(playerData['OwnedBrawlers'][brawler]["PowerLevel"]) # Power Level
            self.writeVInt(0) # 
        
        self.writeVInt(4)
        self.writeDataReference(20, 244444)
        self.writeDataReference(24, 6974) # Points Ranked Battle
        self.writeDataReference(25, 1337) # Record Points Ranked Battle
        self.writeDataReference(27, 1488) # Year create of account

        self.writeString(playerData['Name'])  #PlayerInfo
        self.writeVInt(100)
        self.writeVInt(28000000 + playerData['Thumbnail'])
        self.writeVInt(43000000 + playerData['Namecolor'])
        self.writeVInt(43000000)

        self.writeBoolean(False)

        self.writeString("hello world")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(29, 0)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeDataReference(0)

        self.writeBoolean(False) #alliance

        self.writeDataReference(25, 0) #alliance role
        self.writeVInt(1) # Ranks

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion