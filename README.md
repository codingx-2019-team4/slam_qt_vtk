# SLAM_QT_VTK

## ENV setting up
```
Ubuntu 16.04 LTS
```
### Tools

* [KDevelop IDE](https://www.kdevelop.org/)

* [OpenCV 3.4.2](https://github.com/opencv/opencv/releases/tag/3.4.2)

```
$ wget https://github.com/opencv/opencv/archive/3.4.2.tar.gz
$ tar -xzvf 3.4.2.tar.gz
$ cd opencv-3.4.2
$ mkdir build && cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=OFF ..
$ make -j8
$ sudo make install
``` 

* [vtk 7](https://vtk.org/)
``` 
$ wget https://www.vtk.org/files/release/7.1/VTK-7.1.1.tar.gz
$ tar -xzvf VTK-7.1.1.tar.gz
$ cd VTK-7.1.1 
$ mkdir build && cd build 
$ cmake ..
$ make -j8
$ sudo make install
``` 
* [pcl 1.9.1](http://pointclouds.org/)

```
$ sudo add-apt-repositor ppa:v-launchpad-jochen-sprickerhof-de/pcl
$ sudo apt-get update
$ sudo apt-get install libpcl-all
```
