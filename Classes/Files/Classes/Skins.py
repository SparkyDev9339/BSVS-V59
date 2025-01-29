import csv

class Skins:
    def getSkinsIDSSpecificPrice(self, min, max):
        SkinsID = []
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != 'true':
                        skin_gem_price = row[15]
                        if (skin_gem_price != ''):
                            if int(skin_gem_price) >= min and int(skin_gem_price) <= max:
                                SkinsID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return SkinsID
        
    def getSkinIdByName(name):
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == name:
                        SkinID = (line_count - 2)
                        break
                    if row[0] != "":
                        line_count += 1
        return SkinID
    
    def getBrawlerBySkin(self, skinID):
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == skinID:
                        confName = row[1]
                        with open('Classes/Files/assets/csv_logic/skin_confs.csv') as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count2 = 0
                            for row2 in csv_reader:

                                if line_count2 == 0 or line_count2 == 1:
                                    line_count2 += 1
                                else:
                                    if row2[0] == confName:
                                        brawlerName = row2[1]
                                        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
                                            csv_reader = csv.reader(csv_file, delimiter=',')
                                            line_count3 = 0
                                            for row3 in csv_reader:
                                                if line_count3 == 0 or line_count3 == 1:
                                                    line_count3 += 1
                                                else:
                                                    if row3[0] == brawlerName:
                                                        return line_count3 - 2
                                                    if row3[0] != "":
                                                        line_count3 += 1
                                    if row2[0] != "":
                                        line_count2 += 1
                    if row[0] != "":
                        line_count += 1
    
    def getCostSkinByID(id):
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == id:
                        SkinCost = {"Bling": row[15], "Diamonds": row[16]}
                        break
                    if row[0] != "":
                        line_count += 1
        return SkinCost
    
    def getEmoteSkinByID(id):
        with open('Classes/Files/assets/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == id:
                        SkinEmote = {"Emote": row[5]}
                        break
                    if row[0] != "":
                        line_count += 1
        return SkinEmote
