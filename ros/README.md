# ROS

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

### RUN
```
roslaunch fireHouse fireHouse2_gazebo.launch
roslaunch minibot_simulation simulation_gmapping.launch
rosrun lemon_minibot_control keyboard_teleop.py
rosrun map_server map_saver -f ~/fireHouse
```




