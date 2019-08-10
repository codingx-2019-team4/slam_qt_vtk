cmake_minimum_required(VERSION 3.0)

project(ch2)
set(CMAKE_CXX_FLAGS "-std=c++11")

include_directories( "/usr/include/eigen3" )



add_executable(ch2 src/main.cpp)

install(TARGETS ch2 RUNTIME DESTINATION bin)
