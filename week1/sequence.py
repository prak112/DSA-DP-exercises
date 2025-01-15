"""
TASK

Each element in a sequence of numbers is the smallest positive integer that does not occur earlier in the sequence and that has the same digit in the beginning and in the end.

The sequence begins as follows:
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ...

Your task is to compute the number at the position n in the sequence. You may assume that n is at most 1000.

"""

def generate(n):
  # Option 1 - build logic to deduce the requested nth number in sequence to improve performance time
  # N ranges from 1-9
  # (1 digit) 'N', = 9 
  # (2 digit) 'N N' = 9
  # (3 digit) 'N x1 N', where x1 ranges from 0-9 = 9 * 9 = 81
  # (4 digit) 'N x1 x2 N', where x1 x2 range from 00-99 = 9 * 99 = 891
  # (5-digit) 'N x1 x2 x3 N', where x1 x2 x3 range from 000-999 = 9 * 999 = 8991

  # match n:
  #   case num if 0 < num < 10: # 1-digit
  #     return num
  #   case num if 10 <= num < 19: # 2-digit
  #     return ((num % 10) + 1) * 11
  #   case num if 19 <= num < 100: # 3-digit
  #     rem = ((num % 10 ) + 1) % 10
  #     div = (num // 10) - 1
  #     nth_seq = f"{div}{rem}{div}" 
  #     return int(nth_seq)
  #   case num if 100 <= num < 991: # 4-digit
  #     div = (num // 10) // 10
  #     nth_seq = f"{num}{div}"
  #     return int(nth_seq)


  # Winner - 
  # Option 2 - total sequence <= 1000, so performance time not so affected in generating sequence list
  # generates a sequence list by given condition, first digit == last digit 
  # an initialized integer is incremented in loop until 
    # len(sequence list) < nth number
    # given condition is met to acquire nth number

  # sequence = []
  # num = 1

  # while len(sequence) < n:
  #     str_num = str(num)
  #     if str_num[0] == str_num[-1]:
  #         sequence.append(num)
  #     num += 1
  # return sequence[n-1]


  # Optimal solution
  count = 0
  nth_val = 0  

  while count < n:
    nth_val += 1
    if str(nth_val)[0] == str(nth_val)[-1]:
      count += 1
  return nth_val


if __name__ == "__main__":
  print(generate(1)) # 1
  print(generate(2)) # 2
  print(generate(3)) # 3
  print(generate(10)) # 11
  print(generate(34)) # 252
  print(generate(123)) # 1141


  # --- To Remember ---
  # match-case syntax for strings
  # match-case syntax for numericals