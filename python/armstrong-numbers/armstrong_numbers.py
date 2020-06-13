def is_armstrong_number(number):
    number_chars = list(str(number))
    number_len = len(number_chars)
    sum_of_char_powers = sum(int(n) ** number_len for n in number_chars)

    return sum_of_char_powers == number
