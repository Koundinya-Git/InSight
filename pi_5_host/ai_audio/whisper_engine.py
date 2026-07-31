import whisper
import numpy as np

class WhisperTranscriber:
    def __init__(self, model_size="medium"):
        print(f"SYS: Loading Whisper '{model_size}' model. This will take a moment...")
        # Loads the AI into the Raspberry Pi 5's memory
        self.model = whisper.load_model(model_size)
        print("SYS: Whisper Medium model loaded successfully.")

    def transcribe_audio_chunk(self, audio_data: np.ndarray):
        """
        Transcribes raw audio data into text.
        Takes the numpy array from mic_capture.py as input.
        """
        try:
            # fp16=False is required for standard CPU processing on the Pi 5
            result = self.model.transcribe(audio_data, fp16=False)
            
            # Extract and clean up the text
            text = result.get("text", "").strip()
            return text
            
        except Exception as e:
            print(f"ERR: Transcription failed: {e}")
            return ""
        