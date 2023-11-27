from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def valid_prefix(prefix):
    return prefix in ['0414', '0424', '0416', '0426', '0412']


def valid_vector(v):
    v_str = ''.join(map(str, v))

    if not valid_prefix(v_str[:4]):
        return False

    if '88' not in v_str:
        return False

    if v_str.count('9') == 2 and (
            v_str.index('9') + 2 != v_str.rindex('9') or v_str[v_str.index('9') + 1] == v_str[v_str.index('9') + 2]):
        return False

    if v_str.count('3') == 2 and v_str[v_str.index('3') - 1] != v_str[v_str.rindex('3') + 1]:
        return False

    if int(v_str[-2]) % int(v_str[-1]) != 0:
        return False

    if not is_prime(int(v_str[-1])):
        return False

    return True


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