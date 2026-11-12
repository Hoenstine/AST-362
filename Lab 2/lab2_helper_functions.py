import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling.functional_models import Gaussian2D
from astropy.modeling.functional_models import Ring2D
def implot(image,figsize=(15,13),cmap='gray_r',scale=0.5,colorbar=False,header=None,wcs=None,**kwargs):
    '''
    Plot an astronomical image, setting default options and easy tweaking of parameters
    This function is directly from the Yale Astro 330 course book by Imad Pasha and Marla Geha (2021 and following).    
    Parameters
    ----------
    image: array_like
        2D array containing an astronomical image to be plotted. Cutouts should be input as cutout.data.
    figsize: tuple, optional
        figure size to use. Default: (15,13)
    cmap: str, optional
        Colormap to use for the image. Default: 'gray_r'
    scale: float, optional
        By default, function will scale image to some number of standard deviations about the mean pixel value. Scale sets this number (or fraction). Default: 0.5.
    colorbar: bool, optional
        Whether to add a colorbar or not. Default: False
    header: dict, optional
        If input, function will attempt to create a WCS object from header and plot in celestial coordinates. Default: None
    wcs: WCS object
        If input, the function will plot using a projection set by the WCS. Default: None
    **kwargs
        Additional arguments are passed to matplotlib plotting commands. Currently supported: vmin, vmax.
        
    Returns
    -------
    fig, ax
        figure and axes objects containing currently plotted data.
    '''
    fig, ax = plt.subplots(figsize=figsize)
    mu = np.mean(image)
    s = np.std(image)
    dvmin = mu - scale*s
    dvmax = mu + scale*s
    if all(['vmin','vmax']) in kwargs.keys():
        im = ax.imshow(image,origin='lower',cmap=cmap,vmin=kwargs['vmin'],vmax=kwargs['vmax'])
    elif 'vmin' in kwargs.keys():
        im = ax.imshow(image,origin='lower',cmap=cmap,vmin=kwargs['vmin'],vmax=dvmax)
    elif 'vmax' in kwargs.keys():
        im = ax.imshow(image,origin='lower',cmap=cmap,vmin=dvmin,vmax=kwargs['vmax'])
    else:
        im = ax.imshow(image,origin='lower',cmap=cmap,vmin=dvmin,vmax=dvmax)
    if colorbar:
        cbar = plt.colorbar(im,ax=ax)
    return fig, ax


def psf(center, width_x, width_y, window, inner_rad=300):
    '''
    Evaluates a donut-shaped PSF -- created by combining a 2D ring with a 2D gaussian
    
    Input
    ---
    center: tuple 
        position centroid
    width_x: int
        integer number of pixels to define total width of 2D Gaussian in x-dir
    width_y: int
        integer number of pixels to define total width of 2D Gaussian in y-dir
    window: int
        window size
    inner_rad: int, optional
        value for number of pixels in inner radius. Default: 300
    
    Ouput
    ----
    xx: array
        positions in x around center with size 2x window
    yy: array
        positions in y around center with size 2x window
    normalized: array
        normalized Ring2D * Gauss2D point spread function
    '''

    loc=np.array(center)
    xx, yy = np.meshgrid(np.arange(loc[0]-window,loc[0]+window),
                     np.arange(loc[1]-window,loc[1]+window))
    gauss = Gaussian2D.evaluate(xx,yy,amplitude=1,theta=0,x_mean=loc[0], y_mean=loc[1], x_stddev=width_x, y_stddev=width_y)
    ring = Ring2D.evaluate(xx,yy,1,loc[0],loc[1],inner_rad,width=2*window)
    combined = ring * gauss
    normalized = combined / (np.sum(combined))
    return xx, yy, combined           
