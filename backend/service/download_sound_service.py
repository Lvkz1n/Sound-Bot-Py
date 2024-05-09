import os 
import re
from pytube import YouTube
from moviepy.editor import *

class DownloadSoundService:
    def downloadMusic(self, url, type):
        yt:YouTube = YouTube(url)
        yt:title = f"{yt.tittle}_{yt.length}"
        path = f"{os.path.dirname(os.path.realpath('__file__'))}/backend/sounds"

        if(type == "music"):
            ys = yt.srtreams.filter(only_audio=True)[0]
            ys.download(f"{path}")
            self.convertMp4toWav(path, self.removeSpecialCharacter(yt.title))
            return f"{path}/{self.removeSpecialCharacter(yt.title)}.wav"
        
         
     ys = yt.streams.filter(only_audio=false)[0]
     ys.download(f"{path}")
    
    return f"{path}/{self.removeSpecialCharacter(yt.title)}.mp4"


        def removeSpecialCharacter(self, text):
            text_witout_special = re.sub(r'^/w/s', '', text)
            return text_witout_special
        
        def convertMp4toWav(self, path, filename):
            video = AudioClip(os.path.join(f"{path}/{filename}.mp4"))
            video.write_audiofile(os.path.join(f"{path}/{filename}.wav"))
            os.remove f"{path}/{filename}.mp4"