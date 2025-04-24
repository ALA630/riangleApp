def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: Sides must be greater than 0."
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle: The sum of any two sides must be greater than the third."
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

def main():
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        result = classify_triangle(a, b, c)
        print("Triangle Type:", result)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
