import librosa
import soundfile
import io

def add_clicks(f):
    x, sr = soundfile.read(io.BytesIO(f.read()))
    onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
    # kwargs for peak picking vis a vis librosa.util.peak_pick
    cowbell, _ = librosa.load('audio/cowbell.wav')
    clicks = librosa.clicks(frames=onset_frames, sr=sr, length=len(x), click=cowbell)
    fout = io.BytesIO()
    soundfile.write(fout, clicks + x, sr, format='WAV')
    print(f'sample rate: {sr}\nlength of file: {len(x)}')
    fout.seek(0)
    return fout
