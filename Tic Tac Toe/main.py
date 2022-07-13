one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"


def roles_of_win(lis, mark) -> bool:
    if lis[1-1] == lis[2-1] == lis[3-1] == mark:
        return True
    elif lis[4-1] == lis[5-1] == lis[6-1] == mark:
        return True
    elif lis[7-1] == lis[8-1] == lis[9-1] == mark:
        return True
    elif lis[1-1] == lis[4-1] == lis[7-1] == mark:
        return True
    elif lis[2-1] == lis[5-1] == lis[8-1] == mark:
        return True
    elif lis[3-1] == lis[6-1] == lis[9-1] == mark:
        return True
    elif lis[1-1] == lis[5-1] == lis[9-1] == mark:
        return True
    elif lis[3-1] == lis[5-1] == lis[7-1] == mark:
        return True
    else:
        return False


the_one_who_starts = ""
msg = f"PLayer {the_one_who_starts} will play first because he picked the X marker."


def show_who_plays_first(player):
    global msg
    print(msg)
    msg = ""


def game():
    global one, two, three, four, five, six, seven, eight, nine
    list_of_values = [one, two, three, four, five, six, seven, eight, nine]
    marks = ["X", "O"]
    first_player_name = input("Enter a first Player name: ")
    second_player_name = input("Enter second player name: ")
    first_player_mark = input(f"Choose a mark for {first_player_name} (X/O): ")
    while first_player_mark not in marks:
        print("Please enter a mark X or O")
        first_player_mark = input(f"Choose a mark for {first_player_name} (X/O): ")

    second_player_mark = ""

    if first_player_mark == "X":
        second_player_mark = "O"
    elif first_player_mark == "O":
        second_player_mark = "X"
    the_one_who_plays_second = ""
    mark = ""

    if "X" in first_player_mark:
        the_one_who_starts = first_player_name
        the_one_who_plays_second = second_player_name
    elif "X" in second_player_mark:
        the_one_who_starts = second_player_name
        the_one_who_plays_second = first_player_name

    numbers_to_use = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    taken_values = []
    index = 0
    text = list_of_values[0] + " | " + list_of_values[1] + " | " + list_of_values[2] + "\n" + \
           "----------" + "\n" + \
           list_of_values[3] + " | " + list_of_values[4] + " | " + list_of_values[5] + \
           "\n" + "----------" + "\n" + list_of_values[6] + " | " + list_of_values[7] + " | " + list_of_values[8]
    print(text)
    is_on = True
    while is_on:
        index += 1
        if index == 1 or index == 3 or index == 5 or index == 7 or index == 9:
            mark = "X"
        elif index == 2 or index == 4 or index == 6 or index == 8:
            mark = "O"
        show_who_plays_first(the_one_who_starts)
        position = input("Enter a position to go to: ")
        while position not in numbers_to_use:
            print("Please try to enter non-taken number or a valid number.")
            position = input("Enter a position to go to: ")

        if position not in taken_values:

            for i in range(len(list_of_values)):
                if position == list_of_values[i]:
                    list_of_values[i] = mark

            for n in range(len(list_of_values)):
                if position == list_of_values[n]:
                    list_of_values[n] = mark

            taken_values.append(position)

        X = roles_of_win(list_of_values, "X")
        O = roles_of_win(list_of_values, "O")
        if X:
            print(f"{the_one_who_starts} has won..🤍")
            is_on = False
        if O:
            print(f"{the_one_who_plays_second} has won..🤍")
            is_on = False
        if len(taken_values) == 9 and (X == False) and (O == False):
            print("Draw..🤍")
            is_on = False
        text = list_of_values[0] + " | " + list_of_values[1] + " | " +\
               list_of_values[2] + "\n" + "----------" + "\n" + \
               list_of_values[3] + " | " + list_of_values[4] + " | " \
               + list_of_values[5] + \
               "\n" + "----------" + "\n" + list_of_values[6] + " | " \
               + list_of_values[7] + " | " + list_of_values[8]

        print(text)


game()
