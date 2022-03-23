## How to install API on pc windows

### 1-Install Python (Optional if using anaconda)

Path Setting: 

### 2-Login to [CDS](https://cds.climate.copernicus.eu/user/login) or [ADS](https://ads.atmosphere.copernicus.eu/user/login)

Copy the two-line code in [CDS API](https://cds.climate.copernicus.eu/api-how-to) or [ADS API](https://ads.atmosphere.copernicus.eu/api-how-to)

Code in the following format:

``
url: https://cds.climate.copernicus.eu/api/v2
``

``
key: xxxx
``

*This step is to get credentials.*

### 3-Paste the code copied in step 2

Paste it into a .txt file created in C:\\Users\%username%\, and save it with name as ".cdsapirc" and type as "All File".

### 4-Install API

Copen Anaconda and run the following command:

``
pip install cdsapi
`` for Python 2.7

or

``
pip3 install cdsapi
`` for Python 3

## API comments

For example:

``
import cdsapi #import API

c = cdsapi.Client() #call API variable

c.retrieve(
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
    }, #all the check boxes and options in each dataset, written in dictionary format in API method
    'download.nc' #the downloaded file name)
``
