import sys
import matplotlib.pyplot as plt
import lab2_helper_functions as l2
import glob

from astropy.io import fits


# Enter your file name from the command line as a string.
#filename = sys.argv[1]
# Alt: set your filename as a string
filename='/Users/jameshoenstine/Downloads/Vega_0016-0001.fit'

# Default value is set to 1/2 of each dimension.
center=[2590, 2550]


# Load fits data and header
foo = fits.open(filename)
my_data = foo[0].data
my_header = foo[0].header
foo.close()


print("Click anywhere on the image to place a star and print coordinates.")
print("Press any key to close plot")

def on_click(event):
    print('Your current coords are ')
    print(f' coords {event.xdata} {event.ydata}')
    ax.plot(event.xdata,event.ydata,'*',ms='5')

def on_press(event):
        plt.close()

# Plot fits data and a pink circle, showing where the center point of graph is.
fig, ax = l2.implot(my_data,figsize=[10,7])
plt.connect('button_press_event', on_click)
plt.connect('key_press_event', on_press)
ax.plot(center[0],center[1],'o', color='None', mec='m',ms=10,alpha=0.8)
plt.show()


