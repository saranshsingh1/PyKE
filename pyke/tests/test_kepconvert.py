import pytest
import csv
from astropy.utils.data import get_pkg_data_filename
from pyke import kepconvert
from ..kepio import delete

# fake light curve with transits of period = 2.02 days
# and duration 0.18 days
fake_lc = get_pkg_data_filename("data/golden-lc.fits")

def test_kepconvert():

    with pytest.raises(Exception,
                       message="ERROR -- KEPCONVERT: input file myfile.fits does not exist"):

        kepconvert("myfile.fits", "output.txt", "fits2excel",
                   "TIME,SAP_FLUX,SAP_FLUX_ERR,SAP_QUALITY", True, True)

    with pytest.raises(Exception,
                       message="ERROR -- KEPCONVERT: conversion not supported: fits2excel"):

        kepconvert(fake_lc, "output.txt",
                   "fits2excel", "TIME,SAP_FLUX,SAP_FLUX_ERR,SAP_QUALITY", True, True)

    # convert to csv
    kepconvert(fake_lc, "fake_lc.csv",
               "fits2csv", "TIME,SAP_FLUX", True, True)

    with open('fake_lc.csv', 'r') as csvfile:
        # check header
        line = csvfile.readline()
        first_line = line.split(',')
        assert first_line == ['TIME', 'SAP_FLUX\n']


    delete("fake_lc.csv", "kepconvert.log", False)

    # convert to ascii
    kepconvert(fake_lc, "fake_lc.txt",
               "fits2asc", "TIME,SAP_FLUX", True, True)

    with open('fake_lc.txt', 'r') as asciifile:
        first_line = asciifile.readline()
        first_line = line.split(',')
        assert first_line == ['TIME', 'SAP_FLUX\n']

    delete("fake_lc.txt", "kepconvert.log", False)

