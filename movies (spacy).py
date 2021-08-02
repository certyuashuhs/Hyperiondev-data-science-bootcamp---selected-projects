import spacy

nlp = spacy.load('en_core_web_md')

first_movie = """ Will he safe the world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace.
Unfortunately Hulk land onto the planet Sakaar where he is sold into slavery and trained as a gladiator."""

def next_movie(description):

    # tokenizing the description 
    description_ = nlp(description)
    
    # list of all movies created and stored within the next_movie function
    movie_list = ["Movie A : When Hiccup discovers Toothless isn\'t the only Night Fury, he must seek \"The Hidden World\", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
                  "Movie B : After the death of Superman, several new people present themselves as possible successors.",
                  "Movie C : A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
                  "Movie D : A humorous take on Sir Arthur Conan Doyle\'s classic mysteries featuring Sherlock Holmes and Doctor Watson.",
                  "Movie E : A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
                  "Movie F : In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain\'s uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
                  "Movie G : The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
                  "Movie H : A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
                  "Movie I : Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in town.",
                  "Movie J : Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
                 ]
    # creating a list to store statiscal values obtained from the similarity comparison
    statistics_list = []

    # looping through each movie (while also tokenizing it) and comparing similarity with the first_movie description and then adding the values to the aforementioned list
    for movies in movie_list:
        choice = nlp(movies).similarity(description_)
        statistics_list.append(choice)

    #print(statistics_list) - this line was for testing purpuses to see items in the list

    # obtaining the max value from the list
    maximum = max(statistics_list)

    #print(maximum)  - this line was for testing purpuses to see the maximum value in the list and if it was correct

    #obtaining the max value index from the list and storing it in a variable
    index = statistics_list.index(maximum)

    #print(index) - this line was for testing purpuses to see the maximum values index to see that it pulled correctly

    # printing the next movie to watch
    print("we recommend your next movie to be the following - ", movie_list[index])

# executing the function            
next_movie(first_movie)

    
