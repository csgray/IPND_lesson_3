# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

#toy_story = media.Movie("Toy Story",
#   "A story of a boy and his toys that come to life.",
#   "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#   "https://www.youtube.com/watch?v=vwyZH85NQC4")

#avatar = media.Movie("Avatar",
#   "A Marine on an alien planet.",
#   "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
#   "http://www.youtube.com/watch?v=9ceBgWV8io")

nausicaa = media.Movie("Nausicaa of the Valley of the Wind",
    "Warrior/pacifist Princess Nausicaa desperately struggles to prevent two warring nations from destroying themselves and their dying planet.",
    "http://ia.media-imdb.com/images/M/MV5BMTM1NjIxNTY4OF5BMl5BanBnXkFtZTcwNDE5MDIyNw@@._V1__SX857_SY1027_.jpg",
    "https://youtu.be/6zhLBe319KE")

mononoke = media.Movie("Princess Mononoke",
    "On a journey to find the cure for a Tatarigami's curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.",
    "http://ia.media-imdb.com/images/M/MV5BMjgzNTUwODQzN15BMl5BanBnXkFtZTcwMTc4ODE3OQ@@._V1__SX857_SY1027_.jpg",
    "https://youtu.be/4OiMOHRDs14")

howl = media.Movie("Howl's Moving Castle",
    "When an unconfident young woman is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking castle.",
    "http://ia.media-imdb.com/images/M/MV5BMTY1OTg0MjE3MV5BMl5BanBnXkFtZTcwNTUxMTkyMQ@@._V1__SX857_SY1027_.jpg",
    "https://youtu.be/iwROgK94zcM")

cagliostro = media.Movie("The Castle of Cagliostro",
    "A flamboyant thief and his gang struggle to free a princess from an evil count's clutches and to learn the hidden secret to a fabulous treasure that she holds part of a key to.",
    "http://ia.media-imdb.com/images/M/MV5BMjAwMDc1NDY3MV5BMl5BanBnXkFtZTgwNjUyNjM0MzE@._V1__SX857_SY1027_.jpg",
    "https://youtu.be/wJudurbkv1E")

castle = media.Movie("Castle in the Sky",
    "A young boy and a girl with a magic crystal must race against pirates and foreign agents in a search for a legendary floating castle.",
    "http://ia.media-imdb.com/images/M/MV5BMTU4MTUyMTc3MV5BMl5BanBnXkFtZTYwOTg4Mzk5._V1__SX857_SY1027_.jpg",
    "https://youtu.be/8ykEy-yPBFc")

porco = media.Movie("Porco Rosso",
    "The adventures of 'Porco Rosso', a veteran WW1 pilot in 1930s Italy, who has been cursed to look like an anthropomorphic pig.",
    "http://ia.media-imdb.com/images/M/MV5BOTQ5MzI1ODgyNF5BMl5BanBnXkFtZTgwOTUyMDk2MjE@._V1__SX857_SY1027_.jpg",
    "https://youtu.be/awEC-aLDzjs")

#print(toy_story.storyline)
#print(avatar.storyline)
#toy_story.show_trailer()
#nausicaa.show_trailer()

movies = [mononoke, howl, castle, nausicaa, cagliostro, porco]
fresh_tomatoes.open_movies_page(movies)
