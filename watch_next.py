import spacy

nlp = spacy.load('en_core_web_md')

def watch_next(movie_description, file_name):

    # Dictionaies of movies and similarities
    movies = {}
    movie_similarity = {}

    # Get data from file and put in movies dict
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip("\n")
            split_line = line.split(" :")
            movies[split_line[0]] = split_line[1]

    movie_description = nlp(movie_description)

    # Comparing movie descriptions and adding similarity values to movie_similarity dict
    for movie in movies:
        token = nlp(movies[movie])
        movie_similarity[movie] = token.similarity(movie_description)

    # Return max value ie. greatest similarity, looked up on Stack Overflow.
    return max(movie_similarity, key=lambda key: movie_similarity[key])


# Movie to compare
planet_hulk = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space 
to a planet where the Hulk can live in peace. Unfortunately, 
Hulk land on the planet Sakaar where he is sold into slavery 
and trained as a gladiator."""

print(watch_next(planet_hulk, "movies.txt"))