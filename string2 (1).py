#define a helper function, The method takes a string, slices it on its first letter and capitalizes it, the rest of the string is converted to lowercase
def cap_word(string):
    return string[:1].capitalize() + string[1:].lower()
#Take a paragraph and store it in a string
#then separate the string into words and store them into a list  
string = "hello, my, name, is, haya, and, this, is, my, soulution, thank, you"

lst = string.split(',')
lst = [s.strip() for s in lst]
lst = [cap_word(s) for s in lst]

# Create an empty dictionary
d = dict()
  
# Loop through each line of the list
for line in lst:
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])