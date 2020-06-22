from faker import Faker


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


library = []


def get_movies(library):
    movies = []
    for element in library:
        if isinstance(element, Movie) and not(isinstance(element, Series)):
            movies.append(element)
    return movies


def get_series(library):
    series = []
    for element in library:
        if isinstance(element, Series):
            series.append(element)
    return series


def search(title, library):
    for element in library:
        if title == element.title:
            return element
    else:
        print("Nie znaleziono tytułu w bazie")


def run_func(func):
    for i in range(10):
        func


def generate_views(library):
    fake = Faker()
    random_element = fake.random_int(0, len(library)-1)
    library[random_element].views += fake.random_int(1, 100)
    return library


def top_titles(library, how_many, content_type=None):
    counter = 0
    if content_type == 'movies':
        lib = sorted(get_movies(library), key=lambda element: element.views)
        return lib[:how_many]
    elif content_type == 'series':
        lib = sorted(get_series(library), key=lambda element: element.views)
        return lib[:how_many]
    else:
        lib = sorted(library, key=lambda element: element.views)
        return lib[-how_many:]


my_library = []

print("Biblioteka filmów")
fake = Faker()
genres = ['comedy', 'drama', 'action', 'adventure', 'crime',
          'fantasy', 'historical', 'horror', 'romance', 'sci-fi']

for i in range(50):
    title = " ".join(fake.words(fake.random_int(1, 4)))
    position = Movie(title, fake.year(), fake.word(ext_word_list=genres), 0)
    my_library.append(position)

for i in range(50):
    title = " ".join(fake.words(fake.random_int(1, 2)))
    position = Series(title, fake.year(), fake.word(ext_word_list=genres), 0,
                     fake.random_int(1, 8), fake.random_int(1, 20))
    my_library.append(position)

for element in my_library:
    print(element)

for i in range(10):
    library=generate_views(my_library)

top=top_titles(my_library,3)
for element in top:
    print(element)
