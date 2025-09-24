"""
Method Overriding Examples - Week 2
CSC 242 - Advanced Class Concepts

This file demonstrates different patterns of method overriding:
- Complete replacement
- Method extension with super()
- Abstract method implementation
- Polymorphism in action

Author: CSC 242 Teaching Team
"""

from abc import ABC, abstractmethod
import random


# ============================================================================
# ABSTRACT BASE CLASSES
# ============================================================================

class Shape(ABC):
    """Abstract base class for geometric shapes"""
    
    def __init__(self, name):
        self.name = name
        self.color = "white"
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def set_color(self, color):
        """Concrete method available to all shapes"""
        self.color = color
        return f"{self.name} is now {color}"
    
    def describe(self):
        """Concrete method that can be overridden"""
        return f"This is a {self.color} {self.name}"
    
    def __str__(self):
        return f"{self.color} {self.name}"


class Rectangle(Shape):
    """Rectangle with complete method implementation"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Complete implementation of abstract method"""
        return self.width * self.height
    
    def perimeter(self):
        """Complete implementation of abstract method"""
        return 2 * (self.width + self.height)
    
    def describe(self):
        """Override parent method with specific information"""
        base_description = super().describe()
        return f"{base_description} with dimensions {self.width}×{self.height}"
    
    def is_square(self):
        """Rectangle-specific method"""
        return self.width == self.height
    
    def scale(self, factor):
        """Scale the rectangle"""
        self.width *= factor
        self.height *= factor
        return f"Rectangle scaled by {factor}"


class Circle(Shape):
    """Circle with complete method implementation"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Complete implementation of abstract method"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Complete implementation of abstract method (circumference)"""
        import math
        return 2 * math.pi * self.radius
    
    def describe(self):
        """Override with circle-specific information"""
        base_description = super().describe()
        return f"{base_description} with radius {self.radius}"
    
    def scale(self, factor):
        """Scale the circle"""
        self.radius *= factor
        return f"Circle scaled by {factor}"


# ============================================================================
# EMPLOYEE HIERARCHY WITH METHOD EXTENSION
# ============================================================================

