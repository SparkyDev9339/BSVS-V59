import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

from Classes.Files.Classes.Milestones import Milestones
from Classes.Files.Classes.Pins import Emotes
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Sprays import Sprays
from Classes.Files.Classes.PlayerThumbnails import PlayerThumbnails

class LogicClaimRankUpRewardCommand(LogicCommand):
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
        fields["RewardID"] = calling_instance.readVInt()
        fields['RewardType'] = calling_instance.readVInt()
        fields['BrawlPassSeason'] = calling_instance.readVInt()
        fields['LVL'] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data['RewardTrackType'] = fields['RewardID']
        RewardAvaible = 0

        if fields['RewardID'] == 6:
            MilestoneReader = Milestones.getTrophyRoadLvL(fields['LVL'])
            CountReward = int(MilestoneReader['PrimaryLvlUpRewardCount'])

            if int(MilestoneReader['Trophies']) <= player_data['HighestTrophies']:
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 1:
                    RewardID = 7
                    player_data['Coins'] = player_data['Coins'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)

                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 16:
                    RewardID = 8
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 38:
                    RewardID = 22
                    player_data['RareTokens'] = player_data['RareTokens'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 41:
                    RewardID = 24
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 45:
                    RewardID = 25
                player_data['TrophyRoadTier'] = player_data['TrophyRoadTier'] + 1
                RewardAvaible = 1
            else:
                fields["Socket"] = calling_instance.client
                fields['ServerChecksum'] = 1
                fields['ClientChecksum'] = 1
                fields['Tick'] = 20
                Messaging.sendMessage(24104, fields)

        if fields['RewardID'] == 9 or fields['RewardID'] == 10 or fields['RewardID'] == 12:
            MilestoneReader = Milestones.getBrawlPassLvl(fields['RewardID'], fields['BrawlPassSeason'], fields['LVL'])
            CountReward = int(MilestoneReader['PrimaryLvlUpRewardCount'])
            
            if int(MilestoneReader['BrawlPassTokens']) <= player_data['BPTokens']:
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 1:
                    RewardID = 7
                    player_data['Coins'] = player_data['Coins'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 3:
                    RewardID = 1
                    CsvID = 16
                    CsvID1 = Characters.getBrawlerIdByName(MilestoneReader['PrimaryLvlUpRewardData'])
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 4:
                    RewardID = 9
                    CsvID = 29
                    CsvID1 = Skins.getSkinIdByName(MilestoneReader['PrimaryLvlUpRewardData'])
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 19:
                    RewardID = 11
                    CsvID = 52
                    CsvID1 = Emotes.getEmoteIdByName(MilestoneReader['PrimaryLvlUpRewardData'])
                    player_data['OwnedPins'].append(CsvID1)
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 16:
                    RewardID = 8
                    player_data['Gems'] = player_data['Gems'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 24:
                    RewardID = 9
                    CsvID = 29
                    CsvID1 = Skins.getSkinIdByName(MilestoneReader['PrimaryLvlUpRewardData'])
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 25:
                    RewardID = 11
                    CsvID = 28
                    CsvID1 = PlayerThumbnails.getThumbnailsIdByName(MilestoneReader['PrimaryLvlUpRewardData'])
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 35:
                    RewardID = 11
                    CsvID = 68
                    CsvID1 = Sprays.getEmoteIdByName(MilestoneReader['PrimaryLvlUpRewardData'])
                    player_data['OwnedThumbnails'].append(CsvID1)
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 38:
                    RewardID = 22
                    player_data['RareTokens'] = player_data['RareTokens'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 39:
                    RewardID = 23
                    player_data['ChromaticTokens'] = player_data['ChromaticTokens'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 41:
                    RewardID = 24
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 45:
                    RewardID = 25
                    player_data['Blings'] = player_data['Blings'] + CountReward
                    db_instance.updatePlayerData(player_data, calling_instance)
                if int(MilestoneReader['PrimaryLvlUpRewardType']) == 51:
                    RewardID = 22

                BPFreeReward = True
                BPReward = False
                BPPlusReward = False

                if player_data['BrawlPassBuy'] == 0:
                    BPReward = False
                    BPPlusReward = False
                if player_data['BrawlPassBuy'] == 1:
                    BPReward = True
                    BPPlusReward = False
                if player_data['BrawlPassBuy'] == 2:
                    BPReward = True
                    BPPlusReward = True
                
                RewardAvaible = 1
            else:
                fields["Socket"] = calling_instance.client
                fields['ServerChecksum'] = 1
                fields['ClientChecksum'] = 1
                fields['Tick'] = 20
                Messaging.sendMessage(24104, fields)
        
        if fields['RewardID'] == 6: # Trophy Road
            player_data['BrawlPassSeason'] = fields['BrawlPassSeason']
            player_data['RewardForRank'] = calling_instance.player.TrophyRoadTier + 1
            db_instance.updatePlayerData(player_data, calling_instance)

            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': CountReward, 'DataRef': [0, 0], 'RewardID': RewardID}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)

            db_instance.updatePlayerData(player_data, calling_instance)

        if fields['RewardID'] == 9 or fields['RewardID'] == 12: # Brawl Pass Prem
            player_data['BrawlPassSeason'] = fields['BrawlPassSeason']
            player_data['RewardForRank'] = 2
            db_instance.updatePlayerData(player_data, calling_instance)
            player_data['RewardForRank'] =  player_data['RewardForRank'] + fields['LVL']
            db_instance.updatePlayerData(player_data, calling_instance)

            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            if RewardID == 1 or RewardID == 9 or RewardID == 11:
                item = {'Amount': CountReward, 'DataRef': [CsvID, CsvID1], 'RewardID': RewardID}
            else:
                item = {'Amount': CountReward, 'DataRef': [0, 0], 'RewardID': RewardID}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)

            db_instance.updatePlayerData(player_data, calling_instance)
        
        if fields['RewardID'] == 10: # Brawl Pass Free
            player_data['BrawlPassSeason'] = fields['BrawlPassSeason']
            player_data['RewardForRank'] = 2
            db_instance.updatePlayerData(player_data, calling_instance)
            player_data['RewardForRank'] =  player_data['RewardForRank'] + fields['LVL']
            db_instance.updatePlayerData(player_data, calling_instance)

            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': CountReward, 'DataRef': [0, 0], 'RewardID': RewardID}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)

            db_instance.updatePlayerData(player_data, calling_instance)

        if fields['RewardID'] == 12 and BPPlusReward == True:
            player_data['BrawlPassPlusLevel'].append(fields['LVL']) 
        if fields['RewardID'] == 10 and BPFreeReward == True:
            player_data['BrawlPassFreeLevel'].append(fields['LVL'])
        if fields['RewardID'] == 9 and BPReward == True:
            player_data['BrawlPassLevel'].append(fields['LVL']) 
        db_instance.updatePlayerData(player_data, calling_instance)

        if RewardAvaible:
            fields["Socket"] = calling_instance.client
            fields["Command"] = {"ID": 203}
            fields["PlayerID"] = calling_instance.player.ID
            Messaging.sendMessage(24111, fields)

    def getCommandType(self):
        return 517