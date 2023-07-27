class ItemBase:
    id = 0
    name = ""
    grade = 0
    icon = ""

    def __init__(self, id, name, grade, icon):
        self.id = id
        self.name = name
        self.grade = grade
        self.icon = icon


class ListItem(ItemBase):
    stock = 0
    basePrice = 0
    totalTrades = 0

    def __init__(self, id, name, grade, icon, stock, basePrice, totalTrades):
        super().__init__(id, name, grade, icon)
        self.stock = stock
        self.basePrice = basePrice
        self.totalTrades = totalTrades


class SubListItem(ItemBase):
    enhancement = 0
    stock = 0
    basePrice = 0
    totalTrades = 0
    lastPrice = 0
    lastSale = 0

    def __init__(self, id, name, grade, icon, enhancement, stock, basePrice, totalTrades, lastPrice, lastSale):
        super().__init__(id, name, grade, icon)
        self.enhancement = enhancement
        self.stock = stock
        self.basePrice = basePrice
        self.totalTrades = totalTrades
        self.lastPrice = lastPrice
        self.lastSale = lastSale


class HotListItem(SubListItem):
    changeDirection = 0
    changeValue = 0