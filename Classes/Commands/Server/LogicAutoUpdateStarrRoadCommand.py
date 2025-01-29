from Classes.Commands.LogicServerCommand import LogicServerCommand
from Database.DatabaseHandler import DatabaseHandler
import json

class LogicAutoUpdateStarrRoadCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        #x = fields["UnlockingBrawler"]
        rare = [1, 2, 3, 6, 8, 10, 13, 24]
        super_rare = [4, 7, 9, 18, 19, 22, 25, 27, 34, 61]
        epic = [14, 15, 16, 20, 26, 29, 30, 36, 43, 45, 48, 50, 58, 69]
        mythic = [11, 17, 21, 35, 31, 32, 37, 42, 47, 64, 67, 71]
        legendary = [5, 12, 23, 28, 40, 52, 63]
        
        
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(fields["PlayerID"])[2])
        
        x = player_data["UnlockingBrawler"]
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1) #vint alvays 1!!!
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        if player_data["UnlockingBrawler"] != 0:
            self.writeBoolean(True) #brawler 1 in starr road array
        
            self.writeVInt(1) #brawlers count
        
            self.writeDataReference(16, player_data["UnlockingBrawler"])
            #credit cost start
            if x in rare:
                self.writeVInt(160)
            elif x in super_rare:
                self.writeVInt(430)
            elif x in epic:
                self.writeVInt(925)
            elif x in mythic:
                self.writeVInt(1900)
            elif x in legendary:
                self.writeVInt(3800)
            else:
                self.writeVInt(1)
            #credit cost end
            	
            #gems cost start
            if x in rare:
                self.writeVInt(29)
            elif x in super_rare:
                self.writeVInt(79)
            elif x in epic:
                self.writeVInt(169)
            elif x in mythic:
                self.writeVInt(359)
            elif x in legendary:
                self.writeVInt(699)
            else:
                self.writeVInt(1)
            #gems cost end
            
            self.writeVInt(0)
            self.writeVInt(player_data["RareTokens"])
            self.writeVInt(0)
            self.writeVInt(0)
        else:
            self.writeBoolean(False) #brawler 1 in starr road array
            
        self.writeBoolean(True) #brawler dalee in starr road array
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 227