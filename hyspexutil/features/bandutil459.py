# bands start at 1
# This file is for 459-band HySpex files

import numpy as np
from typing import Union
from pathlib import Path
import xarray as xr
import rioxarray

def get_interpolated_bands(
    hyspexpath: Union[str, Path]) -> np.array: 
    """Create new set of interpolated bands"""
    with xr.open_dataset(hyspexpath, 
        engine="rasterio") as srcDS:
        bandnames = srcDS.band_data.attrs['band_names'].split(',')
        interpolated = [int(item.strip()[5:]) 
            for item in bandnames 
            if item.strip().startswith('band*')]
    return np.array(interpolated)

# interpolated band numbers 
interpolatedbd = np.array(
    [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 109,
    110, 111, 112, 113, 114, 115, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
    131, 132, 133, 134, 135, 136, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163,
    164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179,
    180, 181, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209,
    210, 211, 212, 213, 214, 215, 216, 243, 244, 245, 246, 247, 248, 249, 250, 251,
    252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267,
    268, 269, 270, 271, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336,
    337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352,
    353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363])

# suitable for ML features: not interpolated, not noisy
mlbands = np.array(
    [282, 10, 230, 88, 239, 364, 107, 71, 314, 413, 40, 183, 371, 6, 218, 48, 323, 
    417, 106, 84, 319, 284, 20, 236, 62, 315, 153, 370, 27, 304, 414, 42, 188, 86, 
    299, 283, 8, 425])

# same bands, but indexed from 0:
mlbands_idx = mlbands - 1
