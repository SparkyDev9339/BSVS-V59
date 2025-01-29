from Classes.Packets.PiranhaMessage import PiranhaMessage

from Database.DatabaseHandler import DatabaseHandler

class LeaderboardMessage(PiranhaMessage):
    
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        fields = {}
        db = DatabaseHandler()
        players = db.getSorted()
        playerscount = len(db.getAll())
        
        self.writeBoolean(1) # Leaderboard Variation
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()

        self.writeVInt(playerscount) # Players Count
        for data in players:
            self.writeVInt(data["ID"][0]) # highID
            self.writeVInt(data["ID"][1]) # lowID
            
            self.writeVInt(1)
            self.writeVInt(data["Trophies"]) # Trophies
            
            self.writeVInt(1)
            self.writeString("") # Club Name
            
            self.writeString(data["Name"]) # Player Name
            self.writeVInt(0)
            self.writeVInt(28000000 + data["Thumbnail"]) # Player Thumbnail
            self.writeVInt(43000000 + data["Namecolor"]) # Player Name Color Gradient (brawl pass)
            self.writeVInt(43000000 + data["Namecolor"]) # Player Name Color
            self.writeVInt(0) #UNK


        self.writeVInt(player.Trophies)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("RU")

        
    def decode(self):
        return {}

    def execute(message, calling_instance, cryptoInit, fields):
        pass

    def getMessageType(self):
        return 24403

    def getMessageVersion(self):
        return self.messageVersion