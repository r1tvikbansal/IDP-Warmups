import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file('geo_data/ne_110m_admin_0_countries.shp')

gdf = gdf[gdf['CONTINENT'] == 'South America']

gdf.plot(column='POP_EST', legend=True)

plt.savefig('south_america.png')
