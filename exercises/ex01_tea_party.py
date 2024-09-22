"""Calculates the number of tea bags, treats, and cost for a tea party"""

__author__: str = "730810493"


def main_planner(guests: int) -> None:
    """brings all the subsequent functions together to print intended values"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints the standard message with constimized number of guests

    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # calls the tea_bags function to display number of bags needed concatinated with "Tea Bags"

    print(
        "Treats: " + str(treats(people=guests))
    )  # calls the treats function to display the number of treats needed concatinated with "Treats"

    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# calls the tea_count function and treat_count function as arguements for cost


def tea_bags(people: int) -> int:
    """calculates the number of tea bags that are needed"""
    return people * 2


# mutiplies the number of people by 2 to obtain the number of bags needed and
# is stored as the return value


def treats(people: int) -> int:
    """calculates the number of treats needed for the party"""
    return int(
        tea_bags(people=people) * 1.5
    )  # calls the tea_bag function and multipies it by 1.5 to obtain the
    # amount of treats needed


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the cost of the treats and tea bags"""
    return (tea_count * 0.5) + (treat_count * 0.75)


# calls tea_count and treat_count to muitply them by .5 and .75 respectivly
# it then adds the two products together


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
# needed conditional statement to execute with autograder
