import csv


class Characters:
    def getBrawlersID():
        BrawlersID = []
        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[24] == 'Hero' and row[2].lower() != 'true' and row[0] != "MechaDudeBig":
                        BrawlersID.append(line_count - 2)
                    line_count += 1

            return BrawlersID

    def getBrawlerFromSepcificRarity(self, rarity):
        BrawlersCardsIds = []
        codenames = []
        Brawlers = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[8] == '0' and row[4].lower() != "true" and row[15].lower() == rarity:
                        BrawlersCardsIds.append(line_count - 2)
                        codenames.append(row[3])
                    line_count += 1
            with open("Classes/Files/assets/csv_logic/characters.csv") as characters:
                csv_reader = csv.reader(characters, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0 or line_count == 1:
                        line_count+=1
                    else:
                        if row[0] in codenames and row[31] == 'Hero':
                            Brawlers.append(line_count -2)
                        line_count+=1
                        
            return Brawlers
        
    def getBrawlerIdByName(name):
        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == name:
                        BrawlerID = (line_count - 2)
                        break
                    if row[0] != "":
                        line_count += 1
        return BrawlerID
    
    def getBrawlerNameByID(id):
        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == id:
                        BrawlerName = row[0]
                        break
                    if row[0] != "":
                        line_count += 1
        return BrawlerName
    
    def getBrawlerIDByName(name):
        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == name:
                        BrawlerID = (line_count - 2)
                        break
                    if row[0] != "":
                        line_count += 1
        return BrawlerID