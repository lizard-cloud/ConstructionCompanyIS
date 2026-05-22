from models.order import Order
from models.contract import Contract
from repositories.order_repository import OrderRepository


class OrderController:

    def __init__(self):
        self.repository = OrderRepository()

    def create_order(self, address, land_area,
                     project_type, price_segment,
                     material_type, status,
                     start_date, end_date, prepayment):

        order = Order(
            address,
            land_area,
            project_type,
            price_segment,
            material_type,
            status,
            start_date,
            end_date,
            prepayment
        )

        return order

    def calculate_cost(self, order):

        base_price = 1000

        if order.project_type == "Приватний будинок":
            project_coefficient = 1.5
        elif order.project_type == "Гараж":
            project_coefficient = 1.2
        elif order.project_type == "Торговий центр":
            project_coefficient = 2.0
        elif order.project_type == "Офісна будівля":
            project_coefficient = 1.8
        else:
            project_coefficient = 1.0

        if order.price_segment == "Економ":
            segment_coefficient = 0.9
        elif order.price_segment == "Стандарт":
            segment_coefficient = 1.0
        elif order.price_segment == "Преміум":
            segment_coefficient = 1.3
        else:
            segment_coefficient = 1.0

        if order.material_type == "Базові матеріали":
            material_coefficient = 0.95
        elif order.material_type == "Стандартні матеріали":
            material_coefficient = 1.0
        elif order.material_type == "Преміальні матеріали":
            material_coefficient = 1.4
        else:
            material_coefficient = 1.0

        total_cost = (
                order.land_area
                * base_price
                * project_coefficient
                * segment_coefficient
                * material_coefficient
        )

        order.set_cost(total_cost)

        return total_cost

    def create_contract(self, order):

        contract = Contract(order)

        return contract

    def save_order(self, customer_name, customer_contact, order):
        return self.repository.save_order_with_customer_and_payment(
            customer_name,
            customer_contact,
            order
        )

    def get_all_orders(self):
        return self.repository.get_all_orders()

    def search_orders_by_customer(self, customer_name):
        return self.repository.search_orders_by_customer(customer_name)

    def delete_order(self, order_id):
        self.repository.delete_order(order_id)

    def update_order(self, order_id, order):
        self.repository.update_order(order_id, order)

    def get_payments_by_order(self, order_id):
        return self.repository.get_payments_by_order(order_id)

    def add_payment(self, order_id, payment_date, amount, payment_type):
        self.repository.add_payment(
            order_id,
            payment_date,
            amount,
            payment_type
        )

    def get_total_payments(self, order_id):
        return self.repository.get_total_payments(order_id)

    def get_payment_balance(self, order_id):
        return self.repository.get_payment_balance(order_id)

    def get_all_employees(self):
        return self.repository.get_all_employees()

    def add_employee(self, full_name, position, salary, contact_data):
        self.repository.add_employee(full_name, position, salary, contact_data)

    def delete_employee(self, employee_id):
        self.repository.delete_employee(employee_id)

    def get_all_work_types(self):
        return self.repository.get_all_work_types()

    def add_work_type(self, work_name, description, cost):
        self.repository.add_work_type(work_name, description, cost)

    def delete_work_type(self, work_type_id):
        self.repository.delete_work_type(work_type_id)

    def assign_employee_to_work_type(self, work_type_id, employee_id, role_in_work):
        self.repository.assign_employee_to_work_type(
            work_type_id,
            employee_id,
            role_in_work
        )

    def get_assigned_employees(self):
        return self.repository.get_assigned_employees()

    def get_all_materials(self):
        return self.repository.get_all_materials()

    def get_materials_by_order(self, order_id):
        return self.repository.get_materials_by_order(order_id)

    def add_work_type_to_order(self, order_id, work_type_id):
        self.repository.add_work_type_to_order(order_id, work_type_id)

    def get_work_types_by_order(self, order_id):
        return self.repository.get_work_types_by_order(order_id)

    def update_customer_by_order(self, order_id, customer_name, customer_contact):
        self.repository.update_customer_by_order(
            order_id,
            customer_name,
            customer_contact
        )

    def get_order_details_by_id(self, order_id):
        return self.repository.get_order_details_by_id(order_id)

