from pydub import AudioSegment
from moviepy.editor import *
from pytube import YouTube


def cut_audio(filename: str, start: str, end: str, audio):
    """
    CORTA O AUDIO DE ACORDO COM A NECESSIDADE 
    E GRAVA NA PASTA DE AUDIOS PROCESSADOS
    """
    start = ms(start)
    end = ms(end)
    filename = filename if '.mp3' in filename else f"{filename}.mp3"
    audio[start: end].export(f'audios/processed/{filename}')
    return f'audios/processed/{filename}'


def downloadYouTube(videourl) -> str:
    """
    FAZ O DOWNLOAD DO ARQUIVO COMO MP4 E RETORNA O CAMINHO RELATIVO PARA ELE
    """
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    path = yt.get_highest_resolution().download('videos')
    return path.split('\\')[-1]


def MP4ToMP3(mp4, mp3):
    """
    TRANSFORMA O ARQUIVO MP4 EM MP3 E GRAVA NO CAMINHO ESPECIFICADO POR 'mp3'
    """
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()


def ms(tempo):
    """
    SCRIPT QUE TRANSFORMA TEMPO NO 
    FORMATO min:s PARA MILISSEGUNDOS
    """
    minutos, segundos = map(int, tempo.split(':'))
    total_milissegundos = (minutos * 60 + segundos) * 1000
    return total_milissegundos


def transform_video2audio(mp4, mp3):
    """
    REALIZA A TRANSFORMACAO DO ARQUIVO MP4 
    EM MP3 E GRAVA-O NA PASTA DE AUDIOS
    """
    mp4_path = f"videos/{mp4}"
    mp3_path = f"audios/{mp3}"
    MP4ToMP3(mp4_path, mp3_path)
    return AudioSegment.from_mp3(mp3_path)
