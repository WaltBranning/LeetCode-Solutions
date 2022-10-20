def intToRoman(int_number):
    numerals_map = {10000:{1000: 'M'}, 1000: {900: 'CM', 500: 'D', 400: 'CD', 100: 'C'}, 100: {90: 'XC', 
                    50: 'L', 40: 'XL', 10: 'X'}, 10: {9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}}

    def get_pos_vals(number):
        place_value = []
        for position in [10, 100, 1000, 10000]:
            if number == 0:
                break
            deci_place_value = number % position
            number -= deci_place_value
            place_value.append((position, deci_place_value))
        return place_value
    
    def get_numeral(vals):
        numeral = ""
        for val in vals:
            for rom_val in numerals_map[val[0]]:

                if val[1] == 0:
                    pass

                elif val[1] == rom_val:
                    numeral = numerals_map[val[0]][val[1]] + numeral
                    break

                elif val[1]/val[0]*10 > 5:
                    iter_num = numerals_map[val[0]][int(val[0] / 10 * 5)]
                    for i in range(int(val[1]/val[0]*10) % 5):
                        iter_num += numerals_map[val[0]][int(1 * val[0] /10)]
                    numeral = iter_num + numeral
                    break
                elif val[1]/val[0]*10 < 4:
                    iter_num = ""
                    for i in range(int(val[1]/val[0]*10)):
                        iter_num += numerals_map[val[0]][int(1 * val[0] /10)]
                    numeral = iter_num + numeral
                    break
        return numeral
    
    pos_vals = get_pos_vals(int_number)
    numeral = get_numeral(pos_vals)

    return numeral
