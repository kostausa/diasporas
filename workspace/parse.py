#!/usr/bin/python

import json
import csv
import collections

stats = {}
codes = {}

def getnum(row, index):
  try:
    num = int(row[index])
    return num
  except ValueError:
    return 0

def process(row):
  country = row[1]
  src = row[2]
  dst = row[7]

  if not src in codes:
    codes[src] = country

  startyear = 1960
  endyear = 2000
  inc = 10

  for y in range(startyear, endyear + inc, inc):
    yindex = (y - startyear)/inc + 8
    num = getnum(row, yindex)
    year = str(y)

    if not year in stats:
      stats[year] = []

    stats[year].append({
      "src" : src,
      "dst" : dst,
      "migrant": num      
    })

def main(argv=None):
  with open('migration.csv', 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(datareader)
    for row in datareader:
      process(row)

  data = {
    "name"   : "Global Bilateral Migration 1960-2000",
    "source" : "World DataBank",
    "codes" : collections.OrderedDict(sorted(codes.items())),
    "stats" : stats
  }

  print json.dumps(data, sort_keys=False, indent=2, separators=(',', ': '))

if __name__ == "__main__":
  main()

