from typing import Set, Tuple, List



# Debugging Exercise
# def id_to_fruit(fruit_id: int, fruits: Set[str]) -> str:
#     idx = 0
#     for fruit in fruits:
#         if fruit_id == idx:
#             return fruit
#         idx += 1
#     raise RuntimeError(f"Fruit with id {fruit_id} does not exist")




# Debugging Solution
def id_to_fruit(fruit_id: int, fruits: List[str]) -> str:

    if fruit_id < 0 or fruit_id >= len(fruits):
        raise IndexError(f"Fruit with id {fruit_id} does not exist")

    return fruits[fruit_id]




# Example usage
fruits = ["apple", "orange", "melon", "kiwi", "strawberry"]
print(id_to_fruit(1, fruits)) #>>> orange