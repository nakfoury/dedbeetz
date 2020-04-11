import io

import librosa
import numpy as np
import soundfile


def add_clicks(f):
    x, sr = soundfile.read(io.BytesIO(f.read()))
    if x.shape[1] > 1:
        x = x[:, 0]
    o_env = librosa.onset.onset_strength(x, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, hop_length=128)[1:-1]
    cowbell, _ = librosa.load('audio/cowbell.wav')
    clicks = librosa.clicks(frames=onset_frames, sr=sr, length=len(x), click=cowbell)
    fout = io.BytesIO()
    soundfile.write(fout, clicks + x, sr, format='WAV')
    print(f'sample rate: {sr}\nlength of file: {len(x)}')
    fout.seek(0)
    return fout


def read_formfile(f):
    x, sr = soundfile.read(io.BytesIO(f.read()))
    if x.shape[1] > 1:
        x = x[:, 0]
    return x, sr


def segment(x, sr):
    o_env = librosa.onset.onset_strength(x, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='samples')[1:]
    return np.split(x, onset_frames), onset_frames


def classify(seg):
    # YOUR CODE GOES HERE
    return 'cowbell'


def label_to_sound(label):
    kit1 = {
        'boots': '/path/to/boots',
        'cats': '/path/to/cats',
        'tss': 'path/to/tss',
        'cowbell': 'audio/cowbell.wav',
    }
    cowbell, _ = librosa.load(kit1[label])
    return cowbell


def insert_sound(cumulative_beat, next_beat):
    sound, onset = next_beat
    if onset + len(sound) > len(cumulative_beat):
        cumulative_beat = np.pad(cumulative_beat, (0, (onset + len(sound)) - len(cumulative_beat)))
    cumulative_beat[onset:onset+len(sound)] += sound
    return cumulative_beat


def write_fout_as_wav(x, sr):
    fout = io.BytesIO()
    soundfile.write(fout, x, sr, format='WAV')
    print(f'sample rate: {sr}\nlength of file: {len(x)}')
    fout.seek(0)
    return fout