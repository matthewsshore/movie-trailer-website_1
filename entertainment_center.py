# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

# Begin creating a list of movies to display.
# The parameters taken are title, cast, plot,
# poster, trailer, release_year, and duration.

toy_story = media.Movie("Toy Story",
                        "Tom Hanks",
                        "Story of toys that come to life!",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1995",
                        "81 minutes")


avatar = media.Movie("Avatar",
                     "Sam Worthington",
                     "Story of an imaginary world!",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "2009",
                     "161 minutes")


happy_gilmore = media.Movie("Happy Gilmore",
                            "Adam Sandler",
                            "A hockey player turned pro golfer!",
                            "http://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg",
                            "https://www.youtube.com/watch?v=y1emDAYCfVQ",
                            "1996",
                            "92 minuntes")

school_of_rock = media.Movie("School of Rock",
                             "Jack Black",
                             "Teacher passionate about music!",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "2003",
                             "109 minutes")

ratatouille = media.Movie("Ratatouille",
                          "Patton Oswalt",
                          "A rat who cooks!",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "2007",
                          "111 minutes")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Owen Wilson",
                                "Screenwrite who can travel time.",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "2011",
                                "94 minutes")

# array to pass to fresh_tomatoes.

video_list = [toy_story, avatar, happy_gilmore,
              school_of_rock, ratatouille, midnight_in_paris]

# call the fresh_tomatoes movie page

fresh_tomatoes.open_movies_page(video_list)
