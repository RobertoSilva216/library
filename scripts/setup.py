print("Open the file and set on the script")
raise SystemExit


import os
import django
import sys
from django.db import transaction

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from api.models import Authors, Books

data = [
    ("J.K. Rowling", [("Harry Potter and the Sorcerer's Stone", "A young boy discovers he is a wizard and attends a magical school, facing challenges and friends.", 1997)]),
    ("George Orwell", [("1984", "A dystopian novel about a totalitarian regime that uses surveillance and propaganda.", 1949)]),
    ("Jane Austen", [("Pride and Prejudice", "A classic novel exploring themes of love and social standing in 19th-century England.", 1813)]),
    ("Mark Twain", [("The Adventures of Huckleberry Finn", "A coming-of-age story about a boy traveling down the Mississippi River with an escaped slave.", 1884)]),
    ("F. Scott Fitzgerald", [("The Great Gatsby", "A tale of wealth and love set in the Roaring Twenties, focusing on Jay Gatsby's obsession.", 1925)]),
    ("Harper Lee", [("To Kill a Mockingbird", "A novel about racial injustice and moral growth in the Deep South, seen through a child's eyes.", 1960)]),
    ("J.R.R. Tolkien", [("The Hobbit", "A fantasy adventure of a hobbit named Bilbo Baggins who joins a quest to reclaim a dragon's treasure.", 1937)]),
    ("Gabriel García Márquez", [("One Hundred Years of Solitude", "A multi-generational tale of the Buendía family in the fictional town of Macondo.", 1967)]),
    ("Ernest Hemingway", [("The Old Man and the Sea", "A story of an aging fisherman who battles a giant marlin in the Gulf Stream.", 1952)]),
    ("Leo Tolstoy", [("War and Peace", "A historical novel about the impact of the Napoleonic wars on Russian society.", 1869)]),
    ("Charles Dickens", [("A Tale of Two Cities", "A story set during the French Revolution, contrasting London and Paris.", 1859)]),
    ("Agatha Christie", [("Murder on the Orient Express", "A mystery novel featuring detective Hercule Poirot solving a murder aboard a train.", 1934)]),
    ("Virginia Woolf", [("Mrs. Dalloway", "A modernist novel exploring the thoughts of a woman on a single day in post-World War I England.", 1925)]),
    ("C.S. Lewis", [("The Lion, the Witch and the Wardrobe", "A fantasy novel about children who enter a magical world and help a lion defeat an evil witch.", 1950)]),
    ("Franz Kafka", [("The Metamorphosis", "A surreal story about a man who wakes up to find himself transformed into a giant insect.", 1915)]),
    ("John Steinbeck", [("The Grapes of Wrath", "A novel depicting the struggles of a family during the Great Depression in America.", 1939)]),
    ("Ray Bradbury", [("Fahrenheit 451", "A dystopian tale of a future society where books are banned and 'firemen' burn them.", 1953)]),
    ("Kurt Vonnegut", [("Slaughterhouse-Five", "A satirical novel about the bombing of Dresden and time travel, blending fact and fiction.", 1969)]),
    ("Margaret Atwood", [("The Handmaid's Tale", "A dystopian novel set in a theocratic society where women have lost their rights.", 1985)]),
    ("Philip K. Dick", [("Do Androids Dream of Electric Sheep?", "A science fiction story exploring the nature of humanity and artificial intelligence.", 1968)]),
    ("Douglas Adams", [("The Hitchhiker's Guide to the Galaxy", "A comedic science fiction novel following an unwitting human's adventures in space.", 1979)]),
    ("Toni Morrison", [("Beloved", "A novel about a former enslaved woman haunted by her past and the ghost of her deceased daughter.", 1987)]),
    ("Oscar Wilde", [("The Picture of Dorian Gray", "A philosophical novel about a young man who remains eternally youthful while his portrait ages.", 1890)]),
    ("Neil Gaiman", [("American Gods", "A fantasy novel that explores the clash between old gods and new gods in modern America.", 2001)]),
    ("Stephen King", [("The Shining", "A horror novel about a family staying in an isolated hotel with a sinister past.", 1977)]),
    ("Isabel Allende", [("The House of the Spirits", "A multi-generational saga about a family in Chile and the magical events surrounding them.", 1982)]),
    ("Salman Rushdie", [("Midnight's Children", "A novel about children born at the moment of India's independence, interweaving history and magic.", 1981)]),
    ("John Grisham", [("The Firm", "A legal thriller about a young attorney who discovers his law firm's dark secrets.", 1991)]),
    ("Dan Brown", [("The Da Vinci Code", "A mystery thriller that involves a conspiracy within the Catholic Church and secret societies.", 2003)]),
    ("Robert Louis Stevenson", [("Treasure Island", "A classic adventure novel about pirates and buried treasure.", 1883)]),
    ("H.G. Wells", [("The War of the Worlds", "A science fiction novel about an alien invasion in England.", 1898)]),
    ("Maya Angelou", [("I Know Why the Caged Bird Sings", "An autobiographical work detailing the author's childhood and early adult experiences.", 1969)]),
    ("Alice Walker", [("The Color Purple", "A novel about African American women's struggles in the early 20th century American South.", 1982)]),
    ("Chuck Palahniuk", [("Fight Club", "A novel that explores themes of identity and consumerism through an underground fight club.", 1996)]),
    ("David Mitchell", [("Cloud Atlas", "A genre-bending novel comprising interconnected stories spanning centuries.", 2004)]),
    ("Hilary Mantel", [("Wolf Hall", "A historical novel centered around Thomas Cromwell's rise to power in the Tudor court.", 2009)]),
    ("Richard Adams", [("Watership Down", "A novel about a group of rabbits seeking a new home and their struggles against predators.", 1972)]),
    ("Michael Ende", [("The NeverEnding Story", "A fantasy novel about a boy who enters a magical book and discovers another world.", 1979)]),
    ("Anne Rice", [("Interview with the Vampire", "A gothic novel about a vampire recounting his life story and existential crisis.", 1976)]),
    ("Colson Whitehead", [("The Underground Railroad", "A historical fiction novel about an enslaved woman's journey to freedom through a secret railroad.", 2016)]),
    ("Elie Wiesel", [("Night", "A memoir recounting Wiesel's experiences in Nazi concentration camps during World War II.", 1956)]),
    ("Zadie Smith", [("White Teeth", "A novel exploring the lives of two families in London across multiple generations.", 2000)]),
    ("Jhumpa Lahiri", [("The Namesake", "A novel about the life of an Indian-American man navigating his cultural identity.", 2003)]),
    ("George R.R. Martin", [("A Game of Thrones", "The first book in a fantasy series about noble families vying for power in a fictional kingdom.", 1996)]),
    ("R.L. Stine", [("Goosebumps Series", "A popular children's horror series featuring spooky and thrilling tales.", 1992)]),
    ("Liane Moriarty", [("Big Little Lies", "A contemporary novel about the intertwined lives of women in a suburban community.", 2014)]),
    ("V.E. Schwab", [("Vicious", "A dark fantasy novel about two college students who gain superpowers through near-death experiences.", 2013)]),
    ("Rick Riordan", [("Percy Jackson & The Olympians", "A series of novels following a young demigod's adventures based on Greek mythology.", 2005)]),
    ("Ken Follett", [("Pillars of the Earth", "A historical novel centered around the construction of a cathedral in 12th-century England.", 1989)]),
    ("Ian McEwan", [("Atonement", "A novel exploring themes of love, war, and the effects of a child's misunderstanding.", 2001)]),
]

try:
    with transaction.atomic():
        Authors.objects.all().delete()
        Books.objects.all().delete()

        for author_name, books in data:
            author = Authors.objects.create(name=author_name)
            for title, description, year in books:
                Books.objects.create(title=title, author=author, description=description, year=year)
except Exception as e:
    print(f"An error occurred: {str(e)}")
    raise SystemExit

print("Setup finished with success")
