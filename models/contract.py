from datetime import date


class Contract:
    def __init__(self, order):
        self.order = order
        self.contract_date = date.today()
        self.status = "Сформовано"

    def get_contract_info(self):
        return (
            f"БУДІВЕЛЬНИЙ КОНТРАКТ\n"
            f"Дата укладання: {self.contract_date}\n\n"
            f"{self.order.get_info()}\n\n"
            f"Статус контракту: {self.status}"
        )