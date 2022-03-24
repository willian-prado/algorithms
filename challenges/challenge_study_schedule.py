def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    result = 0
    for period in permanence_period:
        starting_time = period[0]
        ending_time = period[1]

        if not (isinstance(starting_time, int)
                and isinstance(ending_time, int)):
            return None

        if starting_time <= target_time <= ending_time:
            result += 1

    return result
