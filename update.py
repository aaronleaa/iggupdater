#comments are for future reference
from bs4 import BeautifulSoup, SoupStrainer
from pyunpack import Archive
import pathlib
import patoolib
import requests
import gdown
import os
import shutil

version = open("version.txt","r+")
curversion = version.readline()
version.close()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://igg-games.com/among-us-free-download.html"
urllist = []
keyword = 'drive'
links = ""
gid = ""

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, "html.parser")

#Adds all the bluemediafiles links
for link in soup.find_all('a'):
    urllist += [link.get('href')]

#Checks if program is up to date by reading heading of site
for link in soup.find_all('h1'):
    siteversion = link.string
    if curversion == siteversion:
        print("Your program is already up to date.")
        input("Press Enter to continue...")
        os.startfile('Among Us.exe')
        exit()

#Filters the bluemediafiles links to only contain 'Drive'
#so that only Google Drive link would be shown

#Note: This completely bypasses the bluemediafiles ads
for i in range(len(urllist)):
    if keyword in str(urllist[i]):
        links = (urllist[i].split("s://", )[1])
        gid = links.split("drive.google.com/file/d/", )[1]
        gid = gid.split("/view?usp=sharing", )[0]

#Opens the Google Drive download link
if gid != "":
    url2 = "https://drive.google.com/uc?id=" + gid
    page2 = requests.get(url2, headers=headers)
    data2 = page2.text
    keyword2 = '.rar'
    filetype = ""
    soup = BeautifulSoup(data2, "html.parser")
    #Obtains the file name of the file you are going to download
    #e.g. Among.Us.9.9.s.rar
    for link2 in soup.find_all('a'):
        if keyword2 in str(link2.string):
            filetype = link2.string
    #Downloads the file from Google Drive
    if filetype != "":
        print("The file is now downloading... Please wait.")
        print("Please do not close the application until it says Download Complete.")
        gdown.download(url2, filetype, quiet=False)
        #Extracts the downloaded .rar file
        Archive(filetype).extractall(".")
        #Renames the extracted .rar file
        os.rename((filetype.split(".rar", )[0]), "tempholder")
        #Moves extracted files to parent directory
        src = 'tempholder'
        dst = '.'
        filelist = []
        files = os.listdir(src)
        for filename in files:
            filelist.append(filename)
            fullpath = src + '/' + filename
            shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
        #Deletes the unextracted .rar file
        os.remove(filetype)
        #Deletes the tempholder folder
        os.rmdir(src)
        print("Download Complete.")
        #Writes to version.txt to update the text file with the heading
        #of the site, so that when the program is run again, it knows it
        #is already updated.
        version = open("version.txt", "w")
        version.write(siteversion)
        version.close()
        input("Press Enter to continue...")
        #Runs Among Us
        os.startfile('Among Us.exe')
    else:
        #Google Drive download quota exceeded
        print("Sorry, The file could not be downloaded.")
        print("It could be due to:")
        print("- Too many users have downloaded the file at this time.")
        print("- Google has deleted the file as it violated their Privacy & Terms.")
        print("")
        input("Press Enter to continue...")
else:
    #Unable to find Google Drive link from IGG-GAMES
    print("Google drive link is not available on IGG-GAMES.")
    print("The program is not able to update.")
    print("")
    input("Press Enter to continue...")


#Coded by Hana. Last updated 19 Sep
