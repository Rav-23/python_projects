print("█░█ █▀▀ █░░ █░░ █▀█   █▄▄ █░█ █▀▄ █▀▄ █▄█ ░\n█▀█ ██▄ █▄▄ █▄▄ █▄█   █▄█ █▄█ █▄▀ █▄▀ ░█░ █\n")

import instaloader

#creating an instance of the Instaloader class
library = instaloader.Instaloader()

#get basic profile details of any instagram users
def getBasic_profile_details():
    profile_Id = input("Enter Your Instagram User_Id :- \n")
    # download profile photo
    # library.download_profile(profile_Id, profile_pic_only=True)
    profile = instaloader.Profile.from_username(library.context, profile_Id)
    print("User_Name : ",profile.username)
    print("User_Id : ", profile.userid)
    print("Number_Total_No_of_posts : ", profile.mediacount)
    print("My_total_followers_people_counts_are : ", profile.followers)
    print("This_peoples_are_following_my_profile : ", profile.followees)
    print("bio : ", profile.biography)
    print("External_URL : ", profile.external_url)
    print('\n')



# download social media content of your Instagram Id
def download_latest_five_posts_on_Instragram():
    user_Id = input("Enter your Instagram User_Id :- \n")
    
    library.download_profile(user_Id, profile_pic_only=True)
    # download profile pic on profile variable
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


if __name__ == '__main__':
    option = '0'
    while option !=3:
        option = input("Write Chosen Option Number :-  \n1) Get Basic details of any instragram account \n2) Download Latest Five posts and profile photo of any instagram user \n3) Exit This Aplication\n")
        if option == "1":
            getBasic_profile_details()
        elif option == "2":
            download_latest_five_posts_on_Instragram()
        elif option == "3":
            exit()
        else:
            print("wrong Input please try after Sometime")
