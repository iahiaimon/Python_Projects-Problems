

def watch_movie():
    movie_list = ["John Wick" , "Mission Impossible" , "Interstaller" , "Jack Reacher"]
    user = input("\nEnter the movie name :").capitalize()
    if user in movie_list:
        print(f"Movie found named {movie_list}.")

    else:
        print("Movie is not found in the box !!\nWant to see the list of movies ?")


print("\nWelcome to movie box\n")

while True:
    print("\n1 - Watch a Movie Online")
    print("2 - Download a movie")
    print("3 - Upload a Movie\n")

    user = input("What do you want : ")


    if user == "1" or user == "watch movie":
        print(watch_movie())
    elif user == "2" or user == "download":
        print("Download")
    elif user == "3" or user == "upload":
        print("Upload")
    else : 
        print(f"You choose {user}. Please choose a valid number or option\n")



