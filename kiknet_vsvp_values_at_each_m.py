import os
import numpy as np
import matplotlib.pyplot as plt


kiknet_sites_borehole_data = np.load('kiknet_sites_borehole_data.npy', allow_pickle=True)
kiknet_sites_borehole_data.shape

kiknet_sites_info_arr = np.load('kiknet_sites_info_arr.npy', allow_pickle=True)
kiknet_sites_info_arr.shape

kiknet_sites_names = np.load('kiknet_sites_names.npy', allow_pickle=True)
kiknet_sites_names.shape

kiknet_sites_borehole_data[0]
kiknet_sites_names[0]

kiknet_sites_info_arr[np.where(kiknet_sites_info_arr['Site Code']==kiknet_sites_names[0])]['Site Code']
kiknet_sites_borehole_data[0]