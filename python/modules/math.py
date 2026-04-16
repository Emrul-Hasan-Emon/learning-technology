# Math Module in Python
# The math module provides mathematical functions and constants.
# It includes basic arithmetic, trigonometric, logarithmic, and other mathematical operations.

import math

# Mathematical Constants
print(f"Pi: {math.pi}")  # Output - Pi: 3.141592653589793
print(f"Euler's e: {math.e}")  # Output - Euler's e: 2.718281828459045
print(f"Tau (2π): {math.tau}")  # Output - Tau: 6.283185307179586
print(f"Infinity: {math.inf}")  # Output - Infinity: inf
print(f"NaN: {math.nan}")  # Output - NaN: nan

# Rounding Functions
print(f"ceil(4.3): {math.ceil(4.3)}")  # Output - ceil(4.3): 5
print(f"floor(4.7): {math.floor(4.7)}")  # Output - floor(4.7): 4
print(f"trunc(4.9): {math.trunc(4.9)}")  # Output - trunc(4.9): 4
print(f"fabs(-5): {math.fabs(-5)}")  # Output - fabs(-5): 5.0

# Power and Square Root
print(f"sqrt(16): {math.sqrt(16)}")  # Output - sqrt(16): 4.0
print(f"pow(2, 3): {math.pow(2, 3)}")  # Output - pow(2, 3): 8.0
print(f"exp(1): {math.exp(1)}")  # Output - exp(1): 2.718281828459045

# Logarithmic Functions
print(f"log(100): {math.log(100)}")  # Output - log(100): 4.605170 (natural log)
print(f"log10(100): {math.log10(100)}")  # Output - log10(100): 2.0
print(f"log2(8): {math.log2(8)}")  # Output - log2(8): 3.0

# Trigonometric Functions (in radians)
angle_rad = math.pi / 4  # 45 degrees in radians
print(f"sin(π/4): {math.sin(angle_rad)}")  # Output - sin(π/4): 0.7071...
print(f"cos(π/4): {math.cos(angle_rad)}")  # Output - cos(π/4): 0.7071...
print(f"tan(π/4): {math.tan(angle_rad)}")  # Output - tan(π/4): 1.0

# Inverse Trigonometric Functions
print(f"asin(0.5): {math.asin(0.5)}")  # Output - asin(0.5): 0.5236... (π/6 radians)
print(f"acos(0.5): {math.acos(0.5)}")  # Output - acos(0.5): 1.0472... (π/3 radians)
print(f"atan(1): {math.atan(1)}")  # Output - atan(1): 0.7854... (π/4 radians)

# Degree and Radian Conversion
print(f"radians(45): {math.radians(45)}")  # Output - radians(45): 0.7854...
print(f"degrees(π/4): {math.degrees(math.pi/4)}")  # Output - degrees(π/4): 45.0

# Factorial
print(f"factorial(5): {math.factorial(5)}")  # Output - factorial(5): 120
print(f"factorial(0): {math.factorial(0)}")  # Output - factorial(0): 1

# GCD (Greatest Common Divisor)
print(f"gcd(48, 18): {math.gcd(48, 18)}")  # Output - gcd(48, 18): 6
print(f"gcd(100, 50): {math.gcd(100, 50)}")  # Output - gcd(100, 50): 50

# LCM (Least Common Multiple) - Python 3.9+
if hasattr(math, 'lcm'):
    print(f"lcm(12, 18): {math.lcm(12, 18)}")  # Output - lcm(12, 18): 36

# Hyperbolic Functions
print(f"sinh(0): {math.sinh(0)}")  # Output - sinh(0): 0.0
print(f"cosh(0): {math.cosh(0)}")  # Output - cosh(0): 1.0
print(f"tanh(0): {math.tanh(0)}")  # Output - tanh(0): 0.0

# Special Functions
print(f"fsum([0.1, 0.1, 0.1]): {math.fsum([0.1, 0.1, 0.1])}")  # Output - 0.3 (accurate sum)
print(f"prod([1,2,3,4]): {math.prod([1, 2, 3, 4])}")  # Output - 24 (if available)

# Distance Calculation (Euclidean)
print(f"sqrt(3² + 4²): {math.sqrt(3**2 + 4**2)}")  # Output - 5.0 (Pythagorean triple)

# Check for Special Values
print(f"isnan(math.nan): {math.isnan(math.nan)}")  # Output - True
print(f"isinf(math.inf): {math.isinf(math.inf)}")  # Output - True
print(f"isfinite(10): {math.isfinite(10)}")  # Output - True

# ==================== Case Studies and Problems ====================

