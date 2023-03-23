import speech_recognition as sr 

class VoiceToText:
    @classmethod
    def _voice_to_text(cls, source, r=sr.Recognizer()):
        """(1) voice source to text

        Args:
            r (class): Recognizer
            source (class): Microphone

        Returns:
            (str): from voice to text
        """
        try:
            print('Recording...')
            audio = r.listen(source)
            text = r.recognize_google(audio, language='ja-JP')
            return text 
        except sr.UnknownValueError:
            return 
        