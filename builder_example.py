# Data Processing Builder
# Responsible for mixing different data sources into
# Different data Sink
# e.g. Shapefile Data Source --> PostGIS Data Sink
# e.g. GeoJSON Data Source --> Shapefile Data Sink
import abc

class PostGISConnection(object):
    """
    Class represents a PostGIS Connection
    """
    def open_connection(self):
        return 'PostGIS'

class SHPConnection(object):
    """
    Class represents a SHP Connection
    """
    def open_connection(self):
        return 'SHP'

class GeoJSONConnection(object):
    """
    Class represents a GeoJSON Connection
    """
    def open_connection(self):
        return 'GeoJSON'

# Director
class DataTransformDirector(object):

    def __init__(self):
        self.builder = None

    def create(self):
        self.builder.make_source()
        self.builder.make_sink()
        return self.builder.datatransform

# Builder Abstract Interface
class DataTransformBuilder(object):
    __metadata__ = abc.ABCMeta

    @abc.abstractmethod
    def make_source(self):
        raise

    @abc.abstractmethod
    def make_sink(self):
        raise

# Concrete Builder
class PostGIS2SHP(DataTransformBuilder):

    def __init__(self):
        # Constructed with an instance of the product
        self.datatransform = DataTransform()

    def make_source(self):
        # Do work and set attribute on product instance
        # This would create a PostGIS connection
        conn = PostGISConnection()
        self.datatransform.source = conn.open_connection()

    def make_sink(self):
        # Do work and set attribute on product instance
        # This would create an SHP connection
        conn = SHPConnection()
        self.datatransform.sink = conn.open_connection()

# Another Concrete Builder
class GeoJSON2SHP(DataTransformBuilder):

    def __init__(self):
        self.datatransform = DataTransform()

    def make_source(self):
        conn = GeoJSONConnection()
        self.datatransform.source = conn.open_connection()

    def make_sink(self):
        conn = SHPConnection()
        self.datatransform.sink = conn.open_connection()

# Product
# See how the Concrete Builders implement the construction
# logic while the Product Definition defines the attributes
# and method of the thing itself?
class DataTransform(object):

    def __init__(self):
        self.source = None
        self.sink = None

    def process_data(self):
        print "Moving data from {} to {}".format(self.source, self.sink)

if __name__ == '__main__':
    d = DataTransformDirector()

    # I read from a config for CLI
    # that I want this builder.
    d.builder = GeoJSON2SHP()


    # Build an instance of the product
    geojson_source_transform = d.create()
    geojson_source_transform.process_data()

    d.builder = PostGIS2SHP()

    postgis_source_tranform = d.create()
    postgis_source_tranform.process_data()

    # The original GeoJSON instance is still available
    geojson_source_transform.process_data()


