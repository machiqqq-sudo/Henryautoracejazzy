# 🏎️ TurtleBot3 AutoRace for ROS 2 Jazzy (Standalone Simulation)

![ROS 2](https://img.shields.io/badge/ROS_2-Jazzy-34ceeb.svg)
![Gazebo](https://img.shields.io/badge/Gazebo-Harmonic-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

[🇹🇼 切換至中文版 (Traditional Chinese)](#-turtlebot3-autorace-ros-2-jazzy-獨立模擬環境)

## 📌 Overview
This repository provides a fully customized and highly optimized **TurtleBot3 AutoRace 2020 simulation environment** specifically designed for **ROS 2 Jazzy** and **Gazebo Harmonic**. 

The official TurtleBot3 simulation packages currently face several deprecation and compatibility issues when migrating from Humble to Jazzy (e.g., broken textures, physics engine crashes, and missing camera sensors on the Burger model). This project resolves all these issues, providing a pure, standalone, "plug-and-play" environment without the need for complex `colcon build` processes.

## 🌟 Key Features
* **Zero-Build Architecture**: Uses dynamic relative paths (`os.path.dirname`). Just clone and launch. No `src` workspace or `colcon build` required for the simulation.
* **Gazebo Harmonic Ready**: Completely overhauled SDF models replacing old `<script>` materials with modern PBR tags (`<albedo_map>`, `<emissive>`), fixing all texture corruption on the track and traffic lights.
* **Customized Burger Bot (`my_burger.sdf`)**: Manually integrated a 640x480 (30fps) camera and LiDAR into the default Burger model to meet official AutoRace hardware specs.
* **Automated Referee Brain (`autorace_manager.py`)**: A standalone Python manager utilizing `gz topic` for reliable, timer-based control of level elements (e.g., automated tollgate and traffic lights), bypassing ROS 2 publisher sync drops.
* **Full Bridge Integration**: Pre-configured `ros_gz_bridge` for `/cmd_vel`, `/odom`, `/tf`, `/scan`, and `/camera/image_raw`.

## 🚀 Quick Start

### Prerequisites
Ensure you have the following installed on your Ubuntu 24.04 machine:
* ROS 2 Jazzy
* Gazebo Harmonic
* `ros-jazzy-ros2launch`

### Installation & Launch
```bash
# 1. Clone the repository
git clone [https://github.com/machiqqq-sudo/Henryautoracejazzy.git](https://github.com/machiqqq-sudo/Henryautoracejazzy.git)

# 2. Navigate to the directory
cd Henryautoracejazzy

# 3. Launch the simulation
ros2 launch ./autorace.launch.py
