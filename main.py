import sys
total = 0
prices = {
    'apples':100,
    'bananas':150,
    'cherries':75
}
while True:
    s = raw_input('--> ')
    if s in prices:
        total +=prices[s]
    print '%s : %s' % (s, total)

"""
--> apples
apples : 100
--> apples
apples : 200
--> cherries
cherries : 275
--> bananas
bananas : 425
--> apples
apples : 525
-->
"""
