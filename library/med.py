
def exclude(object,subject): # exclude 1 array from another returning array form: 2 arrays
  length = min(len(object), len(subject))
  obj = []
  for i in range(length):
    obj.append(object[i] - subject[i])
  return obj

def exclude__com(object,subject): # exclude 1 array from another returning array form: 2 arrays with comments
  length = min(len(object), len(subject))
  obj = []
  for i in range(length):
    obj.append(object[i] - subject[i])
    print ('---')
    print ('object:', object[i])
    print ('sbject:', subject[i])
    print ('result:', obj[i])
  return obj

def clarify(object,subject,form): # clarify: 3 arrays as big small and their form ex. exclude or include
  length = min(len(object), len(subject))
  obj = []
  for i in range(length):
    maxw = max(object[i], subject[i])
    minw = min(object[i], subject[i])
    if (form[i] > 0):
      obj.append(maxw + form[i])
    else:
      obj.append(minw + form[i])
  return obj

def clarify__com(object,subject,form): # clarify: 3 arrays as big small and their form ex. exclude or include with comments
  length = min(len(object), len(subject))
  obj = []
  for i in range(length):
    maxw = max(object[i], subject[i])
    minw = min(object[i], subject[i])
    if (form[i] > 0):
      obj.append(maxw + form[i])
    else:
      obj.append(minw + form[i])
    print ('---')
    print ('object:', object[i])
    print ('sbject:', subject[i])
    print ('form:', form[i])
    print ('result:', obj[i])
  return obj

def waves(object, subject): # wave: 2 array
  length = min(len(object), len(subject))
  obj1 = []
  obj2 = []
  obj3 = []
  obj4 = []
  obj5 = []
  for i in range(length):
    words_median_amplitude = abs(object[i] - subject[i])
    words_median_hyperbolization = abs(object[i] - subject[i]) / 2
    words_median = (words_median_amplitude) / 2 + min(object[i], subject[i])
    obj1.append(words_median)
    obj2.append(words_median + words_median_amplitude)
    obj3.append(words_median - words_median_amplitude)
    obj4.append(words_median + words_median_hyperbolization)
    obj5.append(words_median - words_median_hyperbolization)
  return obj2, obj4, obj1, obj5, obj3

def wave(object): # wave: 1 array
  length = int(len(object) / 2) 
  obj1 = []
  obj2 = []
  obj3 = []
  obj4 = []
  obj5 = []
  for i in range(length):
    words_median_amplitude = abs(object[i] - object[i + length])
    words_median_hyperbolization = abs(object[i] - object[i + length]) / 2
    words_median = (words_median_amplitude) / 2 + min(object[i], object[i + length])
    obj1.append(words_median)
    obj2.append(words_median + words_median_amplitude)
    obj3.append(words_median - words_median_amplitude)
    obj4.append(words_median + words_median_hyperbolization)
    obj5.append(words_median - words_median_hyperbolization)
  return obj2, obj4, obj1, obj5, obj3

def oil(object,subject): # absolute aka oil: 2 arrays
  length = min(len(object), len(subject))
  obj = []
  for i in range(length):
    maxw = max(object[i], subject[i])
    minw = min(object[i], subject[i])
    obj.append(maxw - minw)
  return obj

def oil__com(object,subject): #absolute as oil: 2 arrays with comments

  length = min(len(object), len(subject))
  obj = []
  for i in range(length):
    maxw = max(object[i], subject[i])
    minw = min(object[i], subject[i])
    obj.append(maxw - minw)
    print ('---')
    print ('object:', object[i])
    print ('sbject:', subject[i])
    print ('max:', maxw)
    print ('min:', minw)
  return obj

def folding(object, times): # 1 array with times to fold twice
  if not times:
    times = len(object) // 2 
  elif times > 4 and len(object) > 32:
    times = 4
  elif times < 1 and len(object) > 4:
    times = 1
  else:
    times = len(object) // 2 

  grp = []

  def fold(object):
    length = int(len(object) / 2)
    obj1 = []
    obj2 = []
    obj3 = []
    med = sum(object) / length
    for i in range(length):
      obj2.append(med)
      sub1 = med + abs(object[i] - med)
      sub2 = med - abs(object[i] - med)
      obj1.append(sub1)
      obj3.append(sub2)
    return obj1,obj2,obj3

  new_grp = list(fold(object))
  grp.extend(new_grp)
  temp_grp = []
  for i in range(times):# copy temp_new_grp to new_grp
    if len(new_grp[0]) > 2:
      
      if len(new_grp) % 2 == 0:
        half_length = int(len(new_grp) / 2)
      else:
        half_length = int(len(new_grp) / 2) + 1

      for j in range(half_length):
        if j % 2 == 0:
          new_grp.pop(j+1)# remove all even index variables from new_grp

      for grp1 in new_grp:
        if len(grp1) < 3:
          grp.extend(new_grp)
          return grp

        temp_grp += fold(grp1)

      grp.extend(temp_grp)
      new_grp = temp_grp

  return grp

def origami(object): # 1 array
  length = len(object)
  obj1 = []
  obj2 = []
  obj3 = []
  obj4 = []
  obj5 = []
  
  med = sum(object) / length
  for i in range(length):
    sub1 = med + abs(object[i] - med)
    sub2 = med - abs(object[i] - med)
    sub3 = med + abs(abs(object[i] - med) / 2 + abs(object[i] - med))
    sub4 = med - abs(abs(object[i] - med) / 2 + abs(object[i] - med))

    obj1.append(med)
    obj2.append(sub1)
    obj3.append(sub2)
    obj4.append(sub3)
    obj5.append(sub4)

  return obj4,obj2,obj1,obj3,obj5

