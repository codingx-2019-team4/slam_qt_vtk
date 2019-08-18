# ROS

<img src="https://github.com/codingx-2019-team4/slam_qt_vtk/blob/master/image%20/gazebo.png" align="right" width="360"/>

## ENV setting up

### Gazebo model
[model](http://data.nvision2.eecs.yorku.ca/3DGEMS/)
```
wget http://data.nvision2.eecs.yorku.ca/3DGEMS/data/furniture.tar.gz
tar -zxf furniture.tar.gz
cd furniture
cp -R * ~/.gazebo/models/
```

### Clone robot

follow this [repo](https://github.com/tony92151/Lemon_minibot) install info

### RUN mapping
```
roslaunch fireHouse fireHouse2_gazebo.launch
roslaunch minibot_simulation simulation_gmapping.launch
rosrun lemon_minibot_control keyboard_teleop.py
rosrun map_server map_saver -f ~/fireHouse
```

### TESTING point cloud to laser scan with map server
<img src="https://github.com/codingx-2019-team4/slam_qt_vtk/blob/master/image%20/gazebo2.png" align="right" width="360"/>
Need robot model from [this repo](https://github.com/tony92151/ros_DQN_guide_dog)
```
roslaunch fireHouse gazebo.launch
roslaunch fire_house point2scan.launch
roslaunch fire_house gmapping.launch
rosrun dog2 keyboard_teleop.py
rosrun map_server map_saver -f ~/depthfireHouse
```




