# Q1. Find the Frequency of Each Word
def find_word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


# Q2. Find the Frequency of Each Character in a Word
def find_character_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

    return frequency


# Q3. Find the First Non-Repeating Character in a Word
def find_first_non_repeating_character(word):
    for char in word:
        if word.count(char) == 1:
            return char

    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


# Q5. Find the First Repeating Character in a String
def find_first_repeating_character(word):
    seen = set()

    for char in word:
        if char in seen:
            return char
        seen.add(char)

    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    result = []
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count = zero_count + 1
        else:
            result.append(num)

    for i in range(zero_count):
        result.append(0)

    return result


# Q7. Find the Second Highest Distinct Number in a List
def find_second_highest(nums):
    largest = None
    second_largest = None

    for num in nums:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    return second_largest


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    total = n * (n + 1) // 2
    current_sum = 0

    for num in nums:
        current_sum = current_sum + num

    return total - current_sum


# Q10. Find the First Pair Whose Sum Equals a Target
def find_first_pair(nums, target):
    # Check the second element from left to right first.
    for j in range(1, len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []


# Q11. Find the Number Closest to Zero
def find_closest_to_zero(nums):
    if len(nums) == 0:
        return None

    closest = nums[0]

    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num

    return closest


# Q12. Find Common Elements Between Two Lists
def find_common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if len(nums) == 0:
        return []

    k = k % len(nums)
    return nums[len(nums) - k:] + nums[:len(nums) - k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def maximum_consecutive_sum(nums):
    maximum = nums[0] + nums[1]

    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > maximum:
            maximum = current_sum

    return maximum


# Q15. Find All Pairs Whose Sum Equals a Target
def find_all_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = [nums[i], nums[j]]
                pair.sort()

                if pair not in result:
                    result.append(pair)

    result.sort()
    return result


