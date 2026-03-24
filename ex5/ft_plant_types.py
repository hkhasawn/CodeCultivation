class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = self.trunk_diameter * self.height
        print(f"{self.name} provides {shade_area} square meters of shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower1 = Flower("Rose", 25, 30, "red")
    flower2 = Flower("Tulip", 20, 25, "yellow")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree2 = Tree("Pine", 400, 1500, 40)
    veg1 = Vegetable("Tomato", 80, 90, "summer", "Vitamin C")
    veg2 = Vegetable("Carrot", 30, 70, "winter", "Vitamin A")
    print(
        f"{flower1.name} (Flower): {flower1.height}cm,"
        f" {flower1.age} days, {flower1.color} color"
    )
    flower1.bloom()
    print(
        f"{tree1.name} (Tree): {tree1.height}cm,"
        f" {tree1.age} days, {tree1.trunk_diameter}cm diameter"
    )
    tree1.produce_shade()
    print(
        f"{veg1.name} (Vegetable): {veg1.height}cm,"
        f" {veg1.age} days, {veg1.harvest_season} harvest"
    )
    print(f"{veg1.name} is rich in {veg1.nutritional_value}")
