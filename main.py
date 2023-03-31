import numpy as np
import matplotlib.pylab as plt
import pandas as pd
#########################
# check file if found or not 
#########################
filename='Test.txt'
try: 
  file = open(filename,'a')
except:
  file = open(filename,'w')
file.write("header for the file\n")
file.close()
