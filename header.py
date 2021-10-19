"""
Changing fits header to work fine with pp

place it in folder with fits frames
"""
#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
from astropy.io import fits

fits_list = [i for i in os.listdir('.') if i.endswith('.fits') or i.endswith('.fit')]
for fits_name in fits_list:
    data, hdr = fits.getdata(fits_name, header=True)
    #hdr = fits.getheader(fits_name, 0)
    if hdr['INSTRUME'] == 'QSI 583ws S/N 00504309 HW 06.00.00 FW 05.02.06 PI 5.5.332.1' or hdr['INSTRUME'] == 'QSI     ':
        hdr['INSTRUME'] = 'QSI     '
        hdr['AIRMASS'] = 1
        hdr['BSCALE'] = 1
        hdr.set('BZERO', 32768)
    fits.writeto(fits_name, data, hdr, overwrite=True)
