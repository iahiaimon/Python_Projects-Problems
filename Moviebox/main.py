
movie_list = ["John Wick" , "Mission Impossible" , "Interstaller" , "Jack Reacher"]
# Watch Movie Function
def watch_movie():
    user = input("\nEnter the movie name :").title()
    if user in movie_list:
        print(f"Movie found named {user}.")

    else:
        print("Movie is not found in the box !!\nWant to see the list of movies ?")


def download_movie():
    user = input("\nWhich movie do you want to download : ")
    if user in movie_list:
        print(f"Yes..!! Movie Found\nYou can download {user} by using the generated link.")
    else:
        print(f"The movie {user} is not in the movie box !!\nWant to see the list of available movies.")

print("\nWelcome to movie box\n")

while True:
    print("\n1 - Watch a Movie Online")
    print("2 - Download a movie")
    print("3 - Upload a Movie\n")

    user = input("What do you want : ")


    if user == "1" or user == "watch movie":
        print(watch_movie())
    elif user == "2" or user == "download":
        print(download_movie())
    elif user == "3" or user == "upload":
        print("Upload")
    else : 
        print(f"You choose {user}. Please choose a valid number or option\n")



