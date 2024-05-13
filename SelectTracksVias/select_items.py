# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SelectItems
###########################################################################

class SelectItems ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_CLOSE, title = u"Select Tracks & Vias", pos = wx.DefaultPosition, size = wx.Size( 316,341 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Track width (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( ( 20, 0), 1, wx.EXPAND, 5 )

		self.m_trackWidth = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		bSizer2.Add( self.m_trackWidth, 0, wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Track layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( ( 20, 0), 1, wx.EXPAND, 5 )

		m_comboTrackLayerChoices = [ u"All Layers", u"F.Cu", u"B.Cu", u"In1.Cu", u"In2.Cu", u"In3.Cu", u"In4.Cu", u"In5.Cu", u"In6.Cu" ]
		self.m_comboTrackLayer = wx.ComboBox( self, wx.ID_ANY, u"F.Cu", wx.DefaultPosition, wx.Size( 110,-1 ), m_comboTrackLayerChoices, wx.CB_READONLY )
		self.m_comboTrackLayer.SetSelection( 1 )
		bSizer3.Add( self.m_comboTrackLayer, 0, wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Via diameter (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_viaDiameter = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		bSizer4.Add( self.m_viaDiameter, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Via drill (mm)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_viaDrill = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		bSizer5.Add( self.m_viaDrill, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer61.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer61, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Net name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		m_comboNetChoices = []
		self.m_comboNet = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 190,-1 ), m_comboNetChoices, wx.CB_READONLY )
		bSizer8.Add( self.m_comboNet, 0, wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button1.SetDefault()
		bSizer7.Add( self.m_button1, 0, wx.ALIGN_BOTTOM|wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnClose( self, event ):
		self.Close(force = True)
		event.Skip()


