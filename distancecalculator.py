from pygeocoder import Geocoder
import numpy as np
import sys

def get_distance(locA,locB):
    earth_rad = 6371.0
    dlat = np.deg2rad(locB[0] - locA[0])
    dlon = np.deg2rad(locB[1] - locA[1])

    a = np.sin(dlat/2) * np.sin(dlat/2) + \
        np.cos(np.deg2rad (locA[0])) * np.cos(np.deg2rad(locB[0])) * \
        np.sin (dlon/2) * np.sin (dlon/2)
    c = 2 * arctan2(np.sqrt(a),np.sqrt(1-a))    
    return earth_rad *c
def get_latlongs(location):
    return Geocoder.geocode(location)[0].coordinates
    
def convert_km_to_miles(km):
    miles_per_km =0.62137
    return km * miles_per_km
    
def main():
    origin = raw_input('Enter the origin :')
    destination = raw_input('Enter the destinaation: ')
    units = ''
    while (units != 'km') & (units ! = 'm'):
         print 'Do you prefer distance units in (kilometers or miles): '
         units = str(raw_input())
         if units in ['clicks','km','kilometers', 'kilometer']:
             units = 'km'
         elif units in ['m','miles','mile']:
             units = 'm'
         else:
           print'Invalid!! Please try again!'
    try:       
         distance = get_distance(get_latlongs(origin),get_latlongs(destination))
         if units =='km':
            print str(disance),'km'
         else:
             distance = convert_km_to_miles(distance)
             print str(distance),'m'
    except:
        print'Error!! Please try again '
        
 if __name__ == '__main__':
     sys.exit(main())
          
        
    
