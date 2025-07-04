# webapp/services/tts_service.py

from gtts import gTTS
import io, base64

class TTSService:
    def __init__(self, lang_code: str):
        self.lang_code = lang_code

    def speak(self, text: str):
        tts = gTTS(text=text, lang=self.lang_code)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode()
        return f"<audio autoplay src='data:audio/mp3;base64,{b64}'></audio>"
