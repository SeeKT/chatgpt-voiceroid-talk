import speech_recognition as sr 
import openai
import sys  
from libs.voice_to_text import VoiceToText
from libs.text_to_chatgpt import TextToChatGPT
from libs.text_to_voiceroid import TextToVoiceRoid

R = sr.Recognizer()
MIC = sr.Microphone()

def main():
    try:
        openai.api_key = sys.argv[1]
        seikasay_path = sys.argv[2]
    except ValueError:
        print('usage: python talk_with_voiceroid.py [your api key] [exe path]')
    
    chattalk = []
    setting = input("Do you want to add some settings to ChatGPT? y/n \n")
    if setting == "y" or setting == "Y":
        content = input("Setting: \n")
        chattalk.append(
            {"role": "system", "content": content}
        )
    
    texttochatgpt = TextToChatGPT(chattalk)
    
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
                break
            else:
                print("-"*50)
                print(f"You: {current_text}")
                message = texttochatgpt._text_to_chatgpt(current_text)
                print(f"ChatGPT: {message}")
                TextToVoiceRoid._text_to_voiceroid(seikasay_path, message)
                

if __name__ == '__main__':
    main()