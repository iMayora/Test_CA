from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def have_common_divisor(a, b, c):
    for i in range(2, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            return True
    return False

def valid_prefix(prefix):
    return prefix in ['0414', '0424', '0416', '0426', '0412']

def valid_vector(v):
    v_str = ''.join(map(str, v))

    if not valid_prefix(v_str[:4]):
        return False

    if '88' not in v_str:
        return False

    if v_str.count('9') == 2 and (v_str.index('9') + 2 != v_str.rindex('9') or v_str[v_str.index('9') + 1] == v_str[v_str.index('9') + 2]):
        return False

    if v_str.count('3') == 2 and v_str[v_str.index('3') - 1] != v_str[v_str.rindex('3') + 1]:
        return False

    if not have_common_divisor(int(v_str[4]), int(v_str[5]), int(v_str[6])):
        return False

    # Check to prevent ZeroDivisionError
    if int(v_str[-1]) != 0 and int(v_str[-2]) % int(v_str[-1]) != 0:
        return False

    if not is_prime(int(v_str[-1])):
        return False

    if v_str.count('9') == 2:
        index_first_9 = v_str.index('9')
        index_second_9 = v_str.rindex('9')
        separator = v_str[index_first_9 + 1]

        if v_str.count(separator) > 1 or separator == v_str[index_first_9 + 2]:
            return False

    for i in range(1, len(v_str) - 1):
        if v_str[i] == '3':
            if v_str[i - 1] != v_str[i + 1]:
                return False

    return True

def find_combinations(v):
    for perm in permutations(v):
        if valid_vector(perm):
            return perm
    return None


def find_combinations(v):
    """Find valid combinations of the vector."""
    for perm in permutations(v):
        if valid_vector(perm):
            return perm
    return None


# Initial vector
vector = []

# Find valid combinations
valid_combination = find_combinations(vector)
print("Valid Combination:", valid_combination)
