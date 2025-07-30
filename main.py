import whisper
import cohere
import pyttsx3
import speech_recognition as sr


recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Say something:")
    audio_data = recognizer.listen(source)
    with open("input.wav", "wb") as f:
        f.write(audio_data.get_wav_data())


model = whisper.load_model("base")
result = model.transcribe("input.wav")
input_text = result["text"]
print(f"📝 You said: {input_text}")


co = cohere.Client("5v3JlhRLScJ7uTWH3zd1sYoWTKusBrJO9KL1enad")
response = co.generate(prompt=input_text, model="command", max_tokens=50)
reply = response.generations[0].text.strip()
print(f"🤖 Bot reply: {reply}")


engine = pyttsx3.init()
engine.say(reply)
engine.runAndWait()
