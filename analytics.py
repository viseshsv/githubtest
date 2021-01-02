def moving_average(time_series):
    number_of_prices = len(time_series)
    total_time_series = 0.0
    for price in time_series:
        total_time_series = total_time_series + price
    return total_time_series / number_of_prices
        