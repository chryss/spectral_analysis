# functions to extract spectral data from HySpex reflectance imagery

import xarray as xr
import rioxarray
import numpy as np
from shapely.geometry import Point
from ..common import HyspexError

def get_spectra_pts(fpth, xcoords, ycoords, bands="all"):
    """opens hyspex dataset, returns spectra at specified points"""
    if len(xcoords) != len(ycoords):
        raise HyspexError(
            "x and y coordinate arrays are not the same length. "
            "These are supposed to be the x and y coordinates of a sequence "
            "of points, so the lengths need to agree."
        )
    if not set(bands).issubset(set(range(1, 460))):
        if bands=='all':
            bands = np.arange(1, 460)
        else:
            raise HyspexError(
                "The 'bands' argument has to be a subset of [1 ... 459]"
            )
    xs = xr.DataArray(xcoords, dims='pt_idx')
    ys = xr.DataArray(ycoords, dims='pt_idx')
    with  xr.open_dataset(fpth, 
        engine="rasterio", 
        chunks={'band': 'auto', 'x': 400, 'y': 400}) as src:
        return src.band_data.sel(x=xs, y=ys, 
            band=bands, method="nearest")

def get_spectrum_single(fpth, x, y, bands=all):
    "Just one point"
    return get_spectra_pts(fpth, [x], [y], bands)

def get_spectra_df(fpth, xs, ys, bands):
    """Multiple spectra, return a dataframe"""
    specDA = get_spectra_pts(fpth, xs, ys, bands
    specDF = specDA.to_dataframe().reset_index().pivot(
       index=['pt_idx', 'x', 'y'], columns=['band'], 
       values='band_data').reindex(columns=bands)
    specDF.columns = [f"band{ii.zfill(3)}" for ii in specDF.columns]
    specDF.columns.name = None
    return specDF

def get_spectra_hexagon(fp, hexa, bands):
    """Multiple specttra, a hexagon from our dataset (row of hexagon dataframe)"""
    xs = np.arange(np.floor(hexa.left), np.ceil(hexa.right)+1)
    ys = np.arange(np.floor(hexa.bottom), np.ceil(hexa.top)+1)
    pts = [Point(x, y) 
        for x in xs for y in ys 
        if row.geometry.contains(Point(x, y))]
    return get_spectra_df(fpth, [pt.x for pt in pts], [pt.y for pt in pts], bands)


if __name__ ==  '__main__':
    print("This is the extract.py submodule speaking.")
