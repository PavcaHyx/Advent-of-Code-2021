from typing import Dict, Tuple


def get_all_binary_codes():
    f = open("input_day_3.txt", "r")
    list_of_binary_codes = f.read().split('\n')
    return list_of_binary_codes


def get_sum_on_specific_positions(codes) -> Dict[int, int]:
    """
       For each position in list of binary codes count sum of numbers on the specific position.
       Result saved into dictionary.
       Eg. [111, 011, 110 ] -> {0: 2,  1: 3, 2: 2}
       Args:
           codes: list of codes in binary format
       Returns:
           Dict[int, int]: keys are numbered positions,
           values are sums of zeros and ones on the specific position
    """
    dict_of_sums_on_specific_positions = {}
    length_of_one_code = len(codes[0])
    for code in codes:
        for i in range(length_of_one_code):
            dict_of_sums_on_specific_positions[i] = dict_of_sums_on_specific_positions.get(i, 0) + int(code[i])
    return dict_of_sums_on_specific_positions


def get_gamma_and_epsilon_rate(dict_of_sums_on_specific_positions) -> Tuple:
    """
        Gamma rate is calculated from most common digit (0 or 1) in each position
        Epsilon rate is opposite number to gamma rate
        (eg. gama rate is '010' then epsilon rate is '101')
        Args:
            dict_of_sums_on_specific_positions (dict): dictionary, sum digits(0 or 1) on specific positions
        Returns:
            Tuple: gamma and epsilon rate
    """

    count_of_codes = len(get_all_binary_codes())
    game_rate = ''
    epsilon_rate = ''
    for value in dict_of_sums_on_specific_positions.values():
        if value > (count_of_codes / 2):
            game_rate += '1'
            epsilon_rate += '0'
        else:
            game_rate += '0'
            epsilon_rate += '1'

    return int(game_rate, 2), int(epsilon_rate, 2)


def filter_list(codes, dict_of_sums_on_specific_positions, criteria) -> str:
    """
        Find 'most' or 'least' common value ('0' or '1') in the current position,
        and keep in a list only those codes with specific number in specific position.
        Args:
            codes (list): list of codes in binary format
            dict_of_sums_on_specific_positions (dict): dictionary, sum of numbers at
                                            position in list of binary codes
            criteria (str): criteria for comparison (values 'most' or 'least')
        Returns:
            str: resulting binary code
    """
    kept_codes = codes[::]
    i = 0
    while len(kept_codes) > 1:
        new_kept_codes = []

        count_of_codes = len(kept_codes)
        count_of_1 = dict_of_sums_on_specific_positions[i]
        count_of_0 = count_of_codes - dict_of_sums_on_specific_positions[i]
        number_to_keep = find_number_to_keep(count_of_0, count_of_1, criteria)

        for code in kept_codes:
            if code[i] == number_to_keep:
                new_kept_codes.append(code)

        kept_codes = new_kept_codes
        dict_of_sums_on_specific_positions = get_sum_on_specific_positions(kept_codes)
        i += 1
    return kept_codes[0]


def find_number_to_keep(count_of_0, count_of_1, criteria) -> str:
    """
       Compare numbers according to a criteria ('most' or 'least').
       Criteria 'most' returns the number of which count is bigger.
       Criteria 'least' returns the number of which count is lesser.
       When counts are equal, criteria 'most' returns '1', and 'least' returns '0'
       Args:
           count_of_0 (int): count of numbers '0'
           count_of_1 (int): count of numbers '1'
           criteria (str): criteria for comparison
       Returns:
           str: resulting number (values '0' or '1')
    """
    if criteria == 'most':
        if count_of_0 == count_of_1:
            return '1'
        else:
            return '0' if count_of_0 > count_of_1 else '1'
    else:
        if count_of_0 == count_of_1:
            return '0'
        else:
            return '0' if count_of_0 < count_of_1 else '1'


if __name__ == '__main__':
    # part_1
    list_of_binary_codes = get_all_binary_codes()
    dict_of_sums_on_specific_positions = get_sum_on_specific_positions(list_of_binary_codes)
    result_part_1 = get_gamma_and_epsilon_rate(dict_of_sums_on_specific_positions)
    print(f"Power consumption of the submarine is {result_part_1[0]}*{result_part_1[1]}= {result_part_1[0] * result_part_1[1]}")

    # part_2
    list_of_binary_codes = get_all_binary_codes()
    dict_of_sums_on_specific_positions = get_sum_on_specific_positions(list_of_binary_codes)
    O2_rating = (int(filter_list(list_of_binary_codes, dict_of_sums_on_specific_positions, 'most'), 2))
    CO2_rating = (int(filter_list(list_of_binary_codes, dict_of_sums_on_specific_positions, 'least'), 2))
    result_part_2 = O2_rating * CO2_rating
    print(f"Life support rating is {O2_rating}*{CO2_rating}= {result_part_2}")

