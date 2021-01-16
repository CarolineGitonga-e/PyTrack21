#MovieFacts

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
#print(movies[0])
#print(movies[1])
#print(movies[2])

#Insert details(corresponding years) to the list.Every time a value is inserted the list grows
movies.insert(1,1975)
#print(movies)
movies.insert(3,1979)
#print(movies)
movies.insert(5,1983)
#print(movies)

#for loop -Iterating through list items
#for movie in movies:
#    print(movie)

#while loop -Iterating through list items
#count = 0
#while count < len(movies):
 #   print(movies[count])
 #   count += 1

#Nested List
holygrail = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
 ["Graham Chapman",
 ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#print(holygrail)

#Iterate Nested List
for each in holygrail:
    if isinstance(each,list):
        for item in each:
            if isinstance(item,list):
              for deeper_item in item:
                  print(deeper_item)
            else:  
                print(item)
    else:
        print(each)
