# InSight: AI-Powered Smart Glasses

## Overview
Well, this is an intuitive assistive device designed to help the deaf, blind, and deaf-blind communities. By integrating AI and our hardware, we built a multi-layered approach to transforming how individuals with sensory impairments interact with the world.

## Key Features
* **Real-Time Subtitles:** Transcribe spoken words into clear text on a high-contrast OLED screen using an MEMS microphone array and Whisper AI, allowing deaf users to fully participate in conversations .
* **Dynamic Obstacle Detection & Haptic Feedback:** Map obstacles in real-time (via HRCSO4 sensors), providing intuitive feedback through vibration motors. This is necessary for deaf-blind users to navigate safely as they have neither sight nor sound.
* **AI-Enhanced Lip-Reading:** Uses a RasPi 5MP RGB camera to enhance transcription accuracy in noisy or obscured environments.
* **Real-Time Auditory Warnings:** Bone-conduction headphones deliver GPS navigation cues and sound warnings directly to the user.

## Hardware Architecture
I used a dual-processor architecture to guarantee real-time performance without bottlenecking the AI inference.
1. **The Raspberry Pi 5 + Hailo 13 TOPS AI HAT:** Include to handle high-level processing. The Pi 5 runs the Whisper AI Medium engine for speech-to-text, while the Hailo NPU handles hardware-accelerated computer vision and lip-reading.
2. **Raspberry Pi Pico:** Acts as the real-time I/O controller, communicating with the Pi 5 over USB. It manages the OLED screen, continuously pings the ultrasonic sensors, and drives the haptic feedback motors instantly.

## Repository Structure
* `/pi_5_host/` - Python code for the Pi 5 (Audio stream, Whisper AI, Serial Bridge, HAILO Vision).
* `/pico_coprocessor/` - MicroPython code for the Pi Pico (Sensor polling, OLED driver, Motor PWM).
* `/docs/` - Architecture diagrams and point-to-point wiring guides.

## Getting Started
1. **Host Setup (Pi 5):** Navigate to `/pi_5_host/` and install dependencies using `pip install -r requirements.txt`. 
2. **Coprocessor Setup (Pico):** Flash the Pico with the official MicroPython `.uf2` firmware and upload the `/pico_coprocessor/` files using Thonny or VS Code (with the MicroPico extension).
3. **Execution:** Connect the Pico to the Pi 5 via standard USB. Execute `main.py` on the Pi 5 to initiate the system bridge and start the AI processes.

## Why It Matters
With a targeted production cost of approximately 15,000 INR per unit, InSight brings unprecedented cost-effectiveness to assistive technology, democratizing access for a wider population. We are not just building a device; we are building a future where technology is a fundamental tool for inclusivity, empowerment, and human flourishing.

## Note

Yeah, this project is still in dev, and definitely untested as I do not have parts.