

f = open("teste_steam_games.csv")


for line in f:
  print(line.strip().split(','))