from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
# urlretrieve(movie_data, movies_csv)

NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')



def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()

cnt = Counter()
for director, movies in directors.items():
    print(director)
    cnt[director] += len(movies)

cnt.most_common(5)

# Still having issues with this portion
def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    directors_new = defaultdict(list)
    for director, movies in directors.items():
        # print(directors[director])
        for m in range(len(movies)):
            # print(movies[m].year)
            if movies[m].year >= MIN_YEAR and len(movies) >= MIN_MOVIES:
                directors_new[director].append(movies[m])
    
    for director, movies in directors_new.items():
        directors_new[director].append(_calc_mean(movies))

    
    return directors_new

# This is finished
def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    total_score = 0
    for _ in movies:
        total_score += _.score

    mean_score = total_score/len(movies)
    return round(mean_score,1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()