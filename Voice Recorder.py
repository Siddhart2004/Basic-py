import pyaudio
import wave
format = pyaudio.paInt16 
channels = 1  
rate = 44100  
chunk = 1024  
rec_sec = 6 
output_file = "output.wav"  
audio = pyaudio.PyAudio()
st = audio.open(format=format, channels=channels,
                    rate=rate, input=True,
                    frames_per_buffer=chunk)

print("Recording...")
frames = []
for _ in range(0, int(rate / chunk * rec_sec)):
    data = st.read(chunk)
    frames.append(data)
print("Recording complete.")
st.stop_stream()
st.close()
audio.terminate()
with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
print(f"Audio saved Will be as {output_file}")