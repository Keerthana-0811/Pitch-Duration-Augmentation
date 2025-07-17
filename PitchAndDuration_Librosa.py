import os
import numpy as np
import librosa
import soundfile as sf

# Set your folder paths
input_folder = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/1_HI_High/M22"
output_folder = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/Librosa_Augmented/Pitch_and_Duration/High/M22"
os.makedirs(output_folder, exist_ok=True)

# Audio settings
sample_rate = 16000
bins_per_octave = 12
pitch_pm = 2  # max pitch shift in semitones (±2)
speed_min = 0.9
speed_max = 1.1

# Process each .wav file
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        filepath = os.path.join(input_folder, filename)

        # Load audio
        y, sr = librosa.load(filepath, sr=sample_rate)

        # Random pitch shift
        pitch_change = pitch_pm * 2 * (np.random.rand() - 0.5)
        y_pitch = librosa.effects.pitch_shift(
            y=y, sr=sr, n_steps=pitch_change, bins_per_octave=bins_per_octave
        )

        # Random speed change
        speed_change = np.random.uniform(speed_min, speed_max)
        y_final = librosa.effects.time_stretch(
            y=y_pitch.astype("float64"), rate=speed_change
        )

        # Save augmented file
        output_path = os.path.join(output_folder, f"augmented_{filename}")
        sf.write(output_path, y_final, sr)

        print(
            f"{filename}: pitch_change = {pitch_change:.2f} semitones, speed_change = {speed_change:.2f}"
        )

print("✅ All audio files processed and saved to:", output_folder)
