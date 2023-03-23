import openai

class TextToChatGPT:
    def __init__(self, chattalk):
        """initialize

        Args:
            chattalk (list): the list of Chat
        """
        self.total_tokens = 0
        self.chattalk = chattalk
    
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
