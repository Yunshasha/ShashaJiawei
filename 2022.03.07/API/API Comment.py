## API comments

For example:

``
import cdsapi #import API

c = cdsapi.Client() #call API variable

c.retrieve( #the only method known is "retrieve", maybe exists others
    'cams-europe-air-quality-forecasts', #name of dataset
    {
        'model': 'ensemble',
        'date': '2022-03-19/2022-03-21', #for time period
        'format': 'netcdf',
        'variable': 'ozone',
        'level': '0',
        'type': 'analysis',
        'time': [
            '00:00', '23:00',
        ], #for multiple choices
        'leadtime_hour': '0',
    }, #all the check boxes and options in each dataset, written in dictionary format in API method input variables
    'download.nc' #the downloaded file name)
``
