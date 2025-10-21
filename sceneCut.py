# Este app ira realizar corte de cenas dos filmes.
# os cortes serao baseado no arquivo de legenda (SRT)

import os
import re
from moviepy import TextClip, VideoFileClip, afx
import words_db as wdb
import json

VIDEO_PATH = "./movies/Back.to.the.Future.1985.720p.BrRip.x264.YIFY.mp4"
SRT_PATH = "./movies/Back.to.the.Future.1985.720p.BrRip.x264.YIFY.srt"
OUT_DIR = "./cortes_curto_legenda"
MIN_DURATION = 2.5  # textos de minima duracao em segundos


def parse_timestamp(ts):
    '''transformando em segundos 1H = 3600s3h; 1min = 60seg, 1000ms = 1seg'''
    h, m, s_ms = ts.split(':')
    s, ms = s_ms.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def load_srt(srt_path):
    '''Carregar arquivo srt e dividir as falas'''

    # Carregando arquivo de legenda
    try:
        with open(srt_path, encoding="utf-8") as f:
            content = f.read()

    except UnicodeDecodeError:

        try:
            with open(srt_path, encoding="latin-1") as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(srt_path, encoding="cp1252") as f:
                content = f.read()

    # O arquivo tem divisoes de cada fala (0:cena ; 1:tempo; 2:legenda) é padrao do arquivo SRT
    # Vou separar esses dados com split e pegar o tempo
    blocks = content.strip().split("\n\n")
    subs = []

    for block in blocks:
        lines = block.splitlines()
        if len(lines) >= 3:
            start = parse_timestamp(lines[1].split(" --> ")[0])
            end = parse_timestamp(lines[1].split(" --> ")[1])
            text = " ".join(lines[2:])

            if (end-start) >= MIN_DURATION:
                subs.append((start, end, text))

    return subs


    
if __name__ == "__main__":

    os.makedirs(OUT_DIR, exist_ok=True) # criando diretorio de saida
    lenPath = len(os.listdir(OUT_DIR))

    data = load_srt(SRT_PATH)  


    jsonToSave = []
    for i in data:

        lenPath += 1 # Forma de numerar os arquivos de saida

        start, end, text = i

        dadosToSave = {
            'MOVIE': VIDEO_PATH.split('/')[-1],
            'START': start,
            'END': end,
            'TEXT': text
        }

        jsonToSave.append(dadosToSave) 

    print(jsonToSave)    

    wdb.save_words_db(jsonToSave)



    # clip = VideoFileClip(VIDEO_PATH).subclipped(start -0.5 ,end +0.5).with_effects([afx.AudioNormalize()])   
    # clip.write_videofile(os.path.join(OUT_DIR, f"{lenPath+1}_{VIDEO_PATH.split("/")[2]}.mp4"), codec="libx264", audio_codec="aac")
    
    
        
