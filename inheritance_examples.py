"""
Inheritance Examples - Week 2
CSC 242 - Advanced Class Concepts

This file demonstrates various inheritance patterns and concepts including:
- Basic inheritance
- Method overriding
- Constructor chaining with super()
- Multiple inheritance scenarios

Author: CSC 242 Teaching Team
"""


# ============================================================================
# BASIC INHERITANCE EXAMPLES
# ============================================================================

class Animal:
    """Base animal class demonstrating inheritance fundamentals"""
    
    # Class variable shared by all animals
    kingdom = "Animalia"
    total_animals = 0
    
    def __init__(self, species="Unknown", language="Silent", age=0):
        """Constructor with default parameters"""
        self.species = species
        self.language = language
        self.age = age
        self.energy = 100
        self.is_sleeping = False
        
        # Update class variable
        Animal.total_animals += 1
        
        print(f"🐾 Created {self.species} (Total animals: {Animal.total_animals})")
    
    def speak(self):
        """Basic speaking behavior"""
        if self.language == "Silent":
            return f"The {self.species} makes no sound"
        return f"I am a {self.species} and I {self.language}"
    
    def sleep(self):
        """Put animal to sleep"""
        self.is_sleeping = True
        self.energy = min(100, self.energy + 20)
        return f"{self.species} is sleeping... 😴"
    
    def wake_up(self):
        """Wake up the animal"""
        self.is_sleeping = False
        return f"{self.species} wakes up! Energy: {self.energy}"
    
    def age_up(self, years=1):
        """Age the animal"""
        self.age += years
        self.energy = max(0, self.energy - years * 5)
        return f"{self.species} aged {years} year(s). Now {self.age} years old."
    
    def get_info(self):
        """Get basic animal information"""
        status = "sleeping" if self.is_sleeping else "awake"
        return f"{self.species}, {self.age} years old, {status}, energy: {self.energy}"
    
    def __str__(self):
        """String representation"""
        return f"{self.species} ({self.age} years old)"
    
    def __repr__(self):
        """Developer representation"""
        return f"Animal('{self.species}', '{self.language}', {self.age})"


