import netCDF4
from netCDF4 import Dataset
import numpy as np
import sys
import os

#查看nc数据基本信息
nc_obj=Dataset('precip.nc')
print(nc_obj)

#查看nc数据各个变量的信息
print(nc_obj.variables.keys())
for i in nc_obj.variables.keys():
    print('___________________________________________')
    print(i)
    print(nc_obj.variables[i])

precip=(nc_obj.variables['precip'][:])
lat=(nc_obj.variables['lat'][:])
lon=(nc_obj.variables['lon'][:])
