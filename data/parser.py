import json
import sys

civs = ['Greek', 'Egyptian', 'Norse', 'Atlantean']
resources = {'F': 'food', 'G': 'gold', 'W': 'wood', 'Fv': 'favor'}
units = []

for civ in civs: 
  f = open('CSV/' + civ + '-Table 1.csv', 'r')

  print "Parsing", civ

  # Top Header
  for i in range(3):
    f.readline()

  columns = f.readline().strip().split(',')
  columns[0] = 'Name'

  for line in f:
    values = line.strip().split(',')
    if values[0] == '':
      continue
    unit = {'civ': civ}
    for val in resources.values():
      unit[val] = 0
  
    for column, value in zip(columns, values):
      value = value.strip()
      column = column.strip()
      if value in ('', '--'):
        value = None
      if column == 'Cost' and value:
        costs = value.split()
        for cost in costs:
          for k, v in resources.items():
            if cost.endswith(k):
              unit[v] = int(cost.strip(k))
      else:
        unit[column] = value
    
    units.append(unit)

output = json.dumps(units)


outfile = open('data.json', 'w')
outfile.write(output)