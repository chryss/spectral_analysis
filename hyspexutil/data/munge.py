from scipy.signal import savgol_filter

def smooth_spectrum(spectrum, 
    savgol=True, window=7, order=2, 
    clip_bands=10, scale_down=True):
    """Smoothes a HySpex spectrum with a Savitzky-Golay filter.
    Optional clipping: removes bands at end 
    Optional downscaling to reflectance 0...1 
    """
    
    if scale_down:
        spectrum = spectrum/10000
    if savgol:
        if clip_bands > 0:
            return savgol_filter(spectrum[:-clip_bands], window, order)
        else:
            return savgol_filter(spectrum, window, order) 
    else:
        if clip_bands > 0:
            return spectrum[:-clip_bands]
        else:
            return spectrum 
    

