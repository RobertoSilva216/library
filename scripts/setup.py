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
    ("J.K. Rowling", [("Harry Potter and the Sorcerer's Stone", "A young boy discovers he is a wizard and attends a magical school, facing challenges and friends.")]),
    ("George Orwell", [("1984", "A dystopian novel about a totalitarian regime that uses surveillance and propaganda.")]),
    ("Jane Austen", [("Pride and Prejudice", "A classic novel exploring themes of love and social standing in 19th-century England.")]),
    ("Mark Twain", [("The Adventures of Huckleberry Finn", "A coming-of-age story about a boy traveling down the Mississippi River with an escaped slave.")]),
    ("F. Scott Fitzgerald", [("The Great Gatsby", "A tale of wealth and love set in the Roaring Twenties, focusing on Jay Gatsby's obsession.")]),
    ("Harper Lee", [("To Kill a Mockingbird", "A novel about racial injustice and moral growth in the Deep South, seen through a child's eyes.")]),
    ("J.R.R. Tolkien", [("The Hobbit", "A fantasy adventure of a hobbit named Bilbo Baggins who joins a quest to reclaim a dragon's treasure.")]),
    ("Gabriel García Márquez", [("One Hundred Years of Solitude", "A multi-generational tale of the Buendía family in the fictional town of Macondo.")]),
    ("Ernest Hemingway", [("The Old Man and the Sea", "A story of an aging fisherman who battles a giant marlin in the Gulf Stream.")]),
    ("Leo Tolstoy", [("War and Peace", "A historical novel about the impact of the Napoleonic wars on Russian society.")]),
    ("Charles Dickens", [("A Tale of Two Cities", "A story set during the French Revolution, contrasting London and Paris.")]),
    ("Agatha Christie", [("Murder on the Orient Express", "A mystery novel featuring detective Hercule Poirot solving a murder aboard a train.")]),
    ("Virginia Woolf", [("Mrs. Dalloway", "A modernist novel exploring the thoughts of a woman on a single day in post-World War I England.")]),
    ("C.S. Lewis", [("The Lion, the Witch and the Wardrobe", "A fantasy novel about children who enter a magical world and help a lion defeat an evil witch.")]),
    ("Franz Kafka", [("The Metamorphosis", "A surreal story about a man who wakes up to find himself transformed into a giant insect.")]),
    ("John Steinbeck", [("The Grapes of Wrath", "A novel depicting the struggles of a family during the Great Depression in America.")]),
    ("Ray Bradbury", [("Fahrenheit 451", "A dystopian tale of a future society where books are banned and 'firemen' burn them.")]),
    ("Kurt Vonnegut", [("Slaughterhouse-Five", "A satirical novel about the bombing of Dresden and time travel, blending fact and fiction.")]),
    ("Margaret Atwood", [("The Handmaid's Tale", "A dystopian novel set in a theocratic society where women have lost their rights.")]),
    ("Philip K. Dick", [("Do Androids Dream of Electric Sheep?", "A science fiction story exploring the nature of humanity and artificial intelligence.")]),
    ("Douglas Adams", [("The Hitchhiker's Guide to the Galaxy", "A comedic science fiction novel following an unwitting human's adventures in space.")]),
    ("Toni Morrison", [("Beloved", "A novel about a former enslaved woman haunted by her past and the ghost of her deceased daughter.")]),
    ("Oscar Wilde", [("The Picture of Dorian Gray", "A philosophical novel about a young man who remains eternally youthful while his portrait ages.")]),
    ("Neil Gaiman", [("American Gods", "A fantasy novel that explores the clash between old gods and new gods in modern America.")]),
    ("Stephen King", [("The Shining", "A horror novel about a family staying in an isolated hotel with a sinister past.")]),
    ("Isabel Allende", [("The House of the Spirits", "A multi-generational saga about a family in Chile and the magical events surrounding them.")]),
    ("Salman Rushdie", [("Midnight's Children", "A novel about children born at the moment of India's independence, interweaving history and magic.")]),
    ("John Grisham", [("The Firm", "A legal thriller about a young attorney who discovers his law firm's dark secrets.")]),
    ("Dan Brown", [("The Da Vinci Code", "A mystery thriller that involves a conspiracy within the Catholic Church and secret societies.")]),
    ("Robert Louis Stevenson", [("Treasure Island", "A classic adventure novel about pirates and buried treasure.")]),
    ("H.G. Wells", [("The War of the Worlds", "A science fiction novel about an alien invasion in England.")]),
    ("Maya Angelou", [("I Know Why the Caged Bird Sings", "An autobiographical work detailing the author's childhood and early adult experiences.")]),
    ("Alice Walker", [("The Color Purple", "A novel about African American women's struggles in the early 20th century American South.")]),
    ("Chuck Palahniuk", [("Fight Club", "A novel that explores themes of identity and consumerism through an underground fight club.")]),
    ("David Mitchell", [("Cloud Atlas", "A genre-bending novel comprising interconnected stories spanning centuries.")]),
    ("Hilary Mantel", [("Wolf Hall", "A historical novel centered around Thomas Cromwell's rise to power in the Tudor court.")]),
    ("Richard Adams", [("Watership Down", "A novel about a group of rabbits seeking a new home and their struggles against predators.")]),
    ("Michael Ende", [("The NeverEnding Story", "A fantasy novel about a boy who enters a magical book and discovers another world.")]),
    ("Anne Rice", [("Interview with the Vampire", "A gothic novel about a vampire recounting his life story and existential crisis.")]),
    ("Colson Whitehead", [("The Underground Railroad", "A historical fiction novel about an enslaved woman's journey to freedom through a secret railroad.")]),
    ("Elie Wiesel", [("Night", "A memoir recounting Wiesel's experiences in Nazi concentration camps during World War II.")]),
    ("Zadie Smith", [("White Teeth", "A novel exploring the lives of two families in London across multiple generations.")]),
    ("Jhumpa Lahiri", [("The Namesake", "A novel about the life of an Indian-American man navigating his cultural identity.")]),
    ("George R.R. Martin", [("A Game of Thrones", "The first book in a fantasy series about noble families vying for power in a fictional kingdom.")]),
    ("R.L. Stine", [("Goosebumps Series", "A popular children's horror series featuring spooky and thrilling tales.")]),
    ("Liane Moriarty", [("Big Little Lies", "A contemporary novel about the intertwined lives of women in a suburban community.")]),
    ("V.E. Schwab", [("Vicious", "A dark fantasy novel about two college students who gain superpowers through near-death experiences.")]),
    ("Rick Riordan", [("Percy Jackson & The Olympians", "A series of novels following a young demigod's adventures based on Greek mythology.")]),
    ("Ken Follett", [("Pillars of the Earth", "A historical novel centered around the construction of a cathedral in 12th-century England.")]),
    ("Ian McEwan", [("Atonement", "A novel exploring themes of love, war, and the effects of a child's misunderstanding.")]),
]
try:
    with transaction.atomic():
        Authors.objects.all().delete()
        Books.objects.all().delete()

        for author_name, books in data:
            author = Authors.objects.create(name=author_name)
            for title, description in books:
                Books.objects.create(title=title, author=author, description=description)
except Exception as e:
    print(f"An error occurred: {str(e)}")
    raise SystemExit

print("Setup finished with success")
