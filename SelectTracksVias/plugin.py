import os
import pcbnew
import wx
import configparser

from pathlib import Path
from .select_items import SelectItems



class SelectTracksVias(pcbnew.ActionPlugin):

    def __init__(self):
        self.name = "Select Tracks & Vias"
        self.category = "Modify PCB"
        self.show_toolbar_button = True
        icon_dir = os.path.dirname(__file__)
        self.icon_file_name = os.path.join(icon_dir, "icon.png")
        self.description = "Select Tracks & Vias"
        
    
    def Run(self):  
        
        tr = 0
        vi = 0
        
        dialog = SelectItems(None)
       
##########################################################################################            
#        net_names = list(set([track.GetNetname() for track in pcbnew.GetBoard().Tracks()]))
#        net_names.sort()
#        dialog.m_comboNet.Append(net_names)
#        dialog.m_comboNet.Insert('', 0)
        
        net_names = list(pcbnew.GetBoard().GetNetInfo().NetsByName())
        for item in net_names:
            dialog.m_comboNet.Append(str(item))#.replace('{slash}', r'/'))
        
        #dialog.m_comboNet.AppendItems(net_names)
        #wx.MessageBox(str(len(netnames)))
        
        
        
##########################################################################################            
        current_dir = os.path.dirname(__file__)
        myfile  = os.path.join(current_dir, "settings.ini")
        
        config = configparser.ConfigParser()

        #myfile = os.path.expanduser("~") + '\settings.ini'
        
        if not os.path.exists(myfile):
            config['Settings'] = {'track_width': '0.2', 'track_layer': '', 'track_net': '', 'via_diameter': '', 'via_drill': ''}        
            config.write(open(myfile, 'w'))        
        
        config.read(myfile)
        
        dialog.m_trackWidth.Value       = config.get("Settings","track_width") 
        dialog.m_comboTrackLayer.SetValue(config.get("Settings","track_layer"))
        dialog.m_comboNet.SetValue(config.get("Settings","track_net"))
        dialog.m_viaDiameter.Value      = config.get("Settings","via_diameter") 
        dialog.m_viaDrill.Value         = config.get("Settings","via_drill") 
                  
##########################################################################################            
        try:
            if dialog.ShowModal() != wx.ID_OK:
                return
                   
##########################################################################################            
            b = pcbnew.GetBoard()
            tracks = b.Tracks()
            
##########################################################################################            
            layer = 0
            netName = ''

            if dialog.m_comboTrackLayer.GetValue() == 'All Layers':
                layer = -1
            if dialog.m_comboTrackLayer.GetValue() == 'F.Cu':
                layer = pcbnew.F_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'B.Cu':
                layer = pcbnew.B_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'In1.Cu':
                layer = pcbnew.In1_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'In2.Cu':
                layer = pcbnew.In2_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'In3.Cu':
                layer = pcbnew.In3_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'In4.Cu':
                layer = pcbnew.In4_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'In5.Cu':
                layer = pcbnew.In5_Cu
            elif dialog.m_comboTrackLayer.GetValue() == 'In6.Cu':
                layer = pcbnew.In6_Cu
            
            netName     = dialog.m_comboNet.GetValue()
            #wx.MessageBox(netName)
            
