"""SSD1351 demo (images)."""
from time import sleep
from ssd1351 import Display
from machine import Pin, SPI

def test():
    """Test code."""
    spi = SPI(0, baudrate=14500000, sck=Pin(18), mosi=Pin(19))  # Using machine.SPI directly
    display = Display(spi, dc=Pin(14), cs=Pin(21), rst=Pin(7))  # Adjust pin assignments

    print("Displaying RaspberryPiWB128x128.raw image...")
    display.draw_image('RaspberryPiWB128x128.raw', 0, 0, 128, 128)

    sleep(10)

    display.cleanup()

test()
