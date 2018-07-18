from __future__ import print_function

import os
import h5py
import json

import numpy as np

def main(_):


def read_data(hf):
  with h5py.File(fname, 'r') as hf:
    return unpack(hf)

    # recusively unpack h5 groups or return numpy wrapped value
    def unpack(r):
      if type(r) is h5py.Group or type(r) is h5py.File:
        return {k: unpack(v) for k, v in r.items()}
      else:
        return np.array(r)

def convert_keys_numerical_suffix_to_list(d, key_prefix):
  """Converts dict keys like prefix_01 to ordered list

  Given a dict with keys whose names are given by a prefix followed by a
  numerical prefix, generates a list with the values in order. Will raise an
  exception if the keys are not contiguous from 0:max_value or 1:max_value

  Args:
    d: dictionary with number-suffix keys
    key_prefix: string prefix for keys

  Returns:
   list with dict values in order
  """
