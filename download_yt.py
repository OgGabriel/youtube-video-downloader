import pytube
import os
import time
from colorama import Fore, Style
import colorama
colorama.init()

banner = r"""
                              ___  _ _____                                                      
                              \  \///__ __\                                                     
                               \  /   / \                                                       
                               / /    | |                                                       
                              /_/     \_/                                                                                                                 
       ____  ____  _      _      _by kp____  ____  ____  _____ ____ 
      /  _ \/  _ \/ \  /|/ \  /|/ \   /  _ \/  _ \/  _ \/  __//  __\
      | | \|| / \|| |  ||| |\ ||| |   | / \|| / \|| | \||  \  |  \/|
      | |_/|| \_/|| |/\||| | \||| |_/\| \_/|| |-||| |_/||  /_ |    /
      \____/\____/\_/  \|\_/  \|\____/\____/\_/ \|\____/\____\\_/\_\
                                                                    

"""

# sample url = "https://www.youtube.com/watch?v=HZrSpgWBAJU"

found = []

def getVideo(url):
    video = pytube.YouTube(url)
    print(Fore.RED + " ! Unable to get video (probably due to copyright)" if video.streams==None else Fore.GREEN + " > Connected to "+ Fore.YELLOW + video.title)
    choice = input(Fore.LIGHTYELLOW_EX+" ? Do you want the whole video or just de audio? (video/audio) ")
    print(" ")
    if "v" in str(choice):
        for stream in video.streams:
            if "video" in str(stream):
                found.append(str(stream).replace("<","").replace(">",""))
        print(Fore.GREEN + " > Found " + str(len(found)) + " results for video downloading:")
        for x in range(len(found)):
            print(Fore.LIGHTYELLOW_EX+ f" #{str(x)} {found[x]}")
        print(" ")
        itag=int(input(Fore.LIGHTYELLOW_EX+" ? Which one do you want to download? (select by itag) "))
        strm = video.streams.get_by_itag(itag)
        print(" ")
        print(Fore.GREEN + " > Downloading file in " + os.getcwd())
        strm.download(output_path=os.getcwd(),filename=video.title)
        print(Fore.GREEN+" > "+Fore.YELLOW+f"{video.title}"+Fore.GREEN+" successfully downloaded!")
    if "a" in str(choice):
        for stream in video.streams:
            if "audio" in str(stream):
                found.append(str(stream).replace("<","").replace(">",""))
        print(Fore.GREEN + " > Found " + str(len(found)) + " results for audio downloading:")
        for x in range(len(found)):
            print(Fore.LIGHTYELLOW_EX+ f" #{str(x)} {found[x]}")
        print(" ")
        itag=int(input(Fore.LIGHTYELLOW_EX+" ? Which one do you want to download? (select by itag) "))
        strm = video.streams.get_by_itag(itag)
        print(" ")
        print(Fore.GREEN + " > Downloading file in "+ Fore.YELLOW + f'"{os.getcwd()}\"')
        strm.download(output_path=os.getcwd(),filename=video.title)
        print(Fore.GREEN+" > Successfully downloaded "+Fore.LIGHTYELLOW_EX+video.title)
        print(" ")
        

def main():
    print(Fore.LIGHTYELLOW_EX + banner)


if __name__ == "__main__":
    os.system("cls")
    os.system("title YouTube video Downloader")
    main()
    url = [item for item in input(Fore.LIGHTYELLOW_EX + " ? What are the videos' url? (split them with commas) ").split(', ')]
    for k in range(len(url)):
        getVideo(url[k])
    print(Fore.RED + " ! Done. Clossing application in 5 seconds...")
    time.sleep(5)
    exit()