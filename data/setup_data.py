import os
import json

os.makedirs("data/raw", exist_ok=True)

# 1. Company Policies (Markdown)
policies_md = """# RoboTech Egypt - Official Company Policies (Updated 2026)

## About Us & Locations
RoboTech Egypt is an electronics and embedded systems supplier based in Cairo, Egypt. 
- Main Branch: 15 El-Tayaran Street, Nasr City, Cairo.
- Working Hours: Sunday to Thursday, 10:00 AM to 8:00 PM. Friday & Saturday: 12:00 PM to 6:00 PM.
- Contact Email: support@robotech-eg.com | Hotline: 19000.

## Shipping & Delivery Policy
- Cairo & Giza: Standard delivery takes 1 to 2 business days. Shipping fee is 60 EGP.
- Alexandria & Delta: Standard delivery takes 2 to 3 business days. Shipping fee is 85 EGP.
- Upper Egypt & Red Sea: Standard delivery takes 3 to 5 business days. Shipping fee is 120 EGP.
- Free Shipping: Available on all orders above 2,500 EGP across Egypt.
- Same-Day Delivery: Available only in Cairo and Giza for orders placed before 1:00 PM, for an extra fee of 110 EGP.

## Return & Refund Policy
- Customers can return unused items in their original sealed packaging within 14 days of delivery for a full refund.
- Defective or Dead-on-Arrival (DOA) items can be replaced or refunded within 30 days of delivery after inspection by our technical team.
- Non-Returnable Items: Soldered components, opened microcontrollers with bent pins, custom-cut wires, and 3D-printed custom parts cannot be returned unless proven defective upon arrival.
- Refunds are processed within 5 to 7 business days via the original payment method (Instapay, Vodafone Cash, or Credit Card).

## Warranty & Technical Support
- All development boards (Arduino, ESP32, Raspberry Pi) carry a 6-month local replacement warranty against manufacturing defects.
- Motors, sensors, and power supplies carry a 3-month warranty.
- Damage caused by reverse polarity, over-voltage, or short circuits voids the warranty immediately.
"""

with open("data/raw/company_policies.md", "w", encoding="utf-8") as f:
    f.write(policies_md)

# 2. Products Catalog (JSON)
products_data = [
  {
    "id": "PROD-001",
    "name": "ESP32-CAM Wi-Fi + Bluetooth Module with OV2640 Camera",
    "category": "Microcontrollers",
    "price_egp": 450,
    "in_stock": True,
    "description": "Low-cost ESP32-based development board with an onboard 2MP OV2640 camera and microSD card slot. Ideal for IoT, video streaming, and basic computer vision projects. Note: Does not have a built-in USB port; requires an external USB-to-TTL FTDI programmer or ESP32-CAM-MB shield to upload code."
  },
  {
    "id": "PROD-002",
    "name": "Arduino Mega 2560 Rev3 Clone (with USB Cable)",
    "category": "Microcontrollers",
    "price_egp": 850,
    "in_stock": True,
    "description": "ATmega2560-based microcontroller board with 54 digital input/output pins (15 PWM outputs), 16 analog inputs, and 4 hardware serial ports (UARTs). Perfect for complex robotics, 3D printers, and multi-sensor systems requiring more memory and pins than an Arduino Uno."
  },
  {
    "id": "PROD-003",
    "name": "L298N Dual H-Bridge DC/Stepper Motor Driver",
    "category": "Motor Drivers",
    "price_egp": 140,
    "in_stock": True,
    "description": "High-voltage, high-current dual full-bridge driver capable of driving two DC motors or one bipolar stepper motor. Operating voltage up to 35V and continuous current of 2A per channel. Includes onboard 5V regulator jumper."
  },
  {
    "id": "PROD-004",
    "name": "RPLIDAR A1M8 360-Degree 2D Laser Range Scanner",
    "category": "Sensors",
    "price_egp": 5200,
    "in_stock": False,
    "description": "Low-cost 360-degree 2D laser scanner (LIDAR) solution capable of taking up to 8,000 samples per second with a 12-meter range. Ideal for autonomous vehicle mapping, SLAM, and obstacle avoidance."
  },
  {
    "id": "PROD-005",
    "name": "12V 5A Switching Power Supply Adapter",
    "category": "Power",
    "price_egp": 320,
    "in_stock": True,
    "description": "Regulated AC-to-DC 12V 5A power brick with standard 5.5mm x 2.1mm DC barrel jack. Built-in over-current and short-circuit protection for powering high-torque motors and LED strips."
  }
]

with open("data/raw/products_catalog.json", "w", encoding="utf-8") as f:
    json.dump(products_data, f, indent=2)

# 3. Support FAQs (Text)
faqs_txt = """Q: How do I upload code to the ESP32-CAM if it has no USB port?
A: The ESP32-CAM does not include an onboard USB-to-Serial chip. To program it, you must either buy the ESP32-CAM-MB micro-USB shield, or connect a 3.3V/5V FTDI USB-to-TTL adapter to the U0R and U0T pins and bridge GPIO 0 to GND while flashing.

Q: My microcontroller smoked when I connected a 12V battery to the 5V pin. Can I replace it under warranty?
A: Unfortunately, no. Applying 12V directly to a 5V pin causes over-voltage damage, which is not covered by our 6-month manufacturing warranty.

Q: Do you offer discounts for university graduation projects?
A: Yes! Undergraduate students receive a 10% discount on orders over 3,000 EGP upon presenting a valid university ID at our Nasr City branch or emailing it to support@robotech-eg.com before ordering.

Q: How can I pay for my order?
A: We accept Cash on Delivery (COD) for orders under 5,000 EGP, as well as Instapay, Vodafone Cash, and Visa/Mastercard online or in-store."""

with open("data/raw/support_faqs.txt", "w", encoding="utf-8") as f:
    f.write(faqs_txt)

print("✅ Phase 1 Data Setup Complete! Check your 'data/raw/' folder.")