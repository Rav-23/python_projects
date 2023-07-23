print()
greet = "██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░  ░░░       ██████╗░░█████╗░░██████╗░██████╗    \n██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗  ░░░       ██╔══██╗██╔══██╗██╔════╝██╔════╝    \n███████║█████╗░░██║░░░░░██║░░░░░██║░░██║  ░░░       ██████╦╝██║░░██║╚█████╗░╚█████╗░    \n██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║  ██╗       ██╔══██╗██║░░██║░╚═══██╗░╚═══██╗    \n██║░░██║███████╗███████╗███████╗╚█████╔╝  ╚█║       ██████╦╝╚█████╔╝██████╔╝██████╔╝    \n╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░  ░╚╝       ╚═════╝░░╚════╝░╚═════╝░╚═════╝░    \n"
print(greet)


import instaloader

#creating an instance of the Instaloader class
library = instaloader.Instaloader()

#get basic profile details of any instagram users
def getBasic_profile_details():
    profile_Id = input("Enter Your Instagram User_Id : ")
    library.download_profile(profile_Id, profile_pic_only=True)
    profile = instaloader.Profile.from_username(library.context, profile_Id)
    print("User_Name : ",profile.username)
    print("User_Id : ", profile.userid)
    print("Number_Total_No_of_posts : ", profile.mediacount)
    print("My_total_followers_people_counts_are : ", profile.followers)
    print("This_peoples_are_following_my_profile : ", profile.followees)
    print("bio : ", profile.biography)
    print("External_URL : ", profile.external_url)
    print('\n')

#get tranding information of any keywords/#hashtags

def searchInformation():
    searchItem = input("Enter the Search keyword or hashtags\n")
    #provide your search_tags here
    search_Results = instaloader.TopSearchResults(library.context, searchItem)
    print('\n')

    # it will iterate over the extracted usernames
    for username in search_Results.get_profiles():
        print(username)

    print('\n')

    # it will iterate over the extracted #hashtags
    for hashtag in search_Results.get_hashtags():
        print(hashtag)

    print('\n')



# getBasic_profile_details()

# download social media content of your Instagram Id
def downloadSocialMediaContentFromInstragram():
    user_Id = input("Enter your Instagram User_Id :- \n")
    
    library.download_profile(user_Id, profile_pic_only=True)
    profile = instaloader.Profile.from_username(library.context, user_Id)

    # Retrieving all posts in an object
    posts = profile.get_posts()
    count = 0
    # print(profile)
    for index, post in enumerate(posts, 1):
        if count<5:
            library.download_post(post,target=f"{profile.username}_{index}")
            count += 1
        else:
            break


downloadSocialMediaContentFromInstragram()