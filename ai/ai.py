import librosa
import soundfile
import io


def add_clicks(f):
    x, sr = soundfile.read(io.BytesIO(f.read()))
    if x.shape[1] > 1:
        x = x[:, 0]
    o_env = librosa.onset.onset_strength(x, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, hop_length=128)
    cowbell, _ = librosa.load('audio/cowbell.wav')
    clicks = librosa.clicks(frames=onset_frames, sr=sr, length=len(x), click=cowbell)
    fout = io.BytesIO()
    soundfile.write(fout, clicks + x, sr, format='WAV')
    print(f'sample rate: {sr}\nlength of file: {len(x)}')
    fout.seek(0)
    return fout
