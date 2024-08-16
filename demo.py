sentence = "This is an example sentence with varied vocabulary."
words = sentence.split(' ')

demo_vocabulary = {'a': 'a','y': 'y','e': 'ee','u': 'uu','o': 'ooo','i': 'iii'} # not rational whatever
new_words = []

def demo_vocabulary_translation(word):
  new_word = ''
  for char in word:
    for key in demo_vocabulary.keys():
      if char == key:
        new_word += demo_vocabulary[key]
  new_words.append(new_word)

for word in words:
  demo_vocabulary_translation(word)

new_sentence = ' '.join(new_words) # iii iii a eeaee eeeeee iii aiiiee oooauuay

