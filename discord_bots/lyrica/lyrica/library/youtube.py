from pytubefix import YouTube
from io import BytesIO
from pydub import AudioSegment
import ffmpeg
import subprocess
from googleapiclient.discovery import build
import os 


def youtube_player(youtube_url):  
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True,file_extension='webm').first()
    print(audio_stream)
    
    buffer = BytesIO()
    audio_stream.stream_to_buffer(buffer)
    buffer.seek(0) 
    
    audio_segment = AudioSegment.from_file(buffer, format="webm")
    
    wav_buffer = BytesIO()
    audio_segment.export(wav_buffer,format="wav")
    wav_buffer.seek(0)
    return wav_buffer
 
    # with BytesIO() as audio_file:
    #     audio_segment.export(audio_file, format="wav")
    #     audio_file.seek(0)
        
    #     process = subprocess.Popen(
    #         ['ffplay', '-nodisp', '-autoexit', '-'],
    #         stdin=subprocess.PIPE
    #     )
    #     process.communicate(input=audio_file.read())
        

youtube_data = build('youtube','v3',developerKey=os.getenv('LYRICA_YT'))    
def youtube_lookup(keywords, max_results=10):
    request = youtube_data.search().list(
        q=keywords,
        part='snippet',
        type='video',
        maxResults = max_results
    )
    response = request.execute()
    
    return {x+1:{'title':i['snippet']['title'],'author':i['snippet']['channelTitle'],'url':f"https://www.youtube.com/watch?v={i['id']['videoId']}"}for x,i in enumerate(response['items'])} 

    # for item in response['items']:
    #     title = item['snippet']['title']
    #     video_id = item['id']['videoId']
    #     author = item['snippet']['channelTitle']
        
    #     print(f'Title: {title}')
    #     print(f'Author: {author}')
    #     print(f'url: https://www.youtube.com/watch?v={video_id}')
        
# results = youtube_lookup('Tell it to my heart')

# for i in results:

#     print(f"{i} - {results[i]['title']}\nBy: {results[i]['author']}\n")
    
    
    
        

# youtube_url = "https://www.youtube.com/watch?v=M8KHrlhDNIY"
# youtube_player(youtube_url)


