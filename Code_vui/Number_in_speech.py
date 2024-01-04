num = int(input())
f = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "night"]
s = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
t = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

firstNum = num // 100
secondNum = num % 100 // 10
thirdNum = num % 10

speech = f[firstNum] + " hundered "
if secondNum == 1:
    speech += s[thirdNum]
else:
    speech = speech + t[secondNum] + " " + f[thirdNum]
print(speech)
