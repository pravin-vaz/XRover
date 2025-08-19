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
Download the git repository <br>

Ensure Python and pip are up-to-date 
```sudo apt install python3 -y 
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py```


Install RPi.GPIO
```sudo pip3 install RPi.GPIO```
