import os

from pyms.GCMS.IO.JCAMP import JCAMP_reader

data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data/jcamp')

jcamp_file = f"{data_dir}/gc01_0812_066.jdx"
data = JCAMP_reader(jcamp_file)
print(data)