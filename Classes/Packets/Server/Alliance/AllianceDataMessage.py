from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
import json

class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        db_instance = DatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])
        db_instance.loadAccount(player, player.ID)
        
        if player.AllianceID == fields["AllianceID"]:
            self.writeBoolean(False) # Show Online Players
        else:
            self.writeBoolean(False) # Show Online Players

        self.writeLong(clubData["HighID"], clubData["LowID"]) # alliance ID
        self.writeString(clubData["Name"]) # alliance name
        self.writeDataReference(8, clubData["BadgeID"]) # alliance icon
        self.writeVInt(clubData["Type"]) # type
        self.writeVInt(len(clubData["Members"])) # member count
        self.writeVInt(clubdb_instance.getTotalTrophies(clubData)) # total trophies
        self.writeVInt(clubData["TrophiesRequired"]) # minimum trophies to enter
        self.writeDataReference(0, 0) # idk lol
        self.writeString('RU') # location
        self.writeVInt(1) # people online
        self.writeVInt(1)
        self.writeBoolean(clubData["FamilyFriendly"]) # isFamilyFriendly
        self.writeVInt(0)
        self.writeVInt(1)
        for i in range(1):
            self.writeVInt(11)
            self.writeVInt(11)

        self.writeVInt(1)
        for i in range(1):
            self.writeVInt(11)
            self.writeVInt(11)

        self.writeString(clubData["Description"])

        self.writeVInt(len(clubData["Members"]))
        for i in clubData["Members"]:
            memberData = clubData['Members'][str(i)]
            print(memberData)
            playerData = json.loads(db_instance.getPlayerEntry([memberData['HighID'], memberData['LowID']])[2])
            self.writeLong(memberData['HighID'], memberData['LowID'])
            self.writeVInt(memberData['Role']) # Role
            self.writeVInt(playerData['Trophies']) # Trophies
            self.writeVInt(0)
            self.writeVInt(1) # last connected time seconds ?
        
            highestPowerLeagueRank = 0
        
            self.writeVInt(highestPowerLeagueRank)
            if highestPowerLeagueRank != 0:
                self.writeVInt(1) 
            self.writeBoolean(False) # boolean always false?

            self.writeString(playerData['Name']) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000 + playerData['Thumbnail']) # Player Thumbnail
            self.writeVInt(43000000 + playerData['Namecolor']) # Player Name Color
            self.writeVInt(46000000 + playerData['Namecolor'])

            self.writeVInt(0) # most people have it -1 but some with something
            self.writeBoolean(False) #
            week = 3 
            self.writeVInt(week)
            if week != 0: # club league week number?
               self.writeVInt(3) # day
               self.writeVInt(18) # total club trophies earned
               self.writeVInt(0) # event day club trophies earned
               self.writeVInt(8) # total tickets used
               self.writeVInt(0) # event day tickets used
               self.writeVInt(6) # event day max tickets
               self.writeVInt(6) # event day tickets left
               self.writeVInt(0) # event day player ranking
               self.writeBoolean(True) # everyone have it to true
            self.writeVInt(0)
            self.writeVInt(0) # a1 + 128

            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(0)
                self.writeVInt(1)
                self.writeVInt(2)

            self.writeVInt(0)
            for i in range(0):
                self.writeVInt(1)
                self.writeVInt(1)
            self.writeVInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion