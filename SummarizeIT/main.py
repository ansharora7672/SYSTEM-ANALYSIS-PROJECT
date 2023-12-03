from youtube_transcript_api import YouTubeTranscriptApi
import os
from openAI import run
# This function will get the URL and return the transcrtipt in a textfile.
def get_youtube_transcript(counter):
    url = input("Enter URL code: ")
    

    # Find the index where the video ID starts
    start_index = url.index("https://www.youtube.com/watch?v=") + len("https://www.youtube.com/watch?v=")

    # Extract the video ID
    video_id = url[start_index:]

    print(f"The video ID is: {video_id}")
    filename = "transcript" + str(counter) + ".txt"
    srt = YouTubeTranscriptApi.get_transcript(video_id)
    with open(filename, "w") as file:
        text = ''
        for i in srt:
            text += i['text'] + "\n"
        
        file.write(text)
    return text
    # os.startfile("file.txt")


def read_counter():
    try:
        with open("counter.txt", "r") as file:
            counter = int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist yet, return 0 as the default value
        counter = 0
    return counter

def write_counter(counter):
    with open("counter.txt", "w") as file:
        file.write(str(counter))

def main():
    # Read the counter from the file
    counter = read_counter()

    # Display the current value of the counter
    print("Current Counter Value:", counter)
    
    transcript = get_youtube_transcript(counter)
    run(transcript)
    # Increment the counter
    counter += 1


    # Write the updated counter back to the file
    write_counter(counter)

if __name__ == "__main__":
    main()