##########################################################################################
            if (dialog.m_trackWidth.Value != ''):
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
                if (layer == -1) and (netName == ''):
                    for t in tracks: 
                        if (t.GetClass() == 'PCB_TRACK') and (t.GetWidth() == pcbnew.FromMM(float(dialog.m_trackWidth.Value.replace(',', '.')))):
                            t.SetSelected()
                            tr += 1
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
                elif (layer == -1) and (netName != ''):    
                    for t in tracks: 
                        if (t.GetClass() == 'PCB_TRACK') and (t.GetWidth() == pcbnew.FromMM(float(dialog.m_trackWidth.Value.replace(',', '.')))) and (t.GetNetname() == netName):
                            t.SetSelected()
                            tr += 1
                    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
                elif (layer != -1) and (netName == ''):    
                    for t in tracks: 
                        if (t.GetClass() == 'PCB_TRACK') and (t.GetWidth() == pcbnew.FromMM(float(dialog.m_trackWidth.Value.replace(',', '.')))) and (t.GetLayer() == layer):
                            t.SetSelected()
                            tr += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
                elif (layer != -1) and (netName != ''):    
                    for t in tracks: 
                        if (t.GetClass() == 'PCB_TRACK') and (t.GetWidth() == pcbnew.FromMM(float(dialog.m_trackWidth.Value.replace(',', '.')))) and (t.GetLayer() == layer) and (t.GetNetname() == netName):
                            t.SetSelected()
                            tr += 1
                    
                pcbnew.Refresh()
                wx.MessageBox('Selected ' + str(tr) + ' tracks')
            
##########################################################################################            
            if (dialog.m_viaDiameter.Value == '') and (dialog.m_viaDrill.Value == ''):
                return

            if (dialog.m_viaDiameter.Value == '') and (dialog.m_viaDrill.Value != ''):
                
                for v in tracks: 
                    if netName == '':
                        if (v.GetClass() == 'PCB_VIA') and (v.GetDrillValue() == pcbnew.FromMM(float(dialog.m_viaDrill.Value.replace(',', '.')))):
                            v.SetSelected()
                            vi += 1
                    else:
                        if (v.GetClass() == 'PCB_VIA') and (v.GetDrillValue() == pcbnew.FromMM(float(dialog.m_viaDrill.Value.replace(',', '.')))) and (v.GetNetname() == netName):
                            v.SetSelected()
                            vi += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
            elif (dialog.m_viaDiameter.Value != '') and (dialog.m_viaDrill.Value == ''):
                
                for v in tracks: 
                    if netName == '':
                        if (v.GetClass() == 'PCB_VIA') and (v.GetWidth() == pcbnew.FromMM(float(dialog.m_viaDiameter.Value.replace(',', '.')))):
                            v.SetSelected()
                            vi += 1
                    else:
                        if (v.GetClass() == 'PCB_VIA') and (v.GetWidth() == pcbnew.FromMM(float(dialog.m_viaDiameter.Value.replace(',', '.')))) and (v.GetNetname() == netName):
                            v.SetSelected()
                            vi += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
            elif (dialog.m_viaDiameter.Value != '') and (dialog.m_viaDrill.Value != ''):

                for v in tracks: 
                    if netName == '':
                        if (v.GetClass() == 'PCB_VIA') and (v.GetWidth() == pcbnew.FromMM(float(dialog.m_viaDiameter.Value.replace(',', '.')))) and (v.GetDrillValue() == pcbnew.FromMM(float(dialog.m_viaDrill.Value.replace(',', '.')))):
                            v.SetSelected()
                            vi += 1
                    else:
                        if (v.GetClass() == 'PCB_VIA') and (v.GetWidth() == pcbnew.FromMM(float(dialog.m_viaDiameter.Value.replace(',', '.')))) and (v.GetDrillValue() == pcbnew.FromMM(float(dialog.m_viaDrill.Value.replace(',', '.')))) and (v.GetNetname() == netName):
                            v.SetSelected()
                            vi += 1
                
            pcbnew.Refresh()
            wx.MessageBox('Selected ' + str(vi) + ' vias')
                        
        finally:
            config.set('Settings', 'track_width',  dialog.m_trackWidth.Value)  
            config.set('Settings', 'track_layer',  dialog.m_comboTrackLayer.GetValue()) 
            config.set('Settings', 'track_net',    dialog.m_comboNet.GetValue()) 
            config.set('Settings', 'via_diameter', dialog.m_viaDiameter.Value)  
            config.set('Settings', 'via_drill',    dialog.m_viaDrill.Value)  
            
            with open(myfile, 'w') as configfile:
                config.write(configfile)            
            
            dialog.Destroy()
