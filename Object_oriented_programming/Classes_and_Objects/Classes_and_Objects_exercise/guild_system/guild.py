from Object_oriented_programming.Classes_and_Objects.Classes_and_Objects_exercise.guild_system.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player not in self.players and player.guild == 'Unaffiliated':
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is in another guild."

    @staticmethod
    def find_player_by_name(name, players):
        for player in players:
            if player.name == name:
                return player
        return None

    def kick_player(self, player_name):
        player = self.find_player_by_name(player_name, self.players)
        if player is None:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player)
        player.guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'

        for player in self.players:
            result += player.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())