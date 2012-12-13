"""
/***************************************************************************
Name			 	 : Pysal Tools
Description          : Pysal plugin for QGIS
Date                 : 06/Nov/12 
copyright            : (C) 2012 by ASU's GPH 498/598
email                :  
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
import resources
import os.path, sys

# Set up current path, so that we know where to look for modules
currentPath = os.path.dirname( __file__ )
sys.path.append( os.path.abspath( os.path.dirname( __file__) + '/tools') )

# import tools
# import localMoran, weights
<<<<<<< HEAD
import localMoran, doAbout, globalgearyDialog, globalMoran
=======
import localMoran, doAbout, globalGearyC
>>>>>>> 7e47fedecdd0383a3f7864b03b9642bbbb50751c
import weightsFromShapefile

class Pysal: 

  def __init__( self, iface ):
    # Save reference to the QGIS interface
    self.iface = iface

  def getThemeIcon( self, icon ):
    settings = QSettings()
    pluginPath = QString( os.path.dirname( __file__ ) )
    themePath = QString( "icons" ) + QDir.separator() + QString( settings.value( "/Themes" ).toString() ) + QDir.separator() + QString( icon)
    defaultPath = QString( "icons" ) + QDir.separator() + QString( "default" ) + QDir.separator() + QString( icon )
    if QFile.exists( pluginPath + QDir.separator() + themePath ):
      return QIcon( ":" + themePath )
    elif QFile.exists( pluginPath + QDir.separator() + defaultPath ):
      return QIcon( ":" + defaultPath )
    else:
      return QIcon()

  def updateThemeIcons( self, theme ):
    self.esdaMenu.setIcon( QIcon ( self.getThemeIcon( "esda.png" ) ) )
    self.weightsMenu.setIcon( QIcon (self.getThemeIcon( "weights.png" ) ) )
    # self.localAutoMenu.setIcon( QIcon (self.getThemeIcon( "lam.png" ) ) )
    # self.globalAutoMenu.setIcon( QIcon (self.getPysalIcon( "gam.png" ) ) )

    self.moransGlobal.setIcon( QIcon (self.getThemeIcon( "mg.png" ) ) )
    self.moransLocal.setIcon( QIcon (self.getThemeIcon( "ml.png" ) ) )
    self.geary.setIcon( QIcon (self.getThemeIcon( "geary.png" ) ) )
    self.getis.setIcon( QIcon (self.getThemeIcon( "getis.png" ) ) )
    self.wfc.setIcon( QIcon (self.getThemeIcon( "mat.png" ) ) )
    self.pysalAbout.setIcon( QIcon (self.getThemeIcon( "about.png" ) ) )


  def initGui(self):  
    # Create action that will start plugin configuration
    # self.action = QAction(QIcon("home/everett/.qgis/python/plugins/Pysal/pysal.png"), \ "PySAL", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.iface, SIGNAL( "currentThemeChanged( QString )" ), self.updateThemeIcons ) 
    
    self.menu = QMenu()    
    self.menu.setTitle( QCoreApplication.translate( "PySAL" , "&PySAL" ) )

    self.esdaMenu = QMenu( QCoreApplication.translate( "PySAL" , "&ESDA" ), self.iface.mainWindow() )
    self.moransLocal = QAction( QCoreApplication.translate( "PySAL" , "Local &Moran's I" ), self.iface.mainWindow() )
    self.moransGlobal = QAction( QCoreApplication.translate( "PySAL" , "Global Moran's &I" ), self.iface.mainWindow() )
    self.geary = QAction( QCoreApplication.translate( "PySAL" , "Geary's &C" ),self.iface.mainWindow() )
    self.getis = QAction( QCoreApplication.translate( "PySAL" , "Getis and Ord's &G" ),self.iface.mainWindow() )
    self.esdaMenu.addActions( [self.moransLocal, self.moransGlobal, self.geary, self.getis] )

    self.weightsMenu = QMenu( QCoreApplication.translate( "PySAL" , "&Weights" ), self.iface.mainWindow() )
    self.wfc = QAction( QCoreApplication.translate( "PySAL" , "&Weights from Contiguity" ), self.iface.mainWindow() )
    self.weightsMenu.addActions( [self.wfc] )

    self.pysalAbout = QAction( QCoreApplication.translate( "PySAL" , "&About PySAL" ), self.iface.mainWindow() )

    self.updateThemeIcons("theme")

    # add submenus under main Pysal menu
    self.menu.addMenu( self.esdaMenu )
    self.menu.addMenu( self.weightsMenu )
    self.menu.addSeparator()
    self.menu.addAction( self.pysalAbout )
        
    # add actions to submenus, other actions will be added to the list here
 
    menu_bar = self.iface.mainWindow().menuBar()
    actions = menu_bar.actions()
    lastAction = actions[ len( actions ) - 1 ]
    menu_bar.insertMenu( lastAction, self.menu )

    # assign methods to actions
    QObject.connect( self.moransLocal, SIGNAL("triggered()"), self.localMoran ) 
    QObject.connect( self.moransGlobal, SIGNAL("triggered()"), self.globalMoran ) 
    QObject.connect( self.wfc, SIGNAL("triggered()"), self.matweight )    
    QObject.connect( self.wfc, SIGNAL("triggered()"), self.matweight )    
    QObject.connect( self.geary, SIGNAL("triggered()"), self.globalGearyC )  
    #QObject.connect( getis, SIGNAL("triggered()"), self.globalGetis )
    QObject.connect( self.pysalAbout, SIGNAL("triggered()"), self.about )

  def unload(self):
    # Remove the plugin menu item and icon
    # self.iface.removePluginMenu("&Pysal",self.action)
    # self.iface.removeToolBarIcon(self.action)
    # del self.toolBar
    del self.menu
 
  def localMoran( self ):
    d = localMoran.localMoranDialog ( self.iface )
    d.exec_()

<<<<<<< HEAD
  #def globalmoran( self ):
  #  d = globalAuto.gaDialog ( self.iface, 1 )
  #  d.exec_()

  def globalMoran( self ):
    d = globalMoran.globalMoranDialog ( self.iface )
    d.exec_()

=======
>>>>>>> 7e47fedecdd0383a3f7864b03b9642bbbb50751c
##  def globalGeary( self ):
##    d = doSumLines.Dialog ( self.iface )
##    d.exec_()

  def globalGearyC(self): 
    d=globalGearyC.globalGearyCDialog(self.iface)
    d.exec_()    

  def matweight( self ) :
    d = weightsFromShapefile.weightsdialog( self.iface )
    d.exec_()

  def about( self ):
    d = doAbout.Dialog (self.iface )
    d.exec_()

