class GameStats:
    def __init__(self,ai_game):
        self.settings=ai_game.settings
        self.reset_stats()

        self.game_active=False

        self.high_score=self._load_high_score()
    
    def reset_stats(self):
        self.ship_left=self.settings.ship_limit
        self.score=0
        self.level=1


    def _load_high_score(self):
        try:
            with open("hs.txt") as hsf:
                line = hsf.readline().strip()
                return int(line) if line else 0
        except (FileNotFoundError, ValueError):
            return 0