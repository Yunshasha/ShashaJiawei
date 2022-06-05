from myFunctions import getSum

ds_name = 'cams-europe-air-quality-forecasts'
ds_time = '2021-01-01/2021-01-01'
ds_variable = 'nitrogen_dioxide'

foo = getSum.getSum_day(ds_name=ds_name, ds_time=ds_time, ds_variable=ds_variable)
   
