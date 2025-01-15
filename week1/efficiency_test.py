"""
TASK

Compare the efficiencies of the two implementations given below, using a list that contains 10^7 randomly chosen numbers.

"""

# implementation 1
def count_even_imp1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result


# implementation 2
def count_even_imp2(numbers):
    return sum(x % 2 == 0 for x in numbers)


# efficiency test
import math, random, time

sample_set = list(range(int(math.pow(10, 8))))
random.seed(42)
random_samples = random.sample(sample_set, int(math.pow(10, 7)))

print(count_even_imp1(random_samples))
print('Implementation 1 (elaborate) :', time.perf_counter())
print(count_even_imp2(random_samples))
print('Implementation 2 (list comprehension) :', time.perf_counter()) 


# --- To Remember ---
# ll = list(range(10))
# print(random.sample(ll, 10))  # sampling WITHOUT substitution/replacement
# # [6, 9, 0, 2, 4, 3, 5, 1, 8, 7]

# print(random.choices(ll, k=10))  # sampling WITH substitution/replacement
# # [5, 9, 5, 2, 7, 6, 2, 9, 9, 8]
