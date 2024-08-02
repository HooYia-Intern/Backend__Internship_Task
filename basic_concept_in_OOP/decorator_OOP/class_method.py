def __init__(self, wheel):
    self.wheel = wheel
    self.Name = "class car"
@classmethod
def get_info(cls):
    return dir(cls)
#Take an Argement when creating the fuction 