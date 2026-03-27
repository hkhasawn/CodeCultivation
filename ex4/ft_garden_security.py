class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}:  {round(self._height, 1)}cm,{self._age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}:  Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}:  Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height += 0.8

    def age_up(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-1)
    print()
    print("Current state: ", end="")
    plant.show()
