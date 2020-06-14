def is_valid(isbn):
    # Removing hypens from isbn string
    isbn_no_hypens = isbn.replace("-", "")

    # Valid isbn is always 10 characters long, so returning False if this
    # condition isn't meet
    if len(isbn_no_hypens) != 10:
        return False

    # Replacing check digit to "10" if it's equal "X" (case insensitive)
    isbn_no_check, check_digit = isbn_no_hypens[:-1], isbn_no_hypens[-1]
    isbn_processed_check = [
        *isbn_no_check, "10" if check_digit.upper() == "X" else check_digit]

    # If there are still no digit characters it means it's not valid isbn,
    # so returning False
    if not all(char.isdigit() for char in isbn_processed_check):
        return False

    # Checksum calculation
    checksum = sum(int(n) * (10 - index)
                   for index, n in enumerate(isbn_processed_check))

    return checksum % 11 == 0
