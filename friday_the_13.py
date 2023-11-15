# Determine how many Friday the 13th's are possible in a year

import time

regular_year = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31,
}

leap_year = {
    "Jan": 31,
    "Feb": 29,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31,
}


dow_list = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

# {'dow': 'wed', 'month': 'Dec', 'day_num': 27}


def create_year(starting_dow_num, days_per_month):
    year = []
    dow_num = starting_dow_num

    for month, num_days in days_per_month.items():
        for date in range(1, num_days + 1):
            year.append({"dow": dow_list[dow_num], "month": month, "day_num": date})
            if dow_num == 6:
                dow_num = 0
            else:
                dow_num += 1

    return year


def count_friday_thirteens(year):
    count = 0
    date_list = []
    for date in year:
        if date["dow"] == "fri" and date["day_num"] == 13:
            count += 1
            date_list.append(date)
    return count


def number_of_fri13_possible():
    possible_counts = []
    for year in range(7):
        new_year = create_year(year, regular_year)
        possible_counts.append(count_friday_thirteens(new_year))
    for year in range(7):
        new_year = create_year(year, leap_year)
        possible_counts.append(count_friday_thirteens(new_year))
    return possible_counts


# get runtime of program while executing
start_time = time.time()

list_of_fri13_counts = number_of_fri13_possible()
print(f"The maximum number of Friday the 13ths is {max(list_of_fri13_counts)}")
print(f"The minimum number of Friday the 13ths is {min(list_of_fri13_counts)}")
print(f"Here is the possible counts of the 14 possible years:\n{list_of_fri13_counts}")

end_time = time.time()
run_time = (end_time - start_time) * 1000
print(f"Execution time: {run_time} milliseconds\n")
