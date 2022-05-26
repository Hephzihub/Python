class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        

    def change_name (self, update_name):
        self.name = update_name

    def change_age (self, update_age):
        self.age = int(update_age)
    
    def add_track (self, new_track):
        self.tracks.append(new_track)
    
    def get_score (self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
