
#Takes input from each family member with their top movie choices and picks which one will be the best choice
#step 1: Ask what movies are playing at the local theater and create a list and  Make list of family members:
#step 2: Ask family member to rank movie choices:
#step 3: Iterate through family to ask movie choices:
#step 5: create a score based on choice
#make an iteration of movie_choices to count how many times they appear in each list first second third...
#step 7: add up each movies score for a final score. If a movie is a first choice it gets 3, then 2 then.
#step 8: Make it a dictionary instead of a list


#ideas for next level: API to micon?
# GUI? or learn python phone app?

# movies = input("What movies are out at local theaters right now? ")
movies = "Mocking Jay, The Color Purple, Auquaman, Trolls, Migration, Wonka, Ferrari, Iron Claw"
movie_choices = [movie.strip() for movie in movies.split(',')]

# family = ["Mom", "Dad", "Ryan", "Christina", "Brandon", "Jordan", "Jason"]
family = ["Mom", "Dad"]

# first_choices = []
# second_choices = []
# third_choices = []
# for person in family:
#     first_choice = input(f"{person}, what is your first choice? ")
#     first_choices.append(first_choice)
#
#     second_choice = input(f"{person}, what is your second choice? ")
#     second_choices.append(second_choice)
#
#     third_choice = input(f"{person}, what is your third choice? ")
#     third_choices.append(third_choice)

# for testing
first_choices = ['Mocking Jay', 'Wonka']
second_choices = ['Trolls', 'Migration']
third_choices = ['Migration', 'The Color Purple']

movie_scores = {}

for movie in movie_choices:
    movie_scores[movie] = 0
    if movie in first_choices:
        movie_scores[movie] = first_choices.count(movie) * 3
    if movie in second_choices:
        movie_scores[movie] = second_choices.count(movie) * 2 + movie_scores[movie]
    if movie in third_choices:
        movie_scores[movie] = third_choices.count(movie) * 1 + movie_scores[movie]

# Step 7: Print the scores
# print("Movie Scores:")
ordered_movie_scores = dict(sorted(movie_scores.items(), key=lambda item: item[1], reverse=True))
count = 0
for movie, score in ordered_movie_scores.items():
    if count == 0:
        print(f"{movie} is the best choice for the Wolff Family movie outing! Score: {score}")
    if score != 0 and count != 0:
        print(f"{movie}: {score}")
    count = count + 1


#scripts
# Mocking Jay, The Color Purple, Auquaman, Trolls, Migration, Wonka, Ferrari, Iron Claw


