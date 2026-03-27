class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age_up(self) -> None:
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25.0, 30)
    initial_height = plant.height
    for day in range(7):
        print(f"=== Day {day + 1} ===")
        plant.show()
        plant.grow()
        plant.age_up()
    print(f"Growth this week: {round(plant.height - initial_height)}cm")
