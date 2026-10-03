import random
import string


movie_list = ["John Wick" , "Mission Impossible" , "Interstaller" , "Jack Reacher"]

# Watch Movie Function
def watch_movie():
    user = input("\nEnter the movie name :").title()
    if user in movie_list:
        print(f"Movie found named {user}. You can watch the movie using the link bellow.\n")
        user = user.replace(" " , "_")
        random_id = ''.join(random.choices(string.ascii_letters + string.digits , k = 15))
        link = f"Watch -- https://{user.lower()}/" + random_id + "/.com"
        print(link)

        # user = input("Want to see another movie : ").title()
        # if user == "Yes" or user == 1 : 
        #     watch_movie()


    elif user not in movie_list:
        print("Movie is not found in the box !!\n")
        user = input("Wnat to see the movie list : ").title()
        number = len(movie_list)
        if user == "Yes":
            print(f"There are {number} movies in the box.\n{movie_list}")


# Download Movie Function
def download_movie():
    user = input("\nWhich movie do you want to download : ").title()
    if user in movie_list:
        print(f"Yes..!! Movie Found\nYou can download {user} by using the generated link.\n")
        user = user.replace(" " , "_")
        random_id = ''.join(random.choices(string.ascii_letters + string.digits , k = 15))
        link = f"Download -- https://{user.lower()}/" + random_id + "/.com"
        print(link)
    else:
        print(f"The movie {user} is not in the movie box !!\nWant to see the list of available movies.")


# Upload movie Function
def upload_movie():
    user = input("Enter the movie name you want to upload : ").title()
    movie_list.append(user)
    print(f"Your movie {user} is added to the movie box successfully ! ")


print("\nWelcome to movie box\n")

# Main Function
def main():
    while True:
        print("\n1 - Watch a Movie Online")
        print("2 - Download a movie")
        print("3 - Upload a Movie\n")

        user = input("What do you want : ")


        if user == "1" or user == "watch movie":
            print(watch_movie())
        elif user == "2" or user == "download":
            print(download_movie())
            break
        elif user == "3" or user == "upload":
            print(upload_movie())
        else : 
            print(f"You choose {user}. Please choose a valid number or option\n")

main()



