from pytvdbapi import api
class Shows:

    def DB(self):
        #Replace ** with your Api Code
        db = api.TVDB('**', banners= True)  #using api code
        return db

    def get_show(self, database, show):
        result = database.search( show, "en")

        print("Shows in database related to your search")
        for a in range(len(result)):
            print(a+1, result[a])   #added +1 since it starts at zero

        choice = int (input("Choose a show number :"))
        showTitle = result[choice - 1]

        Name = showTitle.seriesid   #Get The Series ID from the database
        return Name

    def get_info(self, database, Id):
        show = database.get_series( Id, "en" )

        number = str(Id)

        Seasons = len(show) - 1
        if Seasons == 0:
            Seasons =1

        URL = "http://thetvdb.com/banners/graphical/"+number+"-g.jpg"

        ep_count = 0
        for season in show:
            for episode in season:
                ep_count += 1

        Genre = show.Genre
        name = show.SeriesName

        output =[ URL,name,Seasons, ep_count , Genre ]
        return output



