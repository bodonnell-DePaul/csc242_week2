"""
Operator Overloading Examples - Week 2
CSC 242 - Advanced Class Concepts

This file demonstrates comprehensive operator overloading in Python:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (<, <=, >, >=, ==, !=)
- Container operators (len, [], in, iter)
- String representation (str, repr)

Author: CSC 242 Teaching Team
"""

import math
from functools import total_ordering


# ============================================================================
# MATHEMATICAL VECTOR CLASS
# ============================================================================

class Vector:
    """A 2D vector class with comprehensive operator overloading"""
    
    def __init__(self, x=0, y=0):
        """Initialize vector with x and y components"""
        self.x = float(x)
        self.y = float(y)
    
    # Arithmetic Operators
    def __add__(self, other):
        """Vector addition: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        """Right addition: scalar + vector"""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Vector subtraction: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        """Right subtraction: scalar - vector"""
        if isinstance(other, (int, float)):
            return Vector(other - self.x, other - self.y)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """Scalar multiplication or dot product"""
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            # Dot product
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        """Right multiplication: scalar * vector"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Vector division by scalar"""
        if isinstance(other, (int, float)) and other != 0:
            return Vector(self.x / other, self.y / other)
        else:
            raise ValueError("Cannot divide vector by zero or non-scalar")
    
    def __pow__(self, other):
        """Vector raised to power (magnitude to power)"""
        if isinstance(other, (int, float)):
            magnitude = self.magnitude()
            return magnitude ** other
        else:
            return NotImplemented
    
    # Comparison Operators
    def __eq__(self, other):
        """Equality comparison: v1 == v2"""
        if isinstance(other, Vector):
            return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
        return False
    
    def __lt__(self, other):
        """Less than comparison (by magnitude)"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        elif isinstance(other, (int, float)):
            return self.magnitude() < other
        return NotImplemented
    
    def __le__(self, other):
        """Less than or equal comparison"""
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        """Greater than comparison"""
        if isinstance(other, Vector):
            return self.magnitude() > other.magnitude()
        elif isinstance(other, (int, float)):
            return self.magnitude() > other
        return NotImplemented
    
    def __ge__(self, other):
        """Greater than or equal comparison"""
        return self.__gt__(other) or self.__eq__(other)
    
    # Unary Operators
    def __neg__(self):
        """Negation: -vector"""
        return Vector(-self.x, -self.y)
    
    def __pos__(self):
        """Positive: +vector"""
        return Vector(self.x, self.y)
    
    def __abs__(self):
        """Absolute value: abs(vector) = magnitude"""
        return self.magnitude()
    
    # Utility Methods
    def magnitude(self):
        """Calculate vector magnitude"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)
    
    def angle(self):
        """Return angle in radians"""
        return math.atan2(self.y, self.x)
    
    def cross(self, other):
        """2D cross product (returns scalar)"""
        if isinstance(other, Vector):
            return self.x * other.y - self.y * other.x
        raise TypeError("Cross product requires another Vector")
    
    # String Representations
    def __str__(self):
        """Human-readable string representation"""
        return f"({self.x:.2f}, {self.y:.2f})"
    
    def __repr__(self):
        """Developer string representation"""
        return f"Vector({self.x}, {self.y})"
    
    # Hash support for use in sets/dicts
    def __hash__(self):
        """Make vector hashable"""
        return hash((round(self.x, 10), round(self.y, 10)))


# ============================================================================
# FRACTION CLASS WITH FULL OPERATOR SUPPORT
# ============================================================================

