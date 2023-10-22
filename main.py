nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

zipped = zip(nums1, nums2)
print(zipped)  # <zip object at 0xffffb4810ec0>

zipped = zip(nums1, nums2)
print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]

zipped = zip(nums1, nums2)
print(dict(zipped))  # {1: 4, 2: 5, 3: 6}
