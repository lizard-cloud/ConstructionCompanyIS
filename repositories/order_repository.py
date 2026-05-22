from database import get_connection


class OrderRepository:

    def save_order_with_customer_and_payment(
            self,
            customer_name,
            customer_contact,
            order
    ):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO Customer (full_name, contact_data)
                VALUES (%s, %s)
                """,
                (customer_name, customer_contact)
            )

            customer_id = cursor.lastrowid

            cursor.execute(
                """
                INSERT INTO Orders
                (
                    address,
                    area,
                    project_type,
                    price_segment,
                    material_type,
                    status,
                    start_date,
                    end_date,
                    id_customer,
                    total_cost
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    order.address,
                    order.land_area,
                    order.project_type,
                    order.price_segment,
                    order.material_type,
                    order.status,
                    order.start_date,
                    order.end_date,
                    customer_id,
                    order.cost
                )
            )

            order_id = cursor.lastrowid

            cursor.execute(
                """
                INSERT INTO Payment
                (payment_date, amount, payment_type, id_order)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    order.start_date,
                    order.prepayment,
                    "Передоплата",
                    order_id
                )
            )

            connection.commit()
            return order_id

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_all_orders(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                Orders.id_order,
                Customer.full_name,
                Orders.address,
                Orders.area,
                Orders.project_type,
                Orders.status,
                Orders.start_date,
                Orders.end_date
                
            FROM Orders
            INNER JOIN Customer
            ON Orders.id_customer = Customer.id_customer
            """
        )

        orders = cursor.fetchall()

        cursor.close()
        connection.close()

        return orders

    def search_orders_by_customer(self, customer_name):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                Orders.id_order,
                Customer.full_name,
                Orders.address,
                Orders.area,
                Orders.project_type,
                Orders.status,
                Orders.start_date,
                Orders.end_date
            FROM Orders
            INNER JOIN Customer
            ON Orders.id_customer = Customer.id_customer
            WHERE Customer.full_name LIKE %s
            """,
            (f"%{customer_name}%",)
        )

        orders = cursor.fetchall()

        cursor.close()
        connection.close()

        return orders

    def delete_order(self, order_id):

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                DELETE FROM Payment
                WHERE id_order = %s
                """,
                (order_id,)
            )

            cursor.execute(
                """
                DELETE FROM OrderWorkType
                WHERE id_order = %s
                """,
                (order_id,)
            )

            cursor.execute(
                """
                DELETE FROM Orders
                WHERE id_order = %s
                """,
                (order_id,)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def update_order(self, order_id, order):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE Orders
                SET address = %s,
                    area = %s,
                    project_type = %s,
                    price_segment = %s,
                    material_type = %s,
                    status = %s,
                    start_date = %s,
                    end_date = %s,
                    total_cost = %s
                WHERE id_order = %s
                """,
                (
                    order.address,
                    order.land_area,
                    order.project_type,
                    order.price_segment,
                    order.material_type,
                    order.status,
                    order.start_date,
                    order.end_date,
                    order.cost,
                    order_id
                )
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_payments_by_order(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id_payment,
                payment_date,
                amount,
                payment_type
            FROM Payment
            WHERE id_order = %s
            """,
            (order_id,)
        )

        payments = cursor.fetchall()

        cursor.close()
        connection.close()

        return payments

    def add_payment(self, order_id, payment_date, amount, payment_type):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO Payment
                (payment_date, amount, payment_type, id_order)
                VALUES (%s, %s, %s, %s)
                """,
                (payment_date, amount, payment_type, order_id)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_total_payments(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT SUM(amount)
            FROM Payment
            WHERE id_order = %s
            """,
            (order_id,)
        )

        total = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return total if total else 0

    def get_payment_balance(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                Orders.total_cost - COALESCE(SUM(Payment.amount), 0) AS balance
            FROM Orders
            LEFT JOIN Payment
            ON Orders.id_order = Payment.id_order
            WHERE Orders.id_order = %s
            GROUP BY Orders.id_order, Orders.total_cost
            """,
            (order_id,)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result[0] if result else 0

    def get_all_employees(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id_employee,
                full_name,
                position,
                salary
            FROM Employee
            ORDER BY full_name
            """
        )

        employees = cursor.fetchall()

        cursor.close()
        connection.close()

        return employees

    def add_employee(self, full_name, position, salary, contact_data):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO Employee (full_name, position, salary, contact_data)
                VALUES (%s, %s, %s, %s)
                """,
                (full_name, position, salary, contact_data)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def delete_employee(self, employee_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM WorkTypeEmployee
                WHERE id_employee = %s
                """,
                (employee_id,)
            )

            count = cursor.fetchone()[0]

            if count > 0:
                raise Exception("Працівника не можна видалити, бо він уже призначений на вид роботи.")

            cursor.execute(
                """
                DELETE FROM Employee
                WHERE id_employee = %s
                """,
                (employee_id,)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_all_work_types(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id_work_type,
                work_name,
                description,
                cost
            FROM WorkType
            ORDER BY work_name
            """
        )

        work_types = cursor.fetchall()

        cursor.close()
        connection.close()

        return work_types

    def add_work_type(self, work_name, description, cost):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO WorkType (work_name, description, cost)
                VALUES (%s, %s, %s)
                """,
                (work_name, description, cost)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def delete_work_type(self, work_type_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM OrderWorkType
                WHERE id_work_type = %s
                """,
                (work_type_id,)
            )

            order_count = cursor.fetchone()[0]

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM WorkTypeEmployee
                WHERE id_work_type = %s
                """,
                (work_type_id,)
            )

            employee_count = cursor.fetchone()[0]

            if order_count > 0:
                raise Exception("Вид роботи не можна видалити, бо він уже доданий до замовлення.")

            if employee_count > 0:
                raise Exception("Вид роботи не можна видалити, бо на нього вже призначені працівники.")

            cursor.execute(
                """
                DELETE FROM WorkType
                WHERE id_work_type = %s
                """,
                (work_type_id,)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def assign_employee_to_work_type(self, work_type_id, employee_id, role_in_work):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO WorkTypeEmployee
                (id_work_type, id_employee, role_in_work)
                VALUES (%s, %s, %s)
                """,
                (work_type_id, employee_id, role_in_work)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_assigned_employees(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                WorkType.work_name,
                Employee.full_name,
                Employee.position,
                WorkTypeEmployee.role_in_work
            FROM WorkTypeEmployee
            INNER JOIN WorkType
            ON WorkTypeEmployee.id_work_type = WorkType.id_work_type
            INNER JOIN Employee
            ON WorkTypeEmployee.id_employee = Employee.id_employee
            ORDER BY WorkType.work_name
            """
        )

        assigned_employees = cursor.fetchall()

        cursor.close()
        connection.close()

        return assigned_employees

    def get_all_materials(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                Material.id_material,
                Material.material_name,
                Material.unit,
                Material.price,
                Supplier.supplier_name
            FROM Material
            INNER JOIN Supplier
            ON Material.id_supplier = Supplier.id_supplier
            ORDER BY Material.material_name
            """
        )

        materials = cursor.fetchall()

        cursor.close()
        connection.close()

        return materials

    def add_work_type_to_order(self, order_id, work_type_id):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO OrderWorkType
                (id_order, id_work_type)
                VALUES (%s, %s)
                """,
                (order_id, work_type_id)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_work_types_by_order(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                WorkType.work_name,
                WorkType.description,
                WorkType.cost,
                Employee.full_name,
                Employee.position,
                WorkTypeEmployee.role_in_work
            FROM OrderWorkType
            INNER JOIN WorkType
            ON OrderWorkType.id_work_type = WorkType.id_work_type
            LEFT JOIN WorkTypeEmployee
            ON WorkType.id_work_type = WorkTypeEmployee.id_work_type
            LEFT JOIN Employee
            ON WorkTypeEmployee.id_employee = Employee.id_employee
            WHERE OrderWorkType.id_order = %s
            ORDER BY WorkType.work_name
            """,
            (order_id,)
        )

        work_types = cursor.fetchall()

        cursor.close()
        connection.close()

        return work_types

    def get_materials_by_order(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                WorkType.work_name,
                Material.material_name,
                Material.unit,
                Material.price,
                WorkTypeMaterial.quantity,
                Supplier.supplier_name,
                Material.price * WorkTypeMaterial.quantity AS total_material_cost
            FROM OrderWorkType
            INNER JOIN WorkType
            ON OrderWorkType.id_work_type = WorkType.id_work_type

            INNER JOIN WorkTypeMaterial
            ON WorkType.id_work_type = WorkTypeMaterial.id_work_type

            INNER JOIN Material
            ON WorkTypeMaterial.id_material = Material.id_material

            INNER JOIN Supplier
            ON Material.id_supplier = Supplier.id_supplier

            WHERE OrderWorkType.id_order = %s

            ORDER BY WorkType.work_name, Material.material_name
            """,
            (order_id,)
        )

        materials = cursor.fetchall()

        cursor.close()
        connection.close()

        return materials

    def update_customer_by_order(self, order_id, customer_name, customer_contact):
        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                UPDATE Customer
                INNER JOIN Orders
                ON Customer.id_customer = Orders.id_customer
                SET
                    Customer.full_name = %s,
                    Customer.contact_data = %s
                WHERE Orders.id_order = %s
                """,
                (customer_name, customer_contact, order_id)
            )

            connection.commit()

        except Exception as error:
            connection.rollback()
            raise error

        finally:
            cursor.close()
            connection.close()

    def get_order_details_by_id(self, order_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                Customer.full_name,
                Customer.contact_data,
                Orders.address,
                Orders.area,
                Orders.project_type,
                Orders.price_segment,
                Orders.material_type,
                Orders.status,
                Orders.start_date,
                Orders.end_date,
                Orders.total_cost
            FROM Orders
            INNER JOIN Customer
            ON Orders.id_customer = Customer.id_customer
            WHERE Orders.id_order = %s
            """,
            (order_id,)
        )

        order_details = cursor.fetchone()

        cursor.close()
        connection.close()

        return order_details