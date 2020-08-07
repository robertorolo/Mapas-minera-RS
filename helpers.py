import geopandas
import re
import matplotlib.pyplot as plt

shp_path = "estados_2010.shp"
estados = geopandas.read_file(shp_path)

def plot_rs(ax, color='gray', alpha=0.2):
    estados[estados['sigla'] == 'RS'].plot(color=color, ax=ax, alpha=alpha)

def conversion(coord):
    deg, minutes, seconds, direction =  re.split('[°\'"]', coord)
    return (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)

def plot_bubble(ax, lat, longi, value, alpha=0.5):
    lat = [conversion(i) for i in lat]
    longi = [conversion(j) for j in longi]
    sc = ax.scatter(longi, lat, s=value, c=value, alpha=alpha)
    return sc

def plot_areas(ax, shp_path, color='red', alpha=0.5):
    areas = geopandas.read_file(shp_path)
    areas.plot(color=color, ax=ax, alpha=alpha)

