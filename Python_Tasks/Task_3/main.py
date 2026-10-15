from solutions import (
    find_word_frequency,
    find_character_frequency,
    find_first_non_repeating_character,
    are_anagrams,
    find_first_repeating_character,
    move_zeros_to_end,
    find_second_highest,
    remove_duplicates,
    find_missing_number,
    find_first_pair,
    find_closest_to_zero,
    find_common_elements,
    rotate_right,
    maximum_consecutive_sum,
    find_all_pairs
)

# Q1. Find the Frequency of Each Word
print("Q1:", find_word_frequency("Python makes coding easy Python"))
print("Q1 additional Input:", find_word_frequency("Hello hello world"))

# Q2. Find the Frequency of Each Character in a Word
print("Q2:", find_character_frequency("banana"))
print("Q2 additional Input:", find_character_frequency("apple"))

# Q3. Find the First Non-Repeating Character in a Word
print("Q3:", find_first_non_repeating_character("swiss"))
print("Q3 additional Input:", find_first_non_repeating_character("aabb"))

# Q4. Check Whether Two Strings Are Anagrams
print("Q4:", are_anagrams("listen", "silent"))
print("Q4 additional Input:", are_anagrams("hello", "world"))

# Q5. Find the First Repeating Character in a String
print("Q5:", find_first_repeating_character("programming"))
print("Q5 additional Input:", find_first_repeating_character("python"))

# Q6. Move All Zeros to the End of a List
print("Q6:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 additional Input:", move_zeros_to_end([0, 0, 5, 2]))

# Q7. Find the Second Highest Distinct Number in a List
print("Q7:", find_second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 additional Input:", find_second_highest([8, 8, 5]))

# Q8. Remove Duplicates Without Changing the Original Order
print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 additional Input:", remove_duplicates([1, 1, 2, 3, 2]))

# Q9. Find the Missing Number from 1 to N
print("Q9:", find_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 additional Input:", find_missing_number([1, 3, 4], 4))

# Q10. Find the First Pair Whose Sum Equals a Target
print("Q10:", find_first_pair([2, 7, 11, 15], 9))
print("Q10 additional Input:", find_first_pair([1, 4, 2, 3], 5))

# Q11. Find the Number Closest to Zero
print("Q11:", find_closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 additional Input:", find_closest_to_zero([-4, 3, -1]))

# Q12. Find Common Elements Between Two Lists
print("Q12:", find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 additional Input:", find_common_elements([4, 4, 2, 1], [2, 4]))

# Q13. Rotate a List to the Right by K Positions
print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 additionalInput:", rotate_right([10, 20, 30], 1))

# Q14. Find the Maximum Sum of Two Consecutive Elements
print("Q14:", maximum_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 additionalInput:", maximum_consecutive_sum([-5, -2, -8]))

# Q15. Find All Pairs Whose Sum Equals a Target 
print("Q15:", find_all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 additional Input:", find_all_pairs([1, 2, 3, 4], 5))
