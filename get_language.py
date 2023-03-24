from imdb import Cinemagoer, IMDbError  
import pandas as pd
import numpy as np

movie_df = pd.read_table("movies.tsv",skiprows=range(1,3000), nrows=12001)
 
ia = Cinemagoer()
lst = [['tconst','language']]

counter1=0
counter2=1

for id in movie_df['tconst']:
	if counter1 == 100:
		print(counter2)
		counter2 = counter2+1
		counter1 = 0
	movie = ia.get_movie(id[2::])
	lst.append([id, movie.guessLanguage()])
	counter1=counter1+1

np.savetxt("movie_info_11.tsv", lst, delimiter="\t", fmt ='% s')
print("done")
