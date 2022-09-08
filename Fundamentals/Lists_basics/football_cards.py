info = input().split(" ")
team_a_players = 11
team_b_players = 11
players_gone = []
is_terminated = False

for i in info:
    if i not in players_gone:
        players_gone.append(i)
        if "A" in i:
            team_a_players -= 1
        elif "B" in i:
            team_b_players -= 1
        if team_a_players < 7 or team_b_players < 7:
            is_terminated = True
            break
print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if is_terminated:
    print(f"Game was terminated")
