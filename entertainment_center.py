import media
import movie_trailer

dwaraka=media.Movie("Dwaraka","Making a thief change into a god man",
                    "http://www.telugumirchi.com/en/wp-content/uploads/2016/08/dwaraka-movie-poster.jpg",
                    "https://www.youtube.com/watch?v=DDWPxs8zTzg",
                    "srinivasa ravindra",
                    2017)
#print(toy_story.storyline)

katamraudu=media.Movie("Katamrayudu",
                       "It is Beautuful love song",
                       "http://thehansindia.com/assets/7574_2535_pspk_katamarayudu_new_poster.jpg",
                       "https://www.youtube.com/watch?v=zggQw2wb60M",
                       "kishore kumar pardasani",
                       2017)

sailajareddy_alludu=media.Movie("sailajareddyalludu",
                                "stale story of egos",
                                "http://www.atlantawishesh.com/media/k2/galleries/67589/Sailaja-Reddy-Alludu-08.jpg",
                                "https://www.youtube.com/watch?v=4djA8T6K4iQ",
                                "maruti",
                                2018)

marakata_mani=media.Movie("Marakatamani",
                          "A film about ancient diamond",
                          "https://4.bp.blogspot.com/-SCcfrZULKfQ/WUPqfJeXl_I/AAAAAAAEvUw/5J-NZdPKJfI7SYRHFNqzmgQ0Uo1E_t6mACLcBGAs/s1600/marakathamani%2B....jpg",
                          "https://www.youtube.com/watch?v=_e3IMX7JIIc",
                          "A.R.K.Sarvanan",
                          2017)

rx_100=media.Movie("Rx100",
                   "RX 100 is a story of love, lust and passion marred by excessive and unnecessary gore",
                   "https://www.filmibeat.com/ph-big/2018/07/lip-lock-scenes-from-rx-100_153128190270.jpg",
                   "https://www.youtube.com/watch?v=pffgnV5meN4",
                   "Ajay Bhupathi",
                   2018)

sivam=media.Movie("Sivam",
                  "Dragged out love story by Ram Pothineni",
                  "https://www.filmibeat.com/ph-big/2015/10/shivam_144384768660.jpg",
                  "https://www.youtube.com/watch?v=QydZny84h3E",
                  "Ravi Kishore",
                  2015)

angel=media.Movie("Angel",
                  "The story revolves around two guys who make use of different ways to earn money and enjoy life,but their life changes when they accidentally get a statue, which is an angel from heaven.",
                  "http://www.idlebrain.com/images5/poster-angel6.jpg",
                  "https://www.youtube.com/watch?v=pHlnKdHiZ2Y",
                  "Palani",
                  2017)
chalo=media.Movie("Chalo",
                  "Chalo” is Naga Shaurya latest love story and Kannada heroine Rashmika debut film in Telugu",
                  "https://www.apherald.com/ImageStore/images/movies/movies-wallpapers/Hero-Naga-Shourya-Chalo-Telugu-Movie-Latest-Stills14.jpg",
                  "https://www.youtube.com/watch?v=6_BxEjvWsqs",
                  "Venky Kudumula",
                  2018)


#print(katamraudu.storyline)

#katamraudu.show_trailer()

movies=[dwaraka,katamraudu,sailajareddy_alludu,marakata_mani,rx_100,sivam,angel,chalo]
movie_trailer.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
