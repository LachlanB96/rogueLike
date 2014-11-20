modulePositions = {'map':1,'actions':5,'inventory':3,'skills':4, 'quests':2}
modulePositions[list(modulePositions.keys())[list(modulePositions.values()).index(2)]] = modulePositions['actions']
modulePositions['actions'] = 2
print (modulePositions)