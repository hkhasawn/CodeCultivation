class SecurePlant:
    def __init__(self, name):
        self.name = name
        self._height = 0
        self._age = 0

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)

    print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")
