import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            content = file.read().strip()
            if not content:
                return []  # If file is empty, return an empty list
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Corrupt or invalid JSON in youtube.txt, resetting file.")
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully.")

def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter video number to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            videos[index] = {'name': name, 'time': time}
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted_video = videos.pop(index)
            save_data_helper(videos)
            print(f"Deleted video: {deleted_video['name']}")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1) List all YouTube videos")
        print("2) Add a YouTube video")
        print("3) Update a YouTube video detail")
        print("4) Delete a YouTube video")
        print("5) Delete all videos")
        print("6) Exit")

        choice = input("Enter your choice: ")

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
                confirm = input("Are you sure you want to delete all videos? (y/n): ")
                if confirm.lower() == 'y':
                    videos.clear()
                    save_data_helper(videos)
                    print("All videos deleted.")
                else:
                    print("Operation cancelled.")
            case '6':
                print("Exiting YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid Choice. Please select a valid option.")

if __name__ == "__main__":
    main()


