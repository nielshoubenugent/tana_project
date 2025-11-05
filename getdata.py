import h5py
import numpy as np
from astropy import units

def coordskpc():
    data = h5py.File("cutout_598597.hdf5", 'r')
    hubble_param = data["Header"].attrs["HubbleParam"]
    coords = (np.array(data["PartType1"]["Coordinates"]) / hubble_param) * units.kpc
    return coords

def masssolar():
    data = h5py.File("cutout_598597.hdf5", 'r')
    hubble_param = data["Header"].attrs["HubbleParam"]
    masstable = data["Header"].attrs["MassTable"]
    mass = (masstable[1] / hubble_param) * 1e10 * units.Msun    #index 1 means dark matter
    return mass
    