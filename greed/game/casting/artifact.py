from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """An item on the playing field.
    
    The responsibility of Artifact is to keep track of its appearance and position.
    
    Attrubutes:
        _
    
    
    """

    def __init__(self):
        """Constructs a new Artifact (object on the screen)."""
        super().__init__()

    def calculate_points(self):
        points = 0

        if (self.get_text) == '*':
            point = 1
        else:
            point = -1

        return point
    

