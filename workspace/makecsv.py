#!/usr/bin/python

import json

def process(k, stats, codes):
  stat = stats[k]
  for entry in stat:
    src = entry['src']
    dst = entry['dst']
    srccountry = codes[src]
    dstcountry = codes[dst]
    print "%s,%s,\"%s\",%s,\"%s\",%d" % (k, src, srccountry, dst, dstcountry, entry['migrant']) 

f = open('bilateral-migration.json', 'r')
content = f.read()
f.close()

js = json.loads(content)

process('1960', js['stats'], js['codes'])
process('1970', js['stats'], js['codes'])
process('1980', js['stats'], js['codes'])
process('1990', js['stats'], js['codes'])
process('2000', js['stats'], js['codes'])
process('2010', js['stats'], js['codes'])

  
