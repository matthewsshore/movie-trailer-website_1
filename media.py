import webbrowser

# Create a video class that takes in the common parameters
# title, cast, plot, poster, trailer, release_year


class Video():
    """This class will create a general Video instance"""
    def __init__(self, title, cast, plot, poster, trailer, release_year):
        self.title = title
        self.cast = cast
        self.plot = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.release_year = release_year

    # use webbrowser.open to show a trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# create a movie class that is a child of Video that includes
# the extra parameter of duration. The reason I created movie and video was if
# in the future you wanted to have TV Shows you
# could add this and include TvShow specifics like seasons


class Movie(Video):
    """This class provides a way to store movie related information"""

    def __init__(self, title, cast, plot, poster,
                 trailer, release_year, duration):
        Video.__init__(self, title, cast, plot, poster, trailer, release_year)
        self.duration = duration
