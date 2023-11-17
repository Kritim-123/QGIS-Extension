import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox #To show the pop-up
import shutil


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'new_empty_shape_file_dialog_base.ui'))

class CreateNewEmptySpeciesShapeFileDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CreateNewEmptySpeciesShapeFileDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        # Connect the tool button to the slot
        self.toolButton.clicked.connect(self.tool_button_clicked)

    def tool_button_clicked(self):
        # Getting the value from the Combo-Box
        current_value = self.comboBox.currentText()

        destination_path = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        self.lineEdit.setText(destination_path)

        current_directory = os.path.dirname(os.path.abspath(__file__))


        if current_value == "Point File":
            folder_name = "pointTemplate"
            folder_path = os.path.join(current_directory, folder_name)

        elif current_value == "Polygen File":
            folder_name = "polygonTemplate"
            folder_path = os.path.join(current_directory, folder_name)

        destination_path = os.path.join(destination_path, current_value)
        shutil.copytree(folder_path, destination_path)

        #Showing pop-up after the file has been downloaded
        msg = QMessageBox() # Creating an instance of the MessageBox
        msg.setWindowTitle("Sucess!") #Setting the title of the window
        msg.setText("You have succesfully download the file in the located folder.") # The actual message
        msg.setIcon(QMessageBox.Information) #sets the icon of the pop-up
        msg.setDetailedText("Go to location you previously selected to find the files.") #Gives information on where to find the files

        x = msg.exec_() # To display the message



if __name__ == '__main__':
    pass  # You may add your application entry point here
