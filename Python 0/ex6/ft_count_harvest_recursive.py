def count_days(current, days):
    if current > days:
        return

    print(f"Day {current}")
    count_days(current + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days(1, days)
    print("Harvest time!")
