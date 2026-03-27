class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age
        self._stats = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def show_stats(self) -> None:
            print(f"Stats:  {self._grow_calls} grow,"
                  f" {self._age_calls} age,"
                  f" {self._show_calls} show")

    def show(self) -> None:
        self._stats._show_calls += 1
        print(f"{self.name}:  {round(self._height, 1)}cm,"
              f" {self._age} days old")

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height += 2.1

    def age_up(self) -> None:
        self._stats._age_calls += 1
        self._age += 1

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color:  {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter:  {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show_stats(self) -> None:
        self._stats.show_stats()
        print(f"{self._shade_calls} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season:  {self.harvest_season}")
        print(f"Nutritional value:  {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seed_count: int):
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f"Seeds:  {self.seed_count if self._bloomed else 0}")

    def bloom(self) -> None:
        super().bloom()


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    if isinstance(plant, Tree):
        plant.show_stats()
    else:
        plant._stats.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year?  -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year?  -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    for _ in range(20):
        sunflower.grow()
        sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_stats(anon)
