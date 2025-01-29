import json
import sqlite3
import traceback
from Classes.Files.Classes.Regions import Regions

class DatabaseHandler():
    def __init__(self):
        self.conn = sqlite3.connect("Database/Files/player.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (ID int, Token text, Data json)""")
        except sqlite3.OperationalError:
            pass
        except Exception:
            print(traceback.format_exc())

    def createAccount(self, data):
        try:
            self.cursor.execute("INSERT INTO main (ID, Token, Data) VALUES (?, ?, ?)", (data["ID"][1], data["Token"], json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())

    def getAll(self):
        self.playersId = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                self.playersId.append(self.db[i][0])
            return self.playersId
        except Exception:
            print(traceback.format_exc())

    def getLeaders(self):
        self.playersID = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                self.playersID.append(self.db[i][0])
            return self.playersID
        except Exception:
            print(traceback.format_exc())


    def getPlayer(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return json.loads(self.cursor.fetchall()[0][2])
        except Exception:
            print(traceback.format_exc())

    def getPlayerEntry(self, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            return self.cursor.fetchall()[0]
        except IndexError:
            pass
        except Exception:
            print(traceback.format_exc())

    def loadAccount(self, player, plrId):
        try:
            self.cursor.execute("SELECT * from main where ID=?", (plrId[1],))
            playerData = json.loads(self.cursor.fetchall()[0][2])
            player.ID = playerData["ID"]
            player.Name = playerData["Name"]
            player.AllianceID = playerData["AllianceID"]
            player.RoomID = playerData['RoomID']
            player.Registered = playerData["Registered"]
            player.banned = playerData['banned']
            player.Vip = playerData["Vip"]
            player.Thumbnail = playerData["Thumbnail"]
            player.Namecolor = playerData["Namecolor"]
            player.Region = playerData["Region"]
            player.ContentCreator = playerData["ContentCreator"]
            player.Coins = playerData["Coins"]
            player.Gems = playerData["Gems"]
            player.StarPoints = playerData["StarPoints"]

            player.ChromaticTokens = playerData["ChromaticTokens"]
            player.RareTokens = playerData["RareTokens"]
            player.Blings = playerData['Blings']
            player.UnlockingBrawler = playerData['UnlockingBrawler']
            player.PowerPoints = playerData['PowerPoints']

            player.Trophies = playerData["Trophies"]
            player.HighestTrophies = playerData["HighestTrophies"]
            player.TrophyRoadTier = playerData["TrophyRoadTier"]
            player.Experience = playerData["Experience"]
            player.Level = playerData["Level"]
            player.Tokens = playerData["Tokens"]
            player.TokensDoubler = playerData["TokensDoubler"]
            # BrawlPass
            player.BrawlPassFreeLevel = playerData["BrawlPassFreeLevel"]
            player.BrawlPassLevel = playerData["BrawlPassLevel"]
            player.BrawlPassPlusLevel = playerData["BrawlPassPlusLevel"]

            player.RewardTrackType = playerData['RewardTrackType']
            player.RewardForRank = playerData['RewardForRank']
            player.BrawlPassSeason = playerData['BrawlPassSeason']
            player.BrawlPassBuy = playerData['BrawlPassBuy']
            player.BPTokens = playerData['BPTokens']
            # Profiles
            player.favoriteBrawler = playerData["favoriteBrawler"]
            player.battleIcon = playerData["battleIcon"]
            player.battleIcon1 = playerData["battleIcon1"]
            player.battlePin = playerData["battlePin"]
            player.battleTitke = playerData["battleTitle"]
            player.threeXthreeWins = playerData["threeXthreeWins"]
            player.duoWins = playerData["duoWins"]
            player.soloWins = playerData["soloWins"]
            # Profiles End
            player.IntValueEntry = playerData["IntValueEntry"]
            player.SelectedSkins = playerData["SelectedSkins"]
            player.SelectedBrawlers = playerData["SelectedBrawlers"]
            player.OwnedPins = playerData["OwnedPins"]
            player.OwnedThumbnails = playerData["OwnedThumbnails"]
            player.OwnedSprays = playerData["OwnedSprays"]
            player.OwnedSkins = playerData["OwnedSkins"]
            player.OwnedBrawlers = playerData["OwnedBrawlers"]
            player.NotificationFactory = playerData['NotificationFactory']
        except Exception:
            print(traceback.format_exc())

    def updatePlayerData(self, data, calling_instance):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE ID=?", (json.dumps(data, ensure_ascii=0), calling_instance.player.ID[1]))
            self.conn.commit()
            self.loadAccount(calling_instance.player, calling_instance.player.ID)
        except Exception:
            print(traceback.format_exc())

    def playerExist(self, loginToken, loginID):
        try:
            if loginID[1] in self.getAll():
                if loginToken != self.getPlayerEntry(loginID)[1]:
                    return False
                return True
            return False
        except Exception:
            print(traceback.format_exc())

    def getSorted(self):
        a = []
        self.cursor.execute("SELECT * FROM main")
        this = self.cursor.fetchall()
        for db in this:
            data = json.loads(db[2])
            a.append(data)
        a = sorted(a, key=lambda x:x["Trophies"], reverse=True)
        return a
    
class TeamDatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("Database/Files/team.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (LowID integer, Data json)""")
        except:
            pass

    def createTeam(self, lowID, data):
        try:
            self.cursor.execute("INSERT INTO main (LowID, Data) VALUES (?, ?)",
                                (lowID, json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception as e:
            print(e)

    def deleteTeam(self, lowID):
        try:
            self.cursor.execute("DELETE FROM main where LowID=?", (lowID,))
            self.conn.commit()
        except Exception as e:
            print(e)

    def getDefaultPlayersData(self, player, king):
        return {'HighID': player.HighID, 'LowID': player.LowID, 'Name': player.Name, 'brawlerID': player.SelectedBrawlers[0], 'skinID': player.SelectedSkins, 'King': king, 'Trophies': player.trophies, 'NameColor': player.nameColor, 'Thumbnail': player.thumbnail}
    

    def getMembersSorted(self, clubdata):
        try:
            return sorted(clubdata['Members'].items(), key = lambda x: x[1]['Trophies'], reverse=True)
        except Exception as e:
            print(e)
    
    def updateTeamData(self, data, lowID):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE LowID=?", (json.dumps(data, ensure_ascii=0), lowID))
            self.conn.commit()
        except Exception as e:
            print(e)

    def getTeamWithLowID(self, low):
        try:
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

class ClubDatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("Database/Files/club.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (LowID integer, Data json)""")
        except:
            pass

    def createClub(self, lowID, data):
        try:
            self.cursor.execute("INSERT INTO main (LowID, Data) VALUES (?, ?)",
                                (lowID, json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception as e:
            print(e)

    def deleteClub(self, lowID):
        try:
            self.cursor.execute("DELETE FROM main where LowID=?", (lowID,))
            self.conn.commit()
        except Exception as e:
            print(e)


    def getAllClub(self):
        clubs = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                clubs.append(json.loads(self.db[i][1]))
            return clubs
        except Exception as e:
            print(e)

    def getAllClubByRegion(self, regionID):
        clubs = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                dataLoaded = json.loads(self.db[i][1])
                if dataLoaded['RegionID'] == Regions.getIDByRegion(self, regionID):
                    clubs.append(dataLoaded)
            return clubs
        except Exception as e:
            print(traceback.format_exc())

    def getDefaultMembersData(self, player, role):
        return {'HighID': player.HighID, 'LowID': player.LowID, 'Name': player.Name, 'Role': role, 'Trophies': player.trophies, 'NameColor': player.nameColor, 'Thumbnail': player.thumbnail}

    def getDefaultMessageData(self, eventType, streamType, lastID, playerID, playerName, playerRole, target={}, msgData="", premadeID=-1, messageDataID=-1):
        return {'StreamType': eventType, 'EventType': streamType, 'StreamID': lastID, 'PlayerID': playerID, 'PlayerName': playerName, 'PlayerRole': playerRole, 'Message': msgData, 'Target': target, 'PremadeID': premadeID, 'MessageDataID': messageDataID}

    def getClubWithLowID(self, low):
        try:
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def getMembersSorted(self, clubdata):
        try:
            return sorted(clubdata['Members'].items(), key = lambda x: x[1]['Trophies'], reverse=True)
        except Exception as e:
            print(e)

    def getMemberWithLowID(self, clubData, playerLowID):
        try:
            return clubData["Members"][str(playerLowID)]
        except Exception as e:
            print(e)

    def getTotalTrophies(self, clubData):
        try:
            totalTrophies = 0
            for i in clubData["Members"].values():
                totalTrophies += i['Trophies']
            return totalTrophies
        except Exception as e:
            print(e)

    def LoadAccount(self, low, player):
        try:
            self.player = player
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            self.players = self.cursor.fetchall()
            self.players = json.loads(self.players[0][2])
        except Exception as e:
            print(e)

    def updateClubData(self, data, lowID):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE LowID=?", (json.dumps(data, ensure_ascii=0), lowID))
            self.conn.commit()
        except Exception as e:
            print(e)