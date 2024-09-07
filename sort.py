def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    
    # Determine if the package is bulky or heavy
    bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])
    heavy = mass >= 20
    
    # Sort the package according to the criteria
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(100, 50, 20, 15))  # Expected: STANDARD
print(sort(200, 50, 20, 10))  # Expected: SPECIAL (bulky)
print(sort(100, 50, 20, 25))  # Expected: SPECIAL (heavy)
print(sort(200, 50, 20, 25))  # Expected: REJECTED (bulky and heavy)
