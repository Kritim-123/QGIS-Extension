# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FillFields
                                 A QGIS plugin
 Fill Fields for all rows with the user specified values.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-02-12
        copyright            : (C) 2024 by Kritim Bastola
        email                : kritimbastola2005@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FillFields class from file FillFields.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .fill_fields import FillFields
    return FillFields(iface)