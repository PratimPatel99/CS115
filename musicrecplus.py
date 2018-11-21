'''
Created on Nov 17, 2017

@author: 

I pledge my honor that I have abided by the Stevens Honor System

Liam King 
Pratim Patel
-ppate78
-lking2
'''
from cs115 import map, reduce
import sys

def userInterface(database):
    '''main menu for the program'''
    username = getUser()
    if username not in database:
        enterUserPreferences(username, database)
        
    while True:   
        print('Enter a letter to choose an option:')
        print('e - Enter preferences')
        print('r - Get recommendations')
        print('p - Show most popular artists')
        print('h - How popular is the most popular')
        print('m - Which user has the most likes')
        print('q - Save and quit')

        userInput = input()
       
        if userInput == 'e':
            database = enterUserPreferences(username, database)
        if userInput == 'r':
            getRecs(username, database)
        if userInput == 'p':
            popularArtists(database)
        if userInput == 'h':
            mostPopular(database)
        if userInput == 'm':
            mostLikes(database)
        if userInput == 'q':
            save_and_quit(database)

def enterUserPreferences(username, database):
    '''allows a user to enter his preferences'''
    database[username] = []
    userInput = input('Enter an artist you like (Press Enter to finish): ')
    while userInput != '':
        if userInput in database[username]:
            print('Cannot enter same artist')
            userInput = input('Enter an artist you like (Press Enter to finish): ')
        else:   
            database[username].append(userInput)
            userInput = input('Enter an artist that like (Press Enter to finish): ')
    return database

def popularArtists(database):
    '''Returns popular artists'''
    mostPopular = {}
    max = 1
    mostPopular_artists = []
    for user, artists in database.items():
        if user[-1] != '$':
            for i in artists:
                if i in mostPopular:
                    mostPopular[i] += 1
                    if mostPopular[i] > max:
                        max = mostPopular[i]
                else:
                    mostPopular[i] = 1
    if mostPopular == {}:
        print('Sorry, no artists found')
    else:
        for artist, frequency in mostPopular.items():
            if frequency == max:
                mostPopular_artists.append(artist)
        mostPopular_artists.sort() 
        printOnePerLine(mostPopular_artists)     
def mostPopular(database):
    '''returns most popular artists'''
    mostPopular = {}
    max = 1
    for user, artists in database.items():
        if user[-1] != '$':
            for i in artists:
                if i in mostPopular:
                    mostPopular[i] += 1
                    if mostPopular[i] > max:
                        max = mostPopular[i]
                else:
                    mostPopular[i] = 1
    if mostPopular == {}:
        print('No artists found')
    else:
        print(max)    

def mostLikes(database): 
    '''returns the most liked users'''  
    max = 0
    mostLikes = []
    for user, artists in database.items():
        if user[-1] != '$':
            if len(artists) > max:
                max = len(artists)
    for user, artists in database.items():
        if user[-1] != '$':
            if len(artists) == max: 
                mostLikes.append(user)
    if mostLikes == []:
        print('No user found')
    else:
        list.sort(mostLikes)
        printOnePerLine(mostLikes)
def save_and_quit(database):
    '''saves and quits'''
    handle=open("musicrecplus.txt", "w")
    for key, value in sorted(database.items()):
        if value == []:
            s = key + ':\n'
        else:            
            s = key + ':' + reduce(lambda s, t: s + ',' + t, value) +'\n'
            handle.write(s)
    handle.close() 
    sys.exit(0)           

def readInData():
    database={}
    try:
        handle = open("musicrecplus.txt", "r" )
        lines = handle.read().splitlines()
        handle.close()
        for line in lines:
        #print("line: ",line)
            parts=line.split(":")
            name=parts[0]
            artists=parts[1]
            database[name]=sorted(artists.split(","))
        #print(database)
    except:
        return database
    return database
        
def getUser():    
    print("Enter your name (put a $ symbol if you wish your music preference to remain private):")
    username=input()
    while username == '':
        print("Enter your name (put a $ symbol if you wish your music preference to remain private):")
        username=input()
    return username

def printOnePerLine(iterable):
    for thing in iterable:
        print(thing)      
        
def myMap(fn,iterable):
    ret = [0]*len(iterable)
    i=0
    for thing in iterable:
        ret[i]=fn(thing)
        i+=1
    return ret

def getRecs(user,database):
    '''reccomendations for users'''
    def compare(userArtists,otherArtists,otherUName):
        if otherUName[-1]=='$':
            return -1
        User = 0
        Other = 0
        score =  0
        while User<len(userArtists) and Other<len(otherArtists):
            aUser = userArtists[User]
            aOther = otherArtists[Other]
            if aUser == aOther:
                score+=1
                User+=1
                Other+=1
            elif aUser<aOther:
                User+=1
            else:
                Other+=1
        if len(userArtists)==score == len(otherArtists):
            return -1
        return score
    def diff(userArtists,otherArtists):
        User = 0
        Other = 0
        difference = []
        while User<len(userArtists) and Other<len(otherArtists):
            aUser = userArtists[User]
            aOther = otherArtists[Other]
            if aUser == aOther:
                User += 1
                Other += 1
            elif aUser<aOther:          
                User+=1
            else:
                difference.append(aOther)
                Other+=1
                
        if Other<len(otherArtists):
            difference.extend(otherArtists[Other:])
        return difference
    userArtists=database[user]
    ranked = sorted(myMap(lambda uname: (compare(userArtists, database[uname], uname), uname), database), reverse=True)
    if len(ranked) == 0 or ranked [0][0] == -1:
        print('No recommendations available at this time')
        return
    
    maxScore=ranked[0][0]
    Max=0
    for results in ranked:
        if maxScore != results[0]:
            break
        Max+=1
        
    artists=[]
    for i in range(Max):
        artists.extend(diff(userArtists,database[ranked[i][1]]))
    artists = sorted(artists)
    printOnePerLine(artists)

def main():
    database=readInData()
    userInterface(database)
main()
