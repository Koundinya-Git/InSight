import sys
import uselect
import time

def listen_for_commands():
    poll_obj = uselect.poll()
    poll_obj.register(sys.stdin, uselect.POLLIN)

    print("SYS:Pico Initialized and Listening...")

    while True:
        poll_results = poll_obj.poll(0)
        
        if poll_results:
            command = sys.stdin.readline().strip()
            
            if command:
                process_command(command)
        
        time.sleep(0.01)

def process_command(cmd_string):
    """
    Parses the incoming command and triggers the appropriate hardware response.
    Format is expected to be PREFIX:PAYLOAD (e.g., CMD:PING or VIB:L,255)
    """
    try:
        prefix, payload = cmd_string.split(":", 1)
    except ValueError:
        print(f"ERR:Malformed command format ({cmd_string})")
        return

    if prefix == "CMD" and payload == "PING":
        print("ACK:PONG")
        
    elif prefix == "SUB":
        print(f"SYS:Displaying subtitle -> {payload}")
        # TODO: Send payload to OLED driver
        
    elif prefix == "VIB":
        # e.g., VIB:L,255 (Left motor, max intensity)
        print(f"SYS:Triggering motor -> {payload}")
        # TODO: Send payload to PWM driver
        
    else:
        print(f"ERR:Unknown command prefix ({prefix})")

if __name__ == "__main__":
    listen_for_commands()