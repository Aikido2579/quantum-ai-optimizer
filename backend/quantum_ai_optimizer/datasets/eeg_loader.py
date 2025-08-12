import mne

def load_sample_eeg():
    print("[EEG Loader] Downloading sample EEG dataset...")
    sample_data_raw_file = mne.datasets.sample.data_path() / "MEG" / "sample" / "sample_audvis_raw.fif"
    raw = mne.io.read_raw_fif(sample_data_raw_file, preload=True)
    print(f"[EEG Loader] Data loaded: {raw.info['nchan']} channels, {len(raw.times)} time points")
    return raw

def preprocess_eeg(raw):
    print("[EEG Loader] Applying band-pass filter (1–40 Hz)...")
    raw_filtered = raw.copy().filter(l_freq=1., h_freq=40.)
    return raw_filtered
