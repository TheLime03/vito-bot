crimefile = open('txtlist.txt', 'r')
yourResult = [line.split(',') for line in crimefile.readlines()]
print(yourResult)
