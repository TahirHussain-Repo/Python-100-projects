#Project Description
    # How to rename files with python, and classifying it by number of words and the day of the week.

import os
from datetime import datetime

directory = 'files'

originalFiles = os.listdir(directory)

for ogFiles in originalFiles:
    print(ogFiles)
    
    filepath = os.path.join(directory, ogFiles)

     
