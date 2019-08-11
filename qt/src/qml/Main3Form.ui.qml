import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Window 2.2
import QtQuick.Layouts 1.2

Item {
    width: 400
    height: 400
    
    property alias button1: button1
    
    Button {
        id: button1
        anchors.centerIn: parent
        //x: 54
        //y: 297
        width: 136
        height: 44
        text: qsTr("Click me")
    }
}

