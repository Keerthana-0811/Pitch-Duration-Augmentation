# Pitch-Duration-Augmentation
This script applies both **pitch shifting** and **speed (duration) modification** to `.wav` audio files using the `librosa` library. It is designed to augment datasets for speech recognition, especially in multilingual or speech-impaired data scenarios.

# What It Does
- Loads `.wav` files from an input folder
- Applies **random pitch shifts** (±2 semitones)
- Applies **random speed changes** (0.9× to 1.1×)
- Saves the augmented audio to an output folder
- Prints the pitch and speed values used per file


# Folder Structure
pitch-duration-augmentation/
- pitch_duration_augmentation.py # Main Python script
-  README.md # This file
- .gitignore # (optional) To exclude large files or cache



# Setup Instructions
**1. Install Required Python Packages**

```bash
pip install librosa soundfile numpy
```

2.Modify Input and Output Paths
- input_folder = "/path/to/your/input/audio"
- output_folder = "/path/to/save/augmented/audio"

3.Adjust Parameters (Optional)
- pitch_pm = 2: Max pitch shift range (±2 semitones)
- speed_min = 0.9, speed_max = 1.1: Speed change range (90%–110%)
- sample_rate = 16000: Sampling rate used during loading

# Run the Script
python pitch_duration_augmentation.py

# Sample Output:
- M22_001.wav: pitch_change = -1.33 semitones, speed_change = 1.05
- M22_002.wav: pitch_change = 0.67 semitones, speed_change = 0.92

# Augmented files will be saved as:
- augmented_M22_001.wav
- augmented_M22_002.wav

# License
This project is intended for educational and research use only. All third-party libraries (e.g., librosa, soundfile) are under their respective open-source licenses.

# Acknowledgements
- librosa
- soundfile




 
