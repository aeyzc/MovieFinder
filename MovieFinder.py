import os
import time
while True:
    try:
        import pandas as pd
    except Exception:
        os.system("pip install pandas")
        time.sleep(3)
    else:
        break

def clear(a):
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
    if a==1:
        print('''  __  __            _        ______ _           _           
 |  \/  |          (_)      |  ____(_)         | |          
 | \  / | _____   ___  ___  | |__   _ _ __   __| | ___ _ __ 
 | |\/| |/ _ \ \ / / |/ _ \ |  __| | | '_ \ / _` |/ _ \ '__|
 | |  | | (_) \ V /| |  __/ | |    | | | | | (_| |  __/ |   
 |_|  |_|\___/ \_/ |_|\___| |_|    |_|_| |_|\__,_|\___|_|   
                                                    by aeyzc''')

def letmechoiceRate():
    clear(1)
    try:
        a=float(input("Min Value:"))
        b=float(input("Max Value:"))
    except Exception:
        return 0,10
    
    if a<=b and a>=0 and a<=10 and b>=0 and b<=10:
            return a,b+0.1 
    else:
        print("Wrong Entry!")
        return 0,10

def letmechoiceYear():
    clear(1)
    try:
        a=float(input("Min Value:"))
        b=float(input("Max Value:"))
    except Exception:
        return 0,2020
    
    if a<=b and a>=0 and a<=2020 and b>=0 and b<=2020:
            return a,b+0.5 
    else:
        print("Wrong Entry!")
        return 0,2020
    

while True:
    clear(1)
    select=input('''Choose a Category
1-Action     2-Adventure  3-Animation
4-Biography  5-Comedy     6-Crime
7-Drama      8-Family     9-Fantasy
10-History   11-Horror    12-Mystery
13-Romance   14-Sci-Fi    15-Thriller
16-War       17-Western   18-Exit
''')


    if select=="1": df=pd.read_csv("action.csv")
    elif select=="2": df=pd.read_csv("adventure.csv")
    elif select=="3": df=pd.read_csv("animation.csv")
    elif select=="4": df=pd.read_csv("biography.csv")
    elif select=="5": df=pd.read_csv("comedy.csv")
    elif select=="6": df=pd.read_csv("crime.csv")
    elif select=="7": df=pd.read_csv("drama.csv")
    elif select=="8": df=pd.read_csv("family.csv")
    elif select=="9": df=pd.read_csv("fantasy.csv")
    elif select=="10": df=pd.read_csv("history.csv")
    elif select=="11": df=pd.read_csv("horror.csv")
    elif select=="12": df=pd.read_csv("mystery.csv")
    elif select=="13": df=pd.read_csv("romance.csv")
    elif select=="14": df=pd.read_csv("scifi.csv")
    elif select=="15": df=pd.read_csv("thriller.csv")
    elif select=="16": df=pd.read_csv("war.csv")
    elif select=="17": df=pd.read_csv("western.csv")
    else: break

    pd.set_option('display.max_rows', df.shape[0]+1)

    clear(1)

    pointSelect=input('''Choice Points Range
1-(0-10)    2-(8-10)  3-(7-8)
4-(6-7)     5-(5-6)   6-(4-5)
7-(0-4)     8-Enter Range
''')

    if pointSelect=="1": minp,maxp=0,10
    elif pointSelect=="2": minp,maxp=8,10
    elif pointSelect=="3": minp,maxp=7,8
    elif pointSelect=="4": minp,maxp=6,7
    elif pointSelect=="5": minp,maxp=5,6
    elif pointSelect=="6": minp,maxp=4,5
    elif pointSelect=="7": minp,maxp=0,4
    elif pointSelect=="8": minp,maxp=letmechoiceRate()
    else: minp,maxp=0,10

    clear(1)


    yearSelect=input('''Choice Year Range
1-(1900-2020) 2-(2015-2020)   3-(2010-2015)
4-(2005-2010) 5-(2000-2005)   6-(1990-2000)
7-(1900-1990) 8-Enter Range
''')

    if yearSelect=="1": miny,maxy=0,2020
    elif yearSelect=="2": miny,maxy=2015,2020
    elif yearSelect=="3": miny,maxy=2010,2015
    elif yearSelect=="4": miny,maxy=2005,2010
    elif yearSelect=="5": miny,maxy=2000,2005
    elif yearSelect=="6": miny,maxy=1990,2000
    elif yearSelect=="7": miny,maxy=0,1990
    elif yearSelect=='8': miny,maxy=letmechoiceYear()
    else: miny,maxy=0,2020

    clear(1)

    xtrSelect=input('''Choose a Extra Category
1-Action     2-Adventure  3-Animation
4-Biography  5-Comedy     6-Crime
7-Drama      8-Family     9-Fantasy
10-History   11-Horror    12-Mystery
13-Romance   14-Sci-Fi    15-Thriller
16-War       17-Western   18-Exit
0-No Extra Category

''')

    if xtrSelect=="0": extraCat=""
    elif xtrSelect=="1": extraCat="Action"
    elif xtrSelect=="2": extraCat="Adventure"
    elif xtrSelect=="3": extraCat="Animation"
    elif xtrSelect=="4": extraCat="Biography"
    elif xtrSelect=="5": extraCat="Comedy"
    elif xtrSelect=="6": extraCat="Crime"
    elif xtrSelect=="7": extraCat="Drama"
    elif xtrSelect=="8": extraCat="Family"
    elif xtrSelect=="9": extraCat="Fantasy"
    elif xtrSelect=="10": extraCat="History"
    elif xtrSelect=="11": extraCat="Horror"
    elif xtrSelect=="12": extraCat="Mystery"
    elif xtrSelect=="13": extraCat="Romance"
    elif xtrSelect=="14": extraCat="Sci-Fi"
    elif xtrSelect=="15": extraCat="Thriller"
    elif xtrSelect=="16": extraCat="War"
    elif xtrSelect=="17": extraCat="Western"
    else: extraCat=""

    clear(1)
    print("\n")
    print(df[(df["Rate"]>=minp) & (df["Rate"]<maxp) & (df["Year"]<maxy) & (df["Year"]>=miny) & (df["Category"].str.find(extraCat)>=0)][["Title","Rate","Category","Year"]])

    returnMenu=input("\n1-Main Menu\n2-Exit")
    if returnMenu=='2': break

clear(0)