class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed="Mixed", age=0):
        """Dog constructor"""
        super().__init__("Dog", "Bark", age)  # Call parent constructor
        self.name = name
        self.breed = breed
        self.is_trained = False
        self.tricks = []
    
    def speak(self):
        """Override parent speak method"""
        if self.is_sleeping:
            return f"{self.name} is sleeping and won't bark"
        return f"{self.name} says: Woof! Woof!"
    
    def fetch(self, item="ball"):
        """Dog-specific behavior"""
        if self.is_sleeping:
            return f"{self.name} is sleeping and can't fetch"
        
        self.energy -= 10
        return f"{self.name} fetches the {item}! 🎾"
    
    def learn_trick(self, trick):
        """Teach the dog a new trick"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.is_trained = True
            return f"{self.name} learned '{trick}'!"
        else:
            return f"{self.name} already knows '{trick}'"
    
    def perform_trick(self, trick):
        """Perform a learned trick"""
        if trick in self.tricks:
            self.energy -= 5
            return f"{self.name} performs '{trick}'! 🐕"
        else:
            return f"{self.name} doesn't know '{trick}' yet"
    
    def get_info(self):
        """Extend parent method with dog-specific info"""
        base_info = super().get_info()
        trained_status = "trained" if self.is_trained else "untrained"
        return f"{self.name} the {self.breed} - {base_info}, {trained_status}"
    
    def __str__(self):
        return f"{self.name} the {self.breed}"


class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, color="Unknown", age=0):
        """Cat constructor"""
        super().__init__("Cat", "Meow", age)
        self.name = name
        self.color = color
        self.lives_remaining = 9
        self.is_indoor = True
    
    def speak(self):
        """Override parent speak method"""
        if self.is_sleeping:
            return f"{self.name} purrs softly while sleeping"
        
        moods = ["Meow!", "Purr...", "Hiss!", "Mrow?"]
        import random
        mood = random.choice(moods)
        return f"{self.name} says: {mood}"
    
    def hunt(self, prey="mouse"):
        """Cat-specific hunting behavior"""
        if self.is_sleeping:
            return f"{self.name} is too sleepy to hunt"
        
        if not self.is_indoor:
            self.energy -= 15
            success = random.random() > 0.5
            if success:
                return f"{self.name} successfully caught a {prey}! 🐭"
            else:
                return f"{self.name} missed the {prey}"
        else:
            return f"{self.name} can't hunt indoors"
    
    def go_outside(self):
        """Let cat go outside"""
        if self.is_indoor:
            self.is_indoor = False
            return f"{self.name} goes outside to explore 🚪"
        else:
            return f"{self.name} is already outside"
    
    def come_inside(self):
        """Bring cat inside"""
        if not self.is_indoor:
            self.is_indoor = True
            return f"{self.name} comes back inside"
        else:
            return f"{self.name} is already inside"
    
    def lose_life(self):
        """Cat loses a life (dangerous situations)"""
        if self.lives_remaining > 1:
            self.lives_remaining -= 1
            return f"{self.name} lost a life! {self.lives_remaining} remaining"
        else:
            return f"{self.name} is on their last life!"
    
    def get_info(self):
        """Extend parent method"""
        base_info = super().get_info()
        location = "indoors" if self.is_indoor else "outdoors"
        return f"{self.name} the {self.color} cat - {base_info}, {location}, {self.lives_remaining} lives"
    
    def __str__(self):
        return f"{self.name} the {self.color} cat"


class Bird(Animal):
    """Bird class with flying capabilities"""
    
    def __init__(self, species, can_fly=True, wingspan=0, age=0):
        """Bird constructor"""
        super().__init__(species, "Chirp", age)
        self.can_fly = can_fly
        self.wingspan = wingspan
        self.altitude = 0
        self.migration_distance = 0
    
    def speak(self):
        """Birds have various sounds"""
        if self.is_sleeping:
            return f"The {self.species} sleeps quietly"
        
        sounds = {
            "Eagle": "Screech!",
            "Parrot": "Hello! Hello!",
            "Owl": "Hoot! Hoot!",
            "Robin": "Tweet tweet!",
            "Penguin": "Squawk!"
        }
        sound = sounds.get(self.species, "Chirp!")
        return f"The {self.species} says: {sound}"
    
    def fly(self, height=100):
        """Flying behavior"""
        if not self.can_fly:
            return f"{self.species} cannot fly"
        
        if self.is_sleeping:
            return f"{self.species} needs to wake up first"
        
        self.altitude = height
        self.energy -= height // 10
        return f"{self.species} flies to {height} feet! 🦅"
    
    def land(self):
        """Landing behavior"""
        if self.altitude > 0:
            self.altitude = 0
            return f"{self.species} lands gracefully"
        else:
            return f"{self.species} is already on the ground"
    
    def migrate(self, distance):
        """Migration behavior"""
        if not self.can_fly:
            return f"{self.species} cannot migrate"
        
        self.migration_distance += distance
        self.energy -= distance // 100
        return f"{self.species} migrates {distance} miles (total: {self.migration_distance})"
    
    def get_info(self):
        """Extended bird information"""
        base_info = super().get_info()
        flight_status = f"altitude {self.altitude}ft" if self.altitude > 0 else "on ground"
        flying_ability = "can fly" if self.can_fly else "flightless"
        return f"{base_info}, {flying_ability}, {flight_status}, wingspan: {self.wingspan}cm"


# ============================================================================
# MULTIPLE INHERITANCE EXAMPLE
# ============================================================================

class Swimmer:
    """Mixin class for swimming behavior"""
    
    def __init__(self):
        self.can_swim = True
        self.swimming_speed = 5  # mph
    
    def swim(self, distance=100):
        """Swimming behavior"""
        if hasattr(self, 'energy'):
            self.energy -= distance // 10
        return f"Swimming {distance} meters at {self.swimming_speed} mph! 🏊"
    
    def dive(self, depth=10):
        """Diving behavior"""
        if hasattr(self, 'energy'):
            self.energy -= depth
        return f"Diving to {depth} feet deep! 🤿"


class Duck(Bird, Swimmer):
    """Duck class demonstrating multiple inheritance"""
    
    def __init__(self, name, age=0):
        """Duck constructor - multiple inheritance"""
        Bird.__init__(self, "Duck", True, 60, age)
        Swimmer.__init__(self)
        self.name = name
        self.is_in_water = False
    
    def speak(self):
        """Duck-specific sound"""
        if self.is_sleeping:
            return f"{self.name} sleeps peacefully on the water"
        return f"{self.name} says: Quack! Quack! 🦆"
    
    def enter_water(self):
        """Duck enters water"""
        self.is_in_water = True
        return f"{self.name} splashes into the water!"
    
    def leave_water(self):
        """Duck leaves water"""
        self.is_in_water = False
        return f"{self.name} waddles out of the water"
    
    def fly(self, height=50):
        """Override flying for ducks"""
        if self.is_in_water:
            return f"{self.name} needs to leave the water first"
        return super().fly(height)
    
    def swim(self, distance=50):
        """Override swimming for ducks"""
        if not self.is_in_water:
            self.enter_water()
        return super().swim(distance)
    
    def get_info(self):
        """Complete duck information"""
        base_info = super().get_info()
        water_status = "in water" if self.is_in_water else "on land"
        return f"{self.name} - {base_info}, {water_status}"
    
    def __str__(self):
        return f"{self.name} the Duck"


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_basic_inheritance():
    """Show basic inheritance concepts"""
    print("=== BASIC INHERITANCE DEMONSTRATION ===")
    
    # Create animals
    generic_animal = Animal("Mystery Animal", "Grunt", 5)
    dog = Dog("Buddy", "Golden Retriever", 3)
    cat = Cat("Whiskers", "Orange", 2)
    eagle = Bird("Eagle", True, 200, 4)
    
    print(f"\nCreated animals:")
    for animal in [generic_animal, dog, cat, eagle]:
        print(f"  {animal}")
    
    print(f"\nAll animals speaking:")
    for animal in [generic_animal, dog, cat, eagle]:
        print(f"  {animal.speak()}")
    
    print(f"\nAnimal information:")
    for animal in [generic_animal, dog, cat, eagle]:
        print(f"  {animal.get_info()}")


def demonstrate_method_overriding():
    """Show method overriding in action"""
    print("\n=== METHOD OVERRIDING DEMONSTRATION ===")
    
    # Create different animals
    animals = [
        Animal("Base Animal", "Generic Sound"),
        Dog("Rex", "German Shepherd"),
        Cat("Luna", "Black"),
        Bird("Robin")
    ]
    
    print("Same method, different behaviors:")
    for animal in animals:
        print(f"  {type(animal).__name__}: {animal.speak()}")
    
    # Show method extension with get_info
    print(f"\nMethod extension with get_info():")
    for animal in animals:
        print(f"  {animal.get_info()}")


def demonstrate_special_behaviors():
    """Show class-specific behaviors"""
    print("\n=== SPECIAL BEHAVIORS DEMONSTRATION ===")
    
    # Dog behaviors
    dog = Dog("Fido", "Labrador", 2)
    print(f"Dog behaviors:")
    print(f"  {dog.fetch()}")
    print(f"  {dog.learn_trick('sit')}")
    print(f"  {dog.learn_trick('roll over')}")
    print(f"  {dog.perform_trick('sit')}")
    
    # Cat behaviors
    cat = Cat("Shadow", "Gray", 3)
    print(f"\nCat behaviors:")
    print(f"  {cat.go_outside()}")
    print(f"  {cat.hunt()}")
    print(f"  {cat.come_inside()}")
    
    # Bird behaviors
    bird = Bird("Hawk", True, 150, 5)
    print(f"\nBird behaviors:")
    print(f"  {bird.fly(500)}")
    print(f"  {bird.migrate(1000)}")
    print(f"  {bird.land()}")


def demonstrate_multiple_inheritance():
    """Show multiple inheritance with Duck"""
    print("\n=== MULTIPLE INHERITANCE DEMONSTRATION ===")
    
    duck = Duck("Donald", 4)
    print(f"Duck created: {duck}")
    print(f"MRO: {Duck.__mro__}")
    
    print(f"\nDuck behaviors:")
    print(f"  {duck.speak()}")
    print(f"  {duck.swim(100)}")
    print(f"  {duck.fly(200)}")
    print(f"  {duck.leave_water()}")
    print(f"  {duck.fly(200)}")
    print(f"  {duck.dive(20)}")
    
    print(f"\nFinal duck info: {duck.get_info()}")


def inheritance_quiz():
    """Interactive quiz about inheritance"""
    print("\n=== INHERITANCE QUIZ ===")
    
    # Create objects for testing
    dog = Dog("Quiz Dog", "Beagle")
    cat = Cat("Quiz Cat", "White")
    
    print("Test your understanding:")
    print(f"1. isinstance(dog, Animal): {isinstance(dog, Animal)}")
    print(f"2. isinstance(dog, Dog): {isinstance(dog, Dog)}")
    print(f"3. isinstance(dog, Cat): {isinstance(dog, Cat)}")
    print(f"4. issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
    print(f"5. issubclass(Animal, Dog): {issubclass(Animal, Dog)}")
    
    print(f"\nClass hierarchies:")
    print(f"Dog MRO: {Dog.__mro__}")
    print(f"Cat MRO: {Cat.__mro__}")
    print(f"Duck MRO: {Duck.__mro__}")


def main():
    """Run all inheritance demonstrations"""
    print("🏗️ INHERITANCE EXAMPLES - CSC 242 Week 2")
    print("=" * 60)
    
    demonstrate_basic_inheritance()
    demonstrate_method_overriding()
    demonstrate_special_behaviors()
    demonstrate_multiple_inheritance()
    inheritance_quiz()
    
    print(f"\n" + "=" * 60)
    print(f"Total animals created: {Animal.total_animals}")
    print("✅ All inheritance demonstrations complete!")
    
    print(f"\n💡 Key Concepts Demonstrated:")
    print(f"   1. Basic inheritance with super()")
    print(f"   2. Method overriding and extension")
    print(f"   3. Class-specific behaviors")
    print(f"   4. Multiple inheritance")
    print(f"   5. Method Resolution Order (MRO)")


if __name__ == "__main__":
    main()
