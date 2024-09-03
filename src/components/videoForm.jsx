import { useState } from 'react';
import axios from 'axios';

const VideoDownloadForm = () => {
  const [url, setUrl] = useState('');
  const [mp3File, setMp3File] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://192.168.0.111:5174/processar', { url });
      if (res.data.status === 'sucesso') {
        setMp3File(res.data.mp3);
      }
    } catch (error) {
      console.error('Erro ao processar a URL:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="videoUrl">URL do Vídeo:</label>
        <input
          type="url"
          id="videoUrl"
          name="videoUrl"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
          placeholder="Insira a URL do vídeo"
        />
        <button type="submit">Baixar Vídeo</button>
      </form>
      {mp3File && (
        <div>
          <a href={`http://192.168.0.111:5174/download/${mp3File}`} download>
            <button type="button">Baixar MP3</button>
          </a>
        </div>
      )}
    </div>
  );
};

export default VideoDownloadForm;
