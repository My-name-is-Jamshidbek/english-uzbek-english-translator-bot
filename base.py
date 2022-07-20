def baseadd(id):
    with open('baza.txt','a') as f:
      f.write(id+'\n')
      f.close()

def basereturn(takrorlanish=False):
    if takrorlanish:
        r = []
        with open('baza.txt','r') as f:
            for line in f:
                r.append(line[:-2])
            f.close()
    else:
        r = set()
        with open('baza.txt','r') as f:
            for line in f:
                r.add(line[:-2])
            f.close()
        r = list(r)
    return r
def basereturntext():
    base = basereturn()
    text = ''
    for i in base:text+=i+'\n'
    with open('newbaza.txt','w') as f:
        f.write(text)
    return True