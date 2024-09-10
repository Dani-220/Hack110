"""Takes the number of guests and calculates the number of tea bags, treats, and cost for a tea party"""

__author__: str = "730810493"


def main_planner(guests: int) -> None:
    # brings all the subsequent functions together to print intended values
    print("A Cozy Tea Party for " + guests + " People!")

    print("Tea Bags: " + tea_bags(people=guests))

    print("Treats: " + treats(people=guests))

    print("Cost: $" + cost(tea_count=guests, treat_count=guests))


def tea_bags(people: int) -> int:
    # calculates the number of tea bags that are needed
    return people * 2


def treats(people: int) -> int:
    # calculates the number of treats needed for the party
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    # calculates the cost of the treats and tea bags
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
