
import pandas as pd
import numpy as np
from scipy.spatial import distance
import geopandas

# read population by deso zones

DeSO = geopandas.read_file(
    f'C:/Synthetic_population_new/caglar/synthetic_sweden/input/deso_statistik_shp/Bef_Alder_region.shp')

print(DeSO.crs)




#%%
DeSO['Shape_Area'] = DeSO['geometry'].area

DeSO_poi = DeSO.copy()


DeSO_poi['geometry'] = DeSO['geometry'].representative_point()


DeSO_poi['X'] = DeSO_poi.apply(lambda row: row['geometry'].x, axis=1)
DeSO_poi['Y'] = DeSO_poi.apply(lambda row: row['geometry'].y, axis=1)

#%%

dist_DeSO = distance.cdist(DeSO_poi[['X','Y']],  DeSO_poi[['X','Y']], metric='euclidean')


dist_DeSO[np.diag_indices(len(dist_DeSO)) ] = np.sqrt(DeSO['Shape_Area']/np.pi)
#%%

df_dist_DeSO = pd.DataFrame(dist_DeSO, index = DeSO_poi.rename(columns={'Deso':'origin_deso'}).origin_deso, columns = DeSO_poi.rename(columns={'Deso':'desti_deso'}).desti_deso)

df_dist_DeSO = df_dist_DeSO.stack()
df_dist_DeSO = pd.DataFrame(df_dist_DeSO,columns = ['distance'])
df_dist_DeSO = df_dist_DeSO.reset_index()

df_dist_DeSO.to_pickle(r'C:\MAD4AG\dbs\intermediate\df_DeSO_dist.pkl')