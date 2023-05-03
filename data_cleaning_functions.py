import csv
import pandas as pd
from imdb import Cinemagoer, IMDbError  
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Find
import csv


def get_language_from_imdb(outfile, infile):
    '''appends movies that have languages found on imdb to the outfile'''
    out = open(outfile, "a")

    # create an instance of the Cinemagoer class
    ia = Cinemagoer()

    with open(infile, mode ='r') as file:
    
        # reading the CSV file
        movies = csv.reader(file, delimiter='\t')

        print('Languages:')
        for movie in movies:
            film = ia.get_movie(int(movie[0]))
            if (film.get('languages') is not None):
                print(movie[0],film.get('languages')[0])
                result = movie[0]+'\t'+film.get('languages')[0]+'\t'+movie[1]+'\t'+movie[2]+'\t'+movie[3]+'\t'+movie[4]+'\t'+movie[5]
                result = result + '\t'+movie[6]+'\t'+movie[7]+'\t'+movie[8]+'\t'+movie[9]+'\t'+movie[10]+'\t'+movie[11]+'\n'
            else:
                print(movie[0],"no language")
                result=movie[0]+'\tnolanguage\t'+movie[1]+'\t'+movie[2]+'\t'+movie[3]+'\t'+movie[4]+'\t'+movie[5]
                result = aaaa + '\t'+movie[6]+'\t'+movie[7]+'\t'+movie[8]+'\t'+movie[9]+'\t'+movie[10]+'\t'+movie[11]+'\n'

            out.write(aaaa)
    out.close()

def add_ratings_to_basics(input_file, out_file):
    '''returns outfile that adds star rating and number of ratings to input values'''
    basicsMoviesNoadult = pd.read_csv(input_file, sep='\t')

    ratings = pd.read_csv('title.ratings.tsv', sep='\t')

    my_ratings = ratings['tconst'].unique().tolist()
    new_basic = basicsMoviesNoadult[basicsMoviesNoadult['tconst'].isin(my_ratings)]
    new_basic.to_csv(out_file, sep='\t')

def get_language_from_tmdb(apiKey, input_file):
    '''appends movies that have languages found on tmdb to the outfile'''
    tmdb = TMDb()
    tmdb.api_key = apiKey
    find = Find()

    with open(input_file, mode ='r') as file:
        outfile = open("outfile.tsv", "a")
        # reading the CSV file
        movies = csv.reader(file, delimiter='\t')

        for movie in movies:
            print(movie[2])
            results = find.find_by_imdb_id(movie[2])
            for r in results["movie_results"]:
                result = movie[2]+'\t'+r.original_language+'\t'+movie[3]+'\t'+movie[4]+'\t'+movie[5]+'\t'+movie[6]+'\t'+movie[7]+'\t'
                result = result + movie[8]+'\t'+movie[9]+'\t'+movie[10]+'\t'+movie[11]+'\t'+movie[12]+'\n'
                outfile.write(result)

def missing_values(file1, file2):
    '''returns which films were not found on tmdb'''
    original = pd.read_csv(file1, sep='\t')
    output = pd.read_csv(file2, sep='\t')
    original = original[~original['tconst'].isin(output['tconst'])]
    original.to_csv('output.tsv', sep='\t')

def find_doubles(updated_file, tracking_file):
    '''finds films that have been entered more than once'''
    with open(updated_file, 'r') as file:
        lst = set()
        doubles = []
        movies = csv.reader(file)
        for movie in movies:
            if movie[0] not in lst:
                lst.add(movie[0])
            else:
                doubles.append(movie[0])
                
    with open(tracking_file, 'a') as fl:
        for item in doubles:
            entry = item + '\n'
            fl.write(entry)
