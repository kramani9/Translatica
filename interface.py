import tkinter as tk
from tkinter import filedialog
import os
from dubber import dub
import random
from auto_inference import infer
from dubber import decode_audio

import subprocess

#expand this dictionary
language_codes = {
    "Spanish": "es-es",
    "English": "en"
}

def process_video(video_file, source_selected_language, target_selected_language):
    print(
        f"Processing {source_selected_language} video file: {video_file} in {target_selected_language} language")
    #now we run our exec file here
    #os.system('date +"Today is: %A %d %B"')
    outputname = "outputDir" + source_selected_language + "to" + target_selected_language + str(random.randint(1, 50000))

    file_loc = dub(
        video_file, outputname, language_codes.get(source_selected_language), language_codes.get(target_selected_language),
        storageBucket=None, phraseHints=[], dubSrc=False,
        speakerCount=1, voices={}, srt=False,
        newDir=False, genAudio=False, noTranslate=False)

    #ok now here we call the auto_inference file (from krishna) this will pass in the produced output file that is saved as outputname
    print(file_loc)
    #convert to wav
    inferenceDir = os.path.join(outputname, "inference")
    os.mkdir(inferenceDir)
    wav_file = os.path.join(inferenceDir, "wavfile"+outputname+".wav")
    decode_audio(file_loc, wav_file)
    print(wav_file)
    infer(wav_file)

    #load it with the outfile
    updated_wav_file = os.path.join(inferenceDir,"wavfile"+outputname+".out.wav")
    inference_video = os.path.join(inferenceDir,"final_inference_"+outputname+".mp4")
    replace_audio(video_file, updated_wav_file, inference_video)


    #now write a method that copies the video file, mutes it, and plays the sound as the wav file

from moviepy.editor import VideoFileClip, AudioFileClip

def replace_audio(mp4_file_path, wav_file_path, output_file_path):
    # Load the MP4 video clip
    video_clip = VideoFileClip(mp4_file_path)

    # Load the WAV audio clip
    audio_clip = AudioFileClip(wav_file_path)

    # Replace the audio of the video clip with the loaded WAV audio
    video_clip = video_clip.set_audio(audio_clip)

    # Write the modified video with the replaced audio to the output file
    video_clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

def upload_video():
    file_path = filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4")])
    if file_path:
        selected_video_label.config(text=f"Selected Video: {file_path}")


def process_button_clicked():
    video_file = selected_video_label.cget(
        "text").replace("Selected Video: ", "")
    source_selected_language = source_language_dropdown.get()
    target_selected_language = target_language_dropdown.get()
    process_video(video_file, source_selected_language, target_selected_language)


# Create the main window
root = tk.Tk()
root.title("Translatica")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1280  # Set your desired width
window_height = 832  # Set your desired height
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and configure widgets
select_source_language_label = tk.Label(root, text="Select Source Language:")
select_target_language_label = tk.Label(root, text="Select Target Language:")
source_language_options = ["English", "Spanish", "French", "Mandarin",
                    "Hindi", "Japanese", "Korean", "Punjabi", "German"]
target_language_options = ["English", "Spanish", "French", "Mandarin",
                    "Hindi", "Japanese", "Korean", "Punjabi", "German"]

source_language_dropdown = tk.StringVar()
source_language_dropdown.set(source_language_options[0])
source_language_menu = tk.OptionMenu(root, source_language_dropdown, *source_language_options)

target_language_dropdown = tk.StringVar()
target_language_dropdown.set(target_language_options[0])
target_language_menu = tk.OptionMenu(root, target_language_dropdown, *target_language_options)

selected_video_label = tk.Label(root, text="Selected Video: None")
upload_button = tk.Button(root, text="Upload Video", command=upload_video)
# Changed the command to process_button_clicked
process_button = tk.Button(root, text="Process Video",
                           command=process_button_clicked)

# Place widgets in the window
select_source_language_label.pack()
source_language_menu.pack()
select_target_language_label.pack()
target_language_menu.pack()
selected_video_label.pack()
upload_button.pack()
process_button.pack()

# Start the Tkinter main loop
root.mainloop()