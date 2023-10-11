import subprocess
import os



"""
def train():
    subprocess.run(svc pre-split -i tests\\dataset_raw\\inputVoice -o tests\\dataset_raw\\finishedVoice -l 10)

    subprocess.run(svc pre-resample)
    subprocess.run(svc pre-config)
    subprocess.run(svc pre-hubert)
    subprocess.run(svc train -t)
"""
#convert the mp4 into a wav file and save to a location in the file p


def infer(filename):
    subprocess.run('svc infer -m /Users/baazjhaj/HACKATHON/Translatica/combined/so-vits-svc-fork/logs/44k -c /Users/baazjhaj/HACKATHON/Translatica/combined/so-vits-svc-fork/logs/44k/config.json -na ' + '/Users/baazjhaj/HACKATHON/Translatica/combined/so-vits-svc-fork/'+filename, shell=True)