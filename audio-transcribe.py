import os
import csv
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Define the user
user = "@queenstaralien"

# Define the path to the videos directory
videos_dir = "/Users/mainguyen/Downloads/Business_Project/videos/"

# Define the path to the existing video_info CSV file
csv_file = "/Users/mainguyen/Downloads/Business_Project/videos info/videos_transcription.csv"

# Create a set to store the existing video filenames from the CSV file
existing_videos = set()

# Check if the CSV file exists
if os.path.isfile(csv_file):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Add the existing video filenames to the set
        for row in reader:
            existing_videos.add(row[0])

# Create a list to store the missing video filenames
missing_videos = []

# Open the CSV file in append mode
with open(csv_file, "a", newline="") as file:
    writer = csv.writer(file)

    # Loop through the range of video numbers
    for video_number in range(0, 1500):
        # Construct the video file path
        video_filename = f"{user}-{video_number}.mp4"

        # Skip the transcription if the video filename already exists in the CSV file
        if video_filename[:-4] in existing_videos:
            print(f"Skipping transcription for {video_filename} (already in CSV)")
            continue

        video_path = os.path.join(videos_dir, video_filename)

        # Check if the video file exists
        if not os.path.isfile(video_path):
            missing_videos.append(video_filename)
            continue

        try:
            # Transcribe the video
            result = model.transcribe(video_path)
            transcription = result["text"]

            # Write the video filename and transcription to the CSV file
            writer.writerow([video_filename[:-4], transcription])

            # Print the transcription
            print(f"Transcription for {video_filename}:")
            print(transcription)
            print("-----------")

        except Exception as e:
            # Handle any error that occurs during transcription
            print(f"Error occurred during transcription for {video_filename}:")
            print(e)
            print("-----------")
            continue

# Print the missing videos
print("Missing videos:")
for missing_video in missing_videos:
    print(missing_video)

print("Transcription process completed.")
