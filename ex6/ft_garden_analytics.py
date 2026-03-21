class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: float = 1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_type(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = True

    def bloom(self):
        self.is_blooming = True

    def get_type(self) -> str:
        return "flowering"

    def get_info(self) -> str:
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        prize_points: int
    ):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_type(self) -> str:
        return "prize flowers"

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Prize points: {self.prize_points}"


class GardenManager:

    class GardenStats:
        @staticmethod
        def calculate_score(plants: list) -> int:
            total = 0
            for plant in plants:
                total += int(plant.height)
                if hasattr(plant, 'prize_points'):
                    total += plant.prize_points
            return total

        @staticmethod
        def count_by_type(plants: list) -> dict:
            counts = {"regular": 0, "flowering": 0, "prize flowers": 0}
            for plant in plants:
                ptype = plant.get_type()
                if ptype in counts:
                    counts[ptype] += 1
            return counts

        @staticmethod
        def total_growth(plants: list, initial_heights: list) -> float:
            total = 0
            for plant, initial in zip(plants, initial_heights):
                total += plant.height - initial
            return total

    _total_gardens = 0

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self._initial_heights = []
        self.stats = GardenManager.GardenStats()
        GardenManager._total_gardens += 1

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        self._initial_heights.append(plant.height)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def water_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def generate_report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if hasattr(plant, 'get_info'):
                print(f"  - {plant.get_info()}")
            else:
                print(f"  - {plant.name}: {plant.height}cm")

        growth = self.stats.total_growth(self.plants, self._initial_heights)
        counts = self.stats.count_by_type(self.plants)
        print(
            f"Plants added: {len(self.plants)}, "
            f"Total growth: {int(growth)}cm"
        )
        print(
            f"Plant types: {counts['regular']} regular, "
            f"{counts['flowering']} flowering, "
            f"{counts['prize flowers']} prize flowers"
        )

    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        return [cls(owner) for owner in owners]

    @classmethod
    def get_total_gardens(cls) -> int:
        return cls._total_gardens

    @staticmethod
    def validate_height(height: float) -> bool:
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")

    oak = Plant("Oak Tree", 100, 1825)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print()
    alice_garden.water_all()

    alice_garden.generate_report()

    print()
    is_valid = GardenManager.validate_height(10)
    print(f"Height validation test: {is_valid}")

    bob_garden = GardenManager("Bob")
    fern = Plant("Fern", 15, 60)
    tulip = FloweringPlant("Tulip", 30, 20, "pink")
    bob_garden.add_plant(fern)
    bob_garden.add_plant(tulip)

    alice_score = alice_garden.stats.calculate_score(alice_garden.plants)
    bob_score = bob_garden.stats.calculate_score(bob_garden.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
