class Strategy:
    def __init__(self, educts, products, time=None):
        self.educts = educts
        self.products = products

    def calc_profit(self):
        educt_cost = self.educts.fetch_price()
        product_cost = self.products.fetch_price()
        return product_cost - educt_cost
