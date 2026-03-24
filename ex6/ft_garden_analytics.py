class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def get_info(self):
        state = "blooming" if self.is_blooming else "not blooming"
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers ({state})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        points: int
    ):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        base = super().get_info()
        return f"{base}, Prize points: {self.points}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self, plants):
            self.plants = plants

        def total_growth(self):
            return len(self.plants)

        def count_types(self):
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}’s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"=== {self.owner}’s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        stats = self.GardenStats(self.plants)
        total_growth = stats.total_growth()
        regular, flowering, prize = stats.count_types()
        print(
            f"Plants added: {len(self.plants)}, "
            f"Total growth: {total_growth}cm"
        )
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )

    @classmethod
    def create_garden_network(cls, owners):
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @staticmethod
    def validate_height(height):
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()
    alice.report()

    print(
        f"Height validation test: "
        f"{GardenManager.validate_height(10)}"
    )

    alice_score = sum(p.height for p in alice.plants)
    bob_score = sum(p.height for p in bob.plants)

    print(
        f"Garden scores - Alice: {alice_score}, "
        f"Bob: {bob_score}"
    )
    print(f"Total gardens managed: {GardenManager.total_gardens}")
