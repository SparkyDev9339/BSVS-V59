import json
import random, datetime
import string
from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters
from Database.DatabaseHandler import DatabaseHandler

class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    AllianceID = [0, 0]
    RoomID = [0, 0]
    Token = ""
    Name = "Brawler"
    Registered = False

    Vip = 0
    Thumbnail = 0
    Namecolor = 0
    Region = "RU"
    ContentCreator = ""

    battleTick = 0

    Coins = 100
    CoinsGained = 0
    Gems = 0
    StarPoints = 0

    ChromaticTokens = 0
    RareTokens = 0
    Blings = 0
    UnlockingBrawler = 1

    ClubCoins = 0
    
    Trophies = 50000
    HighestTrophies = 50000
    TrophiesGained = 0
    TrophyRoadTier = 1
    Experience = 0
    Level = 0
    Tokens = 0
    TokensGained = 0
    TokensDoubler = 0

    PushasedOffers = []
    
    delivery_items = {}
    
    BattleLogs = {}
    
    banned = False

    pl_rank = 1

    club_trophies = 0

    club_rank = 1

    club_tickets = 0

    vs = 0

    IntValueEntry = {'TokensGained': 0, 'TrophiesGained': 0, 'StarPointsGained': 0, 'GemsGained': 0, 'DemoAccount': 0, 'ChampionPopup': 0, 'SocialAge': 1, 'InvitesBlock': 0}

    # Brawl Pass
    BrawlPassFreeLevel = []
    BrawlPassLevel = []
    BrawlPassPlusLevel = []

    RewardTrackType = 0
    RewardForRank = 0

    BrawlPassSeason = 0
    BrawlPassBuy = 2
    BPTokens = 0
    # Brawl Pass

    # Teams
    roomID = 0
    roomType = 0
    playerData = []

    # CsvReader
    brawlersID = Characters.getBrawlersID()
    # CsvReader End

    # Profiles
    favoriteBrawler = 0
    battleIcon = -1
    battleIcon1 = -1
    battlePin = -1
    battleTitle = -1

    threeXthreeWins = 0
    solowWins = 0
    duoWins = 0

    PowerPoints = 0
    
    NotificationFactory = {
        1: {'ID': 81, 'Index': 0, 'Read': False, 'Time': datetime.datetime.timestamp(datetime.datetime.now()), 'Message': 'Voucher redeemed', 'ResourceCount': 1, 'ResourceID': 0, 'BrawlerID': 0, 'SkinID': 0}
    }

    SelectedSkins = {'0': 0}

    SelectedBrawlers = [0, 1, 8]
    RandomizerSelectedSkins = []
    OwnedPins = []
    OwnedThumbnails = []
    OwnedSprays = []
    OwnedSkins = []
    SelectedBrawlersSkins = {
        0: 0,
	1: 0,
	8: 0,
    }
    OwnedBrawlers = {
        0: {'CardID': 0, 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 and lowid == 0:
            db = DatabaseHandler()
            playerscount = len(db.getAll())
            self.ID[0] = 0
            self.ID[1] = playerscount + 1
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = 0
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'AllianceID': self.AllianceID,
            'RoomID': self.RoomID,
            'Registered': self.Registered,
            'Vip': self.Vip,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,

            'ChromaticTokens': self.ChromaticTokens,
            'RareTokens': self.RareTokens,
            'Blings': self.Blings,
            'UnlockingBrawler': self.UnlockingBrawler,

            'battleTick': self.battleTick,

            'ClubCoins': self.ClubCoins,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'PushasedOffers': self.PushasedOffers,
            'delivery_items': self.delivery_items,
            'BattleLogs': self.BattleLogs,
            'banned': self.banned,
            'BPTokens': self.BPTokens,
            'pl_rank': self.pl_rank,
            'club_trophies': self.club_trophies,
            'club_rank': self.club_rank,
            'club_tickets': self.club_tickets,
            # Profiles
            'favoriteBrawler': self.favoriteBrawler,
            'battleIcon': self.battleIcon,
            'battleIcon1': self.battleIcon1,
            'battlePin': self.battlePin,
            'battleTitle': self.battleTitle,
            'threeXthreeWins': self.threeXthreeWins,
            'soloWins': self.solowWins,
            'duoWins': self.duoWins,
            # Profiles End
            # BrawlPass
            'BrawlPassFreeLevel': self.BrawlPassFreeLevel,
            'BrawlPassLevel': self.BrawlPassFreeLevel,
            'BrawlPassPlusLevel': self.BrawlPassPlusLevel,
            'RewardTrackType': self.RewardTrackType,
            'RewardForRank': self.RewardForRank,
            'BrawlPassSeason': self.BrawlPassSeason,
            'BrawlPassBuy': self.BrawlPassBuy,
            # BrawlPass End
            'roomID': self.roomID,
            'roomType': self.roomType,
            'playerData': self.playerData,
            'brawlersID': self.brawlersID,
            'vs': self.vs,
            'PowerPoints': self.PowerPoints,
            'NotificationFactory': self.NotificationFactory,
            'IntValueEntry': self.IntValueEntry,
            'SelectedSkins': self.SelectedSkins,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedSprays': self.OwnedSprays,
            'OwnedSkins': self.OwnedSkins,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
