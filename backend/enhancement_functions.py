from file_functions import readCsv, openJSON

enhancementDataPath = "backend/data/enhancement"

blackStoneExchange = {
    5: 5,
    10: 12,
    15: 21,
    20: 33,
    25: 53,
    30: 84,
}


def getItemChances(file: str, currentEnhancement: int) -> list[float]:
    ( header, rows ) = readCsv(file, enhancementDataPath, delimiter=";")

    column = header.index(f"{currentEnhancement+1}")
    chance = []
    
    for row in rows:
        chance.append(float(row[column]))

    return chance


def getItemPossibleEnhancements(file: str) -> list[int]:
    ( header, rows ) = readCsv(file, enhancementDataPath, delimiter=";")
    return header[:-1]


# The parameter chances: list[float] is meant to be a list of the probabilities of success on each number of fs
# getAverageChance(chances[30:]) will return the average chance of success from 30fs onwards
# getCummulativeChance(chances[30:40]) will return the combined chance of success from 30fs to 40fs (10 attempts)
def getAverageChance(chances: list[float]):
    kList = []
    cList = []
    for i in range(chances.__len__()):
        p = chances[i]

        if i == 0:
            kList.append(1)
            cList.append(p)
            continue

        prevK = kList[i-1]
        prevP = chances[i-1]

        k = (1 - prevP) * prevK

        kList.append(k)
        cList.append(p * k)

    return sum(cList)/sum(kList)


# Chance of success from the given list of probabilities
# With this function probability awllways and only increments by 1 (1fs) each iteration
# Does not work for independent attempts (same fs every attempt) or multiple fs gained on each attempt
def getCumulativeChance(chances: list[float]):
    totalP = 0

    for i in range(chances.__len__()):
        p = chances[i]

        if i == 0:
            totalP = p
            continue

        totalP += (1 - totalP) * p
    
    return totalP


def getItemEnhancementCategory(itemId: int) -> str | None:
    categories = openJSON("ItemCategories.json", enhancementDataPath)
    for key in categories.keys():
        if(itemId in categories[key]):
            return key
    return None


def getEnhancementChance(itemId: int, currentEnhancement: int, initialFs: int):
    file = f"{getItemEnhancementCategory(itemId)}.csv" # TODO Determine the required file name from the item id
    chances = getItemChances(file, currentEnhancement)[initialFs:]
    return getAverageChance(chances)


# Fs made using white equipment
# Returns the average amount of fails needed to reach the target amount
def getWhiteFsCost(targetFs: int, initialFs: int = 0) -> float:
    chances = getItemChances("WhiteArmor.csv", 14)
    
    kList = []
    for i in range(targetFs + 1):
        if i == 0:
            kList.append(0)
            continue

        prevK = kList[i-1]
        prevP = chances[i-1]

        k = (prevK + 1) / (1 - prevP)

        kList.append(k)

    return kList[targetFs] - kList[initialFs]


first = getEnhancementChance(14023, 0, 1)
second = getEnhancementChance(14023, 1, 20)
third = getEnhancementChance(14023, 2, 30)

firstAmount = 2 / first
secondAmount = (firstAmount + 1) / second
thirdAmount = (secondAmount + 1) / third

print(first, second, third)
print(firstAmount, secondAmount, thirdAmount)