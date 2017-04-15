count = 0
temp_file = open('final_words.txt', 'a')

with open('words.txt') as f:
    for line in f:
        if(line[0] != '#'):
                temp_file.write(line)