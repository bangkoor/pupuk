from osgeo import gdal
import sys

g = gdal.Open("jonggol.tif")


print "[ RASTER BAND COUNT ]: ", g.RasterCount

for band in range( g.RasterCount ):
    band += 1
    print "[ GETTING BAND ]: ", band
    srcband = g.GetRasterBand(band)
    if srcband is None:
        continue

    stats = srcband.GetStatistics( True, True )
    if stats is None:
        continue

    print "[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
                stats[0], stats[1], stats[2], stats[3] )