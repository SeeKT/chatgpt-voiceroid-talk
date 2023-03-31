import speech_recognition as sr 
import openai
import argparse
import json  
from libs.voice_to_text import VoiceToText
from libs.text_to_chatgpt import TextToChatGPT
from libs.text_to_voicevox import TextToVoicevox 

R = sr.Recognizer()
MIC = sr.Microphone()

def main():
    parser = argparse.ArgumentParser(description='Talk with VOICEROID')
    parser.add_argument('api_key', help='OpenAI API key')
    parser.add_argument('-l', '--history', help='the path of chat history file')
    parser.add_argument('-s', '--speaker', default=3, help='the speaker id of the VOICEVOX character')
    parser.add_argument('-r', '--retry', default=20, help='maximum limit of retry')
    
    args = parser.parse_args()
    openai.api_key = args.api_key 
    
    if args.history is not None:
        # load chat history
        with open(args.history, 'r', encoding='utf-8') as fp:
            chattalk = json.load(fp)
    else:
        chattalk = []
    
    setting = input("Do you want to change or add some settings to ChatGPT? y/n \n")
    if setting == "y" or setting == "Y":
        # delete previous setting
        prev_settings = list(filter(lambda item: item['role'] == 'system', chattalk))
        if len(prev_settings) > 0:
            for prev in prev_settings:
                chattalk.remove(prev)
        content = input("Setting: \n")
        # add new setting
        chattalk.append(
            {"role": "system", "content": content}
        )
    
    texttochatgpt = TextToChatGPT(chattalk)
    texttovoicevox = TextToVoicevox(args.speaker, args.retry)
    
    with MIC as source:
        R.adjust_for_ambient_noise(source)
        while True:
            current_text = VoiceToText._voice_to_text(source, R)
            print("-"*50)
            if current_text == None:
                continue
            elif "終わります" in current_text:
                print("-"*50)
                print(f"The total amount of tokens is {texttochatgpt.total_tokens}.")
                texttochatgpt._save_talking()
                break
            else:
                print("-"*50)
                print(f"You: {current_text}")
                message = texttochatgpt._text_to_chatgpt(current_text)
                print(f"ChatGPT: {message}")
                texttovoicevox._text_to_voicevox(message)
                
                

if __name__ == '__main__':
    main()