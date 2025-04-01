"""
------
Medium
------

1079. Letter Tile Possibilities

You have n tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
"""


from itertools import permutations


def num_tile_possibilities(tiles: str) -> int:
    possibilities = 0

    for i in range(len(tiles)):
        possibilities += len(set(permutations(tiles, i + 1)))

    return possibilities
