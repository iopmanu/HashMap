from typing import Any

class DynamicArray:
    
    def __init__(self, arr=None) -> None:
        self._data = arr.deepcopy() if arr else []

    def __str__(self) -> str:
        return str(self._data)

    def append(self, value: Any) -> None:
        self._data.append(value)

    def pop(self) -> Any:
        return self._data.pop()
    
    def swap(self, i: int, j: int) -> None:
        if i >= len(self) or i < 0:
            raise IndexError("It's impossible to get element with index >= size")

        if j >= len(self) or j < 0:
            raise IndexError("It's impossible to get element with index >= size")

        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def __getitem__(self, index: int) -> Any:
        if index >= len(self) or index < 0:
            raise IndexError("It's impossible to get element with index >= size")
        return self._data[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if index >= len(self) or index < 0:
            raise IndexError("It's impossible to set element with index >= size")
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)