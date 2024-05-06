import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )


''')
def list_videos():
    cursor.execute("Select * from videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("insert into videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name , new_time):
    cursor.execute("Update videos SET  name = ?, time =?, WHERE id = ?",(new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROMM videos where id = ?",(video_id,))
    conn.commit()
def main():
    while True:
        print("\n Youtube Manager app with DB")
        print(" 1. List  a video")
        print(" 2. Add a video")
        print(" 3. Update a video")
        print(" 4. Delete a video")
        print(" 5. Exut App")
        choice = (input("Enter your choice:  "))

        if choice == '1':
            list_videos()
        elif choice == '2':
           name = input("Enter the video name: ")
           time = input("Enter the video time: ")
           add_video(name, time)
        
        elif choice == '3':
           video_id = input("Enter video id to update: ")
           name = input("Enter the video name:  ")
           time = input("Enter the video time:  ")
           update_video(video_id, name, time)

        elif choice == '4':
           video_id = input("Enter video id to delte: ")

           delete_video(video_id)
        
        elif choice == '5':
            break

        else:
            print("Invalid choice")


    conn.close()
if __name__ == "__main":
    main()