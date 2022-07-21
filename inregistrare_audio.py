import pyaudio
import wave


def preparing_audio_recording1():
    p = pyaudio.PyAudio()
    return p


def preparing_audio_recording2(FORMAT, channels, sample_rate, chunk):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    return stream


def starting_audio(stream, chunk, record_seconds, sample_rate):
    frames = []
    count = 0
    print("Starting audio recording")
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
        count += 1
        if count % 43 == 0:
            print("Recording audio...")
    return frames


def end_audio(stream, filename, channels, frames, sample_rate, FORMAT, p):
    print("Finishing audio recording!")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframesraw(b"".join(frames))
    # close the file
    wf.close()


def audio_recording_script():
    filename = "recorded.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 25
    try:
        preparing1 = preparing_audio_recording1()
        preparing2 = preparing_audio_recording2(
            FORMAT, channels, sample_rate, chunk)
        audio = starting_audio(preparing2, chunk, record_seconds, sample_rate)
        end_audio(preparing2, filename, channels, audio,
                  sample_rate, FORMAT, preparing1)
    except:
        print("There is no microphone detected!")
