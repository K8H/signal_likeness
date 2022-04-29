import os

import pandas as pd


class Dataset(object):

    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

    def __int__(self, substance_name):
        substance_df = pd.read_csv(f'{self.data_dir}/{substance_name}.csv', names=['x', 'y'])
        self.X = substance_df.x
        self.Y = substance_df.y
