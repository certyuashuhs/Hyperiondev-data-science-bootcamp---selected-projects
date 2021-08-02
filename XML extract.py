import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')

root = tree.getroot()

#print(root.tag)
print()

print('Movies that are favorites:')

print()

# initiating variable to count favorite movies
count1 = 0
#creating for loop to get all movies that are favorites and also getting the text from the child tags
for movies in root.iter('movie'):
    movie_attributes = movies.attrib
    if movie_attributes['favorite'] == 'True':
        print("Movie:", movie_attributes['title'])
        favorites = "".join(movies.itertext())
        print(favorites)
        count1 += 1
# printing number of favorite movies
print(f'number of favorite movies is {count1}')

print()

print('Movies that are not favorites:')

print()

# initiating variable to count non favorite movies
count2 = 0

# creating for loop to get all movies that are not favorites and also getting the text from the child tags
for movies2 in root.iter('movie'):
    movie_attributes = movies2.attrib
    if movie_attributes['favorite'] == 'False':
        print("Movie:", movie_attributes['title'])
        non_favorites = "".join(movies.itertext())
        print(non_favorites)
        count2 += 1

# printing number of non-favorite movies
print(f'number of non-favorite movies is {count2}')    
    