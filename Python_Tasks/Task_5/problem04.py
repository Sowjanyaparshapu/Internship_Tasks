# Finding frequency of substring in main string
# problem link - https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    freq_count = 0
    for i in range(len(string) - len(sub_string) + 1):
        pair = string[i:i + len(sub_string)]
        if pair == sub_string:
            freq_count = freq_count + 1
    return freq_count
        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
