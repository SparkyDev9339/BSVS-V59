from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Logic.LogicStarrDropData import starrDropOpening
from datetime import datetime
from Database.DatabaseHandler import DatabaseHandler

import json
import time
import random

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        # Sorry Bro for more pou code
        Shop = json.loads(open("JSON/Shop.json", 'r').read())
        Events = json.loads(open("JSON/Events.json", 'r').read())

        nowTime = time.time() + 3600 * 4
        EventIndex = 0
        showDownMap = 0
        for EventData in Events['Events']:
            if int(EventData['TimeToEnd']) <= int(nowTime):
                with open('Events.json') as f:
                    data = json.load(f)
                if data['Events'][EventIndex]['Slot'] == 1:
                    data['Events'][EventIndex]['TimeToEnd'] = time.time() + 3600 * 4 + 86400
                    data['Events'][EventIndex]['MapID'] = random.choice([739, 762, 763, 808])
                if data['Events'][EventIndex]['Slot'] == 2:
                    data['Events'][EventIndex]['TimeToEnd'] = time.time() + 3600 * 4 + 43200
                    data['Events'][EventIndex]['MapID'] = random.choice([731, 774, 776, 814])
                    showDownMap = data['Events'][EventIndex]['MapID']
                if data['Events'][EventIndex]['Slot'] == 4:
                    data['Events'][EventIndex]['TimeToEnd'] = time.time() + 3600 * 4 + 14400
                    data['Events'][EventIndex]['MapID'] = random.choice([637, 638, 677, 678])
                if data['Events'][EventIndex]['Slot'] == 5:
                    data['Events'][EventIndex]['TimeToEnd'] = time.time() + 3600 * 4 + 86400
                    data['Events'][EventIndex]['MapID'] = showDownMap + 1
                if data['Events'][EventIndex]['Slot'] == 4:
                    data['Events'][EventIndex]['TimeToEnd'] = time.time() + 3600 * 4 + 86400
                    data['Events'][EventIndex]['MapID'] = random.choice([638, 639, 640, 719])
                with open('Events.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            EventIndex += 1

        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)

        self.writeVInt(1688816070)
        self.writeVInt(1191532375)
        self.writeVInt(2023189)
        self.writeVInt(73530)

        self.writeVInt(player.Trophies + 5000)
        self.writeVInt(player.HighestTrophies + 5000)
        self.writeVInt(player.HighestTrophies + 5000) 
        self.writeVInt(player.TrophyRoadTier + 200)
        self.writeVInt(player.Experience)
        self.writeDataReference(28, player.Thumbnail)
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(26)
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(len(player.SelectedSkins))
        for brawlerID in player.SelectedSkins:
            self.writeDataReference(29, player.SelectedSkins[str(brawlerID)])

        self.writeVInt(0)

        self.writeVInt(0)
        
        self.writeVInt(len(player.OwnedSkins))
        for x in player.OwnedSkins:
            self.writeDataReference(29, x)

        self.writeVInt(1080)
        for i in range(1080):
            self.writeDataReference(29, i)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeBoolean(True)
        self.writeVInt(115)
        self.writeVInt(335442)
        self.writeVInt(1001442)
        self.writeVInt(5778642) 
        self.writeVInt(0)

        self.writeVInt(120)
        self.writeVInt(200)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(Shop["Offers"])) # Shop Offers
        for shopData in Shop["Offers"]:
            self.writeVInt(len(shopData['Rewards'])) # RewardCount
            for rewardData in shopData['Rewards']:
                self.writeVInt(rewardData['ItemType'])  # ItemType
                self.writeVInt(rewardData['Amount']) # Amount
                self.writeDataReference(rewardData['CsvID'][0], rewardData['CsvID'][1])  # CsvID
                self.writeVInt(rewardData['SkinID']) # SkinID

            self.writeVInt(shopData['Currency']) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
            self.writeVInt(shopData['Cost']) # Cost
            self.writeVInt(0) # Time
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False) # Daily Offer
            self.writeVInt(0) # Old price
            self.writeString(shopData['Text']) # Text
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeString("offer_sushi") # Background
            self.writeVInt(0)
            self.writeBoolean(False) # This purchase is already being processed
            self.writeVInt(0) # Type Benefit
            self.writeVInt(0) # Benefit
            self.writeString()
            self.writeBoolean(False) # One time offer
            self.writeBoolean(False) # Claimed
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
        
        self.writeVInt(20)
        self.writeVInt(1428)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeVInt(30)

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, player.SelectedBrawlers[0]) # selected brawler

        self.writeString(player.Region) # location
        self.writeString(player.ContentCreator) # supported creator

        self.writeVInt(22)
        self.writeDataReference(2, 1)  # Unknown
        self.writeDataReference(3, player.IntValueEntry['TokensGained'])  # Tokens Gained
        self.writeDataReference(4, player.IntValueEntry['TrophiesGained'])  # Trophies Gained
        self.writeDataReference(6, player.IntValueEntry['DemoAccount'])  # Demo Account
        self.writeDataReference(7, player.IntValueEntry['InvitesBlock'])  # Invites Blocked
        self.writeDataReference(8, player.IntValueEntry['StarPointsGained'])  # Star Points Gained
        self.writeDataReference(9, 1)  # Show Star Points
        self.writeDataReference(10, 0)  # Power Play Trophies Gained
        self.writeDataReference(12, 1)  # Unknown
        self.writeDataReference(14, 0)  # Coins Gained
        self.writeDataReference(15, player.IntValueEntry['SocialAge'])  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeDataReference(16, 1)
        self.writeDataReference(17, 0)  # Team Chat Muted
        self.writeDataReference(18, 1)  # Esport Button
        self.writeDataReference(19, 0)  # Champion Ship Lives Buy Popup
        self.writeDataReference(20, player.IntValueEntry['GemsGained'])  # Gems Gained
        self.writeDataReference(21, 1)  # Looking For Team State
        self.writeDataReference(22, 1)
        self.writeDataReference(23, 0)  # Club Trophies Gained
        self.writeDataReference(24, 1)  # Have already watched club league stupid animation
        self.writeDataReference(32447, 28)
        self.writeDataReference(16, 5)

        self.writeVInt(0)

        Free32LVL = 0
        Free64LVL = 0
        Free96LVL = 0

        Pass32LVL = 0
        Pass64LVL = 0
        Pass96LVL = 0

        for LVL in player.BrawlPassFreeLevel:
            if LVL < 30:
                Free32LVL += (2**(LVL + 2))
            if LVL > 30:
                Free64LVL += (2**(LVL-30))
            if LVL > 61:
                Free96LVL += (1**(LVL-61))
        
        for LVL in player.BrawlPassLevel:
            if LVL < 30:
                Pass32LVL += (2**(LVL + 2))
            if LVL > 29:
                Pass64LVL += (2**(LVL-30))
            if LVL > 60:
                Pass96LVL += (1**(LVL-61))
        
        if player.BrawlPassBuy == 0:
            BrawlPassActive = False
            BrawlPassPlusActive = False
        if player.BrawlPassBuy == 1:
            BrawlPassActive = True
            BrawlPassPlusActive = False
        if player.BrawlPassBuy == 2:
            BrawlPassActive = True
            BrawlPassPlusActive = True

        # BrawlPassSeasonData::encode
        self.writeVInt(1)
        for season in range(1):
            self.writeVInt(34)
            self.writeVInt(player.BPTokens)
            self.writeBoolean(BrawlPassActive) # BrawlPass buy
            self.writeVInt(0)
            self.writeBoolean(False)

            self.writeBoolean(True)
            self.writeInt(Pass32LVL)
            self.writeInt(Pass64LVL)
            self.writeInt(Pass96LVL)
            self.writeInt(0)

            self.writeBoolean(True)
            self.writeInt(Free32LVL)
            self.writeInt(Free64LVL)
            self.writeInt(Free96LVL)
            self.writeInt(0)

            self.writeBoolean(BrawlPassPlusActive) # BrawlPass + Buy
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        # BrawlPassSeasonData::encode

        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(0) 

        self.writeBoolean(True) # Vanity items
        self.writeVInt(len(player.OwnedThumbnails) + len(player.OwnedPins) + 1)
        for ThumbnailID in player.OwnedThumbnails:
            self.writeDataReference(28, ThumbnailID)
            self.writeVInt(0)
        for PinID in player.OwnedPins:
            self.writeDataReference(52, PinID)
            self.writeVInt(0)
        for i in range(1):
            self.writeDataReference(28, 186) # IconCreator
            self.writeVInt(0)


        self.writeBoolean(False) # Power league season data

        self.writeInt(0)
        self.writeVInt(0)
        self.writeDataReference(16, player.favoriteBrawler) # favoriteBrawler
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2023189)

        self.writeVInt(40) # event slot id
        for EventID in range(40):
            self.writeVInt(EventID)

        Events = json.loads(open("JSON/Events.json", 'r').read())
        EventIndex = 0

        self.writeVInt(len(Events['Events'])) # Events
        for EventData in Events['Events']:
            self.writeVInt(-1)
            self.writeVInt(EventData['Slot']) # EventSlot
            self.writeVInt(EventData['Slot']) # EventSlot
            self.writeVInt(0)
            self.writeVInt(int(EventData['TimeToEnd']) - int(nowTime))
            self.writeVInt(10) 
            self.writeDataReference(15, EventData['MapID']) # map id
            self.writeVInt(-1)
            self.writeVInt(2) # MapStatus
            self.writeString("")
            self.writeVInt(0)
            self.writeVInt(0)
            if EventData['Slot'] in [20, 21, 22, 23, 24, 35, 36]:
                self.writeVInt(EventData['ChampionShipInfo']['MaxWins']) # Max Wins
            else:
                self.writeVInt(0) # Max Wins
            self.writeVInt(0) # Modifers
            self.writeVInt(0) # Wins
            self.writeVInt(6)
            self.writeBoolean(False) # MapMaker map structure array
            self.writeVInt(0)
            self.writeBoolean(False) # Power League array entry
            self.writeVInt(0)
            self.writeVInt(0)
            if EventData['Slot'] in [20, 21, 22, 23, 24, 35, 36]:
                self.writeBoolean(True) # ChoronosTextEntry::encode
                for ChoronosTextEntry in range(1):
                    self.writeString(EventData['ChampionShipInfo']['ChoronosTextEntry'])
                    self.writeVInt(0)
            else:
                self.writeBoolean(False) # ChoronosTextEntry::encode
            self.writeBoolean(False)
            self.writeBoolean(False)
            if EventData['Slot'] in [20, 21, 22, 23, 24]:
                self.writeBoolean(True)
                for LogicGemOffer in range(1):
                    self.writeVInt(EventData['ChampionShipInfo']['LogicGemOffer']['ID'])
                    self.writeVInt(EventData['ChampionShipInfo']['LogicGemOffer']['Ammount'])
                    self.writeDataReference(EventData['ChampionShipInfo']['LogicGemOffer']['CsvID'][0], EventData['ChampionShipInfo']['LogicGemOffer']['CsvID'][1])
                    self.writeVInt(EventData['ChampionShipInfo']['LogicGemOffer']['SkinID'])
            else:
                self.writeBoolean(False) # LogicGemOffer::encode
            self.writeVInt(1)
            self.writeVInt(6)
            if EventData['Slot'] in [20, 21, 22, 23, 24, 35, 36]:
                self.writeBoolean(True) # ChronosFileEntry::encode
                for ChronosFileEntry in range(1):
                    self.writeString(EventData['ChampionShipInfo']['ChronosFileEntry']['scName'])
                    self.writeString(EventData['ChampionShipInfo']['ChronosFileEntry']['scFile'])
            self.writeBoolean(False) # ChoronosFileEntry::encode
            self.writeBoolean(False)
            self.writeVInt(-1)
            self.writeVInt(0) 
            self.writeVInt(0) 
            self.writeVInt(0) 
            self.writeBoolean(False) 
            self.writeBoolean(False) 
            self.writeBoolean(False)
            self.writeBoolean(False)
            EventIndex += 1

        self.writeVInt(0)
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800])
        ByteStreamHelper.encodeIntList(self, [30, 80, 170, 360]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [300, 880, 2040, 4680]) # Shop Coins Amount

        self.writeVInt(0)

        # IntValueEntry::encode
        self.writeVInt(6)
        for i in range(1):
            self.writeDataReference(41000117, 1) # ThemeID
            self.writeDataReference(89, 6)
            self.writeDataReference(22, 0)
            self.writeDataReference(36, 1)
            self.writeDataReference(73, 1)
            self.writeDataReference(16, 5)
        # IntValueEntry::encode end
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(0, 1) # Player ID

        player.NotificationFactory = playerData['NotificationFactory']

        self.writeVInt(len(player.NotificationFactory)) # Notification factory
        for Notification in player.NotificationFactory:
            self.writeVInt(player.NotificationFactory[str(Notification)]['ID']) # Notification ID
            self.writeInt(player.NotificationFactory[str(Notification)]['Index']) # Notification Index
            self.writeBoolean(player.NotificationFactory[str(Notification)]['Read']) # Notification Read
            self.writeInt(int(datetime.timestamp(datetime.now()) - player.NotificationFactory[str(Notification)]['Time'])) # Notification Time Ago
            self.writeString(player.NotificationFactory[str(Notification)]['Message']) # Notification Message Entry
            self.writeVInt(0)
            if player.NotificationFactory[str(Notification)]['ID'] == 63:
                self.writeVInt(0)
                self.writeVInt(1)
                for i in range(1):
                    self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceID'])
                    self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceCount'])
                    self.writeDataReference(16, player.NotificationFactory[str(Notification)]['BrawlerID'])
                    self.writeVInt(player.NotificationFactory[str(Notification)]['SkinID'])
                
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeString('')
                self.writeBoolean(False)
            if player.NotificationFactory[str(Notification)]['ID'] == 64:
                self.writeVInt(1)
                self.writeVInt(0)
                self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceID'])
                self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceCount'])
            if player.NotificationFactory[str(Notification)]['ID'] == 70:
                self.writeVInt(0)
                self.writeVInt(1)
                for i in range(1):
                    self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceID'])
                    self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceCount'])
                    self.writeDataReference(16, player.NotificationFactory[str(Notification)]['BrawlerID'])
                    self.writeVInt(player.NotificationFactory[str(Notification)]['SkinID'])
                
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeString('')
                self.writeBoolean(False)
            if player.NotificationFactory[str(Notification)]['ID'] == 72:
                self.writeVInt(0) 
                self.writeVInt(52000000 + player.NotificationFactory[str(Notification)]['SkinID']) # Skin Donated
            if player.NotificationFactory[str(Notification)]['ID'] == 73:
                self.writeVInt(0) 
                self.writeVInt(0) # Skin Donated
            if player.NotificationFactory[str(Notification)]['ID'] == 79:
                self.writeVInt(0)
                self.writeVInt(28) # Brawlers Count
                for x in range(28):
                    self.writeVInt(16000000 + x) # Brawler ID
                    self.writeVInt(1400) # Brawler Trophies
                    self.writeVInt(450) # Brawler Trophy Loss
                    self.writeVInt(25) # Star Points Gained
                self.writeVInt(0)
            if player.NotificationFactory[str(Notification)]['ID'] == 81:
                self.writeVInt(0)
            if player.NotificationFactory[str(Notification)]['ID'] == 85:
                self.writeVInt(0)
                self.writeVInt(0) # Revoke Type
                self.writeVInt(5000) # Gems Revoked
                self.writeLong(0, 1) # Player ID
                self.writeVInt(0)
                self.writeString("") # Offer Purchased Timestamp
            if player.NotificationFactory[str(Notification)]['ID'] == 89:
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(player.NotificationFactory[str(Notification)]['ResourceCount']) # Gems Donated
            if player.NotificationFactory[str(Notification)]['ID'] == 90:
                self.writeVInt(1)
                self.writeVInt(1)
                self.writeVInt(1)
                self.writeVInt(1) # Amount
                self.writeVInt(45) # ?
                self.writeVInt(45) # ?
            if player.NotificationFactory[str(Notification)]['ID'] == 93:
                self.writeVInt(0)
                self.writeVInt(0) 
                self.writeVInt(16000000 + player.NotificationFactory[str(Notification)]['BrawlerID']) # Brawler Donated
            if player.NotificationFactory[str(Notification)]['ID'] == 94:
                self.writeVInt(29000000 + player.NotificationFactory[str(Notification)]['SkinID']) 
                self.writeVInt(29000000 + player.NotificationFactory[str(Notification)]['SkinID']) # Skin Donated
                self.writeBoolean(False)
        
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)

        self.writeBoolean(True) # Starr Road
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        if player.UnlockingBrawler != 0:
            self.writeVInt(1) # Unlocking Brawler

            all_brawlers = []
            rare = [1, 2, 3, 6, 8, 10, 13, 24]
            super_rare = [7, 9, 18, 19, 22, 25, 27, 34, 61, 4]
            epic = [14, 15, 16, 20, 26, 29, 30, 36, 39, 43, 44, 45, 46, 49, 48, 50, 51, 53, 58, 65, 68, 69, 77, 79, 82]
            mythic = [11, 17, 21, 35, 31, 32, 37, 41, 42, 47, 54, 55, 57, 59, 60, 62, 64, 66, 67, 71, 72, 73, 74, 75, 78, 81, 83, 84]
            legendary = [5, 12, 23, 28, 38, 40, 52, 63, 70, 76, 80, 85]
            for brawlerID in rare:
                if player.UnlockingBrawler != brawlerID:
                    all_brawlers.append(brawlerID)
            for brawlerID in super_rare:
                if player.UnlockingBrawler != brawlerID:
                    all_brawlers.append(brawlerID)

            x = player.UnlockingBrawler

            if x in rare:
                CreditsNeeded = 160
                GemsNeeded = 29
            if x in super_rare:
                CreditsNeeded = 430
                GemsNeeded = 79
            if x in epic:
                CreditsNeeded = 925
                GemsNeeded = 169
            if x in mythic:
                CreditsNeeded = 1900
                GemsNeeded = 349
            if x in legendary:
                CreditsNeeded = 3800
                GemsNeeded = 699
        
            self.writeDataReference(16, x)
            self.writeVInt(CreditsNeeded) # CreditsNeeded
            self.writeVInt(GemsNeeded) # GemsNeeded
            self.writeVInt(0)
            self.writeVInt(player.RareTokens) # CollectedCredits
            self.writeVInt(0)
            self.writeVInt(0)
        else:
            self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(player.OwnedBrawlers)) # Mastery
        for brawlerID,brawlerData in player.OwnedBrawlers.items():
            self.writeVInt(brawlerData["MasteryPoints"]) #Mastery Points
            self.writeVInt(brawlerData["MasteryClaimed"]) #Claimed Rewards
            self.writeDataReference(16, brawlerID) #brawlers
        #BattleCard
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0) #Brawler's BattleCards

        starrDropOpening.encode(self) # StarDrops

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False) 
        self.writeVInt(0)
        self.writeBoolean(False) 

        # end LogicClientHome

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeStringReference(player.Name)
        self.writeBoolean(player.Registered)
        self.writeInt(-1)

        self.writeVInt(23)
        unlocked_brawler = [i['CardID'] for x,i in player.OwnedBrawlers.items()]
        self.writeVInt(len(unlocked_brawler) + 3)
        for x in unlocked_brawler:
            self.writeDataReference(23, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 21)
        self.writeVInt(-1)
        if player.UnlockingBrawler == 0:
            self.writeVInt(player.RareTokens)
        else:
            self.writeVInt(0)

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(player.Blings)

        self.writeVInt(len(player.OwnedBrawlers)) # HeroScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["Trophies"])

        self.writeVInt(len(player.OwnedBrawlers)) # HeroHighScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["HighestTrophies"])

        self.writeVInt(0) # Array

        self.writeVInt(0) # HeroPower
        
        self.writeVInt(len(player.OwnedBrawlers)) # HeroLevel
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["PowerLevel"]-1)

        self.writeVInt(0) # hero star power gadget and hypercharge

        self.writeVInt(len(player.OwnedBrawlers)) # HeroSeenState
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(2)

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(player.Gems) # Diamonds
        self.writeVInt(player.Gems) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

        """self.writeVInt(1688816070)
        self.writeVInt(1191532375)
        self.writeVInt(2023189)
        self.writeVInt(73530)

        self.writeVInt(player.Trophies + 5000)
        self.writeVInt(player.HighestTrophies + 5000)
        self.writeVInt(player.HighestTrophies + 5000) 
        self.writeVInt(player.TrophyRoadTier + 200)
        self.writeVInt(player.Experience)
        self.writeDataReference(28, player.Thumbnail)
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(26)
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(len(player.SelectedSkins))
        for brawlerID in player.SelectedSkins:
            self.writeDataReference(29, player.SelectedSkins[str(brawlerID)])

        self.writeVInt(0)

        self.writeVInt(0)
        
        self.writeVInt(len(player.OwnedSkins))
        for x in player.OwnedSkins:
            self.writeDataReference(29, x)

        self.writeVInt(1080)
        for i in range(1080):
            self.writeDataReference(29, i)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeBoolean(True)
        self.writeVInt(115)
        self.writeVInt(335442)
        self.writeVInt(1001442)
        self.writeVInt(5778642) 
        self.writeVInt(0)

        self.writeVInt(120)
        self.writeVInt(200)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(Shop["Offers"])) # Shop Offers
        for shopData in Shop["Offers"]:
            self.writeVInt(len(shopData['Rewards'])) # RewardCount
            for rewardData in shopData['Rewards']:
                self.writeVInt(rewardData['ItemType'])  # ItemType
                self.writeVInt(rewardData['Amount']) # Amount
                self.writeDataReference(rewardData['CsvID'][0], rewardData['CsvID'][1])  # CsvID
                self.writeVInt(rewardData['SkinID']) # SkinID

            self.writeVInt(shopData['Currency']) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
            self.writeVInt(shopData['Cost']) # Cost
            self.writeVInt(0) # Time
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False) # Daily Offer
            self.writeVInt(0) # Old price
            self.writeString(shopData['Text']) # Text
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeString("offer_sushi") # Background
            self.writeVInt(0)
            self.writeBoolean(False) # This purchase is already being processed
            self.writeVInt(0) # Type Benefit
            self.writeVInt(0) # Benefit
            self.writeString()
            self.writeBoolean(False) # One time offer
            self.writeBoolean(False) # Claimed
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
        
        self.writeVInt(20)
        self.writeVInt(1428)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeVInt(30)

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, 0)

        self.writeString("RU")
        self.writeString("sprkdv")

        self.writeHexa("0E01160119020F1B271B2898A2C2091C0038A401290A2B8B012DA4012E0035003600370022000000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000100000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000002000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000030000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000400000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000005000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000060000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000700000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000008000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000090000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000A0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000B0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000C0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000D0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000E0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000000F000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000100000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001100000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000012000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000130000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001400000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000015000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000160000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001700000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000018000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000190000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001A0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001B0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001C0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001D0000000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000001EBFAA0200000200000000000000000000000000000000017FFFFFFC00000000000000000000000002000000000000000000000000000000001F3700000200000000000000000000000000000000010000000000000000000000000000000002000000000000000000000000000000002000000002000000000000000000000000000000000100000000000000000000000000000000020000000000000000000000000000000021000000020000000000000000000000000000000001000000000000000000000000000000000200000000000000000000000000000000011AA8042101000303100D100E1014000000001C88030000000000008BED0700067F8FFAF1F70CA9042101000300000000001C88030000000000008BED0700067F8FFAF1F70CAA04210300A0A907000206140000001C88030000000000008BED0701067F8FFAF1F70C97042102000F0310001014101B000000001CB4070000000000000000007F00A104210300A09A0C0310001008100E000000001CB4070000000000000001007F00A30421010005031000100E1014000000001CB4070000000000000000007F00AC04210300A09A0C03100010011012000000001CB4070000000000000000007F00A60421010005031001100D1014000000001CB4070000000000000000007F00A704210300A09A0C031003100E103D000000001CB4070000000000000001007F0096042101000800000000001CB4070000000000000000007F009804210100050000010E00001CB4070000000000000001007F009904210100080000010E00001CA80F0000000000000000007F009A042105000A00000000001CB4070000000000000000007F009B042101000800000000001CB4070000000000000000007F009C04210100050000010E00001CB4070000000000000000007F009E0421030080C41300000000001CB4070000000000000001007F00A504210100050000010E00001CB4070000000000000000007F00AB042106000500000000001CB4070000000000000000007F009D04210300A09A0C000200060000001CB4070000000000000000007F00A40421010005000200060000001CB4070000000000000001007F00AD0421010005000200060000001CB4070000000000000001007F00A204210100050001020000001CB4070000000000000000007F009F042102000F000205180000001CB4070000000000000000007F00A00421010005000205060000001CB4070000000000000000007F00940421010003000135000000391E0000000000008CBF270000A0ED0190CC91F80C950421010003000136000000391E0000000000008CED07000080F40190FAF1F70C8BB3120000010A34920301010134B60201010134800301010184011801010184012901010184011101010134020101018401B102010101342F01010134A91D010101011D000100010000000100010000000000000000007F000000B4B637AF98F701260102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F202122232425260FF2B3FCAA07010000BBB407050FB50D7F00000000000000000000000000000000007F007F7F7F7F00D290F6A907020000BB9102050F0F7F00000000000000000000000000000000007F007F7F7F7F00D294D1A7070300009BE304050F97057F00000000000000000000000000000000007F007F7F7F7F00F2CCE2A2070400009B860A050FB70D7F00000000000000000000000000000000007F007F7F7F7F00D2D2E3A807050000BB9102000F247F00000000000000000000000000000000007F007F7F7F7F00C1CA87A5070600009B860A050F8C077F00000000000000000000000000000000007F007F7F7F7F00A8A4B20E080000BBB407050F860E7F00FFFFFFFF0000000000000000000000007F007F7F7FB4EB0100A1EB0109CCD55DCC9B688BED07000F850E7F00FFFFFFFF000000012B007F00000000000100000011434F4E5445535420326E64206F6620313100007F007F7F7F7F08062D80C60A05EC78020D01960202820203B80104AE0105A401069A010B9001108601153C1A321F28241E29008298B10E0A0000BBB407050FB80D7F00FFFFFFFF0000000000000000000000007F007F7F7FABEB0100F8D0DB9D070C000083D10705001400000000000000000000000000000000007F007F7F7F7F00D897869D070D000093890805000000000000000000000000000210A2CDC8150000000541627973730030003600000000EDDE020000789C6592511285200845FF590CF3AA1DA4E35F7D3543EC7F23CF0B895ACE687440821B3F5A17DA3662E69DB1D675E5B6883F2B67A66CC6844F1D630B766919AE6A5E0E4A316CB16ED62D22667B06BF67548C9A2FA5BAF14D50CB00ACEA1E608D7A419FECAD8BBD55DB315907CF5BBD927BC711A34FA3E4F04ED6403A7A067DCB139A953893E7CD336D79D34CA3B27169CF7B580D9C6E6E4AE6A874521D0ED55ECB5059F497F7E11F3B7EAE80AA084C085C29DCA6830067D40D4FC58453C4A3433DA31E5CFA475D491F853A19F5BC26D5E3A781EAF9D2160761043F6B98BE6559F0C034D31F0DA99403109EEAB207000000044B6F6D79057F00000000007F007F7F7F7F001D0E00CCC9488B95AF0200007F00FFFFFFFF0000000000000000011D000000185449445F425241574C5F504153535F534541534F4E5F333390D6B2F70C90A299FA0C0000000000010000000652414E4B454400020000001152616E646F6D204D6F64652026204D6F6400007F00180F050F360F160F040F84020FB6010F320F190F070FB3010F0B0FBC090F120F350F130F88010FB2040FA4040FA5040FAC040FB0050FA4080FB8060FAF057F01177F00D282DDA5070F00009BE304050F820E7F00000000000000000000000000000000007F007F7F7F7F00FA8D94A707220000BBB407050FBF097F00000000000000000000000000000000007F007F7F7F7F0099ED0124ECA8F37ECCC9488BDBB902000F017F00FFFFFFFF00000000007F0000000000007F010000002831613164363734346637646662376263666135346533383736633934346231646139643037356462000000382F33663864633534372D316165642D346438352D383162302D3332656164313666373437345F636F6C6C61625F746F7973746F72792E7363007F7F7F7F02000001000006000ED299F0AA070100BBB407BBFA11050F197F00000000000000000000000000000000007F007F7F7F7F00F2F5E9A9070200BB9102BBD70C050FA4037F0000000000000000010200000000000000007F007F7F7F7F00F2F9C4A70703009BE3049BA90F050FB10D7F00000000000000000000000000000000007F007F7F7F7F00D2B2D6A20704009B860A9BCC14050FAE0D7F00000000000000000000000000000000007F007F7F7F7F00F2B7D7A8070500BB9102BBD70C000FA5037F00000000000000000000000000000000007F007F7F7F7F00E1AFFBA40706009B860A9BCC14050FBA097F00000000000000000000000000000000007F007F7F7F7F0088E3B20E0800BBB407BB8627050FA00D7F00FFFFFFFF0000000000000000000000007F007F7F7FB8EB0100A3EB0109CCA77D8BED078BBF27000F860E7F00FFFFFFFF000000012B007F00000000000100000011434F4E5445535420337264206F6620313100007F007F7F7F7F08062D80C60A05ABCA1F020D01960202820203B80104AE0105A401069A010B9001108601153C1A321F28241E2900A2D6B10E0A00BBB407BB8627050F9D0D7F00FFFFFFFF0000000000000000000000007F007F7F7FAFEB0100D78AB19E070C0083D10783971205000900000000000000000000000000000000007F007F7F7F7F00F8FCF99C070D0093890893CF1205001400000000000000000000000000000000007F007F7F7F7F00F2E7D0A5070F009BE3049BA90F050F810E7F00000000000000000000000000000000007F007F7F7F7F00DAF387A7072100BBB407BBFA11050F860A7F00000000000000000000000000000000007F007F7F7F7F0088F001238BCB3C8BE3668BB5860100007F00FFFFFFFF000000000000000000000001000000084D4547412050494700020000001252616E646F6D204D61702026204D6F64732100007F00070F970A0F8C0B0F8E0B0F890B0F840B0FB50A0F990A7F0417151F297F01A10100030302010F01000A14238B018C02A204A007A00CA213931DB02B041E9001AA02A80504AC04B00DB81F884995011DB60BFE19304EFFFFFFFF00000000011DB60CFEC4772E7FFFFFFFFFFFFFFF011D930EFF5AC22EFFFFFFFF00000000011D950EFF2DEF2EFFFFFFFF00000000011D8C0EFF2DEF2EFFFFFFFF00000000011D8D0EFF2DEF2EFFFFFFFF00000000011D8B0EFF2DEF2EFFFFFFFF00000000011DBF0DFF2DEF2EFFFFFFFF00000000011DB10EFFAC7F2EFFFFFFFF00000000011D8E10FFB5B9AEFFFFFFFF00000000011DA30FFFD55DAEFFFFFFFFFFFFFFFF011D9F0FFFD6AF2EFFFFFFFFFFFFFFFF011DA20FFFD9522EFFFFFFFFFFFFFFFF011DA70FFFD55DAEFFFFFFFF00000000011DAF0FFFDD46AEFFFFFFFFFFFFFFFF011DB010FFDD46AEFFFFFFFFFFFFFFFF011DAC10FFDD46AEFFFFFFFFFFFFFFFF011DAD0FFFDD46AEFFFFFFFFFFFFFFFF011DAE0FFFDD46AEFFFFFFFFFFFFFFFF011DAD10FFDD46AEFFFFFFFFFFFFFFFF011DAB10FFDD46AEFFFFFFFFFFFFFFFF011DA80FFFDE982EFFFFFFFFFFFFFFFF011DAA0FFFDE982EFFFFFFFFFFFFFFFF011DAB0FFFDE982EFFFFFFFFFFFFFFFF011DB90FFFDE982EFFFFFFFFFFFFFFFF011DBA0FFFDE982EFFFFFFFFFFFFFFFF011DB00FFFDE982EFFFFFFFFFFFFFFFF011DA60FFFDE982EFFFFFFFFFFFFFFFF011D8C10FFDE982EFFFFFFFF00000000011DBB10FFDFE9AEFFFFFFFFFFFFFFFF011DB30BFFFF8DAEFFFFFFFFFFFFFFFF001DBA0BFFFF8DAEFFFFFFFFFFFFFFFF001DBB0BFFFF8DAEFFFFFFFFFFFFFFFF001DB810FFE7D2AEFFFFFFFFFFFFFFFF011DBA10FFE9242EFFFFFFFFFFFFFFFF011D9810FFEE6A2EFFFFFFFFFFFFFFFF001DB510FFEE6A2EFFFFFFFFFFFFFFFF001DB310FFEE6A2EFFFFFFFFFFFFFFFF001DB410FFEE6A2EFFFFFFFFFFFFFFFF001DA00FFFF501AEFFFFFFFF0000000001109701FFAF222EFFFFFFFFFFFFFFFF01109601FFD40C2EFFFFFFFFFFFFFFFF0110990100271AADFFFFFFFFFFFFFFFF0034BF1AFED054AEFFFFFFFFFFFFFFFF0134A81AFED054AEFFFFFFFFFFFFFFFF0134A91AFED054AEFFFFFFFFFFFFFFFF0134AA1AFED054AEFFFFFFFFFFFFFFFF0184018204FE3E63AAFFFFFFFFFFFFFFFF0184018F04FE3E63AAFFFFFFFFFFFFFFFF0184018504FE8AEF4AFFFFFFFFFFFFFFFF0184018604FE8AEF4AFFFFFFFFFFFFFFFF0184019C04FF0510AEFFFFFFFFFFFFFFFF0184019D04FF0510AEFFFFFFFFFFFFFFFF0184019E04FF0510AEFFFFFFFFFFFFFFFF0184019F04FF0510AEFFFFFFFFFFFFFFFF018401B304FF2E438EFFFFFFFFFFFFFFFF018401B404FF2E438EFFFFFFFFFFFFFFFF0184018C05FF5C1AB6FFFFFFFFFFFFFFFF0184018B05FF5C1AB6FFFFFFFFFFFFFFFF0184018A05FF5C1AB6FFFFFFFFFFFFFFFF0184019205FF669FAEFFFFFFFFFFFFFFFF0184019305FF669FAEFFFFFFFFFFFFFFFF018401A505FF7FAC2EFFFFFFFFFFFFFFFF018401A005FF80FDAEFFFFFFFFFFFFFFFF018401A205FF824F2EFFFFFFFFFFFFFFFF018401A405FF83A0AEFFFFFFFFFFFFFFFF018401A105FF84F22EFFFFFFFFFFFFFFFF018401A305FF8643AEFFFFFFFFFFFFFFFF0184019F05FF87952EFFFFFFFFFFFFFFFF018401AD05FFFA63CEFFFFFFFFFFFFFFFF001CBF06FED054AEFFFFFFFFFFFFFFFF011C8007FED054AEFFFFFFFFFFFFFFFF011C8107FED054AEFFFFFFFFFFFFFFFF011C8207FED054AEFFFFFFFFFFFFFFFF011C9809FF669FAEFFFFFFFFFFFFFFFF011C9909FF669FAEFFFFFFFFFFFFFFFF011C9709FFB70B2EFFFFFFFFFFFFFFFF011C8802FFDAA3AEFFFFFFFFFFFFFFFF011C8205FFDAA3AEFFFFFFFFFFFFFFFF0117B80DFFE28CAEFFFFFFFFFFFFFFFF0117B70DFFE28CAEFFFFFFFFFFFFFFFF0117BC0DFFE28CAEFFFFFFFFFFFFFFFF0117B90DFFE28CAEFFFFFFFFFFFFFFFF0117BB0DFFE28CAEFFFFFFFFFFFFFFFF0117BA0DFFE28CAEFFFFFFFFFFFFFFFF0116B507989C0100BE9C011E829D0100839D018C5C8C9D018803B501018002008101B6F28C2701BF83AF5F8302A09A0C8A02008C02019F018BED072F01BB018803BC018BED07300332B4078C11B4078D1101AA0FB4078E1100010401000000000200000000020000000002A1BE01021DB7108DDBB9020000000085010ACEC948010000001150495A5A412050495A5A412050495A5A4100010000000D50495A5A4120464F5220414C4C000000010000001F6F666665725F6267725F70697A7A615F706C616E65745F64656C6976657279008D9FD0010000000085010BCEC948010000000002010000000D4D4F52452050495A5A41202121000000010000001F6F666665725F6267725F70697A7A615F706C616E65745F64656C697665727900000102BAE70100018DDBB90201030000002831336333346365373831623532393162643832323662373363643737613334643235393238656331000000382F36386166656165622D396330392D343536372D386162362D3964353766316536316362385F636C75625F70696767795F747265652E7363A20100CE89F77C0006001D8F01A9029D05BB0A0600A0028207B407A21384270500A4019006A80FB82E000000060792FF140D91010000000C000000058900000027596F75206D6973736564207468652072656D61696E696E67206C6F67696E20726577617264732E1C0191010000000B000000058900000027596F75206D6973736564207468652072656D61696E696E67206C6F67696E20726577617264732E1B0191010000000A000000058900000027596F75206D6973736564207468652072656D61696E696E67206C6F67696E20726577617264732E1A0185010000000900000B0735FFFFFFFF19001F8501000000080100508E92FFFFFFFF18001E860100000007010060AB35FFFFFFFF10011800103DBF0E070000000022D093D09DD098D0AED0A9D095D09520D098D0A1D09FD0ABD0A2D090D09DD098D09521003F00000006010060AB35FFFFFFFF0F0132040000070C00000022D093D09DD098D0AED0A9D095D09520D098D0A1D09FD0ABD0A2D090D09DD098D09521003F00000005010060ABACFFFFFFFF0E0132040000070B00000022D093D09DD098D0AED0A9D095D09520D098D0A1D09FD0ABD0A2D090D09DD098D09521003F00000004010060AC5DFFFFFFFF0D0132040000070A00000022D093D09DD098D0AED0A9D095D09520D098D0A1D09FD0ABD0A2D090D09DD098D09521003F00000003010060ACF7FFFFFFFF0C0132030000070900000022D093D09DD098D0AED0A9D095D09520D098D0A1D09FD0ABD0A2D090D09DD098D09521003F00000002010060AD83FFFFFFFF0B0132030000070800000022D093D09DD098D0AED0A9D095D09520D098D0A1D09FD0ABD0A2D090D09DD098D09521003700000001010067349EFFFFFFFF0301320100001E0037000000000100673551FFFFFFFF0201320100001E007F00000000000001091008100A1007100D10221003100E1001101B00101B01101E9D0EA902009A050001101D9A031006A0021D0000010110021002A0021D0000010110061009AE068F0100000202101610191016AE068F0100000202100910191019AE068F010000020210091016101D9D0EA90200000302102D1010102D9D0EA90200000302101D101010109D0EA90200000302101D102D100BAC1D9D0500000402101110151011AC1D9D0500000402100B10151015AC1D9D0500000402100B10111018A0021D00000501000001A0021D00051013AE068F0100000601000002AE068F0100060002AE068F01000610329D0EA902000007010000039D0EA902000700039D0EA90200071020AC1D9D0500000801000004AC1D9D0500080004AC1D9D0500081017983BBB0A00000902100C1005100C983BBB0A00000902101710051005983BBB0A000009021017100C0001A0021D000A1004AE068F0100000B01000002AE068F01000B0002AE068F01000B102B9D0EA90200000C010000039D0EA902000C00039D0EA902000C102AAC1D9D0500000D01000004AC1D9D05000D0004AC1D9D05000D0002AE068F01000E0002AE068F01000E100F9D0EA90200000F010000039D0EA902000F00039D0EA902000F101C983BBB0A00001001000005983BBB0A00100005983BBB0A0010101A9D0EA9020000110210300010309D0EA90200001102101A0000039D0EA902001100039D0EA90200110002AE068F010012101FAC1D9D0500001302102F00102FAC1D9D0500001302101F000004AC1D9D0500130004AC1D9D05001310249D0EA902000014010000039D0EA902001400039D0EA902001400039D0EA90200141028983BBB0A000015021034001034983BBB0A000015021028000005983BBB0A00150005983BBB0A0015103A9D0EA902000016010000039D0EA902001600039D0EA902001600039D0EA9020016103F983BBB0A00001701000005983BBB0A00170005983BBB0A00170005983BBB0A00171085019D0EA902000018010000039D0EA902001800039D0EA902001800039D0EA90200181025AC1D9D0500001901000004AC1D9D0500190004AC1D9D0500190004AC1D9D05001910239D0EA90200001A010000039D0EA902001A00039D0EA902001A00039D0EA902001A108001AC1D9D0500001B01000004AC1D9D05001B0004AC1D9D05001B0004AC1D9D05001B1026983BBB0A00001C01000005983BBB0A001C0005983BBB0A001C0005983BBB0A001C10279D0EA90200001D010000039D0EA902001D00039D0EA902001D00039D0EA902001D108301AC1D9D0500001E01000004AC1D9D05001E0004AC1D9D05001E0004AC1D9D05001E108601983BBB0A00001F01000005983BBB0A001F0005983BBB0A001F0005983BBB0A001F102E9D0EA902000020010000039D0EA902002000039D0EA902002000039D0EA9020020108701AC1D9D0500002101000004AC1D9D0500210004AC1D9D0500210004AC1D9D050021108C01983BBB0A00002201000005983BBB0A00220005983BBB0A00220005983BBB0A0022108901AC1D9D0500002301000004AC1D9D0500230004AC1D9D0500230004AC1D9D0500230005983BBB0A00240005983BBB0A00240005983BBB0A002400039D0EA902002500039D0EA902002500039D0EA90200250004AC1D9D0500260004AC1D9D0500260004AC1D9D050026109001983BBB0A00002701000005983BBB0A00270005983BBB0A002710339D0EA902000028010000039D0EA902002800039D0EA90200281029AC1D9D0500002901000004AC1D9D0500290004AC1D9D050029109501983BBB0A00002A01000005983BBB0A002A0005983BBB0A002A10359D0EA90200002B010000039D0EA902002B00039D0EA902002B102CAC1D9D0500002C01000004AC1D9D05002C0004AC1D9D05002C0005983BBB0A002D0005983BBB0A002D103C9D0EA90200002E010000039D0EA902002E00039D0EA902002E1031AC1D9D0500002F01000004AC1D9D05002F0004AC1D9D05002F0005983BBB0A00301081019D0EA902000031010000039D0EA902003100039D0EA90200311036AC1D9D0500003201000004AC1D9D0500320004AC1D9D0500321084019D0EA902000033010000039D0EA902003300039D0EA90200331038AC1D9D0500003401000004AC1D9D0500340004AC1D9D0500341088019D0EA902000035010000039D0EA902003500039D0EA90200351039AC1D9D0500003601000004AC1D9D0500360004AC1D9D050036108D019D0EA902000037010000039D0EA902003700039D0EA9020037103BAC1D9D0500003801000004AC1D9D0500380004AC1D9D050038108F019D0EA902000039010000039D0EA902003900039D0EA9020039103EAC1D9D0500003A01000004AC1D9D05003A0004AC1D9D05003A1092019D0EA90200003B010000039D0EA902003B00039D0EA902003B108201AC1D9D0500003C01000004AC1D9D05003C0004AC1D9D05003C1096019D0EA90200003D010000039D0EA902003D00039D0EA902003D108B01AC1D9D0500003E01000004AC1D9D05003E0004AC1D9D05003E00039D0EA902003F00039D0EA902003F108A01AC1D9D050000800101000004AC1D9D050080010004AC1D9D0500800100039D0EA902008101108E01AC1D9D050000820101000004AC1D9D050082010004AC1D9D05008201109101AC1D9D050000830101000004AC1D9D050083010004AC1D9D05008301109301AC1D9D050000840101000004AC1D9D050084010004AC1D9D05008401109401AC1D9D050000850101000004AC1D9D050085010004AC1D9D05008501109701AC1D9D050000860101000004AC1D9D050086010004AC1D9D050086010004AC1D9D050087010004AC1D9D050087010004AC1D9D0500880103038B0104320532000A8E04001000160010010A001012BE0200102228001003B2020010079E02001008840300100AA80200100D0A00100E00000000000000049001017F0F9001007F209001027F0C9001037F03008E96BB7C00008BED0700000000000004008BED0700000000000000000099ED01000000000000000001A1EB0106010698A348000F000000000000")

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])

        reg = 0
        if player.Registered:
            reg = 1
        self.writeStringReference(player.Name)
        self.writeInt(reg)
        self.writeInt(-1)

        self.writeVInt(23)
        unlocked_brawler = [i['CardID'] for x,i in player.OwnedBrawlers.items()]
        self.writeVInt(len(unlocked_brawler) + 3)
        for x in unlocked_brawler:
            self.writeDataReference(23, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 21)
        self.writeVInt(-1)
        if player.UnlockingBrawler == 0:
            self.writeVInt(player.RareTokens)
        else:
            self.writeVInt(0)

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(player.Blings)

        self.writeVInt(len(player.OwnedBrawlers)) # HeroScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["Trophies"])

        self.writeVInt(len(player.OwnedBrawlers)) # HeroHighScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["HighestTrophies"])

        self.writeVInt(0) # Array

        self.writeVInt(0) # HeroPower
        
        self.writeVInt(len(player.OwnedBrawlers)) # HeroLevel
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["PowerLevel"]-1)

        self.writeVInt(0) # hero star power gadget and hypercharge

        self.writeVInt(len(player.OwnedBrawlers)) # HeroSeenState
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(2)

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(player.Gems) # Diamonds
        self.writeVInt(player.Gems) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)"""

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
