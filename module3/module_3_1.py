calls = 0
def count_calls():

    global calls
    calls += 1


def string_info(string1: str):
    count_calls()

    return len(string1), string1.upper(), string1.lower()


def is_contains(string2: str, list_to_search: list):
    count_calls()
    string2 = string2.lower()
    list_to_search = [x.lower() for x in list_to_search]
    if string2 in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True ## Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))# False # No matches
print(calls)
