# https://codevscolor.com/python-get-all-sublists-list
def get_sublists(l):
    if len(l) == 0:
        return [[]]

    sublists = []
    first = l[0]
    remaining = l[1:]
    sublist_remaining = get_sublists(remaining)

    for sublist in sublist_remaining:
        sublists.append([first] + sublist)

    sublists.extend(sublist_remaining)

    return sublists


if __name__ == "__main__":
    given_list = list()
    result_list = list()

    size = int(input("Enter the size of the list: "))

    print("Enter all elements of the list: ")

    for i in range(size):
        given_list.append(int(input("Enter element to add: ")))

    result_list = get_sublists(given_list)

    print(result_list)