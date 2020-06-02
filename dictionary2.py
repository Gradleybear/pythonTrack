#Building Dictionaries
#By now you are familiar with two important concepts: 1) counting with for loops and 2) the dictionary get method. These two can actually be combined to create a useful counter dictionary, something you will likely come across again. For example, we can create a dictionary, word_counter, that keeps track of the total count of each word in a string.

#The following are a couple of ways to do it:

#Method 1: Using a for loop to create a set of countersB
#Let's start with a list containing the words in a series of book titles:
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)
