class value:

    def get_value(self,worksheet, number):
        val = worksheet.acell(number).value
        return val

    def add_value(self,worksheet, location, word):
        worksheet.update_acell( location , word)

    def get_showlist(self,worksheet ):
        values_list = worksheet.col_values(2)
        return values_list
        #print(values_list)

    def isfilled(self, Value):

        if Value:
            #print(Value)
            return False
        else:
            #print("empty")
            return True

    def Add_show(self, value,Currentwork, entry, count, URL, name, seasons, episodes, genre ):

        collum = ["a","b","c","d","e"]

        Pic_URL = '=IMAGE("'+URL+'")'
        #print(Pic_URL)
        value.add_value(Currentwork, collum[0]+count, Pic_URL)
        value.add_value(Currentwork, collum[1]+count, name)
        value.add_value(Currentwork, collum[2]+count, seasons)
        value.add_value(Currentwork, collum[3]+count, episodes)
        value.add_value(Currentwork, collum[4]+count, genre)

        print("COMPLETE!")
