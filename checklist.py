import os
from time import sleep
checklist = list()


colors = {
    "success": '\033[92m',
    "danger": '\033[91m',
    "underline": '\033[4m',
    "end": '\033[0m'
}


def story():
    name = input("Give us your name: ")
    print(f"Welcome {name}, about time you arrived\n You have been given the opportunity to shop\nfor yourself. Take anything you want, it's on us.")
    sleep(3)


def clearScreen():
    sleep(1)
    os.system('clear||cls')


def create(item):
    checklist.append(item)
    print(colors["success"] +
          "Yasss! {} was added to the list!".format(item) + colors["end"])
    # clearScreen()


def read(index):
    print(colors["underline"] +
          "{}".format(checklist[index]) + colors["end"] + " is in your list!")


def update(index, item):
    checklist[index] = item


def destroy(index):
    print(colors["danger"] +
          "You have deleted {} from your list".format(checklist[index]) + colors["end"])
    checklist.pop(index)
    clearScreen()


def list_all_items():
    index = 0
    for list_item in checklist:
        print('Index: {} Item: {}'.format(index, list_item))
        index += 1


def mark_completed():
    index = int(input(
        "Pick the index of the item you would like to check off your list: "))
    checklist[index] = "check {}".format(checklist[index])


def mark_uncompleted():
    index = int(
        input("Enter the index of a completed item you wish to mark incomplete: "))


def select(action):
    if action == 'C':
        item = input("Put an item in your list: ")
        create(item)

    elif action == "R":
        index = int(input("Enter the index of the item you wish to inspect: "))
        read(index)

    elif action == "P":
        list_all_items()
    elif action == "D":
        index = int(input("Enter the index of the item you wish to destroy: "))
        destroy(index)

    elif action == "Q":
        return False

    else:
        print('{} is an Unknown option'.format(action))


def test():
    select("C")
    select("R")
    select("P")
    select("D")
    list_all_items()
    mark_completed()
    list_all_items()
    mark_uncompleted()
    list_all_items()
    select("B")
    select("Q")


# test()
running = True
while running:
    story()
    selection = input(
        "Press C to add to list, R to Read from list and P to display list or Q to quit: ")
    running = select(selection)
