import webbrowser #5) for trailer to work

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #when we describe a constant like this, google python guide suggests using capital letters

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """This function creates space and memory for its arguments
        Args:
            self: It is the object being created, almost like a keyword(but it is not)
            movie_title: It is to receive movie title of each movie
            poster_image: It is to show poster image
            trailer_youtube: It is to receive youtube trailer of the movie
        Behavior:
            Initializes space and memory creation.
        """
    #0)Creates space and memory for title, storyline etc.
    #1)self is the object being created, we can name it differently as well
    #2)self in this case points to the_revenant
    #3)words after self shows what we will receive after we run this function
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This is the function to show trailers,
        Args:
            self: We access to trailer_youtube_url with "self"
        Behavior:
            Opens the webbrowser with the correct url,
            the link is stored at above function def__init__ (trailer_youtube_url)
          """
    #4)each instance method takes its first argument as self,
    #4 cont'd) see above, same as init instance
        webbrowser.open(self.trailer_youtube_url)
