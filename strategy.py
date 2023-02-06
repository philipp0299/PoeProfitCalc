class Strategy:
    def __init__(self, educts, products, time=None):
        self.educts = educts
        self.products = products
        self.time = time

    def calc_profit(self):
        educt_cost = self.educts.fetch_price()
        product_cost = self.products.fetch_price()
        return product_cost - educt_cost

    def __str__(self):
        return str(self.educts) + " => " + str(self.products)

    # TODO: Printable instructions with trade links
