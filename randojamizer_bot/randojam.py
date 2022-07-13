from random import choice, randint

TIME_SIGNATURES = ('4/4',
                   '5/4',
                   '3/4',
                   '6/8',
                   '7/8',
                   '9/8',
                   '11/8')

GENRES = ('Rock', 'Blues', 'Jazz', 'Fusion', 'Trip-hop',
          'Hip-Hop', 'R&B', 'Metal', 'Progressive', 'Soul', 'Reggae', 'Country', 'Folk', 'Disco', 'Electronic', 'Latino', 'African', 'Oriental', 'Indie', 'Shoegaze', 'Punk')

TEMPO = (70, 170)

MAJORS = ('C', 'G', 'D', 'A', 'E', 'B', 'F#/Gb',
          'F', 'Bb', 'Eb', 'Ab', 'Db')

MINORS = ('Am', 'Em', 'Bm',
          'F#m', 'C#m', 'G#m', 'D#m/Ebm', 'Dm', 'Gm', 'Cm', 'Fm', 'Bbm')

TONALITIES = tuple(MAJORS + MINORS)


PROGRESSIONS = ('I V vi IV',
                'iv V IV V',
                'I IV iv V',
                'I ii7 I6 IV',
                'I iv ii V')


class Randojam:
    """Class for keeping track of an item in inventory."""
    genre: str
    progression: str
    tempo: int
    time: str
    tonality: str

    def __init__(self):
        self.genre = choice(GENRES)
        self.progression = choice(PROGRESSIONS)
        self.tempo = randint(70, 170)
        self.time = choice(TIME_SIGNATURES)
        self.tonality = choice(MAJORS)
