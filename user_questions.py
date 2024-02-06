#Constraint functions
def age_check(x): #valid age response
    if(x.isnumeric() == False):
        return False
    return int(x) > 0

def gender_check(x): #valid gender response
    x = x.lower()
    gender_options = ["m", "f"]
    return x in gender_options

#Replace with Brennan's scrape
genres = ['Literature & Fiction', 'History', 'Medical Books', 'Literature & Fiction', 'Reference', 'Literature & Fiction', 'Mystery, Thriller & Suspense', 'Literature & Fiction', 'Humor & Entertainment', 'Cookbooks, Food & Wine', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Sports & Outdoors', 'Literature & Fiction', 'Health, Fitness & Dieting', 'Christian Books & Bibles', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Literature & Fiction', 'Christian Books & Bibles', 'Mystery, Thriller & Suspense', 'Health, Fitness & Dieting', 'History', 'Literature & Fiction', 'Literature & Fiction', 'Teen & Young Adult', 'Teen & Young Adult', 'Literature & Fiction', 'Science & Math', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', "Children's Books", 'Literature & Fiction', 'Politics & Social Sciences', 'Sports & Outdoors', 'Self-Help', 'Science Fiction & Fantasy', 'Teen & Young Adult', 'Literature & Fiction', 'Literature & Fiction', 'Humor & Entertainment', 'Literature & Fiction', 'Literature & Fiction', 'Biographies & Memoirs', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Science Fiction & Fantasy', 'History', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Literature & Fiction', 'Biographies & Memoirs', 'Literature & Fiction', 'Literature & Fiction', 'Business & Money', 'Literature & Fiction', 'Biographies & Memoirs', 'Business & Money', 'Literature & Fiction', 'Humor & Entertainment', 'Science Fiction & Fantasy', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Mystery, Thriller & Suspense', 'Literature & Fiction', 'Literature & Fiction', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Mystery, Thriller & Suspense', 'Literature & Fiction', 'Biographies & Memoirs', 'Humor & Entertainment', 'Literature & Fiction', 'Humor & Entertainment', 'Literature & Fiction', 'Literature & Fiction', 'Biographies & Memoirs', 'Literature & Fiction', 'Biographies & Memoirs', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction', 'Literature & Fiction']

def genre_check(x):
    for term in x.split(", "):
        if term not in genres:
            return False
    return True

def yncheck(x):
    x = x.lower()
    if x == "y" or x == "n":
        return True
    return False


#Question class definition
class Question:
    question_list = []
    
    def __init__(self, question, constraintfunc, errormsg):
        self.question = question #string question to ask the user
        self.constraint = constraintfunc #constraint function to validate the user's response to that question
        self.msg = errormsg #error message if the constraint function returns false (invalid response)
        self.__class__.question_list.append(self)

Question(
    "What is your age?",
    age_check,
    "Please enter an integer greater than zero."
)

Question(
    "What is your gender? [m/f]",
    gender_check,
    "Please enter either m or f."
)

Question(
    "What genres are you interested in?",
    genre_check,
    f"Please enter a comma-seperated list of genres: {genres}"
)

Question(
    "Are you open to other genres? [y/n]",
    yncheck,
    f"Please enter y or n."
)