import re

def highlight(text: str, str_to_select: str, decoration: str) -> str:
    result = re.sub(str_to_select, decoration + str_to_select + decoration, text)
    return result


quote = "Guns. Lots of Guns."
print("1. Result is: ", highlight(quote, "Guns", "**"))
print("2. Result for check is: ", highlight(quote, "guns", "**"))
