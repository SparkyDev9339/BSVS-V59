from io import BytesIO

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class StartLoadingMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeInt(6) # Players Count
        self.writeInt(0)
        self.writeInt(0)

        self.writeInt(6) # Players Count
        # LogicPlayer::encode
        for index in range(6):
            self.writeInt(0)
            self.writeInt(player.ID[1])

            self.writeVInt(index) # Player Index
            teamIndex = 0
            if index > 2:
                teamIndex = 1
            self.writeVInt(teamIndex)
            self.writeVInt(0) # ?

            self.writeInt(0)

            self.writeBoolean(True)

            # Display Data тут блять

            self.writeDataReference(16, 0) # brawlerID ну тут вроде оно

            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)

            self.writeDataReference(29, 0) # skinID ну тут вроде оно

            self.writeString('sprkdv')
            self.writeVInt(0) # Experience
            self.writeVInt(28000000) # ProfileIcon
            self.writeVInt(43000000) # Namecolor
            self.writeVInt(0) # Bpnamecolor

            self.writeBoolean(False) # ??
            self.writeVInt(0)

        self.writeInt(0) # LogicVector

        self.writeInt(0) # ?

        self.writeInt(0) # ?

        self.writeVInt(0) # gameModVariation
        self.writeVInt(1)
        self.writeVInt(1)

        self.writeBoolean(True) 

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(15, 7) # mapID

        self.writeBoolean(False) # PlayerMap
        self.writeBoolean(False) # Undergod
        self.writeBoolean(False) # Friendly Match

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20559

    def getMessageVersion(self):
        return self.messageVersion