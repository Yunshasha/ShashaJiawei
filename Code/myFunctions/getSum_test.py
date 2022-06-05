import cdsapi
import numpy as np
import pandas as pd
import xarray as xr
import datetime

# 获取原始数据 采用不同的方法
# nitrogen_dioxide --> no2_conc   
# pm10_wildfires  -->  pmwf_conc  
# nitrogen_monoxide --> no_conc
# sulphur_dioxide --> so2_conc
# ozone --> o3_conc
# carbon_monoxide --> co_conc
# particulate_matter_2.5um --> pm2p5_conc
def getSum_day(ds_name, ds_time, ds_variable):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': ds_variable,
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 获取原始数据 采用不同的方法
    # nitrogen_dioxide --> no2_conc   
    # pm10_wildfires  -->  pmwf_conc  
    # nitrogen_monoxide --> no_conc
    # sulphur_dioxide --> so2_conc
    # ozone --> o3_conc
    # carbon_monoxide --> co_conc
    # particulate_matter_2.5um --> pm2p5_conc

    if ds_variable == 'nitrogen_dioxide':
        rdata_values = rdata.no2_conc.values
    elif ds_variable == 'pm10_wildfires':
        rdata_values = rdata.pmwf_conc.values
    elif ds_variable == 'nitrogen_monoxide':
        rdata_values = rdata.no_conc.values
    elif ds_variable == 'sulphur_dioxide':
        rdata_values = rdata.so2_conc.values
    elif ds_variable == 'ozone':
        rdata_values = rdata.o3_conc.values
    elif ds_variable == 'carbon_monoxide':
        rdata_values = rdata.co_conc.values
    elif ds_variable == 'particulate_matter_2.5um':
        rdata_values = rdata.pm2p5_conc.values

    # 拿到 原始数据 的 values array 信息
    # rdata_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_values_sum array
    # rdata_values_sum = np.zeros((1,1,420,700))
    rdata_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    # for i in range(len(rdata_values)):
    #     foo.values = foo.values + rdata_values[i]
    # foo.values = foo.values / 24
    foo.values[:,0,:,:] = np.mean(rdata_values[:,0,:,:], axis=0)

    return [foo, rdata]

# nitrogen_dioxide --> no2_conc   
def getSum_day_no2(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'nitrogen_dioxide',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 no2_conc array 信息
    rdata_no2_conc_values = rdata.no2_conc.values
    # rdata_no2_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_no2_conc_values_sum array
    # rdata_no2_conc_values_sum = np.zeros((1,1,420,700))
    rdata_no2_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_no2_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_no2_conc_values)):
        foo.values = foo.values + rdata_no2_conc_values[i]

    return [foo, rdata]

# pm10_wildfires  -->  pmwf_conc  
def getSum_day_pm10(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'pm10_wildfires',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 no2_conc array 信息
    rdata_pmwf_conc_values = rdata.pmwf_conc.values
    # rdata_pmwf_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_pmwf_conc_values_sum array
    # rdata_pmwf_conc_values_sum = np.zeros((1,1,420,700))
    rdata_pmwf_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_pmwf_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_pmwf_conc_values)):
        foo.values = foo.values + rdata_pmwf_conc_values[i]

    return [foo, rdata]

 # nitrogen_monoxide --> no_conc
def getSum_day_no(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'nitrogen_monoxide',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 no2_conc array 信息
    rdata_no_conc_values = rdata.no_conc.values
    # rdata_no_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_no_conc_values_sum array
    # rdata_no_conc_values_sum = np.zeros((1,1,420,700))
    rdata_no_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_no_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_no_conc_values)):
        foo.values = foo.values + rdata_no_conc_values[i]

    return [foo, rdata]

# sulphur_dioxide --> so2_conc
def getSum_day_so2(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'sulphur_dioxide',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 no2_conc array 信息
    rdata_so2_conc_values = rdata.so2_conc.values
    # rdata_so2_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_so2_conc_values_sum array
    # rdata_so2_conc_values_sum = np.zeros((1,1,420,700))
    rdata_so2_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_so2_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_so2_conc_values)):
        foo.values = foo.values + rdata_so2_conc_values[i]

    return [foo, rdata]

# ozone --> o3_conc
def getSum_day_o3(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'ozone',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 o3_conc array 信息
    rdata_o3_conc_values = rdata.o3_conc.values
    # rdata_o3_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_o3_conc_values_sum array
    # rdata_o3_conc_values_sum = np.zeros((1,1,420,700))
    rdata_o3_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_o3_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_o3_conc_values)):
        foo.values = foo.values + rdata_o3_conc_values[i]

    return [foo, rdata]

# carbon_monoxide --> co_conc
def getSum_day_co(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'carbon_monoxide',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 co_conc array 信息
    rdata_co_conc_values = rdata.co_conc.values
    # rdata_co_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_co_conc_values_sum array
    # rdata_co_conc_values_sum = np.zeros((1,1,420,700))
    rdata_co_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_co_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_co_conc_values)):
        foo.values = foo.values + rdata_co_conc_values[i]

    return [foo, rdata]

# particulate_matter_2.5um --> pm2p5_conc
def getSum_day_o3(ds_name, ds_time):

    c = cdsapi.Client()
    c.retrieve(
        ds_name,
        {
            'model': 'ensemble',
            'date': ds_time,
            'format': 'netcdf',
            'variable': 'particulate_matter_2.5um',
            'level': '0',
            'type': 'analysis',
            'leadtime_hour': '0',
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
        },
        'download.nc')
    # 打开数据到 rdata
    rdata = xr.open_dataset("download.nc")
    # rdata

    # 拿到 原始数据 的 pm2p5_conc array 信息
    rdata_pm2p5_conc_values = rdata.so2_conc.values
    # rdata_pm2p5_conc_values

    # 初始化 array 大小参数: 从原始数据array采集
    # time =  np.zeros((1))  #单位为 天 或者 年: 大小为 1
    level = len(rdata.level)  # 默认level
    latitude = len(rdata.latitude)
    longitude = len(rdata.longitude)

    # 初始化 rdata_pm2p5_conc_values_sum array
    # rdata_pm2p5_conc_values_sum = np.zeros((1,1,420,700))
    rdata_pm2p5_conc_values_sum = np.zeros((1, level, latitude, longitude))

    # 从原始 array 复制可选 维度 和 坐标
    time = np.zeros((1))
    level = rdata.level
    latitude = rdata.latitude
    longitude = rdata.longitude

    # 创建一个 DataArray 并提供 维度 和 坐标 信息
    foo = xr.DataArray(rdata_pm2p5_conc_values_sum, coords=[
                       time, level, latitude, longitude], dims=['time', 'level', 'latitude', 'longitude'])

    # 从原始 array 复制 属性表
    foo.attrs = rdata.attrs

    # 添加新属性信息 time 告诉用户我这是 day 的数据
    foo.attrs['time'] = 'day'

    # foo

    # 原始数据array求和
    for i in range(len(rdata_pm2p5_conc_values)):
        foo.values = foo.values + rdata_pm2p5_conc_values[i]

    return [foo, rdata]