# Case Study 1: Calculate Circle Area and Circumference
def circle_calculations(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return {"area": area, "circumference": circumference}

r = 5
result = circle_calculations(r)
print(f"\nCircle with radius {r}:")
print(f"  Area: {result['area']:.2f}")  # Output - Area: 78.50
print(f"  Circumference: {result['circumference']:.2f}")  # Output - Circumference: 31.42

# Case Study 2: Right Triangle - Find Hypotenuse
def find_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

h = find_hypotenuse(3, 4)
print(f"\nHypotenuse of 3-4 triangle: {h}")  # Output - 5.0

# Case Study 3: Distance Between Two Points
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

dist = distance_between_points(0, 0, 3, 4)
print(f"Distance between (0,0) and (3,4): {dist}")  # Output - 5.0

# Case Study 4: Convert Temperature
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

c = 25
f = celsius_to_fahrenheit(c)
print(f"\n{c}°C = {f:.2f}°F")  # Output - 25°C = 77.00°F

# Case Study 5: Angle Between Two Lines
def angle_between_lines(m1, m2):
    """m1 and m2 are slopes"""
    if m1 * m2 == -1:
        return 90  # Perpendicular
    tan_angle = abs((m1 - m2) / (1 + m1 * m2))
    return math.degrees(math.atan(tan_angle))

angle = angle_between_lines(1, 2)
print(f"\nAngle between lines with slopes 1 and 2: {angle:.2f}°")

# Case Study 6: Find Prime Factors using Math Functions
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

factors = prime_factors(60)
print(f"\nPrime factors of 60: {factors}")  # Output - [2, 2, 3, 5]

# Case Study 7: Calculate Compound Interest
def compound_interest(principal, rate, time, compounds_per_year):
    """Calculate compound interest"""
    amount = principal * (1 + rate / (100 * compounds_per_year)) ** (compounds_per_year * time)
    interest = amount - principal
    return {"amount": amount, "interest": interest}

result = compound_interest(1000, 5, 2, 4)
print(f"\nCompound Interest:")
print(f"  Principal: $1000, Rate: 5%, Time: 2 years")
print(f"  Amount: ${result['amount']:.2f}")
print(f"  Interest earned: ${result['interest']:.2f}")

# Case Study 8: Calculate Loan EMI (Equated Monthly Installment)
def calculate_emi(principal, annual_rate, years):
    """Calculate monthly EMI for a loan"""
    monthly_rate = annual_rate / (12 * 100)
    num_payments = years * 12
    if monthly_rate == 0:
        emi = principal / num_payments
    else:
        emi = principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
              ((1 + monthly_rate) ** num_payments - 1)
    return emi

emi = calculate_emi(100000, 8, 5)
print(f"\nLoan EMI: ${emi:.2f} per month")  # Output - ~2028.64

# Case Study 9: Standard Deviation and Variance
def calculate_variance_std(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return {"mean": mean, "variance": variance, "std_dev": std_dev}

data = [10, 20, 30, 40, 50]
stats = calculate_variance_std(data)
print(f"\nData: {data}")
print(f"  Mean: {stats['mean']:.2f}")
print(f"  Variance: {stats['variance']:.2f}")
print(f"  Std Dev: {stats['std_dev']:.2f}")

# Case Study 10: Pythagorean Theorem Verification
def verify_pythagorean(a, b, c):
    """Check if a, b, c form a valid right triangle"""
    return math.isclose(a**2 + b**2, c**2)

print(f"\nIs (3, 4, 5) a right triangle? {verify_pythagorean(3, 4, 5)}")  # Output - True
print(f"Is (1, 2, 3) a right triangle? {verify_pythagorean(1, 2, 3)}")  # Output - False

# Case Study 11: Normalize Angle (Convert to 0-360 degrees)
def normalize_angle(angle):
    """Normalize angle to 0-360 degrees"""
    return angle % 360

print(f"\nNormalize 450°: {normalize_angle(450)}°")  # Output - 90°
print(f"Normalize -45°: {normalize_angle(-45)}°")  # Output - 315°

# Case Study 12: Calculate Percentage
def calculate_percentage(part, whole):
    return (part / whole) * 100

percentage = calculate_percentage(25, 100)
print(f"\n25 out of 100 is {percentage:.1f}%")  # Output - 25%

# Case Study 13: Build Quadratic Equation Solver
def solve_quadratic(a, b, c):
    """Solve ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return {"type": "complex", "message": "No real roots"}
    elif discriminant == 0:
        root = -b / (2*a)
        return {"type": "single", "root": root}
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return {"type": "two", "root1": root1, "root2": root2}

roots = solve_quadratic(1, -5, 6)
print(f"\nQuadratic x² - 5x + 6 = 0:")
if roots["type"] == "two":
    print(f"  Roots: {roots['root1']}, {roots['root2']}")  # Output - 3, 2

# Case Study 14: Calculate Velocity and Acceleration
def calculate_motion(initial_velocity, acceleration, time):
    """v = u + at, s = ut + (1/2)at²"""
    final_velocity = initial_velocity + acceleration * time
    distance = initial_velocity * time + 0.5 * acceleration * time ** 2
    return {"velocity": final_velocity, "distance": distance}

motion = calculate_motion(0, 10, 5)
print(f"\nMotion with u=0, a=10 m/s², t=5s:")
print(f"  Final velocity: {motion['velocity']} m/s")
print(f"  Distance: {motion['distance']} m")

# Case Study 15: Calculate Power and Energy
def calculate_power(work, time):
    """Power = Work / Time"""
    return work / time

def calculate_kinetic_energy(mass, velocity):
    """KE = (1/2)mv²"""
    return 0.5 * mass * velocity ** 2

power = calculate_power(100, 5)
ke = calculate_kinetic_energy(10, 20)
print(f"\nPower (100J in 5s): {power} W")
print(f"Kinetic Energy (m=10kg, v=20 m/s): {ke} J")

# Case Study 16: Fibonacci with Math Functions
def fibonacci_with_formula(n):
    """Calculate nth Fibonacci number using Binet's formula"""
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi**n - psi**n) / math.sqrt(5))

