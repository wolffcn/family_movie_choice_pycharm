
#takes input from each family member with their top movie choices and picks which one will be the best choice


movies = input("What movies are out at local theaters right now? ")
movie_choices = [movie.strip() for movie in movies.split(',')]

family = ["Mom", "Dad", "Ryan", "Christina", "Brandon", "Jordan", "Jason"]

first_choices = []
second_choices = []
third_choices = []
for person in family:
    first_choice = input(f"{person}, what is your first choice? ")
    first_choices.append(first_choice)

    second_choice = input(f"{person}, what is your second choice? ")
    second_choices.append(second_choice)

    third_choice = input(f"{person}, what is your third choice? ")
    third_choices.append(third_choice)


#makes a score based on families movie ranking
movie_scores = {}

for movie in movie_choices:
    movie_scores[movie] = 0
    if movie in first_choices:
        movie_scores[movie] = first_choices.count(movie) * 3
    if movie in second_choices:
        movie_scores[movie] = second_choices.count(movie) * 2 + movie_scores[movie]
    if movie in third_choices:
        movie_scores[movie] = third_choices.count(movie) * 1 + movie_scores[movie]

#prints movies scores to determine the best choice for a family movie

ordered_movie_scores = dict(sorted(movie_scores.items(), key=lambda item: item[1], reverse=True))
count = 0
for movie, score in ordered_movie_scores.items():
    if count == 0:
        print(f"{movie} is the best choice for the Wolff Family movie outing! Score: {score}")
    if score != 0 and count != 0:
        print(f"{movie}: {score}")
    count = count + 1



