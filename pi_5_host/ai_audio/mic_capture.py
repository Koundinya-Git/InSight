import pyaudio
import numpy as np

class MicCapture:
    def __init__(self, rate=16000, chunk_duration=3):
        self.rate = rate
        self.chunk_size = rate * chunk_duration 
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=4096)
        print("SYS: MEMS Mic capture initialized.")

    def get_audio_chunk(self):
        frames = []
        num_reads = int(self.chunk_size / 4096)
        
        for _ in range(num_reads):
            data = self.stream.read(4096, exception_on_overflow=False)
            frames.append(np.frombuffer(data, dtype=np.float32))
        
        audio_data = np.concatenate(frames, axis=0)
        return audio_data

    def close(self):
        """Shuts down the microphone stream safely."""
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()