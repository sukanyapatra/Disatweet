import json
f=open('raw.json')
g=open('extracted1','a')
i=1
for s in f:
    j=json.loads(s)
    j=j['text']
    h=json.dumps(j)
    number=str(i) + ':' + ' '
    g.write(h)
    g.write('\n\n')
    i=i+1
