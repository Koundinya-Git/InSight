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

## Images:

<img width="852" height="832" alt="image" src="https://github.com/user-attachments/assets/a016f98a-f5fc-40fd-a276-4789317e5923" />

<img width="948" height="702" alt="image" src="https://github.com/user-attachments/assets/7ef94ce4-52a9-4b45-9494-c2803ed2f6dc" />

<img width="1024" height="559" alt="Circuit_Diagram" src="https://github.com/user-attachments/assets/6e4cd7b5-3d9b-4311-9f0c-4d1dad6e0671" />


## Bill of Materials

## 🧾 Bill of Materials (BoM)
The following table outlines the complete hardware requirements for building the InSight smart glasses prototype from scratch, including core processing modules, vision/audio peripherals, sensors, and outsourced manufacturing costs.

| Item Name | Quantity | Notes/Specifications | Approximate Cost (INR) | Approximate Cost (USD) |
| :--- | :--- | :--- | :--- | :--- |
| Raspberry Pi 5 | 1 | 2GB Model should be enough, downgrading to Whisper Base | 7,500 | $80.00 |
| Raspberry Pi AI Kit | 1 | Hailo 13 TOPS M.2 HAT with PCIe cable | 7,500 | $80.00 |
| Raspberry Pi Pico | 1 | Micro-controller for I/O hub | 400 | $5.00 |
| 5MP RGB Camera Module | 1 | OV5647 with MIPI CSI ribbon cable | 500 | $6.00 |
| MEMS Microphone Array | 1 | USB plug-and-play (e.g., ReSpeaker) | 2,500 | $30.00 |
| USB GPS / GNSS Receiver | 1 | Standard USB dongle (e.g., u-blox VK-162) | 800 | $10.00 |
| Bluetooth Bone-Conduction Headphones | 1 | Generic wireless headphones | 1,500 | $18.00 |
| Ultrasonic Distance Sensors | 4 | RCWL-1601 (3.3V preferred) | 400 | $5.00 |
| 0.96" OLED Display | 1 | I2C SSD1306 module | 200 | $3.00 |
| Coin Vibration Motors | 2 | Standard 3V micro flat motors | 100 | $1.50 |
| Haptic Motor Drivers / MOSFETs | 2 | DRV2605L boards or 2N7002/IRLZ44N MOSFETs | 200 | $3.00 |
| High-Discharge Power Bank | 1 | 5V/5A Power Delivery (27W+) | 2,000 | $25.00 |
| USB-C Power Cable | 1 | Short, high-quality thick-gauge cable | 300 | $4.00 |
| Half-Size Solderless Breadboards | 2 | For initial circuit testing | 150 | $2.00 |
| Jumper Wire Kit | 1 | Mixed M-M, M-F, F-F dupont wires | 200 | $3.00 |
| Perfboard / Protoboard | 1 | For final soldered Pico connections | 50 | $1.00 |
| USB Data Cable | 1 | Short USB-A to Micro-USB/USB-C for Pico bridge | 150 | $2.00 |
| Hardware Fasteners | 1 | M2.5 brass standoffs and screws | 150 | $2.00 |
| FDM 3D Printing Service | 1 | For Pi 5 enclosure (PETG/ABS) | 500 | $6.00 |
| SLA / Resin 3D Printing Service | 1 | For lightweight glasses frame | 1,500 | $18.00 |
| **Total** | **26 Parts** | ~~~~~ | **26,600** | **$304.50** |


## Note

Yeah, this project is still in dev, and definitely untested as I do not have parts.
