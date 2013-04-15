PRICES = {
    'apples':100,
    'bananas':150,
    'cherries':75
}
total = 0
def running_total(s):
    global total
    if s in PRICES:
        total += PRICES[s]
    return '%s : %s' % (s, total)

def resettotal():
    global total
    total = 0