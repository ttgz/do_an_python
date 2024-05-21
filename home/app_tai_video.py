import yt_dlp
 
def download_youtube_video(video_url, resolution="360p", filename=None, save_path="./video_da_tai_xuong"):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
        'outtmpl': f'{save_path}/{filename}.%(ext)s' if filename else f'{save_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return True
    except Exception as e:
        return False
    
 