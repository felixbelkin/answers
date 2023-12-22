def convert_time(time_str):
    if time_str[-2:] in ('AM', 'PM'):
        # Если входное время в 12-часовом формате (содержит AM или PM)
        hours, minutes = map(int, time_str[:-6].split(':'))
        is_pm = time_str[-2:] == 'PM'

        if is_pm and hours != 12:
            hours += 12
        elif not is_pm and hours == 12:
            hours = 0

        return f"{hours:02d}:{minutes:02d}"

    else:
        # Если входное время в 24-часовом формате
        hours, minutes = map(int, time_str.split(':'))
        is_pm = hours >= 12

        if hours > 12:
            hours -= 12
        elif hours == 0:
            hours = 12

        period = 'PM' if is_pm else 'AM'
        return f"{hours:02d}:{minutes:02d} {period}"

# Пример использования:
time_12h = "02:30 PM"
time_24h = convert_time(time_12h)
print(f"12-часовой формат: {time_12h} -> 24-часовой формат: {time_24h}")

time_24h = "14:45"
time_12h = convert_time(time_24h)
print(f"24-часовой формат: {time_24h} -> 12-часовой формат: {time_12h}")
