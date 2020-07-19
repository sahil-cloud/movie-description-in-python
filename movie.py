import imdb

# initialising the imdb class
ia = imdb.IMDb()

# geeting movie info by movie name


def movie_by_name():
    movie = input('Enter the name of the movie')
    # it will return a list of movie matching the movie name we will select the first one
    movies = ia.search_movie(movie)
    index = movies[0].getID()
    movie_ = ia.get_movie(index)
    # year = movie_.infoset2keys
    year = movie_['year']
    cast = movie_['cast']
    list_cast = ','.join(map(str, cast))
    genres = movie_['genres']
    box_office = movie_['box office']
    director = movie_['director']
    list_dir = ','.join(map(str, director))
    rating = movie_['rating']
    plot = movie_['plot outline']
    country = movie_['countries']
    title = movie_['title']
    writer = movie_['writer']
    list_wri = ','.join(map(str, writer))
    producer = movie_['producers']
    list_pro = ','.join(map(str, producer))
    # print(title,writer[0],country)
    print(f'title: {title}')
    print(f'year of release: {year}')
    print(f'cast: {list_cast}')
    print(f'rating: {rating}')
    print(f'genres: {genres}')
    print(f'director: {list_dir}')
    print(f'writer: {list_wri}')
    print(f'country: {country}')
    print(f'producer: {list_pro}')
    print(f'plot: {plot}')
    print(f'box_office: {box_office}')


def movie_by_key():
    movie = input('Enter the keyword')
    movies = ia.get_keyword(movie)
    # print(movies[0])
    list_movie = ','.join(map(str, movies))
    a = 0
    for i in movies:
        a = a+1
        index = i.getID()
        movie_ = ia.get_movie(index)
        print(movie_, end="  ")
        print(movie_['genres'], end="  ")
        print(movie_['year'])
        print(movie_['plot outline'])
        print()
        print()
        if(a == 50):
            break


def top_250():
    movies = ia.get_top250_movies()
    list_movie = ','.join(map(str, movies))
    a = 0
    print('Top 50 Movies inImdb')
    for i in movies:
        a = a+1
        index = i.getID()
        movie_ = ia.get_movie(index)
        print(movie_, end="  ")
        print(movie_['genres'], end="  ")
        print("rating:", end="")
        print(movie_['rating'], end="  ")
        print(movie_['year'])
        print(movie_['plot outline'])
        print()
        print()
        if(a == 50):
            break


# movie_by_key()
# movie_by_name()
top_250()
