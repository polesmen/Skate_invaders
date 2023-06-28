class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """statistics init"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """time changing statistic"""
        self.guns_left = 2
        self.score = 0
