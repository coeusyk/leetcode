"""
[2570] Merge Two 2D Arrays by Summing Values

--- **Easy** ---

You are given two 2D integer arrays nums1 and nums2.

- nums1[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.
- nums2[i] = [id_i, val_i] indicate that the number with the id id_i has a value equal to val_i.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

- Only ids that appear in at least one of the two arrays should be included in the resulting array.
- Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.
"""


def mergeArrays(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    ids = [i for i, _ in nums1]
    index_pointer = 0

    nums2_index = 0

    while nums2_index < len(nums2):
        nums2_elem = nums2[nums2_index]

        if nums2_elem[0] == ids[index_pointer]:
            nums1[index_pointer][1] += nums2_elem[1]
            nums2_index += 1
            index_pointer += 1

        elif (nums2_elem[0] > ids[index_pointer - 1]) and (nums2_elem[0] < ids[index_pointer]):
            nums1.insert(index_pointer, nums2_elem)
            ids.insert(index_pointer, nums2_elem[0])
            nums2_index += 1

        else:
            index_pointer += 1

        if index_pointer == len(ids):
            nums1.extend(nums2[nums2_index:])

    return nums1


print(mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
