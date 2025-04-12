def add_fractions(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * denominator2 + numerator2 * denominator1
    denominator = denominator1 * denominator2
    return numerator, denominator

def subtract_fractions(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * denominator2 - numerator2 * denominator1
    denominator = denominator1 * denominator2
    return numerator, denominator

def multiply_fractions(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    return numerator, denominator

def divide_fractions(numerator1, denominator1, numerator2, denominator2):
    numerator = numerator1 * denominator2
    denominator = denominator1 * numerator2
    return numerator, denominator