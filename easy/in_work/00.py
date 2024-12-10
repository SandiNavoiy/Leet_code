from datetime import datetime

def is_third_tuesday(dt_str: str) -> bool:
    dt = datetime.strptime(dt_str, '%b %d, %Y')
    dt = dt.date()


    if dt.isoweekday() ==2 and 14 <= dt.day <= 21:
        return  True
    else:
        return False





assert is_third_tuesday("Sep 19, 2023")
assert not is_third_tuesday("Sep 12, 2023")
assert is_third_tuesday("Jul 18, 2023")
assert not is_third_tuesday("Jul 11, 2023")
assert not is_third_tuesday('Jun 23, 2015')
assert is_third_tuesday('Jun 16, 2015')
assert is_third_tuesday('Jul 21, 2015')
assert is_third_tuesday("Oct 20, 2015")
assert is_third_tuesday("Nov 17, 2015")

#
# print('Good')