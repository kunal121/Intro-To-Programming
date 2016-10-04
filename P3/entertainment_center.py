#import used to import fresh_tomatoes file and importing media file which are included for this project
#fresh_tomatoes file cointains html and other content to execute website
#media create different variables as movie title 
import fresh_tomatoes
import media
toy_story=media.Movie("Toy Story","8.3/10","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#adding title,rating,poster,trailer of movie toy_story in variable toy_story

fault_in_our_star=media.Movie("Fault in our stars","7.83/10","https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png",
                              "https://www.youtube.com/watch?v=9ItBvH5J6ss")
#adding title,rating,poster,trailer of movie fault in our star in variable fault_in_our_star
Now_you_see_me_2=media.Movie("Now you see me 2",
                             "6.6/10","https://upload.wikimedia.org/wikipedia/en/9/9a/Now_You_See_Me_2_poster.jpg",
                             "https://www.youtube.com/watch?v=AuEjHzOIgBE")
#adding title,rating,poster,trailer of movie now you see me 2 in variable Now_you_see_me_2
The_Martian=media.Movie("The Martian","8.0/10"
                        ,"https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg","https://www.youtube.com/watch?v=ej3ioOneTy8")
#adding title,rating,poster,trailer of movie the martian in variable The_Martian
Interstellar=media.Movie("Interstellar","8.6/10"
                         ,"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg","https://www.youtube.com/watch?v=zSWdZVtXT7E")
#adding title,rating,poster,trailer of movie Interstellar in variable Interstellar
Kingsman=media.Movie("Kingsman","7.8/10",
                     "https://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg","https://www.youtube.com/watch?v=kl8F-8tR8to")
#adding title,rating,poster,trailer of movie Kingsman in variable Kingsman


movie=[toy_story,fault_in_our_star,Now_you_see_me_2,The_Martian,Interstellar,Kingsman]
#making list of movies in movie variable to further call it in another file
fresh_tomatoes.open_movies_page(movie)
