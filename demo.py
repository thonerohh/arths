import library.med as med

sentence = "This is an example sentence with varied vocabulary."
words = sentence.split(' ')

demo = 'aeiouy'
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

sentence_length = len(sentence)
new_sentence_length = len(new_sentence)

words_length = []
for word in words:
  words_length.append(len(word))

new_words_length = []
for word in new_words:
  new_words_length.append(len(word))

words_sum = sum(words_length)
new_words_sum = sum(new_words_length)

word_biases = list(med.origami(words_length))
new_word_biases = list(med.origami(new_words_length))

words_patt = med.exclude(words_length,new_words_length)
words_diff = med.clarify(words_length,new_words_length,med.exclude(words_length,new_words_length))

print (sentence)
print (new_sentence)
print ('---')
print (sentence_length)
print (new_sentence_length)
print (words_sum)
print (new_words_sum)
print ('---')
diff_coef = ((words_sum + new_words_sum) / len(words_length) * 2) / ((sentence_length + new_sentence_length) / 2)
patt = []
patt_lens = []
_temppatt = []
for char in sentence:
  temp = ''
  if char not in demo:
    temp += char
  else:
    temp += char
    _temppatt += [temp]

temp2 = ''
for splitter in _temppatt:
  # find first index splitter in sentence and slice
  index = sentence.index(splitter)
  temp2 += sentence[:index]
  sentence = sentence[index:]
  patt += [[len(temp2), temp2]]
  patt_lens += [len(temp2)]

print (diff_coef)
print (_temppatt)
print (patt)
print (patt_lens)

print ('---')
sentence_coef = (((sentence_length + new_sentence_length + sum(patt_lens)) / (len(_temppatt) ** diff_coef))) / (((sentence_length - len(words_length))) / ((words_sum + len(words_length))))
new_sentence_coef = (((new_sentence_length + sentence_length + sum(patt_lens)) / (len(_temppatt) ** diff_coef))) / ((( new_sentence_length - len(new_words_length))) / ((new_words_sum + len(new_words_length))))
print (sentence_coef)
print (new_sentence_coef)

checksum = abs(sentence_coef / len(words_length) - sentence_length)
checksum_new = abs(new_sentence_coef / len(new_words_length) - new_sentence_length)

print (checksum)
print (checksum_new)
print ('---')

print (words_length)
print (new_words_length)
print (words_patt)
print (words_diff)
print ('---')
print (word_biases)
print (new_word_biases)

upper_bias = med.exclude(list(med.origami(words_length))[2], list(med.origami(new_words_length))[2])
upper_active_bias = med.clarify(list(med.origami(words_length))[3], list(med.origami(new_words_length))[3],med.exclude(list(med.origami(words_length))[2], list(med.origami(new_words_length))[2]))

print (upper_bias)
print (upper_active_bias)
print ('---')

bottom_bias = med.exclude(list(med.origami(words_length))[1], list(med.origami(new_words_length))[1])
bottom_correctional_bias = med.clarify(list(med.origami(words_length))[4], list(med.origami(new_words_length))[4],med.exclude(list(med.origami(words_length))[0], list(med.origami(new_words_length))[1]))
print (bottom_bias)
print (bottom_correctional_bias)



# print ('sentence len:', len(sentence))
# print ('original words lengths:', each_word_len, "sum:", sum(each_word_len), 'len:', len(each_word_len), 'sent diff:', len(sentence) - sum(each_word_len))
# print ('modified words lengths:', each_new_word_len, "sum:", sum(each_new_word_len), 'len:', len(each_new_word_len),'sent diff:', len(sentence) - sum(each_new_word_len))
# print ('modified words bias:', new_words_medians, "sum:", sum(new_words_medians), 'len:', len(new_words_medians), 'sent diff:', len(sentence) - sum(new_words_medians))
# print ('diff between words:', words_difference, "sum:",sum(words_difference), 'len:', len(words_difference), 'sent diff:', len(sentence) - sum(words_difference))
# print ('fair new words len:', brand_new_words_array, "sum:", sum(brand_new_words_array), 'len:', len(brand_new_words_array), 'sent diff:', len(sentence) - sum(brand_new_words_array))