import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable, TimerAction, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    # 取得當前這個 launch 檔所在的資料夾路徑 (GitHub 下載後的主目錄)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # 使用我們打包在資料夾裡的賽道與模型！
    world_path = os.path.join(current_dir, 'worlds', 'turtlebot3_autorace_2020.world')
    models_path = os.path.join(current_dir, 'models')
    
    sdf_path = os.path.join(current_dir, 'my_burger.sdf')
    manager_path = os.path.join(current_dir, 'autorace_manager.py')

    return LaunchDescription([
     
        # 1. 環境變數設定
       
        # 告訴 Gazebo：不要去官方找，來我這裡找修好的 3D 模型！
        SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', models_path),
        SetEnvironmentVariable('GZ_IP', '127.0.0.1'),
        
        # [for henry] Nvidia RTX 顯卡優化 (預設註解)
        # SetEnvironmentVariable('__NV_PRIME_RENDER_OFFLOAD', '1'),
        # SetEnvironmentVariable('__GLX_VENDOR_LIBRARY_NAME', 'nvidia'),
        # SetEnvironmentVariable('__EGL_VENDOR_LIBRARY_FILENAMES', '/usr/share/glvnd/egl_vendor.d/10_nvidia.json'),

      
        # 2. 啟動賽道 (Gazebo Harmonic)
    
        LogInfo(msg="🏎️ 正在啟動賽道..."),
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_path],
            output='screen'
        ),

     
        # 3. 延遲 5 秒後啟動車輛與大腦
      
        TimerAction(
            period=5.0,
            actions=[
                LogInfo(msg=" 正在啟動..."),
                ExecuteProcess(
                    cmd=['python3', manager_path],
                    output='screen'
                ),

                LogInfo(msg=" 正在召喚機器人..."),
                Node(
                    package='ros_gz_sim',
                    executable='create',
                    arguments=[
                        '-file', sdf_path, 
                        '-name', 'burger', 
                        '-x', '0.44', '-y', '-1.75', '-z', '0.01', '-Y', '0.0'
                    ],
                    output='screen'
                ),

                LogInfo(msg="建立 ROS-GZ 通訊橋樑..."),
                Node(
                    package='ros_gz_bridge',
                    executable='parameter_bridge',
                    arguments=[
                        '/cmd_vel@geometry_msgs/msg/Twist[gz.msgs.Twist',
                        '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
                        '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
                        '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
                        '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image',
                        '/camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo'
                    ],
                    output='screen'
                ),
                
                LogInfo(msg=" 準備就緒！(按 Ctrl+C 可安全關閉)")
            ]
        )
    ])