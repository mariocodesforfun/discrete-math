from constants import IS_MULTIPLE_OF_3_TEST_CASES

#if pq is not a multiple of 3,then p is not a multiple of 3 and q is not a multiple of 3.
def is_pq_multiple_of_3(p: int, q: int) -> bool:
    if p*q % 3 != 0:
        if p % 3 != 0 and q % 3 != 0:
            return False
    return True

# contrapositive of above statement
# if p is a multiple of 3 or q is a multiple of 3, then pq is a multiple of 3
# DE Morgan's law
def is_pq_multiple_of_3_contrapositive(p: int, q: int) -> bool:
    if p % 3 == 0 or q % 3 == 0:
        if p*q % 3 == 0:
            return True 
    return False 

# test given statments
def test_is_pq_multiple_of_3() -> list:
    final_result = []
    for p, q, expected in IS_MULTIPLE_OF_3_TEST_CASES:
        result = is_pq_multiple_of_3(p, q)
        
        # append x or print x to see the results
        # x = f"p = {p}, q = {q}, expected = {expected}, result = {result}, passed = {result == expected}"
        
        final_result.append(result)
    
    return final_result

# test contrapositive - result should be same as above
def test_is_pq_multiple_of_3_contrapositive():
    final_result = []
    for p, q, expected in IS_MULTIPLE_OF_3_TEST_CASES:
        result = is_pq_multiple_of_3_contrapositive(p, q)
        
        # append x or print x to see the results
        # x = f"p = {p}, q = {q}, expected = {expected}, result = {result}, passed = {result == expected}"
        
        final_result.append(result)

    return final_result


def are_results_same() -> bool:
    result1 = test_is_pq_multiple_of_3()
    result2 = test_is_pq_multiple_of_3_contrapositive()
    return result1 == result2

print(are_results_same())

