# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FillFieldsDialog
                                 A QGIS plugin
 Fill Fields for all rows with the user specified values.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-02-12
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Kritim Bastola
        email                : kritimbastola2005@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.core import QgsProcessingMultiStepFeedback, QgsVectorLayer, QgsMessageLog, QgsVectorFileWriter, QgsProject

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'fill_fields_dialog_base.ui'))


class FillFieldsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(FillFieldsDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        destination_path = ""
        sci_name_field = ""
        
#        self.addParameter(QgsProcessingParameterVectorLayer('input_vector_file', 'Input Vector File', types=[QgsProcessing.TypeVectorPoint,QgsProcessing.TypeVectorPolygon], defaultValue=None))
#        self.addParameter(QgsProcessingParameterField('sci_name_field', 'Sci_name field', type=QgsProcessingParameterField.Any, parentLayerParameterName='input_vector_file', allowMultiple=False, defaultValue='sci_name'))
#        self.addParameter(QgsProcessingParameterString('species_binomial_name', 'Species Binomial Name', multiLine=False, defaultValue=''))
        
        self.input_toolButton.clicked.connect(self.tool_button_clicked)
        self.button_box.accepted.connect(self.button_box_clicked)
        
        
        
    def tool_button_clicked(self):
        
        destination_path, _ = QFileDialog.getOpenFileName(self, "Select Destination Folder")
            
        self.input_lineEdit.setText(destination_path)
            
    def button_box_clicked(self):
        
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        sci_name_field = sci_name_lineEdit.text()
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': parameters['sci_name_field'],
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'FORMULA': '@species_binomial_name',
            'INPUT': parameters['input_vector_file'],
            'OUTPUT': parameters['input_vector_file'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        #Get the output file path
        output_file_path = outputs['FieldCalculator']['OUTPUT']
        
        #Rewrite the input file with the output
        self.rewrite_input_file(destination_path, output_file_path)
        
    def rewrite_input_file(self, input_file_path, output_file_path):
        #Create a vector layer from the output file
        output_layer = QgsVectorLayer(output_file_path, "temporary_output", "ogr")
        
        #Check if the layer was loaded sucessfully
        if not output_layor.isValid():
            QgsMessageLog.logMessage("Error loading the output layer", "Fill Fields", QgsMessage.ERROR)
            return
            
        #Write the features from the output layer to the input file
        writer = QgsVectorFileWriter.writeASVectorFormat(output_layer, input_file_path, "UTF-8", output_layer.crs(), "ESRI Shapefile")
        
        #Check if the writing was successful
        
        if writer[0] != QgsVectorFileWriter.NoError:
            QgsMessageLog.logMessage("Error writing features to the input file", "Fill Fields", QgsMessageLog.ERROR)
        else:
            QgsMessageLog.logMessage("Features successfully written to the input file", "Fill Fields", QgsMessageLog.ERROR)
            
        QgsProject.instance().removeMapLayer(output_layer)
            
            
            
            
        
        
            
