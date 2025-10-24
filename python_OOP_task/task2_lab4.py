from datetime import datetime

class OrderManager:
    def __init__(self, orders=None):
        if orders is None:
            orders = []
        self.__orders = orders

    def getOrders(self):
        return self.__orders

    # 6) Get all orders having products in a given category
    def getOrdersHavingPInAGivenCategory(self, category):
        return [o for o in self.getOrders() if len(o.getPByCategory(category)) != 0]

    # 7) Get all products ordered by a customer with a tier of 2 from 01/2/2025 to 01/04/2025
    def getPOrderedByCustomerTier2(self):
        return [
            o for o in self.getOrders()
            if o.getCustomer().getTier() == 2
            and datetime(2025, 2, 1) <= o.getOrderDate() <= datetime(2025, 4, 1)
        ]

    # 8) Get 3 recent orders
    def get3RecentOrder(self):
        oList = sorted(self.getOrders(), key=lambda o: o.getOrderDate(), reverse=True)
        return oList[:3]

    # 9) Get all orders ordered on 15/03/2025
    def getAOrderOrderedOn15_03_2025(self):
        return [o for o in self.getOrders() if o.getOrderDate().date() == datetime(2025, 3, 15).date()]

    def costOfAllOrdersDateTime(self, dateTimeInput):
        return sum([o.getAllCost() for o in self.getOrders() if o.getOrderDate().date() == dateTimeInput.date()])

    # 10) Cost of all orders in 2/2025
    def costOfAllOrdersIn2_2025(self):
        return sum([o.getAllCost() for o in self.getOrders() if o.getOrderDate().month == 2 and o.getOrderDate().year == 2025])

    # 11) Average cost of all orders bought on 15/03/2025
    def averageCostOfAllOrdersBoughtOn15_03_2025(self):
        orders_on_date = [o for o in self.getOrders() if o.getOrderDate().date() == datetime(2025, 3, 15).date()]
        if not orders_on_date:
            return 0
        return sum(o.getAllCost() for o in orders_on_date) / len(orders_on_date)

    # 12) Get statistics for each order and the number of products
    def getStatisticsOfOrderAndTheNumberOfProducts(self):
        return {
            o.getOid(): o.getTotalP()
            for o in sorted(self.getOrders(), key=lambda o: o.getTotalP())
        }

    # 13) Get statistics of orders by customer
    def getStatisticsOfOrdersByCustomer(self):
        return {
            cid: [o for o in self.getOrders() if o.getCustomer().getCid() == cid]
            for cid in {o.getCustomer().getCid() for o in self.getOrders()}
        }

    # 14) Get statistics of orders and their cost
    def getStatisticsOfOrdersAndTheirCost(self):
        return {o.getOid(): o.getAllCost() for o in self.getOrders()}


class Order:
    def __init__(self, oid, status, orderDate, deliveryDate, customer, items=None):
        if items is None:
            items = []
        self.__oid = oid
        self.__status = status
        self.__orderDate = orderDate
        self.__deliveryDate = deliveryDate
        self.__customer = customer
        self.__items = items

    def getOid(self):
        return self.__oid

    def getOrderDate(self):
        return self.__orderDate

    def getCustomer(self):
        return self.__customer

    def getItems(self):
        return self.__items

    def getPBelongToCategoryHigherThanThresold(self, category, threshold):
        return [item.getP() for item in self.getItems()
                if item.getP().getCategory() == category and item.getP().getPrice() > threshold]

    def getPBaseOnAGivenACategoryAndDecrease10Percent(self, category):
        return [item.getP().decreasePriceByPercent(0.1)
                for item in self.getItems()
                if item.getP().getCategory() == category]

    def getCheapestPInGivenCategory(self, category):
        filtered = [item.getP() for item in self.getItems() if item.getP().getCategory() == category]
        return min(filtered, key=lambda p: p.getPrice()) if filtered else None

    def getStatisticsOfPByCategory(self):
        categories = {item.getP().getCategory() for item in self.getItems()}
        return {
            category: [item.getP() for item in self.getItems() if item.getP().getCategory() == category]
            for category in categories
        }

    def getTheMostExpensiveProductsByCategory(self):
        categories = {item.getP().getCategory() for item in self.getItems()}
        return {
            category: max(
                [item.getP() for item in self.getItems() if item.getP().getCategory() == category],
                key=lambda p: p.getPrice()
            )
            for category in categories
        }

    def getPByCategory(self, category):
        return [item.getP() for item in self.getItems() if item.getP().getCategory() == category]

    def getAllP(self):
        return [item.getP() for item in self.getItems()]

    def getAllCost(self):
        return sum(item.getP().getPrice() * item.getQuantity() for item in self.getItems())

    def getTotalP(self):
        return sum(item.getQuantity() for item in self.getItems())


class OrderItem:
    def __init__(self, quantity, p):
        self.__quantity = quantity
        self.__p = p

    def getP(self):
        return self.__p

    def getQuantity(self):
        return self.__quantity


class Customer:
    def __init__(self, cid, name, tier):
        self.__cid = cid
        self.__name = name
        self.__tier = int(tier)

    def getName(self):
        return self.__name

    def getCid(self):
        return self.__cid

    def getTier(self):
        return self.__tier


