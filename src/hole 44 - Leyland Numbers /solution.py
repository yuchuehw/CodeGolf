"""
ranked 4th as of 01/17/2024. the comma at the end of line 4 is necessary.
"""
r=range(2,99);*map(print,sorted({x**y+y**x for x in r for y in r})[:107]),
