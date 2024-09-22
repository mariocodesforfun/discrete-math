
# 25  test cases for the is_multiple_of_3 function
IS_MULTIPLE_OF_3_TEST_CASES = [
    # Case 1: Both p and q are multiples of 3
    (3, 6, True),
    
    # Case 2: p is a multiple of 3 but q is not
    (3, 4, True),
    
    # Case 3: q is a multiple of 3 but p is not
    (5, 9, True),
    
    # Case 4: Neither p nor q is a multiple of 3, but pq is not a multiple of 3
    (2, 5, False),
    
    # Case 5: p is not a multiple of 3, q is a multiple of 3, and pq is a multiple of 3
    (2, 9, True),
    
    # Case 6: p is a multiple of 3, q is a multiple of 3, and pq is a multiple of 3
    (9, 6, True),
    
    # Case 7: Both p and q are not multiples of 3 and pq is not a multiple of 3
    (4, 8, False),
    
    # Case 8: p is not a multiple of 3 and q is a multiple of 3
    (7, 3, True),
    
    # Case 9: q is a large multiple of 3, p is not a multiple of 3
    (2, 300, True),
    
    # Case 10: p is a large multiple of 3, q is not a multiple of 3
    (15, 7, True),
    
    # Case 11: Neither p nor q are multiples of 3, and pq is not a multiple of 3
    (1, 2, False),
    
    # Case 12: p is not a multiple of 3, q is not a multiple of 3, but pq is a multiple of 3
    (2, 3, True),
    
    # Case 13: Both p and q are multiples of 3, small values
    (3, 3, True),
    
    # Case 14: p is zero (multiples of 3 include 0)
    (0, 10, True),
    
    # Case 15: q is zero (multiples of 3 include 0)
    (15, 0, True),
    
    # Case 16: Both p and q are zero
    (0, 0, True),
    
    # Case 17: Negative p is multiple of 3, q is not
    (-3, 5, True),
    
    # Case 18: Negative q is multiple of 3, p is not
    (7, -6, True),
    
    # Case 19: Neither p nor q are multiples of 3, both negative
    (-4, -7, False),
    
    # Case 20: p is negative and not a multiple of 3, q is positive and a multiple of 3
    (-2, 6, True),
    
    # Case 21: Large multiples of 3 for both p and q
    (300, 900, True),
    
    # Case 22: Neither p nor q are multiples of 3, large numbers
    (1001, 5002, False),
    
    # Case 23: Negative p is a multiple of 3, q is also a multiple of 3
    (-9, 12, True),
    
    # Case 24: Both p and q are multiples of 3 and pq is a multiple of 3
    (18, 9, True),
    
    # Case 25: Random case where p*q is not a multiple of 3, and neither p nor q are multiples of 3
    (7, 11, False)
]