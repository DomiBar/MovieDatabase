from datetime import date
from faker import Faker


my_library = []


class Movie:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self):
        self.views += 1


class Series(Movie):
    def __init__(self, title, year, genre, views, episode, season):
        super().__init__(title, year, genre, views)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"

    def show_episodes(self, library=my_library):
        counter = 0
        for element in library:
            if self.title == element.title:
                counter += 1
        print(f"W bibliotece znajduje się {counter} odcinków serialu '{self.title}'")


def get_movies(library=my_library):
    movies = []
    for element in library:
        if isinstance(element, Movie) and not(isinstance(element, Series)):
            movies.append(element)
    return movies


def get_series(library=my_library):
    series = []
    for element in library:
        if isinstance(element, Series):
            series.append(element)
    return series


def search(title, library=my_library):
    for element in library:
        if title == element.title:
            return element
    else:
        print("Nie znaleziono tytułu w bazie")


def run_func(func):
    for i in range(10):
        func()


def generate_views(library=my_library):
    fake = Faker()
    random_element = fake.random_int(0, len(library)-1)
    library[random_element].views += fake.random_int(1, 100)
    return library


def top_titles(how_many, library=my_library, content_type=None):
    counter = 0
    if content_type == 'movies':
        lib = sorted(get_movies(library), key=lambda element: element.views)
        return lib[-how_many:]
    elif content_type == 'series':
        lib = sorted(get_series(library), key=lambda element: element.views)
        return lib[-how_many:]
    else:
        lib = sorted(library, key=lambda element: element.views)
        return lib[-how_many:]


def add_series(title, year, genre, season_number, episodes_number, library=my_library):
    for i in range(1, episodes_number-1):
        position = Series(title, year, genre, 0, i, season_number)
        library.append(position)
    return library


fake = Faker()
# list of movie genres for faker
genres = ['comedy', 'drama', 'action', 'adventure', 'crime',
          'fantasy', 'historical', 'horror', 'romance', 'sci-fi']

# fill my_library with random movies
for i in range(20):
    title = " ".join(fake.words(fake.random_int(1, 4)))
    position = Movie(title, fake.year(), fake.word(genres), 0)
    my_library.append(position)

# fill my_library with random series
for i in range(5):
    title = " ".join(fake.words(fake.random_int(1, 3)))
    my_libray = add_series(title, fake.year(), fake.word(genres), fake.random_int(1, 8),
                           fake.random_int(1, 24)
                           )


print("Biblioteka filmów".center(51, '*'))
run_func(generate_views)
today = date.today().strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {today}")
top = top_titles(3)
for element in top:
    print(f"{element} - {element.views} views")