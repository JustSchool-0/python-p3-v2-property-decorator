APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        """Get the dog's name"""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            raise ValueError(
                "Name must be string between 1 and 25 characters.")
        
    @name.deleter
    def name(self):
        del self._name

    @property
    def breed(self):
        """Get the dog's breed"""
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

    @breed.deleter
    def breed(self):
        del self._breed