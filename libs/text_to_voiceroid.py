import subprocess 
import sys 

class TextToVoiceRoid:
    @classmethod
    def _text_to_voiceroid(cls, path, text, cid):
        """Run SeikaSay2.exe

        Args:
            path (str): the path of exe file
            text (str): the text that VOICEROID speaks
            cid (str): the cid of VOICEROID software.
        """
        res = subprocess.run([
            path, '-cid', cid, '-t', text
        ])
