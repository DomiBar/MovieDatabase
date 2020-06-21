class Movie:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views

    def __str__(self):
        return f"{self.title} ({year})"

    def play(self):
        self.views += 1


class Series(Movie):
    def __init__(self, title, year, genre, views, episode, season):
        super().__init__(title, year, genre, views)
        self.episode = episode
        self.season = season

    def __str__(self):
        #return "%s S%02dE%02d" % (self.title, self.season, self.episode)
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"
