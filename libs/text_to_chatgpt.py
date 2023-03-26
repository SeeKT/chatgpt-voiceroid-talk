import openai
import datetime
import json 
import os 

class TextToChatGPT:
    def __init__(self, chattalk):
        """initialize

        Args:
            chattalk (list): the list of Chat
        """
        self.total_tokens = 0
        self.chattalk = chattalk
        self.historydir = 'history/'
        if not os.path.exists(self.historydir):
            os.makedirs(self.historydir)
    
    def _text_to_chatgpt(self, current_text):
        """_summary_

        Args:
            current_text (str): the input to ChatGPT

        Returns:
            (str): the output of ChatGPT
        """
        self.chattalk.append(
            {"role": "user", "content": current_text}
        )
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.chattalk
        )
        message = resp['choices'][0]['message']['content'].lstrip()
        self.total_tokens += resp['usage']['total_tokens']
        self.chattalk.append(
            {"role": "assistant", "content": message}
        )
        return message 

    def _save_talking(self):
        """save the history of talking 
        """
        current_time = datetime.datetime.now()
        suffix = current_time.strftime('%Y%m%d%H%M%S')
        history_file = self.historydir + 'history_{0}.json'.format(suffix)
        with open(history_file, 'w', encoding='utf-8') as fp:
            json.dump(self.chattalk, fp, indent=2, ensure_ascii=False)
        