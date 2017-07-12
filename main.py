# taken from https://stackoverflow.com/a/41406282

import time;
import ctypes;
SPI_SETDESKWALLPAPER = 20

wallpaper = r"D:\projects\py-wallpaper-analog\img\mountain.jpg"

# localtime = time.localtime(time.time())
# wkd = localtime[6]
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 3)
