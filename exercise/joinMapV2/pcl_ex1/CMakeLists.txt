cmake_minimum_required(VERSION 2.8)

project(pcl_ex1)
set( CMAKE_CXX_FLAGS "-std=c++11 -O3" )


find_package( OpenCV 3 REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

include_directories( "/usr/include/eigen3/" )

find_package( Boost REQUIRED )
include_directories( ${Boost_INCLUDE_DIRS} )

find_package(VTK 7.1 REQUIRED)

find_package( PCL 1.8 REQUIRED common io visualization)
include_directories( ${PCL_INCLUDE_DIRS} )
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})



add_executable(${PROJECT_NAME} "main.cpp")
target_link_libraries(${PROJECT_NAME}
    ${OpenCV_LIBS}
    ${Boost_LIBS}
    ${Eigen3_LIBS}
    ${VTK_LIBS}
    ${PCL_LIBRARIES})

