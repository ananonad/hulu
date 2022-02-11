from django.shortcuts import render
from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView



class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Movie:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


movies = [
    Movie("Dune", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQPqS6UaUbAFXbexufzQLa9PrCxjjw5MFTsEjsDC0ppVOhBcrmw", "Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence, only those who can conquer their own fear will survive."),
    Movie("Don't Look Up", "https://m.media-amazon.com/images/M/MV5BNjZjNDE1NTYtYTgwZS00M2VmLWEyODktM2FlNjhiYTk3OGU2XkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg", "It tells the story of two astronomers attempting to warn humanity about an approaching comet that will destroy human civilization. The impact event is an allegory for climate change, and the film is a satire of government, political, and media indifference to the climate crisis."),
    Movie("Spider-Man: No Way Home", "https://m.media-amazon.com/images/M/MV5BZWMyYzFjYTYtNTRjYi00OGExLWE2YzgtOGRmYjAxZTU3NzBiXkEyXkFqcGdeQXVyMzQ0MzA0NTM@._V1_FMjpg_UX1000_.jpg", "With Spider-Man's identity now revealed, our friendly neighborhood web-slinger is unmasked and no longer able to separate his normal life as Peter Parker from the high stakes of being a superhero. When Peter asks for help from Doctor Strange, the stakes become even more dangerous, forcing him to discover what it truly means to be Spider-Man."),
    Movie("Wonder Woman 1984", "https://www.dolby.com/siteassets/xf-site/content-detail-pages/ww84_updated.jpg", "Diana Prince lives quietly among mortals in the vibrant, sleek 1980s -- an era of excess driven by the pursuit of having it all. Though she's come into her full powers, she maintains a low profile by curating ancient artifacts, and only performing heroic acts incognito. But soon, Diana will have to muster all of her strength, wisdom and courage as she finds herself squaring off against Maxwell Lord and the Cheetah, a villainess who possesses superhuman strength and agility."),
    Movie("Shang-Chi and the Legend of The Ten Rings", "https://m.media-amazon.com/images/M/MV5BNTliYjlkNDQtMjFlNS00NjgzLWFmMWEtYmM2Mzc2Zjg3ZjEyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_FMjpg_UX1000_.jpg", "Martial-arts master Shang-Chi confronts the past he thought he left behind when he's drawn into the web of the mysterious Ten Rings organization."),
    Movie("Black Widow", "https://bloximages.newyork1.vip.townnews.com/thebatt.com/content/tncms/assets/v3/editorial/e/b4/eb49c6ee-e362-11eb-acfa-8f29fb976f93/60ecc6494c0b9.image.jpg?crop=607%2C941%2C18%2C11&resize=400%2C620&order=crop%2Cresize", "Natasha Romanoff, aka Black Widow, confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises. Pursued by a force that will stop at nothing to bring her down, Natasha must deal with her history as a spy, and the broken relationships left in her wake long before she became an Avenger."),
    Movie("Call Me By Your Name", "https://m.media-amazon.com/images/M/MV5BNDk3NTEwNjc0MV5BMl5BanBnXkFtZTgwNzYxNTMwMzI@._V1_FMjpg_UX1000_.jpg","It's the summer of 1983, and precocious 17-year-old Elio Perlman is spending the days with his family at their 17th-century villa in Lombardy, Italy. He soon meets Oliver, a handsome doctoral student who's working as an intern for Elio's father. Amid the sun-drenched splendor of their surroundings, Elio and Oliver discover the heady beauty of awakening desire over the course of a summer that will alter their lives forever."),
    Movie("Interstellar", "https://m.media-amazon.com/images/I/A1JVqNMI7UL._SL1500_.jpg", "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home."),

]
class MovieList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = movies 
        return context