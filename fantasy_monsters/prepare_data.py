__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"


import csv
import os
import re
import sys

import pandas as pd


SEP = '[SEP]'

def read_data(data_fn, output_fn):
    data = pd.read_csv(data_fn)
    with open(output_fn, "w") as f:
        for i, row in data.iterrows():
            f.write(f"{row['Name']}{SEP}{row['Description_Visual']}\n")
    return


if __name__ == '__main__':
    data_dir = sys.argv[1]
    read_data(
        os.path.join(data_dir, 'monster_bestiary_full - Updated 27Jul2015.csv'), os.path.join(data_dir, 'monster-description.csv'))
