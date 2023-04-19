# Fraction Datatype

The Fraction datatype is a Python class that represents a fraction with a numerator and denominator. It supports the following operations:

Simplify a fraction
Print a fraction
Add two fractions
Subtract two fractions
Multiply two fractions
Divide two fractions
Check if two fractions are equal
Check if one fraction is less than another
Check if one fraction is greater than another
Check if one fraction is less than or equal to another
Check if one fraction is greater than or equal to another
Convert a fraction to a float
Convert a fraction to an integer
Get the absolute value of a fraction
Invert the numerator and denominator of a fraction
Round off a fraction to a specified number of decimal places


## Getting Started
To use the Fraction datatype in your Python program, you first need to create an instance of the Fraction class with a numerator and denominator value:

```
from Fraction_class import Fraction
my_fraction = Fraction(3, 4)
```

## Operations

### Simplify a fraction
To simplify a fraction, call the simplify method on a Fraction object:

```
my_fraction.simplify()
This will simplify the fraction to its lowest terms.
```

### Print a fraction
To print a fraction, simply call the print function on a Fraction object:

```
print(my_fraction)
```
This will print the fraction in the form "numerator/denominator".

### Add two fractions
To add two fractions, use the + operator:

```
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 3)
result = fraction1 + fraction2
```
This will add the two fractions and store the result in result.

### Subtract two fractions
To subtract two fractions, use the - operator:

```
fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 2)
result = fraction1 - fraction2
```
This will subtract the second fraction from the first and store the result in result.

### Multiply two fractions
To multiply two fractions, use the * operator:

```
fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 2)
result = fraction1 * fraction2
```
This will multiply the two fractions and store the result in result.

### Divide two fractions
To divide two fractions, use the / operator:

```
fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 2)
result = fraction1 / fraction2
```
This will divide the first fraction by the second and store the result in result.

### Check if two fractions are equal
To check if two fractions are equal, use the == operator:

```
fraction1 = Fraction(3, 4)
fraction2 = Fraction(6, 8)
if fraction1 == fraction2:
    print("Fractions are equal")
```
This will check if the two fractions are equal and print a message if they are.

### Check if one fraction is less than / greater than/ less than equal to/ greater than equal to another
To check if one fraction is less than another, use the < operator:

```
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
if fraction1 < fraction2:
    print("Fraction 1 is less than Fraction 2")
```
This will check if the first fraction is less than the second and print a message if it is.

###



