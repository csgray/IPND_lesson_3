# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

# class: a blueprint for objects that can include data and methods
# instance: multiple objects based on a class
# constructor: the __init__ inside the class to create the object
# self: Python common practice for referring back to the object
# instance methods: functions within a class that refers to itself

import webbrowser

class Movie():
    """This class provides a way to store movie related information."""
    def __init__(self, movie_title, rating, duration, release_date, movie_storyline, poster_image, trailer_youtube):
        # Initializes instance of class Movie
        self.title = movie_title
        self.rating = rating
        self.duration = duration
        self.release_date = release_date
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Opens a browser window with the movie trailer from YouTube
        webbrowser.open(self.trailer_youtube_url)

