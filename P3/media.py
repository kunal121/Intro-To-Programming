# import webbrowser which is an inbuild function in python standard library
import webbrowser
class Movie():# class Movie() is used to define instances and call it in another file whenever we want  
    def __init__(self,movie_title,rating,
                 poster_image,trailer_youtube):
  #__init__ is a inbuild method in python to create an object      
  #the self variable represents the instance of the object itself      
        self.title=movie_title
        self.rating=rating
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
  #show_trailer function is declared to open the webbrowser and play the trailer      
         
        webbrowser.open(self.trailer_youtube_url)
    
    
