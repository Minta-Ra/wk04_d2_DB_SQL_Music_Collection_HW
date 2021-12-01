class Artist():
    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    # Display the name rather than space in memory
    # def __str__(self):
    #     return {"id" : self.id, "name" : self.name}