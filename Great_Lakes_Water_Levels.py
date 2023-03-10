# +
<<<<<<< HEAD
#""""
=======

>>>>>>> origin/kriser
#To use this notebook for your in-class assignment, you will need these 
#files, which you shoujld have downloaded:
#* mhu.csv -- Lake Michigan and Lake Huron
#* sup.csv -- Lake Superior
#* eri.csv -- Lake Erie
#* ont.csv -- Lake Ontario

#As instructed in the in-class activity notebook for today, you are 
#only expected to complete one PART below. Do not worry if your group 
#is not big enough to finish all parts below, but if you have extra 
<<<<<<< HEAD
#time, you're welcome to do so. 
#""""
=======
#time, you're welcome to do so.
>>>>>>> origin/kriser

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# -


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

mhu_data = pd.read_csv('mhu.csv')

mhu_data

plt.plot(mhu_data['time'],mhu_data['lake average'])
plt.ylabel('lake average')
plt.xlabel('year')

# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years
df = pd.read_csv("CMSE202/repositories/Day_04_Git_Collab/sup.csv")
x_dhar = df["lake levels"]
y_dhar = df["year"]

plt.plot(y_dhar, x_dhar)


# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years



# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years
ont = pd.read_csv("ont.csv")
plt.plot(ont["year"], ont["Lake Ontario annual averages"])


# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.



# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.



# PART 7
# Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.


