import teaser
import fresh_tomatoes
andamina_jeevitam=teaser.lovedfilms("Andamina Jeevitam","Rich personchanges into"
                                    "poor person ","https://1847884116.rsc."
                                    "cdn77.org/telugu/gallery/movies/"
                                    "andamainajeevitham_2017/thumb.jpg",
                                    "https://youtu.be/miLJxKmGGjc")
#print(andamina_jeevitam.storyline)
darling=teaser.lovedfilms("Darling","About love story","http://4.bp.blogspot.com/"
                          "_8Yhj0stXsEU/S5zd5F0FUjI/AAAAAAAABsY/f_XtTDDFE34/s400"
                          "/Darling+01.jpg","https://youtu.be/YYI4n5Y28QU")
#print(darling.storyline)
rite_rite=teaser.lovedfilms("Rite Rite","about bus driver love story","https:"
                            "//m.media-amazon.com/images/M/MV5BZWZlMTI3YzQtYWI"
                            "4Mi00ZjRmLWJjM2ItYWFhNWJkNDg4MWYyXkEyXkFqcGdeQXVy"
                            "NTU1NTgzNTk@._V1_UY268_CR110,0,182,268_AL_.jpg",
                            "https://youtu.be/yexvRLh_Hbw")
juliet_lover_of_idiot=teaser.lovedfilms("Juliet Lover Of Idiot ","about girl "
                                        "lover story",
                                        "https://d2h7z5r5pp4sed.cloudfront.net"
                                        "/telugu/news/juliet041217_m.jpg",
                                        "https://youtu.be/P6QbJrTD47c")
hello_guru_prema_kosame=teaser.lovedfilms("Hello Guru Prema Kosame","love "
                                          "story betwwen  boy and girl",
                                          "http://www.cinejosh.com/reviewsimg/"
                                          "big/hello-guru-prema-kosame-revie"
                                          "w_b_1810180325.jpg","https://youtu"
                                          ".be/PoA36wDTlRA")
mass=teaser.lovedfilms("Mass","love story","https://photogallery.indiatimes.com/photo/47812571.cms","https://youtu.be/hq16gHVAAPQ")

movies=[andamina_jeevitam,darling,rite_rite,juliet_lover_of_idiot,hello_guru_prema_kosame,mass]
fresh_tomatoes.open_movies_page(movies)
