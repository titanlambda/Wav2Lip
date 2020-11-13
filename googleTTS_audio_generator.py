from logger import logger
import traceback
logger.info("Configuration loaded")

from google.cloud import texttospeech
from google.auth import compute_engine
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file("key.json")

# Audio generation
client = texttospeech.TextToSpeechClient(credentials=credentials)
client = client.from_service_account_json("key.json")

#text = request.args.get('text')
voice_language_code="en-IN"
voice_language_name="en-IN-Wavenet-C"
voice_gender=texttospeech.SsmlVoiceGender.MALE
voice_encoding=texttospeech.AudioEncoding.MP3


def generate_audio_tts(text, audio_path):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code=voice_language_code,name=voice_language_name,ssml_gender=voice_gender)
    audio_config = texttospeech.AudioConfig(audio_encoding=voice_encoding)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    logger.info("Audio synthetized")

    # The response's audio_content is binary.
    with open(audio_path, "wb") as out:
       out.write(response.audio_content)
       logger.info("Audio content written to file {}".format(audio_path))

if __name__ == '__main__':
	audio_path = "./output/audio.mp3"
	text = "YO YO, Honey Singh!"
	generate_audio_tts(text, audio_path)
