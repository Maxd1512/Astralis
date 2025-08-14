# 🚀 Astralis

Welcome to the official repository of **Team Astralis**, participants in the World Robot Olympiad (WRO) 2025 under the Future Engineers category.

Here you'll find the full development journey of our autonomous robot — from initial concepts to final deployment. This includes technical schematics, code, component details, and documentation of the engineering process behind our robot.

---

## 📚 Table of Contents

- 👥 Meet the Team  
- 🎯 About the Challenge  
- 🤖 Robot Overview  
- ⚙️ Hardware Components  
- 🔧 Build and Assembly  
- 🛠️ Sensors & Power System  
- 💰 Budget Overview  
- 🛑 Obstacle Detection Strategy  
- 📦 Project Structure  
- 🦅 Showcase  
- 🙏 How to Build it for Yourself  

---

## 👥 Meet the Team

**Robert Măntălau**  
Age: 14  
School: Theoretical Highschool "Ovidius"
Hello! I'm Robert from Romania, and this is my second WRO season. I previously competed in Future Innovators. I'm passionate about building robots and programming. 
This is my first time participating in the second WRO season.
![Robert](https://github.com/user-attachments/assets/242c249c-581c-4a54-8377-0ed21059be7d)

**Dumitru Maximilian**  
Age: 14  
School: "Decebal" Theoretical School, Constanţa  
Hi! I'm Maximilian from Romania, and this is my second WRO season. I previously competed in Future Innovators and have taken part in many similar competitions. I’m passionate about robotics and electronics.  This is my first time participating i  the second phase of WRO.
![Maximilian](https://github.com/user-attachments/assets/1f422bd9-9257-4ad6-86b1-da500ac2f081)

**Edi Haivas**  
Age: 14  
School: ICHC
Hi! My name is Edi. I'm from Romania, and this is my second WRO season. I previously participated in the Future Innovators category. I'm passionate about robotics, coding, and technology. 
This is my first time participating in the second phase of WRO.
![Edi](https://github.com/user-attachments/assets/d40bfefe-6c6a-4065-89cb-2d61a35c7454)

---

## 🎯 Challenge Overview

The WRO 2025 Future Engineers challenge requires us to develop an autonomous vehicle capable of navigating a dynamic, randomized racetrack using sensors and intelligent control systems. Our robot must:

- Complete multiple laps while detecting and responding to traffic signs  
- Perform a precise parallel parking maneuver at the end

---

## ⚙️ Hardware Components

-   Open MV H7 Camera
  ![417EAJ1fqcL jpg_BO30,255,255,255_UF900,850_SR1910,1000,0,C_QL100_](https://github.com/user-attachments/assets/aef0fb11-0d3e-48e7-a669-152e25fceb5a)

- 30:1 gear motor 
  ![638130__54581](https://github.com/user-attachments/assets/bfb9bd4d-ed6f-46a7-b8f3-3c136bf82111)

- Arduino Nano ESP32 
  <img width="1000" height="1000" alt="bitmi-placa-de-dezvoltare-arduino-nano-esp32-programare-arduino-si-micropython-p3-555280" src="https://github.com/user-attachments/assets/bd48b85a-4561-44b4-ad1f-0d459dd1baae" />

- Battery Holder  
  ![71xTnwH0-dL _AC_SY200_QL15_](https://github.com/user-attachments/assets/35cdfa4f-e872-4d71-9146-b39d793efe16)

- hw123 IT6/MPU Sensor
  
  ![61Xr7VGOl1L _UF350,350_QL80_](https://github.com/user-attachments/assets/26a4aa5f-e899-4bac-bab0-1c515c43623c)

- High Quality Non-Skid Tire
  
  ![Tire](https://github.com/user-attachments/assets/9affc216-47e9-4679-b25b-b531a57a7081)

- Motor Driver L298N

  <img width="200" height="200" alt="resized-web-2d730ee3-ac86-43f0-856b-a11c51a82e91" src="https://github.com/user-attachments/assets/699c269b-483b-48a7-8b32-d0ab0027a5d9" />

- MG90S Servo Motor
  
  ![images (2)](https://github.com/user-attachments/assets/1a6e7300-5676-45ac-ba26-54b5a1f03544)



---

## 🔧 Build and Assembly

This section will detail our robot's mechanical assembly steps, including:

- Chassis preparation  
- Mounting motors and electronics  
- Cable management and layout  
- Power distribution setup

---

## 💰 Budget Overview

| Component                     | Estimated Price (USD) | Notes                                           |
|------------------------------|------------------------|-------------------------------------------------|
| Open MV H7 Camera            | $80.00                 | Great camera for colour detecting               |
| 30:1 gear motor              | $30.00                 | Moves the robot                                 |
| Car Wheel 44mm N20           | $5.00                  | Durable racing tires                            |
| MG90S Servo Motor            | $4.50                  | For accurate steering                           |
| Motor Driver L298N           | $3.50                  | Provides signal to the motors                   |
| Battery Holder               | $3.00                  | Secure battery mounting                         |
| MPU6050 Gyroscope            | $3.00                  | Know how much the robot has turned              |
| Miscellaneous Components     | $17.50                 | Wires, connectors, screws, etc.                 |
| **Total Estimated Cost**     | **$146.5**          
| Final Price                                     |

---

## 🛑 Obstacle Management

Our robot uses a smart camera to detect red and green colours:

- 🟥 **Red** → Stay on the **right**  
- 🟩 **Green** → Stay on the **left**

The robot adjusts its path in real-time based on color signals detected via its onboard camera system.

---
## 📦 Project Structure

```bash
Astralisfr/
├── 3d/                     # 3D model showcase and HTML page
│   ├── 3dmodelshowcase.gif
│   ├── model_showcase.html
│   └── README.md
├── resources/              # Static resources and media
│   ├── preview.png
│   └── medila/
│       ├── showcase.gif
│       └── showcase.mp4
├── src/                    # Code and development notebooks
│   └── code.ipynb
├── .git/                   # Git internals (hidden in repo view)
├── README.md               # Main README (you’re reading it!)
```
---

## 🦅 Showcase
Here is a short video showcasing how the robot works.


---

## 🧠 Model Used
Here are our 3D models used for this robot.


---

## 🙏 How to Build it for Yourself
Firstly. Take the base and your servo motor, screw the 8 cm bar 

---
          
