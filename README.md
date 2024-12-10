
```bash
sudo apt install python3-watchdog
sudo apt install python3-pandas

colcon build
source install/setup.bash
ros2 launch model_generator model_generator.launch.py data_path:=data_sheet_folder_path
```