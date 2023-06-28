class Stats():
    """отслкживание статистики"""

    def __init__(self):
        """statistics init"""
        self.reset_stats()

    def reset_stats(self):
        """time changing statistic"""
        self.guns_left = 2
