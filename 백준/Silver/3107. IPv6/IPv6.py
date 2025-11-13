import sys
input = sys.stdin.readline

def doubleColoneExpand(str):
    left, right = str.split("::")
    leftParts = left.split(":") if left else []
    # print("leftParts: ", leftParts)
    rightParts = right.split(":") if right else []
    # print("rightParts: ", rightParts)
    middlePartsCount = 8 - (len(leftParts) + len(rightParts))
    middleParts = ["0000"] * middlePartsCount
    # print("middleParts: ", middleParts)
    fullParts = leftParts + middleParts + rightParts
    # print("fullParts: ", fullParts  )
    return ":".join(fullParts)

def main(str):
    if "::" in str:
        str = doubleColoneExpand(str)
    strParts = str.split(":")
    for i in range(len(strParts)):
        if (strParts[i]) != 4:
            strParts[i] = ("0" * (4 - len(strParts[i]))) + strParts[i]
        # print("i after append: ", strParts[i])
    str = ":".join(strParts)
    return str


str = input().strip()
print(main(str))
