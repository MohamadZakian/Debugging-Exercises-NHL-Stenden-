import numpy as np

# Debugging Exercise
# def swap(coords: np.ndarray):
    
#     coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
    
#     return coords




# Debugging Solution
def swap(coords: np.ndarray) -> np.ndarray:
    swapped = coords.copy()

    swapped[:, 0] = coords[:, 1]
    swapped[:, 1] = coords[:, 0]
    swapped[:, 2] = coords[:, 3]
    swapped[:, 3] = coords[:, 2]

    return swapped



# Example usage
coords = np.array([[0, 1, 2, 3],[1, 0, 3, 2]])

print(swap(coords))  #[[1 0 3 2],[0 1 2 3]]