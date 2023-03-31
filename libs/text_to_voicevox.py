import requests
import json 
import time 
import re 
import simpleaudio 

class TextToVoicevox:
    def __init__(self, speaker_id, max_retry):
        """_summary_

        Args:
            speaker_id (int): the speaker id of the VOICEVOX character
            max_retry (int): maximum limit of retry
        """
        self.base_url = "http://127.0.0.1:50021/"
        self.speaker_id = speaker_id
        self.max_retry = max_retry
    
    def _generate_query(self, text):
        """Generate query to synthesis audio

        Args:
            text (str): the text to read

        Raises:
            ConnectionError: error of connection

        Returns:
            (dict): query of the audio
        """
        query_input = {
            "text": text, "speaker": self.speaker_id
        }
        for _ in range(self.max_retry):
            r = requests.post(
                self.base_url + "audio_query",
                params=query_input, 
                timeout=(10.0, 300.0)
            )
            if r.status_code == 200:
                query = r.json()
                break 
            time.sleep(1)
        else:
            raise ConnectionError("maximum limit of retry", text, r.text)
        return query
    
    def _synthesis(self, query):
        """_summary_

        Args:
            query (dict): query of the audio

        Raises:
            ConnectionError: error of the audio

        Returns:
            _type_: _description_
        """
        synthesis_input = {
            "speaker": self.speaker_id
        }
        for _ in range(self.max_retry):
            r = requests.post(
                self.base_url + "synthesis",
                params=synthesis_input,
                data=json.dumps(query),
                timeout=(10.0, 300.0)
            )
            if r.status_code == 200:
                return r.content
            time.sleep(1)
        else:
            raise ConnectionError("Audio error: maximum limit of retry", r)
    
    def _text_to_voicevox(self, texts):
        """play audio

        Args:
            texts (str): input text
        """
        texts = re.split("(?<=！|。|？)",texts)
        play_obj = None 
        for text in texts:
            query = self._generate_query(text)
            voice_data = self._synthesis(query)
            if play_obj is not None and play_obj.is_playing():
                play_obj.wait_done()
            wave_obj = simpleaudio.WaveObject(voice_data,1,2,24000)
            play_obj = wave_obj.play()