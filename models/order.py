class Order:
    def __init__(self, address, land_area, project_type,
                 price_segment, material_type,
                 status,
                 start_date, end_date, prepayment):
        self.address = address
        self.land_area = land_area
        self.project_type = project_type
        self.price_segment = price_segment
        self.material_type = material_type
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.prepayment = prepayment
        self.cost = 0
        
    def set_cost(self, cost):
        self.cost = cost

    def set_status(self, status):
        self.status = status

    def get_info(self):
        return (
            f"Адреса: {self.address}\n"
            f"Площа ділянки: {self.land_area}\n"
            f"Тип проєкту: {self.project_type}\n"
            f"Ціновий сегмент: {self.price_segment}\n"
            f"Тип матеріалів: {self.material_type}\n"
            f"Дата початку: {self.start_date}\n"
            f"Дата завершення: {self.end_date}\n"
            f"Передоплата: {self.prepayment}\n"
            f"Вартість: {self.cost}\n"
            f"Статус: {self.status}"
        )