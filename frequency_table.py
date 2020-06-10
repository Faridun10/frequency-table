

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# Extract the specific column from list of lists data set 
def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

# Pass in the column index number 
genres = extract(11)
user_ratings = extract(7)

# Generate the frequency table
def freq_table(a_list):
    frequency_table ={}
    for row in a_list:
        if row in frequency_table:
            frequency_table[row] += 1
        else:
            frequency_table[row] = 1
    return frequency_table

genres_ft = freq_table(genres)
user_ratings_ft = freq_table(user_ratings)
print(genres_ft)
print('\n')
print(user_ratings_ft)


# Version 2
## Shorter version of the same function

def freq_table(index):
    frequency_table = {}
    for row in apps_data[1:]:
        column = row[index]
        if column in frequency_table:
            frequency_table[column] += 1
        else:
            frequency_table[column] = 1
    return frequency_table

ratings_ft = freq_table(7)
print(ratings_ft)
