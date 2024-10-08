for left in range(10):
    for right in range(left, 10):
        print("[" + str(left)  + str(right) + "]", end=" ")
    print()

print("\n*** End of the program ***\n")

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

print("\n*** End of the program ***\n")
