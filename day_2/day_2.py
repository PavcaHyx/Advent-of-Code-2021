def get_all_directions():
    f = open("input_day_2.txt", "r")
    list_of_directions = f.read().split('\n')
    list_of_directions_separated = [line.split() for line in list_of_directions]
    return list_of_directions_separated


def get_my_position(directions) -> list[int]:
    """
       Apply directions to submarine coordinates, starting as [0, 0]
       Directions are "forward", "down" and "up".
       Where:
           "down X" decreases the vertical position by X units
           "up X" increases the vertical position by X units
           "forward X" increases the horizontal position by X units

       Eg. apply directions ["down 2", "up 1", "forward 2"]

        o - - -             - - - -           - - - -                - - - -
        - - - -  down 2 ->  - - - -  up 1 ->  o - - -  forward 2 ->  - - o -
        - - - -             o - - -           - - - -                - - - -
        [0, 0]              [0, -2]           [0, -1]                [2, -1]

       Args:
           directions (List[str]): list of directions
       Returns:
           list: resulting coordinates [x, y]
    """

    horizontal_position = 0
    vertical_position = 0
    for direction in directions:
        if direction[0] == 'forward':
            horizontal_position += int(direction[1])
        elif direction[0] == 'down':
            vertical_position += int(direction[1])
        elif direction[0] == 'up':
            vertical_position -= int(direction[1])
    result = [horizontal_position, vertical_position]
    return result


def get_my_position_advanced_way(directions) -> list[int]:
    """
       Apply directions to submarine coordinates, starting as [0, 0, 0]
       Third value is "aim" with special consenquences to submarine movement.
       Directions are "forward", "down" and "up".
       Where:
           "down X" increases "aim" by X units
           "up X" decreases "aim" by X units
           "forward X"
               - increases the horizontal position by X units
               - decreases the vertical position by "aim" * X
       Eg. apply directions ["down 2", "up 1", "forward 2"]
        o - - -             o - - -           o - - -                - - - -
        - - - -  down 2 ->  - - - -  up 1 ->  - - - -  forward 2 ->  - - - -
        - - - -             - - - -           - - - -                - - o -
       [0, 0, 0]           [0, 0, 2]          [0, 0, 1]             [2, -2, 0]
       Args:
           directions (List[str]): list of directions
       Returns:
           list: resulting coordinates [x, y, z]
    """
    horizontal_position = 0
    vertical_position = 0
    aim_position = 0
    for direction in directions:
        if direction[0] == 'forward':
            horizontal_position += int(direction[1])
            vertical_position += aim_position * int(direction[1])
        elif direction[0] == 'down':
            aim_position += int(direction[1])
        elif direction[0] == 'up':
            aim_position -= int(direction[1])
    result = [horizontal_position, vertical_position, aim_position]
    return result


if __name__ == '__main__':
    # part 1
    result = get_my_position(get_all_directions())
    print(f"Position is{result}, result is {result[0]}*{result[1]}= {result[0]*result[1]}")

    #part 2
    result = get_my_position_advanced_way(get_all_directions())
    print(f"Position is{result}, result is {result[0]}*{result[1]}= {result[0] * result[1]}")
