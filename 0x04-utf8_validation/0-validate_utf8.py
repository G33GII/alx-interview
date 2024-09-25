#!/usr/bin/python3
"""Function to check if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Checks if the provided data list
    contains a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers
        where each integer represents a byte.

    Returns:
        bool: True if the data is a valid UTF-8
        encoding, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant
    # bit (8th bit from the left) is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits of the number
        byte = num & 0xFF

        # If it's the start of a new UTF-8 character
        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            mask = mask1
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False

            # Account for the first byte
            n_bytes -= 1
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

            n_bytes -= 1

    # Check if all characters were complete
    return n_bytes == 0
