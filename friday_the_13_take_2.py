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

# day types 0 through 6
dow_list = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


def day_type_of_next_ftt(current_day_type, days_to_next_ftt):
    days_to_add = days_to_next_ftt % 7
    theoretical_new_day = current_day_type + days_to_add
    if theoretical_new_day > 6:
        return theoretical_new_day % 7
    return theoretical_new_day


def day_types_of_all_ftt(first_ftt_day_type, year_type):
    current_day_type = first_ftt_day_type
    list_of_all_ftt = [first_ftt_day_type]
    for month, num_days_month in year_type.items():
        if month == "Dec":
            break
        next_month_ftt = day_type_of_next_ftt(current_day_type, num_days_month)
        list_of_all_ftt.append(next_month_ftt)
        current_day_type = next_month_ftt
    # print(f"The day types of all Friday 13ths: {list_of_all_ftt}")
    # print(f"There are {list_of_all_ftt.count(5)} Friday the 13ths this year")
    return list_of_all_ftt.count(5)


def get_all_ftt_count():
    list_of_ftt_count = []
    for year in range(7):
        year_count = day_types_of_all_ftt(year, regular_year)
        list_of_ftt_count.append(year_count)

    for year in range(7):
        year_count = day_types_of_all_ftt(year, leap_year)
        list_of_ftt_count.append(year_count)
    print(f"\nThis is the list of the counts of Friday the 13ths:\n{list_of_ftt_count}")
    print(f"The miniumum number is {min(list_of_ftt_count)}")
    print(f"The maximum number is {max(list_of_ftt_count)}")


# get runtime of program while executing
start_time = time.time()
get_all_ftt_count()
end_time = time.time()
run_time = (end_time - start_time) * 1000
print(f"Execution time: {run_time} milliseconds\n")
