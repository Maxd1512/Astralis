WRO 2025 FUTURE ENGINEERS - Astralis
# Astralis
Github for WRO.
Welcome to the official repository of **Team Astralis**, participants in the World Robot Olympiad (WRO) 2025 under the Future Engineers category.
Here you'll find the full development journey of our autonomous robot — from initial concepts to final deployment. This includes technical schematics, code,
component details, and documentation of the engineering process behind our robot.

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
👥 Meet the Team

**Robert Măntălau**  
Age: 14 
School:
Hello! I'm Robert from Romania,and this is my second WRO season in which i am competing. I have previously competed in Future Inoovators. I have a passion about making robots and programming.
![WhatsApp Image 2025-05-31 at 19 30 35_a4d4b29c](https://github.com/user-attachments/assets/242c249c-581c-4a54-8377-0ed21059be7d)

**Dumitru Maximilian**
Age: 14
School:"Decebal" Theoretical School, Constanţa.
Hi! I am Maximilian from Romania, and this is my second season i am compeating in, previously competing in Future Innovators.
I have competed in many other competitons such as this one. I am passionate about Robotics and electronics.
![WhatsApp Image 2025-05-31 at 19 30 55_3c32aff5](https://github.com/user-attachments/assets/1f422bd9-9257-4ad6-86b1-da500ac2f081)


**Edi Haivas**  
Age: 14  
School:
Hi! My name is Edi from Romania, and this is my second WRO season, previously participating the Future Innovators Category.
Iam passionate about Robotics, Coding, and Technology.
![WhatsApp Image 2025-05-31 at 19 31 07_f8582e12](https://github.com/user-attachments/assets/d40bfefe-6c6a-4065-89cb-2d61a35c7454)


We are a team of young robotics enthusiasts with a passion for engineering, coding, and autonomous systems. This is our WRO 2025 project,
and we're excited to showcase our work in the Future Engineers category.

---
## 🎯 Challenge Overview

The WRO 2025 Future Engineers challenge requires us to develop an autonomous vehicle capable of navigating a dynamic, randomized racetrack using sensors and intelligent control systems. Our robot must:

- Complete multiple laps while detecting and responding to traffic signs.
- Perform a precise parallel parking maneuver at the end.

---
## ⚙️ Components

- Dual-Mode Wireless NIC
  
  ![wireless-ac8265-1](https://github.com/user-attachments/assets/e4c7223c-9c9f-4dcb-8ea8-81261553a3ee)
  
- Metal Gear Steering Servo

  ![4-550x550](https://github.com/user-attachments/assets/72add62d-3f78-4788-a811-b60b9dbcb9db)
  
- Dual High Power Metal Motor
  
  ![37mm-motor-with-gear-reduction](https://github.com/user-attachments/assets/9908b2ac-a674-4da1-8981-bcae9a912c33)


- Battery holder

![PH9274_3-x-aa-side-by-side-flat-battery-holder_89828](https://github.com/user-attachments/assets/94bf3fb5-b9ff-4697-b42e-3f6cc5349dfa)

  
- Sony IMX219 Sensor

  ![images (1)](https://github.com/user-attachments/assets/f48b255c-7672-40d9-b5ab-0acbf9377cfb)

  
- High Quality Non-Skid Tire

  ![images (2)](https://github.com/user-attachments/assets/9affc216-47e9-4679-b25b-b531a57a7081)

  
- NVIDIA Jetson Nano

  ![images (3)](https://github.com/user-attachments/assets/f4f76555-1cd6-4bf2-8487-6e0c5d0eab65)



---
## 🔧 Assembly Process

This section will detail our robot's mechanical assembly steps, including:

- Chassis preparation  
- Mounting motors and electronics  
- Cable management and layout  
- Power distribution setup

---
## 💰 Budget Overview

We’ve documented all hardware costs to ensure transparency and reproducibility. The breakdown includes electronics, structural parts, and 3D printing material.
---
## 🛑 Obstacle Management

Our robot uses computer vision to detect red and green signs:

- 🟥 Red: Stay on the right
- 🟩 Green: Stay on the left

The logic adjusts the robot’s path in real time based on the color signals detected via camera input.
---
## 📦 Project Structure



## How to Build it for Yourself
Simply go into **[src/code.ipnyb](src/code.ipnyb)** then upload it to your jetson's jupyter lab
# Model Used
![JetRacer AI Robot Car](3d/3dmodelshowcase.gif)
[![JetRacer AI Robot Car Kit](https://sketchfab.com/static/thumbnail.png)](https://sketchfab.com/3d-models/jetracer-ai-robot-car-kit-for-nvidia-jetson-a6e25e470de1425281f17aba1a721f7d)

# Showcase
Watch our robot in action:  
**[resources/media/showcase.mp4](resources/medila/showcase.mp4)**
