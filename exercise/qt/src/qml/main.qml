import QtQuick 2.4
import QtQuick.Window 2.2

import QtQuick.Controls 1.3
import QtQuick.Dialogs 1.2


Window {
    visible: true
    title: qsTr("Hello user")
    width: 500
    height: 400
 
    
    Main3Form {
        anchors.fill: parent
        button1.onClicked: messageDialog.show(qsTr("Don't click me. I'm shy."))
    }
    
    MessageDialog {
        id: messageDialog
        title: qsTr("Hey, you ~~")

        function show(caption) {
            messageDialog.text = caption;
            messageDialog.open();
        }
    }
}


