# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GenerateSwmmInp
                                 A QGIS plugin
 This plugin generates SWMM Input files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-09
        copyright            : (C) 2023 by Jannik Schilling
        email                : jannik.schilling@posteo.de
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

__author__ = 'Jannik Schilling'
__date__ = '2023-05-09'
__copyright__ = '(C) 2023 by Jannik Schilling'


# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessingAlgorithm,
    QgsProcessingException,
    QgsProcessingParameterCrs,
    QgsProcessingParameterEnum,
    QgsCoordinateReferenceSystem,
    QgsProcessingParameterFolderDestination
)
import os
import shutil
import processing
pluginPath = os.path.dirname(__file__)


class GenerateDefaultFolder(QgsProcessingAlgorithm):
    """
    generates default data
    """

    # Constants
    SWMM_FOLDER = 'SWMM_FOLDER'
    SWMM_VERSION = 'SWMM_VERSION'
    TRANSFORM_CRS = 'TRANSFORM_CRS'

    def initAlgorithm(self, config):
        """
        inputs and output of the algorithm
        """

        self.addParameter(
            QgsProcessingParameterFolderDestination(
            self.SWMM_FOLDER,
            self.tr('Where should the default data be saved? Select/Create a folder')
            )
        )

        self.addParameter(
            QgsProcessingParameterEnum(
                self.SWMM_VERSION,
                self.tr("Default data for SWMM version..."),
                ['Test data set for SWMM 5.1','Test data set for SWMM 5.2', 'Empty layers'],
                defaultValue=1
            )
        )

        self.addParameter(
            QgsProcessingParameterCrs(
                self.TRANSFORM_CRS,
                self.tr('Desired CRS for the data set (default is epsg:25833)'),
                optional=True
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        data_save_folder = self.parameterAsString(parameters, self.SWMM_FOLDER, context)
        swmm_version_num = self.parameterAsEnum(parameters, self.SWMM_VERSION, context)
        transform_crs = self.parameterAsCrs(parameters, self.TRANSFORM_CRS, context)
        transform_crs_string = str(transform_crs.authid())
        if transform_crs_string == '':
            transform_crs_string = 'NA'

        if parameters['SWMM_FOLDER'] == 'TEMPORARY_OUTPUT':
            raise QgsProcessingException('The default data set needs to be saved in a directory (temporary folders won´t work). Please select a directoy')

        if not os.path.exists(data_save_folder):
            os.makedirs(data_save_folder)
            
        try:
            doc_file = os.path.join(pluginPath,'documentation','g_s_i_documentation_v_0_35.pdf')
            shutil.copy(doc_file, data_save_folder)
            feedback.setProgressText(self.tr('documentation file saved to folder '+data_save_folder))
            feedback.setProgress(1)
        except BaseException:
            raise QgsProcessingException(self.tr('Could not add documentation file to chosen folder'))

        data_path = os.path.join(pluginPath,'test_data','swmm_data')
        if swmm_version_num == 0: #5.1
            read_file = os.path.join(data_path,'Test_5_1.inp')
            create_empty = False
            version_prefix = '5_1'
        if swmm_version_num == 1: #5.2
            read_file = os.path.join(data_path,'Test_5_2.inp')
            create_empty = False
            version_prefix = '5_2'
        if swmm_version_num == 2: #empty
            read_file = os.path.join(data_path,'Test_empty.inp')
            create_empty = True
            version_prefix = 'empty'
            
        alg_params = {
            'DATA_CRS': QgsCoordinateReferenceSystem('epsg:25833'),
            'GEODATA_DRIVER': 1,  # GPKG
            'INP_FILE': read_file,
            'PREFIX': version_prefix,
            'SAVE_FOLDER': data_save_folder,
            'CREATE_EMPTY': create_empty,
            'TRANSFORM_CRS': transform_crs_string
        }
        subalg_outputs = processing.run('GenSwmmInp:ImportInpFile', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        return {}

    def name(self):
        return 'GenerateDefaultFolder'

    def shortHelpString(self):
        return self.tr(""" The tool generates a default swmm data set in a folder selected by the user. The documentation file for the plugin will be copied to the same folder\n
        Choosing a folder name such as \"swmm_data\" is recommended.\n
        The default layers (geopackages) are added to the QGIS project.\n
        You can edit layers and tables in the folder to create your first inp file with the second tool.
        """)

    def displayName(self):
        return self.tr('1_GenerateDefaultData')

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return ''

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return GenerateDefaultFolder()
