cmake_minimum_required(VERSION 3.0)

project(ch3_2)

set(CMAKE_CXX_FLAGS "-std=c++11")

include_directories( "/usr/include/eigen3" )

find_package (Eigen3 REQUIRED)
message(STATUS "Eigen3 library status:")
message(STATUS "    config: ${Eigen3_DIR}")
message(STATUS "    version: ${Eigen3_VERSION}")
message(STATUS "    libraries: ${Eigen3_LIBS}")
message(STATUS "    include path: ${Eigen3_INCLUDE_DIRS}")
INCLUDE_DIRECTORIES(${Eigen3_INCLUDE_DIR})

find_package(Pangolin REQUIRED)
message(STATUS "Pangolin library status:")
message(STATUS "    config: ${Pangolin_DIR}")
message(STATUS "    version: ${Pangolin_VERSION}")
message(STATUS "    libraries: ${Pangolin_LIBS}")
message(STATUS "    include path: ${Pangolin_INCLUDE_DIRS}")
INCLUDE_DIRECTORIES( ${Pangolin_INCLUDE_DIR} )

add_executable(ch3_2 src/main.cpp)
target_link_libraries( ch3_2 
    ${Pangolin_LIBRARIES} 
    ${Eigen3_LIBS})

install(TARGETS ch3_2 RUNTIME DESTINATION bin)
