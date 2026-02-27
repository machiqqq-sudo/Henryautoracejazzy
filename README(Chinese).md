# TurtleBot3 AutoRace Jazzy 模擬環境 🏎️

這是一個專為 ROS 2 Jazzy 打造的 TurtleBot3 AutoRace 模擬環境。修復了官方原本在 Jazzy 版本中缺失的模型、材質破圖問題，並整合了實體比賽規格的機器人與自動裁判大腦。

## 🌟 核心功能 (Features)
* **Jazzy 完美相容**：修復 Gazebo Harmonic 的 PBR 材質與物理引擎 Bug。
* **比賽規格 Burger**：手動植入 Camera (640x480, 30fps) 與光達感測器。
* **裁判大腦 (Manager)**：內建 10 秒定時自動升降平交道柵欄，方便演算法測試。
* **免編譯即插即用**：採用相對路徑架構，無需 `colcon build` 即可執行。

## 🚀 快速啟動 (Quick Start)

請確保您的系統已安裝 ROS 2 Jazzy 與 Gazebo Harmonic。

1. 複製本專案：
   `git clone https://github.com/machiqqq-sudo/Henryautoracejazzy.git`
2. 進入目錄：
   `cd Henryautoracejazzy`
3. 一鍵啟動：
   `ros2 launch ./autorace.launch.py`
