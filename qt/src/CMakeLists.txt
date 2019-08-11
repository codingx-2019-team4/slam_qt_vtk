qt5_add_resources(qt_SRCS resources.qrc)


add_executable(qt main.cpp ${qt_SRCS})

target_link_libraries(qt Qt5::Qml Qt5::Gui)

