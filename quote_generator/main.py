import random

quotes = [
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("'ve failed over and over and over again in my life. And that is why I succeed.", "Michael Jordan"),
    ("Winners never quit and quitters never win.", "Vince Lombardi"),
    ("Champions aren't made in the gyms. Champions are made from something they have deep inside them—a desire, a dream, a vision.", "Muhammad Ali"),
    ("Champions keep playing until they get it right.", "Billie Jean King"),
    ("A champion is someone who gets up when he can't.", "Jack Dempsey"),
    ("Never let the fear of striking out get in your way.", "Babe Ruth"),
    ("Great moments are born from great opportunity.", "Herb Brooks"),
    ("It ain't over till it's over.", "Yogi Berra"),
    ("Excellence is not a singular act but a habit. You are what you do repeatedly.", "Shaquille O'Neal")
]

def get_random_quote():
    return random.choice(quotes)

random_quote = get_random_quote()
print(f'"{random_quote[0]}" - {random_quote[1]}')