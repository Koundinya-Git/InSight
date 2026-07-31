import serial
import time
import threading

class PicoBridge:
    def __init__(self, port='COM3', baudrate=115200):
        try:
            self.conn = serial.Serial(port, baudrate, timeout=1)
            print(f"SYS: Connected to Pico on {port}")
            time.sleep(2)  
        except serial.SerialException as e:
            print(f"ERR: Failed to connect to Pico: {e}")
            self.conn = None

        self.running = True
        
        if self.conn:
            self.listener_thread = threading.Thread(target=self._listen, daemon=True)
            self.listener_thread.start()

    def send_command(self, prefix, payload):
        """Sends a formatted command string to the Pico."""
        if not self.conn:
            print("ERR: Cannot send command, no connection.")
            return
            
        command = f"{prefix}:{payload}\n"
        self.conn.write(command.encode('utf-8'))
        print(f"Host Sent -> {command.strip()}")

    def _listen(self):
        """Runs in the background, reading incoming lines from the Pico."""
        while self.running and self.conn:
            if self.conn.in_waiting > 0:
                try:
                    line = self.conn.readline().decode('utf-8').strip()
                    if line:
                        print(f"Pico Replied <- {line}")
                except Exception as e:
                    print(f"ERR: Serial read error: {e}")

    def close(self):
        """Safely shuts down the connection."""
        self.running = False
        if self.conn:
            self.conn.close()
            print("SYS: Connection closed.")

if __name__ == "__main__":
    bridge = PicoBridge(port='COM3') 
    
    if bridge.conn:
        print("\n--- Running Bridge Tests ---\n")
        
        bridge.send_command("CMD", "PING")
        time.sleep(1)
        
        bridge.send_command("SUB", "System Initialized")
        time.sleep(1)
        
        bridge.send_command("VIB", "L,255")
        time.sleep(1)
        
        print("\n--- Tests Complete ---\n")
        bridge.close()