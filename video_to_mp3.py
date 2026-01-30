import os 
import subprocess

files = os.listdir("VIDEOS")
os.makedirs("AUDIOS", exist_ok=True)

for file in files :
   print(file)
   tutorial_number = file.split(" - ")[0]
   file_name = file.split(" - ")[1].split(".")[0]
   #print(f"tutorial_number: {tutorial_number}, file_name: {file_name}")
   subprocess.run([
        "ffmpeg",
        "-nostdin",      
        "-y",
        "-i", f"VIDEOS/{file}",
        f"AUDIOS/{tutorial_number}_{file_name}.mp3"
    ]
    )
