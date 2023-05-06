import pandas as pd
import csv

# directors.basics.tsv lines:
# directors	primaryName	birthYear	deathYear	primaryProfession
# nm0000005	Ingmar Bergman	1918	2007	writer,director,actor

# title.directors.purged.tsv lines:
# tconst	directors
# tt0000001	nm0005690 

directors_names = pd.read_csv('directors.basics.tsv', sep='\t')
tt_vs_directors = pd.read_csv('title.directors.purged.tsv', sep='\t')
merged_inner = pd.merge(left=directors_names, right=tt_vs_directors, left_on='directors', right_on='directors')
merged_inner.to_csv('new_directors.basics.tsv', sep='\t')

combineddata = pd.read_csv('combineddata.tsv', sep='\t')
tt_vs_directors = pd.read_csv('title.directors.purged.tsv', sep='\t')
merged_inner = pd.merge(left=combineddata, right=tt_vs_directors, left_on='tconst', right_on='tconst')
merged_inner.to_csv('new_combineddata.tsv', sep='\t')

combineddata = pd.read_csv('new_combineddata.tsv', sep='\t')
directors = pd.read_csv('directors.basics.tsv', sep='\t')
merged_inner = pd.merge(left=combineddata, right=directors, left_on='directors', right_on='directors')
merged_inner.to_csv('combineddata_with_directors.tsv', sep='\t')
