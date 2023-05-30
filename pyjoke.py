import pyjokes


def whysoserious():

    Joker = pyjokes.get_jokes('en', 'all')

    return Joker


def warumsoernst():

    Witzbold = pyjokes.get_jokes('de', 'all')

    return Witzbold
