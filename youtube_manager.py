import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)


# def list_all_videos(videos):
#     print("\n")
#     print("*" * 70)
#     for index, video in enumerate(videos, start=1):
#         print(f"{index}. {video['name']},Duration: {video['time']}")
#     print("\n")
#     print("*" * 70)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        if 'name' in video and 'time' in video:
            print(f"{index}. {video['name']}, Duration: {video['time']}")
        else:
            print(f"Invalid video format at index {index}: {video}")
    print("\n")
    print("*" * 70)

        

def add_video(videos):
   name= input("Enter video name :")
   time= input("Enter video time :")
   videos.append({"name":name,"time":time})
   save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video number to update"))
    if 1 <=index <= len(videos):
       name = input("enter the new Video name: ")
       time = input("enter the new Video time: ")
       videos[index-1] = {'name ': name, 'time': time}
       save_data_helper(videos)
    else:
        print("invalid index selected: ")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video no to be deleted: "))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid index selected")
def main():
    videos = load_data()




    while True:
        print("\n Youtube Manager | choose an option")
        print("\n 1. Search for a video")
        print(" 2. Add a video")
        print(" 3. Update a youtube Video details")
        print(" 4. Delete a youtube Video")
        print(" 5. Exit the app")
        choice = (input("Enter your choice:  "))
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                print("Exiting the app...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()
