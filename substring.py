def get_substring(s):
    n = len(s)
    substring = []
    for i in range(1 << n):
        current_substring = ""
        for j in range(n):
            if (i & (1 << j)):
                current_substring += s[j]
        if current_substring:
            substring.append(current_substring)
    return substring

input_string = "abc"
result = get_substring(input_string)
print(f"Original string = {input_string}")
print(f"All substring = {result}")

input_string2 = "apple"
result2 = get_substring(input_string2)
print(f"Orginal string = {input_string2}")
print(f"All substring = {result2[:10]}")