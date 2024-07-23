import openai
import whisper
import torchaudio
from elevenlabs import clone, generate, play, save
from elevenlabs import set_api_key
model="gpt-3.5-turbo"


messages = [
    {"role": "system", "content": "You are an AI assisstant, your task is to understand the user will say and respond according to that. After understanding, cinsider the user input as a prompt format."},
]
def chatbot(text):
    if text:
        messages.append({"role": "user", "content": text})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        return reply

model = whisper.load_model("medium")

def transcribe(audio):

    audio_read, _ = torchaudio.load(audio)
    torchaudio.save('./streaming.wav', audio_read, sample_rate=22050)
    #load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    text = result.text
    response = chatbot(text)
    return response

audio = "/content/test.mp3"
note = transcribe(audio)
#from playsound import playsound

# for playing note.wav file
#playsound('./note.mp3')
#print('playing sound using  playsound')

text = transcribe(audio)

voice = clone(
    name="clone",
    description="An old American male voice with a slight hoarseness in his throat. Perfect for news",
    files=["/content/test.mp3"]
    )

audio = generate(text=text, voice=voice)
output_mp3_filename = "output_voice.mp3"
save(audio,output_mp3_filename)

from IPython.display import Audio

# Replace 'output_voice.mp3' with your audio file's path
audio_file = '/content/output_voice.mp3'
Audio(audio_file)
