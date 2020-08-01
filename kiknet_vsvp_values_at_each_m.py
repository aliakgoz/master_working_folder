import os
import numpy as np
import matplotlib.pyplot as plt

def interp_vs(x,borehole_depth=[],borehole_vs=[]):
    if borehole_depth[0] >= x:
        return borehole_vs[0]
    else:
        return borehole_vs[np.argmax(borehole_depth>=x)-1]


kiknet_sites_borehole_data = np.load('kiknet_sites_borehole_data.npy', allow_pickle=True)
kiknet_sites_borehole_data[120]

kiknet_sites_info_arr = np.load('kiknet_sites_info_arr.npy', allow_pickle=True)
kiknet_sites_info_arr[298]
kiknet_sites_info_arr.dtype.names

int(kiknet_sites_info_arr["Sensor Depth from Surface (m)"][0])

kiknet_sites_names = np.load('kiknet_sites_names.npy', allow_pickle=True)
kiknet_sites_names.shape

kiknet_sites_borehole_data[298]
kiknet_sites_names[298]

int(kiknet_sites_info_arr[np.where(kiknet_sites_info_arr['Site Code']==kiknet_sites_names[0])]["Sensor Depth from Surface (m)"][0])
kiknet_sites_borehole_data[0]['Vp (m/s)']

kiknet_1m_borehole_vsvp_data = []

for i in np.arange(kiknet_sites_borehole_data.shape[0]):

    try:

        borehole_vs = np.zeros(kiknet_sites_borehole_data[i]['Vs (m/s)'].shape,dtype=np.float32)
        borehole_vp = np.zeros(kiknet_sites_borehole_data[i]['Vp (m/s)'].shape,dtype=np.float32)
        borehole_depth = np.zeros(kiknet_sites_borehole_data[i]['Depth (m)'].shape,dtype=np.float32)
        np.copyto(borehole_vs,kiknet_sites_borehole_data[i]['Vs (m/s)'])
        np.copyto(borehole_vp,kiknet_sites_borehole_data[i]['Vp (m/s)'])
        np.copyto(borehole_depth,kiknet_sites_borehole_data[i]['Depth (m)'])
        borehole_depth[-1]=borehole_depth[-2]*1.1  # last value of depth is '-1' making it 1.1 times of last acceptable value


        vs = np.zeros(int(kiknet_sites_info_arr[np.where(kiknet_sites_info_arr['Site Code']==kiknet_sites_names[i])]["Sensor Depth from Surface (m)"][0]),dtype=np.float32)
        vp = np.zeros(int(kiknet_sites_info_arr[np.where(kiknet_sites_info_arr['Site Code']==kiknet_sites_names[i])]["Sensor Depth from Surface (m)"][0]),dtype=np.float32)
        depth = np.zeros(int(kiknet_sites_info_arr[np.where(kiknet_sites_info_arr['Site Code']==kiknet_sites_names[i])]["Sensor Depth from Surface (m)"][0]),dtype=np.float32)

        
        for j in np.arange(vs.shape[0]):
            vs[j]=interp_vs(j+1,borehole_depth,borehole_vs)
            vp[j]=interp_vs(j+1,borehole_depth,borehole_vp)
            depth[j] = float(j+1)

        one_site_data = np.array(tuple([kiknet_sites_names[i],vs,vp,depth]),
            dtype=[('File Name',np.dtype('U25')),('Depth_values',np.object),('Vs_values',np.object),('Vp_values',np.object)])

        kiknet_1m_borehole_vsvp_data.append(one_site_data)
    except:
        continue

kiknet_1m_borehole_vsvp_data = np.array(kiknet_1m_borehole_vsvp_data)
kiknet_1m_borehole_vsvp_data.shape  

kiknet_1m_borehole_vsvp_data[0]['File Name']  
kiknet_1m_borehole_vsvp_data[0]['Vs_values']
