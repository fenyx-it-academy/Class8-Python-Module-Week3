def colors(string):
    return "-".join(sorted(string.split("-")))

print(colors("green-red-yellow-black-white"))