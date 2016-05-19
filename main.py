import SpreadSheet, SpreadValue, Shows

def main():

    end = 0
    while(end == 0):
        Doc = SpreadSheet.Document()
        value = SpreadValue.value()

        token = Doc.get_user()
        Currentwork = Doc.Setup(token)

        #Get List of Tv Shows
        Tv_shows = value.get_showlist(Currentwork)
        [print(shows) for shows in Tv_shows if shows]  # list comprehension, Doesnt show empty space

        shows = Shows.Shows()  #Initialize DB
        db = shows.DB()

        Title =input("Enter A tv Show Title :")
        Id = shows.get_show(db,Title)
        print("ID: ", Id)
        Showinfo = shows.get_info(db, Id)

        URL = Showinfo[0]
        name = Showinfo[1]
        seasons = Showinfo [2]
        episodes = Showinfo [3]
        genre = Showinfo [4]


        #See if a space is empty
        entry = 2                           #Starts at b2
        while  entry < len(Tv_shows):
            count = str(entry)
            Field = 'b' + count

            CurrentSection = value.get_value(Currentwork, Field)
            space_check = value.isfilled(CurrentSection)

            if space_check:
                value.Add_show(value,Currentwork,entry,count,URL,name,seasons,episodes,genre)
                break
            else:
                entry += 2


        Continue = input("Do you want another show?")
        if Continue.startswith("y"):
            end = 0
        else:
            print("Bye Bye!")
            break




main()
