from fastio import walk

def filepaths(DIR):
  '''
  Return path of every file located in dir and subdir of DIR
  '''
  paths = []
  files = walk(DIR)
  for i in files: # for (path, subdir, files) in files
    for j in i[-1]:# for filenames in  files
        paths.append(i[0]+'\\'+j)
  return paths

def extension(path):
  return path.split('\\')[-1].split('.')[-1]

def ext_discover(path):
  exts = []
  files = filepaths(path)
  for i in files:
    ext = extension(i).lower()
    if len(ext) < 6:
      if ext not in exts:
        exts.append(ext)
  return exts

def classify(path):
  files = filepaths('g://')
  d = {
    'Music':['mp3', 'wav'],
    'Pic':['jpg', 'gif', 'jpeg'],
    'Movie':['mkv', 'mp4']
       }
  data = {}
  for filename in files:
    for i in d.values():
      if extension(filename) in  i:
        if len(data[list(d.keys())[(list(d.values()).index(i))] ]) == 0:
          data[list(d.keys())[(list(d.values()).index(i))] ] = [filename]
        else:
          data[list(d.keys())[(list(d.values()).index(i))] ].append(filename)
  print(data)
  

#print(ext_discover('e://'))
classify('g://')
