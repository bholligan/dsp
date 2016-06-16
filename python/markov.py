#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import random, sys, re

#Assign the first and second args from command line to variables
filename = sys.argv[1]
word_limit = int(sys.argv[2])

#Put text file into a string
with open(filename, newline='', encoding = 'utf-8') as file:
    file_text = file.read().replace('\n','')

#Create and populate dictionary with every x-letter sequence in the text as the key and the following letter as the value
mega_dict = {}
increment = 4   #Used to determine the length of the letter sequence 
for idx, letter in enumerate(file_text):
    if idx == (len(file_text)-increment):
        break #Stop the dictionary creation at the end of the file
    else:
        let_seq = file_text[idx:(idx+increment)]
        if let_seq in mega_dict:
            mega_dict[let_seq].append(file_text[idx+increment])
        else:
            mega_dict[let_seq] = []
            mega_dict[let_seq].append(file_text[idx+increment])

#Create an output string based on the created dictionary.
#Randomizing the choice of which letter to use next from the list of letters in the dictionary will satisfy Markov rules
#For example, if the key 'othe' has values ['r','r','l'], the letter 'r' will be picked 2/3 of the time          
def markov_string(total_words):
    #Perhaps breaking rules, but this starts output with random 4 letter sequence that leads with upper case   
    output = random.choice([key for key in mega_dict if key[0].isupper()])
    pos = increment
    word_count = 0
    next_value = ''
    while word_count < total_words or next_value != ' ': 
        last_seq = output[(pos-increment):pos]
        if last_seq in mega_dict:
            dict_values = mega_dict[last_seq]
            random_num = random.randint(0,(len(dict_values)-1)) #Generate a random number that falls within the size of the dict value list
            next_value = dict_values[random_num] #Get a random letter from the list of letters
        else:
            next_value = random.choice([mega_dict[key] for key in mega_dict])
        output += next_value
        pos += 1
        word_count = len(re.findall(r'\b\S+\b',output)) #Get current word count
    return output

print(markov_string(word_limit))