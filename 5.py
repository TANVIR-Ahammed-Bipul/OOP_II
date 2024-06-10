class Tournament:
    def __init__(self, players):
        self.players = players
        self.matches = []
        self.bracket = []
        self.next_round_players = []

    def organize_matches(self):
        """Organize matches for the current round."""
        self.matches = []
        self.next_round_players = []
        
        if len(self.players) % 2 != 0:
            # If odd number of players, the last player gets a bye
            self.players.append(None)
        
        for i in range(0, len(self.players), 2):
            match = (self.players[i], self.players[i+1])
            self.matches.append(match)
    
    def record_result(self, match, winner):
        """Record the result of a match."""
        if match not in self.matches:
            raise ValueError("Match not found in the current round.")
        
        if winner not in match:
            raise ValueError("Winner must be one of the players in the match.")
        
        self.bracket.append((match, winner))
        
        if winner:
            self.next_round_players.append(winner)
    
    def display_bracket(self):
        """Display the current state of the bracket."""
        print("Current Bracket:")
        for match, winner in self.bracket:
            player1, player2 = match
            match_str = f"{player1} vs {player2}" if player2 else f"{player1} (bye)"
            print(f"{match_str} -> Winner: {winner}")
    
    def is_tournament_finished(self):
        """Check if the tournament is finished."""
        return len(self.players) == 1

    def get_winner(self):
        """Get the winner of the tournament."""
        if self.is_tournament_finished():
            return self.players[0]
        else:
            raise ValueError("The tournament is not yet finished.")

    def next_round(self):
        """Prepare for the next round."""
        self.players = self.next_round_players
        self.organize_matches()

# Example usage:
players = ["Player1", "Player2", "Player3", "Player4"]
tournament = Tournament(players)

# Round 1
tournament.organize_matches()
tournament.display_bracket()
tournament.record_result(("Player1", "Player2"), "Player1")
tournament.record_result(("Player3", "Player4"), "Player4")
tournament.next_round()
tournament.display_bracket()

# Round 2
tournament.organize_matches()
tournament.display_bracket()
tournament.record_result(("Player1", "Player4"), "Player1")
tournament.next_round()
tournament.display_bracket()

# Tournament finished
if tournament.is_tournament_finished():
    print(f"The winner is: {tournament.get_winner()}")
