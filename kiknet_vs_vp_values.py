import os
import numpy as np
import matplotlib.pyplot as plt


def interp_vs(x,depth=[],vs=[]):
    return vs[np.argmax(depth>x)-1]
#print(pt.Path(__file__).parent.absolute())

kiknet_soil_folder = "../sitedat_kiknet/"


kiknet_soil_file_list = os.listdir(kiknet_soil_folder)
kiknet_soil_file_list[0]

 
all_st = []
kiknet_st_names =[]
i=0     
for each_st in kiknet_soil_file_list:
    try:
        #print(i)
        each_st_arr = np.array([tuple(x.replace('\n','').replace('-----','-1.0').split(',')) for x in 
                open(kiknet_soil_folder + each_st).readlines()[2:]],
                dtype=[('No',np.int32),('Thickness (m)',np.float32),('Depth (m)',np.float32)
                ,('Vp (m/s)',np.float32),('Vs (m/s)',np.float32)])
        all_st.append(each_st_arr)
        kiknet_st_names.append(each_st.replace('.dat',''))
    except:
        i=i+1
    
 

all_st_arr = np.array(all_st)
all_st_arr.shape
all_st_arr[0]

np.save("kiknet_sites_borehole_data.npy",all_st_arr)

all_st_arr['Vs (m/s)']
kiknet_st_names = np.array(kiknet_st_names)
kiknet_st_names.shape


np.save("kiknet_sites_names.npy",kiknet_st_names)