class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.years_employed = 0
        self.performance_rating = 3  # 1-5 scale
    
    def calculate_salary(self):
        """Base salary calculation"""
        return self.base_salary
    
    def get_benefits(self):
        """Base benefits calculation"""
        return ["Health Insurance", "Vacation Days"]
    
    def annual_review(self, rating):
        """Conduct annual review"""
        self.performance_rating = rating
        self.years_employed += 1
        return f"{self.name} reviewed: Rating {rating}/5, {self.years_employed} years employed"
    
    def get_employee_info(self):
        """Get basic employee information"""
        return {
            "name": self.name,
            "id": self.employee_id,
            "salary": self.calculate_salary(),
            "benefits": self.get_benefits(),
            "years": self.years_employed,
            "rating": self.performance_rating
        }
    
    def __str__(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"


class Manager(Employee):
    """Manager extends Employee with additional responsibilities"""
    
    def __init__(self, name, employee_id, base_salary, department):
        super().__init__(name, employee_id, base_salary)
        self.department = department
        self.team_size = 0
        self.budget_responsibility = 0
    
    def calculate_salary(self):
        """Override: Add management bonus"""
        base = super().calculate_salary()
        management_bonus = self.team_size * 2000  # $2k per team member
        budget_bonus = self.budget_responsibility * 0.01  # 1% of budget
        return base + management_bonus + budget_bonus
    
    def get_benefits(self):
        """Extend: Add manager-specific benefits"""
        base_benefits = super().get_benefits()
        manager_benefits = ["Executive Parking", "Company Car", "Stock Options"]
        return base_benefits + manager_benefits
    
    def annual_review(self, rating, team_performance=3):
        """Extend: Include team performance in review"""
        base_review = super().annual_review(rating)
        team_bonus = team_performance * 1000
        review_summary = f"{base_review}, Team Performance: {team_performance}/5"
        if team_performance >= 4:
            review_summary += f", Team Bonus: ${team_bonus}"
        return review_summary
    
    def add_team_member(self):
        """Manager-specific method"""
        self.team_size += 1
        return f"{self.name} now manages {self.team_size} team members"
    
    def set_budget(self, amount):
        """Manager-specific method"""
        self.budget_responsibility = amount
        return f"{self.name} responsible for ${amount:,} budget"


class SalesEmployee(Employee):
    """Sales employee with commission-based pay"""
    
    def __init__(self, name, employee_id, base_salary, commission_rate=0.05):
        super().__init__(name, employee_id, base_salary)
        self.commission_rate = commission_rate
        self.sales_total = 0
        self.monthly_sales = []
    
    def calculate_salary(self):
        """Override: Add commission to base salary"""
        base = super().calculate_salary()
        commission = self.sales_total * self.commission_rate
        return base + commission
    
    def get_benefits(self):
        """Extend: Add sales-specific benefits"""
        base_benefits = super().get_benefits()
        sales_benefits = ["Sales Bonus Pool", "Travel Allowance", "Client Entertainment"]
        return base_benefits + sales_benefits
    
    def record_sale(self, amount):
        """Sales-specific method"""
        self.sales_total += amount
        self.monthly_sales.append(amount)
        commission_earned = amount * self.commission_rate
        return f"${amount} sale recorded! Commission: ${commission_earned:.2f}"
    
    def get_sales_report(self):
        """Sales-specific reporting"""
        if not self.monthly_sales:
            return "No sales recorded"
        
        avg_sale = sum(self.monthly_sales) / len(self.monthly_sales)
        return f"Total Sales: ${self.sales_total:,}, Average: ${avg_sale:.2f}, Count: {len(self.monthly_sales)}"


# ============================================================================
# VEHICLE HIERARCHY WITH POLYMORPHISM
# ============================================================================

class Vehicle:
    """Base vehicle class demonstrating polymorphism"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = 100
        self.is_running = False
        self.mileage = 0
    
    def start_engine(self):
        """Base engine start behavior"""
        if self.fuel_level > 0:
            self.is_running = True
            return f"{self.make} {self.model} engine started"
        else:
            return f"Cannot start - no fuel!"
    
    def stop_engine(self):
        """Base engine stop behavior"""
        self.is_running = False
        return f"{self.make} {self.model} engine stopped"
    
    def drive(self, distance):
        """Base driving behavior"""
        if not self.is_running:
            return "Start the engine first!"
        
        fuel_needed = distance * 0.1  # Base consumption
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            self.mileage += distance
            return f"Drove {distance} miles. Fuel: {self.fuel_level:.1f}%"
        else:
            return "Not enough fuel for this trip!"
    
    def refuel(self):
        """Refuel the vehicle"""
        self.fuel_level = 100
        return f"{self.make} {self.model} refueled"
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
    """Electric car with overridden fuel system"""
    
    def __init__(self, make, model, year, battery_capacity=100):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 100  # Override fuel_level concept
    
    def start_engine(self):
        """Override: Electric cars don't have traditional engines"""
        if self.charge_level > 0:
            self.is_running = True
            return f"{self.make} {self.model} electric motor activated silently"
        else:
            return "Cannot start - battery depleted!"
    
    def drive(self, distance):
        """Override: Different energy consumption"""
        if not self.is_running:
            return "Activate the motor first!"
        
        energy_needed = distance * 0.05  # More efficient than gas
        if self.charge_level >= energy_needed:
            self.charge_level -= energy_needed
            self.mileage += distance
            return f"Drove {distance} miles silently. Battery: {self.charge_level:.1f}%"
        else:
            return "Not enough battery charge for this trip!"
    
    def refuel(self):
        """Override: Charging instead of refueling"""
        self.charge_level = 100
        return f"{self.make} {self.model} battery charged to 100%"
    
    def regenerative_brake(self, energy_recovered=5):
        """Electric car specific feature"""
        self.charge_level = min(100, self.charge_level + energy_recovered)
        return f"Regenerative braking recovered {energy_recovered}% charge"


class Motorcycle(Vehicle):
    """Motorcycle with different characteristics"""
    
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
        self.has_sidecar = False
    
    def start_engine(self):
        """Override: Motorcycle-specific start behavior"""
        base_start = super().start_engine()
        if self.is_running:
            return f"{base_start} - VROOM! 🏍️"
        return base_start
    
    def drive(self, distance):
        """Override: More fuel efficient but weather dependent"""
        if not self.is_running:
            return "Start the engine first!"
        
        # More fuel efficient than cars
        fuel_needed = distance * 0.05
        if self.fuel_level >= fuel_needed:
            self.fuel_level -= fuel_needed
            self.mileage += distance
            weather_msg = self._check_weather()
            return f"Rode {distance} miles. Fuel: {self.fuel_level:.1f}%. {weather_msg}"
        else:
            return "Not enough fuel for this trip!"
    
    def _check_weather(self):
        """Private method for weather simulation"""
        weather_conditions = ["Perfect riding weather!", "Light rain - be careful!", 
                            "Sunny day ahead!", "Windy conditions!"]
        return random.choice(weather_conditions)
    
    def wheelie(self):
        """Motorcycle-specific behavior"""
        if self.is_running:
            return f"{self.make} {self.model} pops a wheelie! 🤸"
        else:
            return "Start the engine first!"


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_abstract_classes():
    """Show abstract base class implementation"""
    print("=== ABSTRACT BASE CLASSES ===")
    
    # Cannot instantiate abstract class
    try:
        shape = Shape("Generic")  # This will fail
    except TypeError as e:
        print(f"Cannot instantiate abstract class: {e}")
    
    # Create concrete implementations
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    shapes = [rectangle, circle]
    
    print(f"\nShape calculations:")
    for shape in shapes:
        print(f"  {shape.describe()}")
        print(f"    Area: {shape.area():.2f}")
        print(f"    Perimeter: {shape.perimeter():.2f}")
        shape.set_color("blue")
        print(f"    After coloring: {shape}")


def demonstrate_method_extension():
    """Show method extension with employee hierarchy"""
    print("\n=== METHOD EXTENSION WITH EMPLOYEE HIERARCHY ===")
    
    # Create different employee types
    base_employee = Employee("John Doe", "E001", 50000)
    manager = Manager("Jane Smith", "M001", 80000, "Engineering")
    sales_person = SalesEmployee("Bob Johnson", "S001", 45000, 0.08)
    
    # Set up additional data
    manager.add_team_member()
    manager.add_team_member()
    manager.add_team_member()
    manager.set_budget(500000)
    
    sales_person.record_sale(10000)
    sales_person.record_sale(15000)
    sales_person.record_sale(8000)
    
    employees = [base_employee, manager, sales_person]
    
    print(f"Employee Information:")
    for emp in employees:
        print(f"\n{emp}")
        info = emp.get_employee_info()
        print(f"  Salary: ${info['salary']:,.2f}")
        print(f"  Benefits: {', '.join(info['benefits'][:3])}...")
        
        # Demonstrate polymorphic behavior
        review = emp.annual_review(4)
        print(f"  Review: {review}")


def demonstrate_polymorphism():
    """Show polymorphism with vehicle hierarchy"""
    print("\n=== POLYMORPHISM WITH VEHICLES ===")
    
    # Create different vehicle types
    vehicles = [
        Vehicle("Toyota", "Camry", 2023),
        ElectricCar("Tesla", "Model 3", 2023),
        Motorcycle("Harley", "Street 750", 2022, 750)
    ]
    
    print("Vehicle Operations (Polymorphism in Action):")
    for vehicle in vehicles:
        print(f"\n{vehicle}:")
        print(f"  {vehicle.start_engine()}")
        print(f"  {vehicle.drive(50)}")
        print(f"  {vehicle.refuel()}")
        
        # Try vehicle-specific methods if available
        if hasattr(vehicle, 'regenerative_brake'):
            print(f"  {vehicle.regenerative_brake()}")
        elif hasattr(vehicle, 'wheelie'):
            print(f"  {vehicle.wheelie()}")


def method_override_patterns():
    """Show different patterns of method overriding"""
    print("\n=== METHOD OVERRIDE PATTERNS ===")
    
    print("1. Complete Replacement:")
    electric = ElectricCar("Nissan", "Leaf", 2023)
    gas_car = Vehicle("Honda", "Civic", 2023)
    
    print(f"  Gas car start: {gas_car.start_engine()}")
    print(f"  Electric start: {electric.start_engine()}")
    
    print("\n2. Method Extension:")
    manager = Manager("Alice", "M002", 90000, "Sales")
    employee = Employee("Charlie", "E002", 55000)
    
    print(f"  Employee benefits: {employee.get_benefits()}")
    print(f"  Manager benefits: {manager.get_benefits()}")
    
    print("\n3. Abstract Implementation:")
    rect = Rectangle(4, 6)
    circle = Circle(3)
    
    print(f"  Rectangle area: {rect.area()}")
    print(f"  Circle area: {circle.area():.2f}")


def main():
    """Run all method overriding demonstrations"""
    print("🔄 METHOD OVERRIDING EXAMPLES - CSC 242 Week 2")
    print("=" * 60)
    
    demonstrate_abstract_classes()
    demonstrate_method_extension()
    demonstrate_polymorphism()
    method_override_patterns()
    
    print(f"\n" + "=" * 60)
    print("✅ All method overriding demonstrations complete!")
    
    print(f"\n💡 Key Patterns Demonstrated:")
    print(f"   1. Abstract base classes with required implementations")
    print(f"   2. Method extension using super()")
    print(f"   3. Complete method replacement")
    print(f"   4. Polymorphism - same interface, different behaviors")
    print(f"   5. Class-specific method additions")


if __name__ == "__main__":
    main()