@total_ordering  # Automatically generates comparison operators
class Fraction:
    """A fraction class with comprehensive operator overloading"""
    
    def __init__(self, numerator, denominator=1):
        """Initialize fraction and reduce to lowest terms"""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Handle negative fractions
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        
        # Reduce to lowest terms
        gcd_val = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd_val
        self.denominator = denominator // gcd_val
    
    @staticmethod
    def _gcd(a, b):
        """Calculate greatest common divisor"""
        while b:
            a, b = b, a % b
        return a
    
    # Arithmetic Operators
    def __add__(self, other):
        """Addition: f1 + f2 or f + number"""
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        elif isinstance(other, (int, float)):
            return self + Fraction(other)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        """Right addition: number + fraction"""
        return self.__add__(other)
    
    def __sub__(self, other):
        """Subtraction: f1 - f2 or f - number"""
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        elif isinstance(other, (int, float)):
            return self - Fraction(other)
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        """Right subtraction: number - fraction"""
        if isinstance(other, (int, float)):
            return Fraction(other) - self
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """Multiplication: f1 * f2 or f * number"""
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, 
                          self.denominator * other.denominator)
        elif isinstance(other, (int, float)):
            return self * Fraction(other)
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        """Right multiplication: number * fraction"""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Division: f1 / f2 or f / number"""
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Fraction(self.numerator * other.denominator,
                          self.denominator * other.numerator)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return self / Fraction(other)
        else:
            return NotImplemented
    
    def __rtruediv__(self, other):
        """Right division: number / fraction"""
        if isinstance(other, (int, float)):
            return Fraction(other) / self
        else:
            return NotImplemented
    
    def __pow__(self, other):
        """Exponentiation: fraction ** power"""
        if isinstance(other, int):
            if other >= 0:
                return Fraction(self.numerator ** other, self.denominator ** other)
            else:
                return Fraction(self.denominator ** abs(other), self.numerator ** abs(other))
        else:
            return NotImplemented
    
    # Comparison Operators (only need __eq__ and __lt__ with @total_ordering)
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Fraction):
            return (self.numerator == other.numerator and 
                   self.denominator == other.denominator)
        elif isinstance(other, (int, float)):
            return self == Fraction(other)
        return False
    
    def __lt__(self, other):
        """Less than comparison"""
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator < 
                   other.numerator * self.denominator)
        elif isinstance(other, (int, float)):
            return self < Fraction(other)
        return NotImplemented
    
    # Unary Operators
    def __neg__(self):
        """Negation: -fraction"""
        return Fraction(-self.numerator, self.denominator)
    
    def __pos__(self):
        """Positive: +fraction"""
        return Fraction(self.numerator, self.denominator)
    
    def __abs__(self):
        """Absolute value: abs(fraction)"""
        return Fraction(abs(self.numerator), self.denominator)
    
    # Type Conversion
    def __int__(self):
        """Convert to integer"""
        return self.numerator // self.denominator
    
    def __float__(self):
        """Convert to float"""
        return self.numerator / self.denominator
    
    # String Representations
    def __str__(self):
        """Human-readable representation"""
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        """Developer representation"""
        return f"Fraction({self.numerator}, {self.denominator})"
    
    # Hash support
    def __hash__(self):
        """Make fraction hashable"""
        return hash((self.numerator, self.denominator))


# ============================================================================
# CUSTOM LIST CLASS WITH CONTAINER OPERATORS
# ============================================================================

class SmartList:
    """A list-like class with enhanced operator overloading"""
    
    def __init__(self, items=None):
        """Initialize with optional items"""
        self._items = list(items) if items else []
    
    # Container Protocol
    def __len__(self):
        """Length: len(smart_list)"""
        return len(self._items)
    
    def __getitem__(self, index):
        """Get item: smart_list[index]"""
        return self._items[index]
    
    def __setitem__(self, index, value):
        """Set item: smart_list[index] = value"""
        self._items[index] = value
    
    def __delitem__(self, index):
        """Delete item: del smart_list[index]"""
        del self._items[index]
    
    def __contains__(self, item):
        """Membership test: item in smart_list"""
        return item in self._items
    
    def __iter__(self):
        """Iterator: for item in smart_list"""
        return iter(self._items)
    
    # Arithmetic Operators
    def __add__(self, other):
        """Concatenation: list1 + list2"""
        if isinstance(other, SmartList):
            return SmartList(self._items + other._items)
        elif isinstance(other, list):
            return SmartList(self._items + other)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        """Right addition: list + smart_list"""
        if isinstance(other, list):
            return SmartList(other + self._items)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        """Repetition: smart_list * n"""
        if isinstance(other, int):
            return SmartList(self._items * other)
        else:
            return NotImplemented
    
    def __rmul__(self, other):
        """Right multiplication: n * smart_list"""
        return self.__mul__(other)
    
    # Comparison Operators
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, SmartList):
            return self._items == other._items
        elif isinstance(other, list):
            return self._items == other
        return False
    
    def __lt__(self, other):
        """Less than comparison (by length)"""
        if isinstance(other, (SmartList, list)):
            other_items = other._items if isinstance(other, SmartList) else other
            return len(self._items) < len(other_items)
        return NotImplemented
    
    # Additional Methods
    def append(self, item):
        """Add item to end"""
        self._items.append(item)
    
    def extend(self, items):
        """Extend with multiple items"""
        self._items.extend(items)
    
    def pop(self, index=-1):
        """Remove and return item"""
        return self._items.pop(index)
    
    def sum(self):
        """Sum all numeric items"""
        return sum(item for item in self._items if isinstance(item, (int, float)))
    
    def filter_type(self, type_class):
        """Return new SmartList with only items of specified type"""
        return SmartList([item for item in self._items if isinstance(item, type_class)])
    
    # String Representations
    def __str__(self):
        """Human-readable representation"""
        return f"SmartList{self._items}"
    
    def __repr__(self):
        """Developer representation"""
        return f"SmartList({self._items!r})"


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_vector_operations():
    """Show vector operator overloading"""
    print("=== VECTOR OPERATOR OVERLOADING ===")
    
    # Create vectors
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    
    # Arithmetic operations
    print(f"\nArithmetic Operations:")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"v1 • v2 (dot product) = {v1 * v2}")
    
    # Comparison operations
    print(f"\nComparison Operations:")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 > v2: {v1 > v2}")
    print(f"v1 < Vector(5, 0): {v1 < Vector(5, 0)}")
    
    # Unary operations
    print(f"\nUnary Operations:")
    print(f"-v1 = {-v1}")
    print(f"abs(v1) = {abs(v1):.2f}")
    print(f"v1 magnitude = {v1.magnitude():.2f}")
    print(f"v1 normalized = {v1.normalize()}")


def demonstrate_fraction_operations():
    """Show fraction operator overloading"""
    print("\n=== FRACTION OPERATOR OVERLOADING ===")
    
    # Create fractions
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 2)
    f3 = Fraction(6, 8)  # Should reduce to 3/4
    
    print(f"Fraction 1: {f1}")
    print(f"Fraction 2: {f2}")
    print(f"Fraction 3: {f3} (auto-reduced)")
    
    # Arithmetic operations
    print(f"\nArithmetic Operations:")
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 ** 2 = {f1 ** 2}")
    print(f"f1 + 1 = {f1 + 1}")
    print(f"2 * f1 = {2 * f1}")
    
    # Comparison operations
    print(f"\nComparison Operations:")
    print(f"f1 == f3: {f1 == f3}")
    print(f"f1 > f2: {f1 > f2}")
    print(f"f2 < 1: {f2 < 1}")
    
    # Type conversions
    print(f"\nType Conversions:")
    print(f"float(f1) = {float(f1)}")
    print(f"int(f1) = {int(f1)}")


def demonstrate_smart_list():
    """Show custom list operator overloading"""
    print("\n=== SMART LIST OPERATOR OVERLOADING ===")
    
    # Create smart lists
    sl1 = SmartList([1, 2, 3])
    sl2 = SmartList(['a', 'b', 'c'])
    
    print(f"Smart List 1: {sl1}")
    print(f"Smart List 2: {sl2}")
    
    # Container operations
    print(f"\nContainer Operations:")
    print(f"len(sl1) = {len(sl1)}")
    print(f"sl1[1] = {sl1[1]}")
    print(f"2 in sl1: {2 in sl1}")
    print(f"Items in sl1: {[item for item in sl1]}")
    
    # Arithmetic operations
    print(f"\nArithmetic Operations:")
    print(f"sl1 + sl2 = {sl1 + sl2}")
    print(f"sl1 * 2 = {sl1 * 2}")
    
    # Smart list specific methods
    print(f"\nSmart List Methods:")
    mixed_list = SmartList([1, 'hello', 2.5, 'world', 3])
    print(f"Mixed list: {mixed_list}")
    print(f"Numbers only: {mixed_list.filter_type((int, float))}")
    print(f"Strings only: {mixed_list.filter_type(str)}")
    print(f"Sum of numbers: {mixed_list.filter_type((int, float)).sum()}")


def operator_precedence_demo():
    """Demonstrate operator precedence and associativity"""
    print("\n=== OPERATOR PRECEDENCE DEMONSTRATION ===")
    
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(5, 6)
    
    print(f"Vectors: v1={v1}, v2={v2}, v3={v3}")
    
    # Addition is left-associative
    result1 = v1 + v2 + v3
    result2 = (v1 + v2) + v3
    print(f"\nAddition associativity:")
    print(f"v1 + v2 + v3 = {result1}")
    print(f"(v1 + v2) + v3 = {result2}")
    print(f"Results equal: {result1 == result2}")
    
    # Multiplication has higher precedence than addition
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    f3 = Fraction(2, 3)
    
    print(f"\nFractions: f1={f1}, f2={f2}, f3={f3}")
    print(f"f1 + f2 * f3 = {f1 + f2 * f3}")
    print(f"(f1 + f2) * f3 = {(f1 + f2) * f3}")


def comprehensive_operator_test():
    """Comprehensive test of all implemented operators"""
    print("\n=== COMPREHENSIVE OPERATOR TEST ===")
    
    # Test all vector operators
    v = Vector(3, 4)
    print(f"Testing Vector {v}:")
    
    operators_to_test = [
        ("+", lambda: v + Vector(1, 1)),
        ("-", lambda: v - Vector(1, 1)),
        ("* (scalar)", lambda: v * 2),
        ("/ (scalar)", lambda: v / 2),
        ("==", lambda: v == Vector(3, 4)),
        ("<", lambda: v < Vector(5, 5)),
        ("abs", lambda: abs(v)),
        ("neg", lambda: -v),
    ]
    
    for op_name, op_func in operators_to_test:
        try:
            result = op_func()
            print(f"  {op_name}: {result}")
        except Exception as e:
            print(f"  {op_name}: Error - {e}")


def main():
    """Run all operator overloading demonstrations"""
    print("⚙️ OPERATOR OVERLOADING EXAMPLES - CSC 242 Week 2")
    print("=" * 60)
    
    demonstrate_vector_operations()
    demonstrate_fraction_operations()
    demonstrate_smart_list()
    operator_precedence_demo()
    comprehensive_operator_test()
    
    print(f"\n" + "=" * 60)
    print("✅ All operator overloading demonstrations complete!")
    
    print(f"\n💡 Key Concepts Demonstrated:")
    print(f"   1. Arithmetic operator overloading (+, -, *, /, **)")
    print(f"   2. Comparison operator overloading (<, <=, ==, >, >=)")
    print(f"   3. Container protocol (__len__, __getitem__, __contains__)")
    print(f"   4. Unary operators (__neg__, __pos__, __abs__)")
    print(f"   5. Right-hand operators (__radd__, __rmul__, etc.)")
    print(f"   6. Type conversion operators (__int__, __float__)")
    print(f"   7. String representation (__str__, __repr__)")


if __name__ == "__main__":
    main()
