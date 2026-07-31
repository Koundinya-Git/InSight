import machine
from drivers.ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

def wrap_text(text, max_chars_per_line=16):
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
            
    if current_line:
        lines.append(current_line.strip())
        
    return lines

def update_subtitle(text):
    display.fill(0) # Clear the screen with black pixels
    
    display.text("InSight CC:", 0, 0, 1)
    display.hline(0, 10, 128, 1) # Draw a dividing line under the header
    
    lines = wrap_text(text)
    y_offset = 15
    for line in lines:
        if y_offset < 64: # Prevent text from drawing off the bottom edge
            display.text(line, 0, y_offset, 1) # 1 = white pixels
            y_offset += 10
            
    display.show() 