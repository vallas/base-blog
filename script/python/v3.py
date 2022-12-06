import os

def visualize(directory, mode='tree'):
  if mode == 'tree':
    print(f'+ {directory}')
    for root, dirs, files in os.walk(directory):
      level = root.replace(directory, '').count(os.sep)
      indent = ' ' * 4 * (level)
      print(f'{indent}|- {os.path.basename(root)}/')
      subindent = ' ' * 4 * (level + 1)
      for f in files:
        print(f'{subindent}|- {f}')
  elif mode == 'diagram':
    print(f'{directory}/')
    for root, dirs, files in os.walk(directory):
      level = root.replace(directory, '').count(os.sep)
      indent = ' ' * 4 * (level)
      print(f'{indent}|- {os.path.basename(root)}/')
      subindent = ' ' * 4 * (level + 1)
      for f in files:
        print(f'{subindent}|- {f}')
  else:
    print('Invalid visualization mode')

visualize('./', mode='tree')
