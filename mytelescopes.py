"""
Personal Photometry Pipeline Configuation File
2016-11-01, michael.mommert@nau.edu
"""

# Photometry Pipeline 
# Copyright (C) 2016  Michael Mommert, michael.mommert@nau.edu

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.


##### telescope/instrument configurations
"""
# MYTELESCOPE setup parameters
mytelescope_param = {
    'telescope_instrument' : 'MyTelescope/MyCamera', # telescope/instrument name
    'telescope_keyword'    : 'MYTELESCOPE',      # telescope/instrument keyword
    'observatory_code'     : 'XXX',         # MPC observatory code
    'secpix'               : (0.1, 0.1), # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx'                : True,
    'flipy'                : False,
    'rotate'               : 0,

    # instrument-specific FITS header keywords
    'binning'              : ('CCDBIN1', 'CCDBIN2'), # binning in x/y
    'extent'               : ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra'                   : 'RA',  # telescope pointing, RA
    'dec'                  : 'DEC', # telescope pointin, Dec 
    'radec_separator'      : ':',   # RA/Dec hms separator, use 'XXX'
                                    # if already in degrees
    'date_keyword'         : 'DATE-OBS|TIME-OBS', # obs date/time
                                                  # keyword; use
                                                  # 'date|time' if
                                                  # separate
    'obsmidtime_jd'        : 'MIDTIMJD', # obs midtime jd keyword
                                         # (usually provided by
                                         # pp_prepare
    'object'               : 'OBJECT',  # object name keyword 
    'filter'               : 'FILTER',  # filter keyword
    'filter_translations'  : {'Johnson_V': 'V', 'Johnson_R': 'R', 
                              'none': None, 'Johnson_B': 'B'},
                             # filtername translation dictionary
    'exptime'              : 'EXPTIME', # exposure time keyword (s)
    'airmass'              : 'AIRMASS', # airmass keyword

    # source extractor settings
    'source_minarea'       : 12, # default sextractor source minimum N_pixels
    'aprad_default'        : 5, # default aperture radius in px 
    'aprad_range'          : [2, 10], # [minimum, maximum] aperture radius (px)
    'sex-config-file'      : rootpath+'/setup/mytelescope.sex',
    'mask_file'            : {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file'    : rootpath+'/setup/mytelescope.scamp', 

    # default catalog settings
    'astrometry_catalogs'  : ['URAT-1', '2MASS', 'USNO-B1'], 
    'photometry_catalogs'  : ['SDSS-R9', 'APASS9', '2MASS']
}
##### add telescope configurations to 'official' telescopes.py
#implemented_telescopes.append('MYTELESCOPE')

### translate INSTRUME (or others, see _pp_conf.py) header keyword into
#   PP telescope keyword 
# example: INSTRUME keyword in header is 'mytel'
#instrument_identifiers['mytel'] = 'MYTELESCOPE'

### translate telescope keyword into parameter set defined here
#telescope_parameters['MYTELESCOPE'] = mytelescope_param
"""

# QSI
qsi_param = {
    'telescope_instrument': 'QSI',  # telescope/instrument name
    'telescope_keyword': 'QSI',  # telescope/instrument keyword
    'observatory_code': '',  # MPC observatory code
    'secpix': (1.11, 1.11),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'Lum': 'V', 'Rc':'R', 'V':'V'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath+'/setup/QSI.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath+'/setup/QSI.scamp',
    'reg_max_mag'          : 19,  
    'reg_search_radius'    : 0.5, # deg   
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('TELESCOP,INSTRUME,FILTER,EXPTIME,OBJECT,' +
                              'DATE-OBS,TIME-OBS,RA,DEC,SECPIX,AIRMASS,' +
                              'TEL_KEYW'),
    #                         keywords to be copied in image
    #                         combination using swarp
    'swarp-config-file'    : rootpath+'/setup/QSI.swarp', 

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['SDSS-R9', 'APASS9', '2MASS']
}

##### add telescope configurations to 'official' telescopes.py

implemented_telescopes.append('QSI')

### translate INSTRUME (or others, see _pp_conf.py) header keyword into
#   PP telescope keyword
# example: INSTRUME keyword in header is 'mytel'
instrument_identifiers['INSTRUME'] = 'QSI'

### translate telescope keyword into parameter set defined here
telescope_parameters['QSI'] = qsi_param

#### SC8
sc8_param = {
    'telescope_instrument': 'SC8',  # telescope/instrument name
    'telescope_keyword': 'SC8',  # telescope/instrument keyword
    'observatory_code': '',  # MPC observatory code
    'secpix': (0.91, 0.91),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('XBINNING', 'YBINNING'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'OBJCTRA',  # telescope pointing, RA
    'dec': 'OBJCTDEC',  # telescope pointin, Dec
    'radec_separator': ' ',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'JD',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'Ninguno': 'V',},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath+'/setup/SC8.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath+'/setup/SC8.scamp',
    'reg_max_mag'          : 19,  
    'reg_search_radius'    : 0.5, # deg   
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords'        : ('TELESCOP,INSTRUME,FILTER,EXPTIME,OBJECT,' +
                              'DATE-OBS,TIME-OBS,OBJCTRA,OBJCTDEC,SECPIX,AIRMASS,' +
                              'TEL_KEYW'),
    #                         keywords to be copied in image
    #                         combination using swarp
    'swarp-config-file'    : rootpath+'/setup/SC8.swarp', 

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['SDSS-R9', 'APASS9', '2MASS']
}

##### add telescope configurations to 'official' telescopes.py

implemented_telescopes.append('SC8')

### translate INSTRUME (or others, see _pp_conf.py) header keyword into
#   PP telescope keyword
# example: INSTRUME keyword in header is 'mytel'
instrument_identifiers['INSTRUME'] = 'SC8'

### translate telescope keyword into parameter set defined here
telescope_parameters['SC8'] = sc8_param



