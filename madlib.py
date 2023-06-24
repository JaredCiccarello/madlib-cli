import re

print("Welcome to madlib!")

def read_template(file_path):
  with open (file_path, 'r') as file:
    template = file.read()

    return template
    
def parse_template(template):
  # nonCurly variable is used to keep track whether or not characters are inside curly braces
  nonCurly = False
  # 
  storyDictionary = ''
  # emptyFiller variable is used to store content inside curly braces
  emptyFiller = ''
  # wholeWordList stores individual words found inside the curly braces
  wholeWordList = []
  # ignore simply ignores these specific characters when reading the template
  ignore = ['{', '}']  

  for char in template:
    if char == '}':
      wholeWordList.append(emptyFiller)
      emptyFiller = ''
      nonCurly = False
    if char == '{':
      storyDictionary += char
      nonCurly = True
    if nonCurly == False:
        storyDictionary += char
    else: 
      if char not in ignore:
        emptyFiller += char
  return storyDictionary, tuple(wholeWordList)

def newList(wholeWordList):
  newWholeWordList = []

  for i in wholeWordList:
    userInput = input(f"Enter a(n) {i}: ")
    newWholeWordList.append(userInput)
  print(newWholeWordList)
  return tuple(newWholeWordList)

def merge(storyDictionary, newWholeWordTuple):
  newWholeWordList = list(newWholeWordTuple)
  pattern = r"\{([^}]*)\}"
  result = re.sub(pattern, lambda x: newWholeWordList.pop(0), storyDictionary)
  print(result)
  return result

def write_madlib_to_file(file_path, madlib):
  with open(file_path, 'w') as file:
    file.write(madlib)

if __name__ == "__main__":
  template = read_template('madlib.txt')
  stripped_template, parts = parse_template(template)
  newList = newList(parts)
  finalStory = merge(stripped_template, newList)
  write_madlib_to_file('finished_madlib.txt', finalStory)
  parse_template(template)
  


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