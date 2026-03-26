from data import movies

def display_movies(movies):
    movie_list = {}
    for movie in movies:
        if movie['Watched']==False:
            movie_list[movie['Title']] = movie['Rating']
    return movie_list

def recommend_movie(movies):
    movie_list = {}
    for movie in movies:
        if movie['Rating']>9 and movie['Watched']==False:
            movie_list[movie['Title']] = movie['Rating']
    return movie_list




watched=display_movies(movies)
print("Unwatched movies:")
print()
for movie in watched:
    print(movie,":",watched[movie])
print()




recommend=recommend_movie(movies)
if recommend:
    print("Recommend movies:")
    print()
    for movie in recommend:
        print(movie,":",recommend[movie])