# 👶🌡️ Embedded System Project: Baby Room Thermometer

- **Date:** 21/12/2023  
- **Supervisor:** Dr. Salman Alaraibi  
- **University:** American University of Bahrain (AUBH) 
- **Student:** Dana Barhoom  
- **ID:** A00200  

---

## 🧠 The Challenge

Newborns require their environment to be consistently warm, ideally **above 20°C**. However, it’s common for room temperatures to drop without notice, particularly when parents or guardians are away or asleep. The main challenge addressed in this project is ensuring that parents are **immediately alerted** if the baby’s room temperature falls below a safe threshold, even when they are not actively monitoring it.

---

## 💡 The Solution

This project introduces a **Baby Room Thermometer** that:

- Monitors room temperature in real time using the Raspberry Pi Pico’s internal temperature sensor.
- Displays the current temperature on an OLED screen.
- Uses a **buzzer** and **LED light** to **alert** parents when the temperature drops below **22°C**.
- Is designed with a **baby-friendly appearance**, resembling a decorative item (e.g., a flower), making it suitable for a nursery.
- Operates continuously by being plugged into a wall socket.

---

## 🔧 System Block Design

The system includes:

- **Input**: Built-in temperature sensor on the Raspberry Pi Pico (ADC Channel 4).
- **Processor**: Raspberry Pi Pico microcontroller.
- **Outputs**:
  - OLED Display: Shows current temperature in °C.
  - LED: Lights up when the room is too cold.
  - Buzzer: Sounds an alarm if the temperature drops below 22°C.

---

## 🧱 Hardware and Materials

| Component                  | Description                                           |
|---------------------------|-------------------------------------------------------|
| Raspberry Pi Pico         | Main microcontroller unit                            |
| OLED Display              | Shows the live temperature reading                   |
| Built-in Temperature Sensor | Internal temperature source on ADC channel 4      |
| LED                       | Visual alert when temp < 22°C                         |
| Buzzer                    | Audible alert when temp < 22°C                        |
| USB Cable                 | Powers the system                                     |
| Plastic Casing            | Durable, aesthetic housing for components             |

The system is powered via USB, connected to an AC wall adapter. The plastic casing ensures safety and visual appeal for use in a baby’s room.

---

## 💻 Software & Implementation

The software is implemented in **MicroPython** using two scripts:

### 1. `ssd1306.py`
This driver file supports the **SSD1306 OLED display** via I2C or SPI. It sets up the display parameters, buffer, and communication protocols.

### 2. `main.py`
This script:
- Reads the temperature using the internal ADC.
- Displays the result on the OLED.
- Activates the **LED** and **buzzer** if temperature < 22°C.

> See the `code` folder for full scripts.

---

## 🧪 Testing and Results

| Test Case | Description | Success Rate (1–10) |
|-----------|-------------|---------------------|
| 1         | OLED displays accurate temperature | 8 |
| 2         | LED and Buzzer activate at <22°C   | 10 |
| 3         | Full system integration (OLED + LED + Buzzer) | 7 |

Challenges included integrating all outputs with correct timing and signal management. After refinement, all systems functioned effectively.

---

## 🖼️ Prototype & Design

- Designed in a **flower shape** to appeal to babies and look decorative.
- Plastic casing was selected for durability and ease of manufacturing.
- Colorful and toy-like to blend into a baby’s room environment.

---

## 🔌 Powering

Powered via micro-USB connected to an AC outlet. No batteries are used, ensuring **continuous operation**.

---

## 🧩 Interface Overview

- **Digital Display (OLED)**: Continuously shows temperature in °C.
- **Alert System (LED + Buzzer)**: Activates when temperature drops below 22°C.

---

## 🚀 Future Work

- Add wireless alerts (e.g., Wi-Fi push notifications).
- Include temperature logging and history tracking.
- Support adjustable temperature thresholds via buttons or mobile interface.
- Upgrade the enclosure with commercial-grade materials.

---

## 🧠 Lessons Learned

- Gained experience with Raspberry Pi Pico and MicroPython.
- Learned to integrate multiple I/O devices (OLED, Buzzer, LED).
- Developed troubleshooting skills in real-time embedded systems.

---

## 📚 Citations

1. [Bodi-Tek Digital Thermometer](https://www.bodi-tek.com/products/room-thermometer-and-hygrometer)
2. [Purflo Baby Room Thermometer (Amazon UK)](https://www.amazon.co.uk/Purflo-Starlight-Changing-Temperature-Monitor/dp/B0763RQBX9)

---

## 📂 File Structure

```

Baby-Room-Thermometer/
│
├── ssd1306.py       # OLED driver
├── main.py          # Main temperature monitoring script
└── README.md        # Project documentation

```

---

### ✅ Summary

This Baby Room Thermometer provides a **practical**, **safe**, and **aesthetically pleasing** solution to help parents maintain a safe room temperature for their babies, combining real-time monitoring with immediate alerts via light and sound.
