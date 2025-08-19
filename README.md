# XRover
Experimental rover with some reality.<br>

## Requirements
Raspberry pi 3  <br>
Power adaptor (5v, 2.1A)  <br>
Kit set robot with 2 DC motors, L298N Motor controllers, Battery pack  <br>
Webcam  

## Installation
Install Jammy Jellyfish (Server image: https://cdimage.ubuntu.com/releases/jammy/release/) on the Pi  <br>
Install ROS2 Humble using instructions (https://docs.ros.org/en/humble/Installation.html) using the deb packages  <br>
Clone the git repository <br>
```git clone https://github.com/pravin-vaz/XRover.git```

### Ensure Python and pip are up-to-date <br>
```python
sudo apt install python3 -y 
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

### Install RPi.GPIO <br>
```python
sudo pip3 install RPi.GPIO
```

### Errors
No module named 'rclpy' (when you run rosHelloWorld.py) <br>
Run
```$ source /opt/ros/humble/setup.bash```