class Product:
    def __init__(self, pid, name, category, price):
        self.__pid = pid
        self.__name = name
        self.__category = category
        self.__price = price

    def getPid(self):
        return self.__pid

    def getName(self):
        return self.__name

    def getCategory(self):
        return self.__category

    def getPrice(self):
        return self.__price

    def decreasePriceByPercent(self, percent):
        self.__price *= (1 - percent)
        return self

def main():
    from datetime import datetime

    # ==== Create Products ====
    p1 = Product("P01", "Laptop", "Electronics", 1200)
    p2 = Product("P02", "Phone", "Electronics", 800)
    p3 = Product("P03", "Book", "Books", 30)
    p4 = Product("P04", "Tablet", "Electronics", 600)
    p5 = Product("P05", "Notebook", "Books", 10)

    # ==== Create Customers (cid as long/int) ====
    c1 = Customer(1, "Alice", 2)
    c2 = Customer(2, "Bob", 1)
    c3 = Customer(3, "Charlie", 2)

    # ==== Create OrderItems ====
    oi1 = OrderItem(1, p1)
    oi2 = OrderItem(2, p2)
    oi3 = OrderItem(3, p3)
    oi4 = OrderItem(1, p4)
    oi5 = OrderItem(5, p5)

    # ==== Create Orders ====
    o1 = Order(1, "Delivered", datetime(2025, 2, 15), datetime(2025, 2, 20), c1, [oi1, oi2])
    o2 = Order(2, "Delivered", datetime(2025, 3, 15), datetime(2025, 3, 20), c2, [oi3, oi5])
    o3 = Order(3, "Pending", datetime(2025, 3, 15), datetime(2025, 3, 18), c3, [oi4])
    o4 = Order(4, "Delivered", datetime(2025, 2, 25), datetime(2025, 3, 1), c1, [oi5])
    o5 = Order(5, "Delivered", datetime(2025, 1, 20), datetime(2025, 1, 25), c2, [oi1, oi3, oi5])

    # ==== Create OrderManager ====
    manager = OrderManager([o1, o2, o3, o4, o5])

    # 1) Get all products belonging to a given category and price > threshold
    print("\n(1) Products in Electronics > 700:")
    for p in o1.getPBelongToCategoryHigherThanThresold("Electronics", 700):
        print(f"- {p.getName()} (${p.getPrice()})")

    # 2) Decrease price by 10% for category
    print("\n(2) Decrease 10% for Books:")
    o2.getPBaseOnAGivenACategoryAndDecrease10Percent("Books")
    for p in o2.getAllP():
        if p.getCategory() == "Books":
            print(f"- {p.getName()} new price: ${p.getPrice():.2f}")

    # 3) Cheapest product in a given category
    print("\n(3) Cheapest Electronics product:")
    cheapest = o1.getCheapestPInGivenCategory("Electronics")
    print(f"- {cheapest.getName()} (${cheapest.getPrice()})")

    # 4) Statistics of products by category
    print("\n(4) Statistics of products by category (O1):")
    stats = o1.getStatisticsOfPByCategory()
    for cat, plist in stats.items():
        print(f"- {cat}: {[p.getName() for p in plist]}")

    # 5) Most expensive product by category
    print("\n(5) Most expensive product by category (O1):")
    expensive = o1.getTheMostExpensiveProductsByCategory()
    for cat, p in expensive.items():
        print(f"- {cat}: {p.getName()} (${p.getPrice()})")

    # 6) Orders having products in Books category
    print("\n(6) Orders having products in Books category:")
    for o in manager.getOrdersHavingPInAGivenCategory("Books"):
        print(f"- {o.getOid()}")

    # 7) Orders by customers with tier = 2 from 01/2/2025 → 01/4/2025
    print("\n(7) Orders by tier=2 customers between Feb–Apr 2025:")
    for o in manager.getPOrderedByCustomerTier2():
        print(f"- {o.getOid()} ({o.getCustomer().getName()}) on {o.getOrderDate().date()}")

    # 8) 3 recent orders
    print("\n(8) 3 most recent orders:")
    for o in manager.get3RecentOrder():
        print(f"- {o.getOid()} on {o.getOrderDate().date()}")

    # 9) Orders ordered on 15/03/2025
    print("\n(9) Orders ordered on 15/03/2025:")
    for o in manager.getAOrderOrderedOn15_03_2025():
        print(f"- {o.getOid()}")

    # 10) Total cost of all orders in 2/2025
    print("\n(10) Total cost of all orders in Feb 2025:")
    print(f"→ ${manager.costOfAllOrdersIn2_2025():.2f}")

    # 11) Average cost of all orders on 15/03/2025
    print("\n(11) Average cost of orders on 15/03/2025:")
    print(f"→ ${manager.averageCostOfAllOrdersBoughtOn15_03_2025():.2f}")

    # 12) Statistics: each order → number of products
    print("\n(12) Statistics: order → number of products:")
    print(manager.getStatisticsOfOrderAndTheNumberOfProducts())

    # 13) Statistics: customer → list of orders
    print("\n(13) Statistics: customer → orders:")
    for cid, orders in manager.getStatisticsOfOrdersByCustomer().items():
        print(f"- {cid}: {[o.getOid() for o in orders]}")

    # 14) Statistics: order → cost
    print("\n(14) Statistics: order → cost:")
    for oid, cost in manager.getStatisticsOfOrdersAndTheirCost().items():
        print(f"- {oid}: ${cost:.2f}")


if __name__ == "__main__":
    main()

