# My Project

This project contains a Python module that provides a function to determine if all boxes can be unlocked.

## Files

- `my_module.py`: Contains the implementation of the `canUnlockAll` function.
- `README.md`: Project documentation.

## Usage

To use the `canUnlockAll` function, import it from `my_module` and pass a list of lists as the argument. The function returns `True` if all boxes can be unlocked, otherwise it returns `False`.

Example:
```python
from my_module import canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Should print True

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # Should print False
