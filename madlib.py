import re
def welcome_message():
  message = "Welcome to madlib!"

  print(message)

def read_template():
  with open('madlib.txt', "r")as file:
    template = file.read()

    print (template)
  

non_curly = False
story_dictionary = ''
story_list = []
word_list = []
empty_filler = ''
ignore = ["{","}"]
new_list = []

# parse template into useable parts
for char in template:
    if char == "}":
        word_list.append(empty_filler)
        empty_filler = ''
        non_curly = False

    if char == "{":
        # when changing value use single =
        non_curly = True
        story_dictionary = ''

    if non_curly == False:
        if char not in ignore:
          story_dictionary += char

    else:
        if char not in ignore:
          empty_filler += char

# prompt user to submit words for matching spaces
for i in word_list:  
  user_input = input(f"enter a(n) {i}: ")
#  take user input and populate the template with user answer
  updated_string = new_list.append(user_input)

print(new_list)
#  give user back completed response


pattern = r"\{([^}]*)\}"
result = re.sub(pattern, lambda word: new_list.pop(0), template)

print(result)


with open('finished_madlib.txt', "w")as file:
    template = file.write(result)


if __name__ == "__main__":
  welcome_message()
  words = read_template(template)
  pass
  


# Adjective 1: {Adjective}
# Adjective 2: {Adjective}
# First Name 1: {A First Name}
# Past Tense Verb: {Past Tense Verb}
# First Name 2: {A First Name}
# Adjective 3: {Adjective}
# Plural Noun 1: {Plural Noun}
# Large Animal: {Large Animal}
# Small Animal: {Small Animal}
# Girl's Name: {A Girl's Name}
# Adjective 4: {Adjective}
# Plural Noun 2: {Plural Noun}
# Adjective 5: {Adjective}
# Plural Noun 3: {Plural Noun}
# Number 1-50: {Number 1-50}
# First Name 3: {First Name}
# Number: {Number}
# Plural Noun 4: {Plural Noun}
# Number: {Number}
# Plural Noun 5: {Plural Noun}