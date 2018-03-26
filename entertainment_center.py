import fresh_tomatoes
import media

the_revenant = media.Movie("The Revenant",
"While exploring the uncharted wilderness in 1823, frontiersman Hugh Glass sustains life-threatening injuries from a brutal bear attack. When a member of his hunting team kills his young son and leaves him for dead, Glass must utilize his survival skills to find a way back to civilization. Grief-stricken and fueled by vengeance, the legendary fur trapper treks through the snowy terrain to track down the man who betrayed him.",
"https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
"https://www.youtube.com/watch?v=NyRD_8HKRMY")
#0)above (the_revenant) using class movie from media file that
#I have created ..This function initializes or creates space for the_revenant
#print (the_revenant.storyline)

interstellar = media.Movie("Interstellar",
"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand, a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
"https://www.youtube.com/watch?v=0vxOhd4qlnA")
#print (interstellar.storyline)
#interstellar.show_trailer()

inception = media.Movie("Inception",
"Dom Cobb is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.",
"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
"https://www.youtube.com/watch?v=YoHD9XEInc0")
#print (inception.storyline)
#inception.show_trailer()

the_green_mile = media.Movie("The Green Mile",
"Paul Edgecomb walked the mile with a variety of cons. He had never encountered someone like John Coffey, a massive black man convicted of brutally killing a pair of young sisters. Coffey had the size and strength to kill anyone, but not the demeanor. Beyond his simple, naive nature and a deathly fear of the dark, Coffey seemed to possess a prodigious, supernatural gift. Paul began to question whether Coffey was truly guilty of murdering the two girls.",
"https://upload.wikimedia.org/wikipedia/en/e/e2/The_Green_Mile_%28movie_poster%29.jpg",
"https://www.youtube.com/watch?v=ctRK-4Vt7dA")
#print (the_green_mile.storyline)
#the_green_mile.show_trailer()

catch_me_if_you_can = media.Movie("Catch Me If You Can",
"Frank Abagnale, Jr. worked as a doctor, a lawyer, and as a co-pilot for a major airline -- all before his 18th birthday. A master of deception, he was also a brilliant forger, whose skill gave him his first real claim to fame: At the age of 17, Frank Abagnale, Jr. became the most successful bank robber in the history of the U.S. FBI Agent Carl Hanratty makes it his prime mission to capture Frank and bring him to justice, but Frank is always one step ahead of him.",
"http://img.moviepostershop.com/catch-me-if-you-can-movie-poster-2002-1020233910.jpg",
"https://www.youtube.com/watch?v=71rDQ7z4eFg")
#print (catch_me_if_you_can.storyline)
#catch_me_if_you_can.show_trailer()

the_big_sick = media.Movie("The Big Sick",
"Kumail is a Pakistani comic who meets an American graduate student named Emily at one of his stand-up shows. As their relationship blossoms, he soon becomes worried about what his traditional Muslim parents will think of her. When Emily suddenly comes down with an illness that leaves her in a coma, Kumail finds himself developing a bond with her deeply concerned mother and father.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BZWM4YzZjOTEtZmU5ZS00ZTRkLWFiNjAtZTEwNzIzMDM5MjdmXkEyXkFqcGdeQXVyNDg2MjUxNjM@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
"https://www.youtube.com/watch?v=PJmpSMRQhhs")
#print (the_big_sick.storyline)
#the_big_sick.show_trailer()

movies = [the_revenant, interstellar, inception, the_green_mile, catch_me_if_you_can, the_big_sick]
fresh_tomatoes.open_movies_page(movies)     #takes in a list or array of movies
#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
