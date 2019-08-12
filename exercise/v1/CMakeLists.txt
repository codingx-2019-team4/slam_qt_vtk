cmake_minimum_required(VERSION 3.0)

project(v1)

set(CMAKE_CXX_FLAGS "-std=c++11")

find_package(OpenCV 3.4.2 REQUIRED)

message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")
include_directories(${OpenCV_INCLUDES_DIRS})

FIND_PACKAGE( Boost COMPONENTS program_options REQUIRED )
message(STATUS "Boost library status:")
message(STATUS "    config: ${Boost_DIR}")
message(STATUS "    version: ${Boost_VERSION}")
message(STATUS "    libraries: ${Boost_LIBS}")
message(STATUS "    include path: ${Boost_INCLUDE_DIRS}")
INCLUDE_DIRECTORIES( ${Boost_INCLUDE_DIR} )

find_package (Eigen3 REQUIRED)
message(STATUS "Eigen3 library status:")
message(STATUS "    config: ${Eigen3_DIR}")
message(STATUS "    version: ${Eigen3_VERSION}")
message(STATUS "    libraries: ${Eigen3_LIBS}")
message(STATUS "    include path: ${Eigen3_INCLUDE_DIRS}")
INCLUDE_DIRECTORIES(${Eigen3_INCLUDE_DIR})

find_package(VTK REQUIRED)
INCLUDE_DIRECTORIES(${VTK_INCLUDE_DIR})
message(STATUS "VTK library status:")
message(STATUS "    config: ${VTK_DIR}")
message(STATUS "    version: ${VTK_VERSION}")
message(STATUS "    libraries: ${VTK_LIBS}")
message(STATUS "    include path: ${VTK_INCLUDE_DIRS}")


#INCLUDE_DIRECTORIES(${EIGEN3_INCLUDE_DIR})


#find_package(VTK REQUIRED)
#include_directories(${VTK_INCLUDES_DIRS})
#include(${VTK_USE_FILE})
find_package(PCL REQUIRED COMPONENTS common io)
INCLUDE_DIRECTORIES(${PCL_INCLUDE_DIRS})
link_libraries(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})
message(STATUS "PCL library status:")
message(STATUS "    config: ${PCL_DIR}")
message(STATUS "    version: ${PCL_VERSION}")
message(STATUS "    libraries: ${PCL_LIBS}")
message(STATUS "    include path: ${PCL_INCLUDE_DIRS}")






add_executable(v1 src/main.cpp)
target_link_libraries(v1 
    ${OpenCV_LIBS} 
    ${Boost_LIBS} 
    ${Eigen3_LIBS} 
    ${VTK_LIBS} 
    ${PCL_LIBRARIES})


install(TARGETS v1 RUNTIME DESTINATION bin)
