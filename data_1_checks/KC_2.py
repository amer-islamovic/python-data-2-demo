import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

mangas = pd.read_csv('C:/Users/aisla/OneDrive/Desktop/Pi/data_1_checks/assets/manga.csv')

Manga_Name = mangas['rank']
Manga_Popularity = mangas['popularity']

plt.figure(figsize = (12, 6))
plt.scatter(Manga_Name, Manga_Popularity, marker = 's', color = 'orange')
plt.xlabel('Rank')
plt.ylabel('Popularity')
plt.title('Scatterplot of Manga Rank vs. Popularity')
plt.show()