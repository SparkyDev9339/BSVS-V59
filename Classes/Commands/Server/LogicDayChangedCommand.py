from Classes.Commands.LogicServerCommand import LogicServerCommand

from Classes.ByteStreamHelper import ByteStreamHelper

import time
import json
import random

class LogicDayChangedCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        nowTime = time.time() + 3600 * 4
        self.writeBoolean(True)
        Events = json.loads(open("Events.json", 'r').read())
        EventIndex = 0

        self.writeVInt(2023189)
        
        self.writeVInt(38) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13) 
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18) 
        self.writeVInt(19)
        self.writeVInt(20)
        self.writeVInt(21) 
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)
        self.writeVInt(33)
        self.writeVInt(34)
        self.writeVInt(35)
        self.writeVInt(36)
        self.writeVInt(37)
        self.writeVInt(38)

        Events = json.loads(open("Events.json", 'r').read())
        EventIndex = 0

        self.writeVInt(len(Events['Events'])) # Events
        for EventData in Events['Events']:
            self.writeVInt(-1)
            self.writeVInt(EventData['Slot']) # EventSlot
            self.writeVInt(EventData['Slot']) # EventSlot
            self.writeVInt(0)
            self.writeVInt(int(EventData['TimeToEnd']) - int(nowTime))
            self.writeVInt(10) 
            self.writeDataReference(15, 636) # map id
            self.writeVInt(-1)
            self.writeVInt(1) # MapStatus
            self.writeString("")
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False) # MapMaker map structure array
            self.writeVInt(0)
            self.writeBoolean(False) # Power League array entry
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(-1)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(-1)
            self.writeVInt(0) 
            self.writeVInt(0) 
            self.writeVInt(0) 
            self.writeBoolean(False) 
            self.writeBoolean(False) 
            self.writeBoolean(False)

            if int(EventData['TimeToEnd']) <= int(nowTime):
                with open('Events.json') as f:
                    data = json.load(f)
                data['Events'][EventIndex]['TimeToEnd'] = time.time() + 3600 * 4 + 120
                data['Events'][EventIndex]['MapID'] = random.choice([7, 8, 9])
                with open('Events.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            EventIndex += 1
                

        self.writeVInt(0)
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800])
        ByteStreamHelper.encodeIntList(self, [30, 80, 170, 360]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [300, 880, 2040, 4680]) # Shop Coins Amount

        # ReleaseEntry::encode
        self.writeVInt(0) 
        # ReleaseEntry::encode

        # IntValueEntry::encode
        self.writeVInt(1)
        for i in range(1):
            self.writeDataReference(41000108, 1) # ThemeID
        # IntValueEntry::encode end

        # TimedIntValueEntry::encode
        self.writeVInt(0) 
        # TimedIntValueEntry::encode end
        # CustomEvent::encode
        self.writeVInt(0)
        # CustomEvent::encode end
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(4)
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 204