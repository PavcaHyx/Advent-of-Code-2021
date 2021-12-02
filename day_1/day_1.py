def get_all_measurements():
    f = open("input_day_1.txt", "r")
    list_of_measurements = f.read().split('\n')
    return list_of_measurements


def get_count_of_increased_sequent(measurements) -> int:
    """
        Count how many sequent increases are in a list of measurements
        Args:
            measurements (List[int]): list of measurements
        Returns:
            int: number of sequent increases
    """

    if len(measurements) < 2:
        raise ValueError("List contains less than 2 values to compare")
    count_of_increased_sequent = 0

    for i in range(len(measurements)-1):
        if int(measurements[i+1]) > int(measurements[i]):
            count_of_increased_sequent += 1
    return count_of_increased_sequent


def get_count_of_increased_triplets(measurements) -> int:
    """
        Count how many sequent increases are between triplets.
        Compare a sum of each triplet to determine increase / decrease.
        Triples are made as follow:
            199  A
            200  A B
            208  A B C
            210    B C D
            200  E   C D
            207  E F   D
            240  E F G
            269    F G H
            260      G H
            263        H
        Args:
            measurements (List[int]): list of measurements
        Returns:
            int: number of sequent increases between triplets
    """
    if len(measurements) < 6:
        raise ValueError("List contains less than 6 values to compare")

    count_of_increased_triplets = 0

    list_of_sum_of_three_items = []
    for i in range(len(measurements)-2):
        sum_of_three_items = (int(measurements[i]) + int(measurements[i+1]) + int(measurements[i+2]))
        list_of_sum_of_three_items.append(sum_of_three_items)

    for i in range(len(list_of_sum_of_three_items) - 1):
        if int(list_of_sum_of_three_items[i + 1]) > int(list_of_sum_of_three_items[i]):
            count_of_increased_triplets += 1
    return count_of_increased_triplets


if __name__ == '__main__':
    # part_1
    print(get_count_of_increased_sequent(get_all_measurements()))
    # part_2
    print(get_count_of_increased_triplets(get_all_measurements()))
