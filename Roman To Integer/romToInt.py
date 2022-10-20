def romanToInt(numeral_number):
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals_map = dict(zip(numerals, values))
    num_split = []

    loop_count = 0
    fall_back_count = 0
    while len(numerals) >= loop_count or fall_back_count >= 200:
        idx = numeral_number.find(numerals[loop_count])
        if idx == 0:
            rm_idx = len(numerals[loop_count])
            num_split.append(numeral_number[: rm_idx])
            numeral_number = numeral_number[rm_idx :]     
            if len(numeral_number) == 0: loop_count = len(numerals) + 1            
        elif idx == -1 or idx >= 1:
            loop_count += 1
        fall_back_count += 1   
    return(sum(numerals_map[num] for num in num_split))
