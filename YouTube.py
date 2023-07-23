# *******Download Youtube Video  ******
print()
greet = "██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░  ░░░       ██████╗░░█████╗░░██████╗░██████╗    \n██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗  ░░░       ██╔══██╗██╔══██╗██╔════╝██╔════╝    \n███████║█████╗░░██║░░░░░██║░░░░░██║░░██║  ░░░       ██████╦╝██║░░██║╚█████╗░╚█████╗░    \n██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║  ██╗       ██╔══██╗██║░░██║░╚═══██╗░╚═══██╗    \n██║░░██║███████╗███████╗███████╗╚█████╔╝  ╚█║       ██████╦╝╚█████╔╝██████╔╝██████╔╝    \n╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░  ░╚╝       ╚═════╝░░╚════╝░╚═════╝░╚═════╝░    \n"

greet1 = "█░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀    ▀▀█▀▀ █▀▀█    █▀▀▄ █▀▀ █░░░█    █░░▒█ █▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀▄ █▀▀    ▒█░░▒█ ░▀░ █▀▀▄ █▀▀ █▀▀█    ▒█▀▀▄ █▀▀█ █░░░█ █▀▀▄ █░░ █▀▀█ █▀▀█ █▀▀▄ ░▀░ █▀▀▄ █▀▀▀    █▀▀█ █▀▀█ █▀▀█\n█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀    ░░█░░ █░░█    █░░█ █▀▀ █▄█▄█    █▄▄▄█ █░░█ █░░█ ░▒█░░ █░░█ █▀▀▄ █▀▀    ░▒█▒█░ ▀█▀ █░░█ █▀▀ █░░█    ▒█░▒█ █░░█ █▄█▄█ █░░█ █░░ █░░█ █▄▄█ █░░█ ▀█▀ █░░█ █░▀█    █▄▄█ █░░█ █░░█\n░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀    ░░▀░░ ▀▀▀▀    ▀░░▀ ▀▀▀ ░▀░▀░    ░▒█░░ ▀▀▀▀ ░▀▀▀ ░▒█░░ ░▀▀▀ ▀▀▀░ ▀▀▀    ░░▀▄▀░ ▀▀▀ ▀▀▀░ ▀▀▀ ▀▀▀▀    ▒█▄▄▀ ▀▀▀▀ ░▀░▀░ ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░░▀ ▀▀▀▀    ▀░░▀ █▀▀▀ █▀▀▀\n"

print(greet)
print(greet1)

from pytube import YouTube 

link = str(input("enter your youtube video-link : "))  # link"

# get an YouTube object of this link on this below variable youtube
youtube = YouTube(link)

# get  youtube video title
print("youtube.title :=> ",youtube.title)

# get youtube video thumbnail
thumbnail = youtube.thumbnail_url   #print(youtube.thumbnail_url)
print("thumbnail :=> ",thumbnail)

# get all youtube_video download streams option comes with proper indexing starting with 0 and continue to last.
videos = youtube.streams.all() #All Format 


# get all audio download streams option comes with proper indexing starting with 0 and continue to last.
# videos = youtube.streams.filter(only_audio=True) #Audio format Only



my_video = list(enumerate(videos))
# print("my_video :=> ",my_video)

index = 0
for i in my_video:
    print("index_No : {index}",i,'\n')
    index +=1

index = int(input("enter your chosen download_Index number  :    "))

# download the video/audio based index number
videos[index].download()

print("         ✅ Downloaded Successfully        ")