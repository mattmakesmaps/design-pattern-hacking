# A factory that generates different connectors
# to parcel data stores.
import abc

# Factory
def getParcelData(county_name):
    if county_name == 'King':
        return KingCountyParcels()
    elif county_name == 'Whatcom':
        return WhatcomCountyParcels()

# Interface
class ParcelDataSourceInterface(object):
    __metadata__ = abc.ABCMeta
    @abc.abstractproperty
    def parcel_id(self):
        raise

    @abc.abstractproperty
    def zip_code(self):
        raise

    @abc.abstractmethod
    def open_connection(self):
        raise

# Products
class KingCountyParcels(ParcelDataSourceInterface):
    def __init__(self):
        self.conn = self.open_connection()

    @property
    def parcel_id(self):
        return 'King County Parcel ID'

    @property
    def zip_code(self):
        return 'King County Zip Code'

    @abc.abstractmethod
    def open_connection(self):
        return 'King County DB Conn'

class WhatcomCountyParcels(ParcelDataSourceInterface):
    def __init__(self):
        self.conn = self.open_connection()

    @property
    def parcel_id(self):
        return 'Whatcom County Parcel ID'

    @property
    def zip_code(self):
        return 'Whatcom County Zip Code'

    @abc.abstractmethod
    def open_connection(self):
        return 'Whatcom County DB Conn'

if __name__ == '__main__':

    for county in ('King','Whatcom'):
        parcel_data = getParcelData(county)
        print parcel_data.parcel_id
        print parcel_data.zip_code

