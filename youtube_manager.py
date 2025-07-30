import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
def list_all_videos(videos):
    for index,video in enumerate(videos,start = 1)
        print(f"{index}.")
def add_video(videos):
    pass
def update_video(videos):
    pass
def delete_video(videos):
    pass
def main():
    
    videos=load_data() 
    print(videos)
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1) List all youtube videos")
        print("2) add a youtube video")
        print("3)update a yt video detail ")
        print("4) delete a youtube video")
        print("5) delete the app")
        choice = input("Enter your choice")
        match choice:
            case '1':
                list_all_videos(videos) 
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')
if __name__ == "__main__":
    main()
