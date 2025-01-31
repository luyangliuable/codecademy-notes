# import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd


iris = datasets.load_iris()

samples = iris.data

target = iris.target

model = KMeans(n_clusters=3)

model.fit(samples)

labels = model.predict(samples)

# Code starts here:
species = np.chararray(target.shape, itemsize=150)
print(species)


for i in range(len(samples)):
  if target[i] == 0:
    species[i] = 'setosa'


df = pd.DataFrame({'labels': labels, 'species': species})

# perform cross-tabulation
ct = pd.crosstab(df['labels'], df['species'])
print(ct)
