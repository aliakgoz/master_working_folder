import os
import numpy as np
import matplotlib.pyplot as plt

my_raw_data_file = open(
    "D:/00-GENEL/08-MASTER/00-TEZ/04_Data_Jap/kiknet_seismograph_data_with_depths.txt"
).readlines()

# Site Code,Site Name,Latitude,Longitude,Altitude (m),Depth (m),Prefecture,Lat_Seism,Lon_Seism,Seismograph,height,sensor depth,hole depth
# ABSH01,OMU,44.5276,142.8444,105,100,HOKKAIDO,44.5253,142.8483,KiK-net06,105,3.48,103
# ABSH02,OKOPPE-W,44.4234,143.0264,38,113,HOKKAIDO,44.421,143.0304,KiK-net06,38,-76.52,116
# ABSH03,OKOPPE-E,44.3843,143.2407,30,100,HOKKAIDO,44.3819,143.2446,KiK-net06,30,-71.52,103

kiknet_sites_info_arr = []

for each_line in my_raw_data_file[1:-1]:
    site_code = each_line.replace("\n", "").split(',')[0]
    site_name = each_line.replace("\n", "").split(',')[1]
    latitude = float(each_line.replace("\n", "").split(',')[2])
    longitude = float(each_line.replace("\n", "").split(',')[3])
    altitude = float(each_line.replace("\n", "").split(',')[4])
    depth = float(each_line.replace("\n", "").split(',')[5])
    prefecture = each_line.replace("\n", "").split(',')[6]
    lat_seism = float(each_line.replace("\n", "").split(',')[7])
    lon_seism = float(each_line.replace("\n", "").split(',')[8])
    seismograph_type = each_line.replace("\n", "").split(',')[9]
    altitude_height = float(
        each_line.replace("\n", "").split(',')[10]
    )  # should be same with the altitude, just for control
    sensor_depth = float(each_line.replace("\n", "").split(',')[11])
    hole_depth = float(each_line.replace("\n", "").split(',')[12])

    each_line_arr = np.array(
        tuple(
            [
                site_code,
                site_name,
                latitude,
                longitude,
                altitude,
                depth,
                prefecture,
                lat_seism,
                lon_seism,
                seismograph_type,
                altitude_height,
                sensor_depth,
                altitude_height-sensor_depth,
                hole_depth,
            ]
        ),
        dtype=[
            ("Site Code", np.dtype("U25")),
            ("Site Name", np.dtype("U25")),
            ("Latitude", np.float32),
            ("Longitude", np.float32),
            ("Altitude (m)", np.float32),
            ("Depth (m)", np.float32),
            ("Prefecture", np.dtype("U25")),
            ("Lat_Seism", np.float32),
            ("Lon_Seism", np.float32),
            ("Seismograph Type", np.dtype("U25")),
            ("Altitude Height (m)", np.float32),
            ("Sensor Depth (Altitude) (m)", np.float32),
            ("Sensor Depth from Surface (m)", np.float32),
            ("Hole Depth (m)", np.float32),           
        ],
    )

    kiknet_sites_info_arr.append(each_line_arr)


kiknet_sites_info_arr = np.array(kiknet_sites_info_arr)

print(kiknet_sites_info_arr.shape)

np.save("kiknet_sites_info_arr.npy",kiknet_sites_info_arr)

kiknet_sites_info_arr["Sensor Depth from Surface (m)"]