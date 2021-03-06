import trailerinator
import media
import scraper

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                  scraper.Imdb("tt0114709").rating)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                scraper.Imdb("tt0499549").rating)

school_of_rock = media.Movie("School Of Rock", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                "https://www.youtube.com/watch?v=3PsUJFEBC74",
                scraper.Imdb("tt0332379").rating)

ratatouille = media.Movie("Ratatouille", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                scraper.Imdb("tt0382932").rating)

midnight_in_paris = media.Movie("Midnight In Paris", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                scraper.Imdb("tt1605783").rating)

hunger_games = media.Movie("Hunger Games", "Storyline",
                "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                "https://www.youtube.com/watch?v=mfmrPu43DF8",
                scraper.Imdb("tt1392170/?").rating)

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
trailerinator.open_movies_page(movies)
