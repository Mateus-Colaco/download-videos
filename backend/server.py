import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from my_audio import downloadYouTube, transform_video2audio, cut_audio
app = Flask(__name__)
AUDIO = ''
FILE = ''
CORS(app, resources={r"/*": {"origins": "*"}})  # Para permitir requisições de outros domínios (CORS)

def processar(url):
    global AUDIO
    global FILE
    mp4 = downloadYouTube(url)
    FILE = mp4.replace('.mp4', '')
    AUDIO = transform_video2audio(mp4, mp4.replace("mp4", "mp3"))
    return {
        "status": "sucesso", 
        'mp3': mp4.replace("mp4", "mp3"), 
        'mp4': mp4 
    }


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    filename = filename.replace("mp4", "mp3")
    if filename in os.listdir('audios'):
        return send_file(f'audios/{filename}', as_attachment=True)
    else:
        return

@app.route('/download_cut/<filename>', methods=['GET'])
def download_file_cut(filename):
    filename = filename.replace("mp4", "mp3")
    filename = filename if '.mp3' in filename else f"{filename}.mp3"
    if filename in os.listdir('audios/processed'):
        print(filename)
        return send_file(f'audios/processed/{filename}', as_attachment=True)
    else:
        return


@app.route('/processar', methods=['POST'])
def processar_video():
    data = request.get_json()
    url = data.get('url')
    print(url)
    if not url:
        return jsonify({"status": "erro", "message": "URL não fornecida"}), 400
    resultado = jsonify(processar(url))
    print(resultado)
    return resultado


@app.route('/corte_audio', methods=['POST'])
def cortar_audio():
    global AUDIO
    data = request.get_json()
    print(request.get_data())
    import time
    time.sleep(30)
    try:
        filename = data['row']['filename']
        tempoInicial = data['row']['tempoInicial']
        tempoFinal = data['row']['tempoFinal']
        cut_audio(filename, tempoInicial, tempoFinal, AUDIO)
        return filename
    except: 
        print('Arquivo nao cortado')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5174)
