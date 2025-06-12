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
School:  
Hello! I'm Robert from Romania, and this is my second WRO season. I previously competed in Future Innovators. I'm passionate about building robots and programming.  
![Robert](https://github.com/user-attachments/assets/242c249c-581c-4a54-8377-0ed21059be7d)

**Dumitru Maximilian**  
Age: 14  
School: "Decebal" Theoretical School, Constanţa  
Hi! I'm Maximilian from Romania, and this is my second WRO season. I previously competed in Future Innovators and have taken part in many similar competitions. I’m passionate about robotics and electronics.  
![Maximilian](https://github.com/user-attachments/assets/1f422bd9-9257-4ad6-86b1-da500ac2f081)

**Edi Haivas**  
Age: 14  
School:  
Hi! My name is Edi. I'm from Romania, and this is my second WRO season. I previously participated in the Future Innovators category. I'm passionate about robotics, coding, and technology.  
![Edi](https://github.com/user-attachments/assets/d40bfefe-6c6a-4065-89cb-2d61a35c7454)

---

## 🎯 Challenge Overview

The WRO 2025 Future Engineers challenge requires us to develop an autonomous vehicle capable of navigating a dynamic, randomized racetrack using sensors and intelligent control systems. Our robot must:

- Complete multiple laps while detecting and responding to traffic signs  
- Perform a precise parallel parking maneuver at the end

---

## ⚙️ Hardware Components

- Dual-Mode Wireless NIC  
  ![NIC](https://github.com/user-attachments/assets/e4c7223c-9c9f-4dcb-8ea8-81261553a3ee)

- Metal Gear Steering Servo  
  ![Servo](https://github.com/user-attachments/assets/72add62d-3f78-4788-a811-b60b9dbcb9db)

- High Power Metal Motor  
  ![Motor](https://github.com/user-attachments/assets/9908b2ac-a674-4da1-8981-bcae9a912c33)

- Battery Holder  
  ![Battery](https://github.com/user-attachments/assets/94bf3fb5-b9ff-4697-b42e-3f6cc5349dfa)

- Sony IMX219 Sensor  
  ![Sensor](https://github.com/user-attachments/assets/f48b255c-7672-40d9-b5ab-0acbf9377cfb)

- High Quality Non-Skid Tire  
  ![Tire](https://github.com/user-attachments/assets/9affc216-47e9-4679-b25b-b531a57a7081)

- NVIDIA Jetson Nano  
  ![Jetson Nano](https://github.com/user-attachments/assets/f4f76555-1cd6-4bf2-8487-6e0c5d0eab65)

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
| Jetson Nano Developer Kit    | $89.00                 | Entry-level AI computing platform               |
| 8MP IMX219 Camera Module     | $21.20                 | For computer vision                             |
| High Quality Non-Skid Tire   | $5.00                  | Durable racing tires                            |
| Metal Gear Steering Servo    | $10.00                 | For accurate steering                           |
| Dual High Power Metal Motor  | $15.00                 | Torque for movement                             |
| Battery Holder               | $3.00                  | Secure battery mounting                         |
| Dual-Mode Wireless NIC       | $10.00                 | Wireless communications                         |
| Miscellaneous Components     | $20.00                 | Wires, connectors, screws, etc.                 |
| **Total Estimated Cost**     | **$173.20**            |                                                 |

---

## 🛑 Obstacle Management

Our robot uses computer vision to detect red and green signs:

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

Watch our robot in action:  
**[resources/medila/showcase.mp4](resources/medila/showcase.mp4)**  
![Robot Showcase](resources/medila/showcase.gif)

---

## 🧠 Model Used

![JetRacer AI Robot Car](3d/3dmodelshowcase.gif)  
[🔗 JetRacer AI Robot Kit on Sketchfab](https://sketchfab.com/3d-models/jetracer-ai-robot-car-kit-for-nvidia-jetson-a6e25e470de1425281f17aba1a721f7d)

---

## 🙏 How to Build it for Yourself

Simply open **[src/code.ipynb](src/code.ipynb)** on your Jetson Nano via JupyterLab and follow the instructions inside each cell.

---