fib = fibonacci_with_formula(10)
print(f"\n10th Fibonacci number (using formula): {fib}")  # Output - 55

# Case Study 17: Calculate Resonant Frequency
def resonant_frequency(inductance, capacitance):
    """f = 1 / (2π√(LC))"""
    return 1 / (2 * math.pi * math.sqrt(inductance * capacitance))

freq = resonant_frequency(1, 1)
print(f"\nResonant frequency (L=1H, C=1F): {freq:.4f} Hz")

# Case Study 18: Calculate Mortgage Payment
def mortgage_payment(principal, annual_rate, years):
    """Calculate monthly mortgage payment"""
    monthly_rate = annual_rate / (12 * 100)
    num_payments = years * 12
    
    if monthly_rate == 0:
        payment = principal / num_payments
    else:
        payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
                  ((1 + monthly_rate)**num_payments - 1)
    
    total_paid = payment * num_payments
    total_interest = total_paid - principal
    
    return {
        "monthly_payment": payment,
        "total_paid": total_paid,
        "total_interest": total_interest
    }

mortgage = mortgage_payment(300000, 6, 30)
print(f"\nMortgage ($300k, 6%, 30 years):")
print(f"  Monthly: ${mortgage['monthly_payment']:.2f}")
print(f"  Total: ${mortgage['total_paid']:.2f}")

# Case Study 19: Calculate Pressure (Physics)
def calculate_pressure(force, area):
    """Pressure = Force / Area"""
    return force / area

pressure = calculate_pressure(100, 5)
print(f"\nPressure (100N on 5m²): {pressure} Pa")

# Case Study 20: Calculate Gravitational Force
def gravitational_force(mass1, mass2, distance):
    """F = G(m1*m2)/r²"""
    G = 6.674e-11  # Gravitational constant
    return G * (mass1 * mass2) / (distance ** 2)

force = gravitational_force(1e24, 1e24, 1e11)
print(f"\nGravitational force: {force:.2e} N")

# Case Study 21: Calculate Mean, Median, Mode
def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    return {"mean": mean, "median": median}

nums = [1, 2, 2, 3, 4, 5, 5, 5, 6]
stats = calculate_statistics(nums)
print(f"\nStatistics for {nums}:")
print(f"  Mean: {stats['mean']:.2f}")
print(f"  Median: {stats['median']:.2f}")

# Case Study 22: Calculate Angle Between Vectors
def angle_between_vectors(v1, v2):
    """Calculate angle between two 2D vectors"""
    dot_product = v1[0]*v2[0] + v1[1]*v2[1]
    mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cos_angle = dot_product / (mag1 * mag2)
    return math.degrees(math.acos(cos_angle))

v1 = (1, 0)
v2 = (0, 1)
angle = angle_between_vectors(v1, v2)
print(f"\nAngle between vectors (1,0) and (0,1): {angle:.1f}°")  # Output - 90°

# Case Study 23: Check Perfect Square
def is_perfect_square(n):
    sqrt_n = math.sqrt(n)
    return sqrt_n == int(sqrt_n)

print(f"\nIs 16 a perfect square? {is_perfect_square(16)}")  # Output - True
print(f"Is 17 a perfect square? {is_perfect_square(17)}")  # Output - False

# Case Study 24: Calculate Capacity (Geometry)
def cylinder_volume(radius, height):
    """V = πr²h"""
    return math.pi * radius ** 2 * height

def sphere_volume(radius):
    """V = (4/3)πr³"""
    return (4/3) * math.pi * radius ** 3

cyl_vol = cylinder_volume(5, 10)
sphere_vol = sphere_volume(5)
print(f"\nCylinder (r=5, h=10) volume: {cyl_vol:.2f}")
print(f"Sphere (r=5) volume: {sphere_vol:.2f}")

# Case Study 25: Simple Interest
def simple_interest(principal, rate, time):
    """SI = (P * R * T) / 100"""
    return (principal * rate * time) / 100

si = simple_interest(1000, 5, 2)
print(f"\nSimple Interest ($1000, 5%, 2 years): ${si:.2f}")
