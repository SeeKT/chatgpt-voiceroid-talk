import subprocess 
import sys 

class TextToVoiceRoid:
    @classmethod
    def _text_to_voiceroid(cls, path, text, cid='1707'):
        """Run SeikaSay2.exe

        Args:
            path (str): the path of exe file
            text (str): the text that VoiceRoid speaks
            cid (str, optional): the cid of VoiceRoid software. Defaults to '1707'.
        """
        res = subprocess.run([
            path, '-cid', cid, '-t', text
        ])
