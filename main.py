from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime

# Initialize temperature sensor
sensor_temp = ADC(4)
conversion_factor = 3.3 / 65535

# Setup LED and buzzer
LED = Pin(16, Pin.OUT)
buzzer = Pin(15, Pin.OUT)

# OLED setup
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Main loop
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    print("Temperature:", temperature)

    # Display temperature on OLED
    oled.fill(0)
    oled.text("Temp:", 0, 8)
    oled.text(str(round(temperature, 2)) + " C", 50, 8)
    oled.show()

    # Alert logic
    if temperature < 22:
        buzzer.high()
        LED.high()
    else:
        buzzer.low()
        LED.low()

    utime.sleep(2)
