import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from controllers.order_controller import OrderController


class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Інформаційна система будівельної компанії")
        self.window.geometry("1100x850")
        self.controller = OrderController()
        self.configure_styles()

        self.customer_name_entry = None
        self.customer_contact_entry = None
        self.address_entry = None
        self.land_area_entry = None

        self.project_type_combo = None
        self.price_segment_combo = None
        self.material_type_combo = None

        self.status_combo = None

        self.start_date_entry = None
        self.end_date_entry = None
        self.prepayment_entry = None

        self.create_contract_button = None
        self.show_orders_button = None
        self.search_orders_button = None

        self.delete_order_entry = None
        self.delete_order_button = None
        self.update_order_button = None
        self.clear_form_button = None

        self.show_payments_button = None

        self.show_employees_button = None
        self.employees_table = None
        self.employee_name_entry = None
        self.employee_position_entry = None
        self.employee_salary_entry = None

        self.add_employee_button = None
        self.delete_employee_button = None

        self.show_work_types_button = None
        self.work_types_table = None
        self.work_name_entry = None
        self.work_description_entry = None
        self.work_cost_entry = None
        self.add_work_type_button = None
        self.delete_work_type_button = None
        self.show_materials_button = None

        self.materials_table = None
        self.total_materials_cost_label = None
        self.current_materials_cost = 0

        self.work_type_id_entry = None
        self.employee_id_entry = None
        self.role_in_work_combo = None

        self.assign_employee_button = None
        self.show_assignments_button = None
        self.assignments_table = None

        self.payment_date_entry = None
        self.payment_amount_entry = None
        self.payment_type_combo = None

        self.payments_table = None
        self.total_payments_label = None
        self.balance_label = None

        self.add_payment_button = None
        self.show_order_works_button = None
        self.order_works_table = None
        self.total_works_cost_label = None

        self.current_works_cost = 0
        self.estimate_total_label = None

        self.orders_table = None

        self.total_orders_label = None
        self.total_orders_cost_label = None
        self.total_paid_label = None
        self.total_debt_label = None
        self.status_statistics_label = None

        self.original_order_data = None
        self.selected_order_id = None

        self.work_type_combo = None
        self.employee_combo = None

        self.notebook = None

        self.orders_tab = None
        self.payments_tab = None
        self.workers_tab = None
        self.materials_tab = None
        self.analytics_tab = None

        self.employee_contact_entry = None

        self.order_combo = None
        self.work_type_order_combo = None
        self.add_work_to_order_button = None

        self.create_widgets()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        self.window.configure(bg="#f8f9fa")

        style.configure(
            "TNotebook",
            background="#f8f9fa",
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 10),
            padding=(12, 6),
            background="#e9ecef",
            foreground="#212529"
        )

        style.map(
            "TNotebook.Tab",
            background=[("selected", "#ffffff")],
            foreground=[("selected", "#0066cc")]
        )

        style.configure(
            "TLabelframe",
            background="#f8f9fa",
            bordercolor="#ced4da",
            relief="solid"
        )

        style.configure(
            "TLabelframe.Label",
            background="#f8f9fa",
            foreground="#212529",
            font=("Segoe UI", 11, "bold")
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=(10, 6),
            background="#e9ecef",
            foreground="#212529",
            borderwidth=0
        )

        style.map(
            "TButton",
            background=[("active", "#dee2e6")]
        )

        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(10, 7),
            background="#ff6b00",
            foreground="#ffffff",
            borderwidth=0
        )

        style.map(
            "Accent.TButton",
            background=[("active", "#e85f00")],
            foreground=[("active", "#ffffff")]
        )

        style.configure(
            "Danger.TButton",
            font=("Segoe UI", 10),
            padding=(10, 6),
            background="#f8d7da",
            foreground="#842029",
            borderwidth=0
        )

        style.map(
            "Danger.TButton",
            background=[("active", "#f1aeb5")]
        )

        style.configure(
            "Treeview",
            font=("Segoe UI", 9),
            rowheight=24,
            background="#ffffff",
            fieldbackground="#ffffff",
            foreground="#212529"
        )

        style.map(
            "Treeview",
            background=[("selected", "#dfe6ee")],
            foreground=[("selected", "#212529")]
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 9),
            background="#f1f3f5",
            foreground="#212529",
            padding=(4, 4)
        )

    def create_widgets(self):
        title_label = tk.Label(
            self.window,
            text="Складання будівельного контракту",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=15)

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.orders_tab = tk.Frame(self.notebook)
        self.payments_tab = tk.Frame(self.notebook)
        self.workers_tab = tk.Frame(self.notebook)
        self.materials_tab = tk.Frame(self.notebook)
        self.analytics_tab = tk.Frame(self.notebook)

        self.notebook.add(self.orders_tab, text="Замовлення")
        self.notebook.add(self.payments_tab, text="Платежі")
        self.notebook.add(self.workers_tab, text="Роботи і працівники")
        self.notebook.add(self.materials_tab, text="Матеріали")
        self.notebook.add(self.analytics_tab, text="Аналітика")

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

        left_panel = tk.Frame(self.orders_tab)
        left_panel.pack(side="left", padx=20, pady=10, anchor="n")

        form_frame = tk.LabelFrame(
            left_panel,
            text="Дані замовлення",
            padx=15,
            pady=10
        )
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="ПІБ замовника:").grid(row=0, column=0, sticky="w", pady=5)
        self.customer_name_entry = tk.Entry(form_frame, width=30)
        self.customer_name_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Контактні дані:").grid(row=1, column=0, sticky="w", pady=5)
        self.customer_contact_entry = tk.Entry(form_frame, width=30)
        self.customer_contact_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Адреса об'єкта:").grid(row=2, column=0, sticky="w", pady=5)
        self.address_entry = tk.Entry(form_frame, width=30)
        self.address_entry.grid(row=2, column=1, pady=5)

        tk.Label(form_frame, text="Площа ділянки:").grid(row=3, column=0, sticky="w", pady=5)
        self.land_area_entry = tk.Entry(form_frame, width=30)
        self.land_area_entry.grid(row=3, column=1, pady=5)

        tk.Label(form_frame, text="Тип проєкту:").grid(row=4, column=0, sticky="w", pady=5)
        self.project_type_combo = ttk.Combobox(
            form_frame,
            values=["Приватний будинок", "Офісна будівля", "Котедж", "Гараж", "Торговий центр"],
            width=27,
            state="readonly"
        )
        self.project_type_combo.grid(row=4, column=1, pady=5)

        tk.Label(form_frame, text="Ціновий сегмент:").grid(row=5, column=0, sticky="w", pady=5)
        self.price_segment_combo = ttk.Combobox(
            form_frame,
            values=["Економ", "Стандарт", "Преміум"],
            width=27,
            state="readonly"
        )
        self.price_segment_combo.grid(row=5, column=1, pady=5)

        tk.Label(form_frame, text="Тип матеріалів:").grid(row=6, column=0, sticky="w", pady=5)
        self.material_type_combo = ttk.Combobox(
            form_frame,
            values=["Базові матеріали", "Стандартні матеріали", "Преміальні матеріали"],
            width=27,
            state="readonly"
        )
        self.material_type_combo.grid(row=6, column=1, pady=5)

        tk.Label(form_frame, text="Дата початку (РРРР-ММ-ДД):").grid(row=7, column=0, sticky="w", pady=5)
        self.start_date_entry = tk.Entry(form_frame, width=30)
        self.start_date_entry.grid(row=7, column=1, pady=5)

        tk.Label(form_frame, text="Дата завершення (РРРР-ММ-ДД):").grid(row=8, column=0, sticky="w", pady=5)
        self.end_date_entry = tk.Entry(form_frame, width=30)
        self.end_date_entry.grid(row=8, column=1, pady=5)

        tk.Label(form_frame, text="Розрахована вартість:").grid(row=9, column=0, sticky="w", pady=5)
        self.prepayment_entry = tk.Entry(
            form_frame,
            width=30,
            state="readonly"
        )
        self.prepayment_entry.grid(row=9, column=1, pady=5)

        tk.Label(form_frame, text="Статус:").grid(row=10, column=0, sticky="w", pady=5)

        self.status_combo = ttk.Combobox(
            form_frame,
            values=["Нове", "У роботі", "Завершено", "Скасовано"],
            width=27,
            state="readonly"
        )
        self.status_combo.grid(row=10, column=1, pady=5)
        self.status_combo.set("Нове")

        buttons_frame = tk.Frame(left_panel)
        buttons_frame.pack(pady=10)

        self.create_contract_button = ttk.Button(
            buttons_frame,
            text="Сформувати контракт",
            width=25,
            command=self.create_contract,
            style="Accent.TButton"
        )
        self.create_contract_button.pack(pady=5)

        self.show_orders_button = ttk.Button(
            buttons_frame,
            text="Показати замовлення",
            width=25,
            command=self.show_orders
        )
        self.show_orders_button.pack(pady=5)

        self.search_orders_button = ttk.Button(
            buttons_frame,
            text="Знайти замовлення",
            width=25,
            command=self.search_orders
        )
        self.search_orders_button.pack(pady=5)

        self.delete_order_button = ttk.Button(
            buttons_frame,
            text="Видалити замовлення",
            width=25,
            command=self.delete_order,
            style="Danger.TButton"
        )
        self.delete_order_button.pack(pady=5)

        bottom_buttons_frame = tk.Frame(buttons_frame)
        bottom_buttons_frame.pack(pady=5)

        self.update_order_button = ttk.Button(
            bottom_buttons_frame,
            text="Оновити",
            width=12,
            command=self.update_order
        )
        self.update_order_button.pack(side="left", padx=3)

        self.clear_form_button = ttk.Button(
            bottom_buttons_frame,
            text="Очистити",
            width=12,
            command=self.clear_form
        )
        self.clear_form_button.pack(side="left", padx=3)

        employees_section = tk.LabelFrame(
            self.workers_tab,
            text="Працівники",
            padx=10,
            pady=10
        )
        employees_section.pack(fill="x", padx=10, pady=5)

        employee_form = tk.Frame(employees_section)
        employee_form.pack(side="left", padx=10, pady=5, anchor="n")

        tk.Label(employee_form, text="ПІБ:").grid(row=0, column=0, sticky="w", pady=3)
        self.employee_name_entry = tk.Entry(employee_form, width=25)
        self.employee_name_entry.grid(row=0, column=1, pady=3)

        tk.Label(employee_form, text="Посада:").grid(row=1, column=0, sticky="w", pady=3)
        self.employee_position_entry = tk.Entry(employee_form, width=25)
        self.employee_position_entry.grid(row=1, column=1, pady=3)

        tk.Label(employee_form, text="Зарплата:").grid(row=2, column=0, sticky="w", pady=3)
        self.employee_salary_entry = tk.Entry(employee_form, width=25)
        self.employee_salary_entry.grid(row=2, column=1, pady=3)

        tk.Label(employee_form, text="Контакти:").grid(row=3, column=0, sticky="w", pady=3)
        self.employee_contact_entry = tk.Entry(employee_form, width=25)
        self.employee_contact_entry.grid(row=3, column=1, pady=3)

        self.add_employee_button = ttk.Button(
            employee_form,
            text="Додати працівника",
            width=25,
            command=self.add_employee
        )
        self.add_employee_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.delete_employee_button = ttk.Button(
            employee_form,
            text="Видалити працівника",
            width=25,
            command=self.delete_employee
        )
        self.delete_employee_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.show_employees_button = ttk.Button(
            employees_section,
            text="Показати працівників",
            width=25,
            command=self.show_employees
        )
        self.show_employees_button.pack(side="left", padx=10, pady=5, anchor="n")

        employees_table_frame = tk.Frame(employees_section)
        employees_table_frame.pack(
            side="left",
            padx=(20, 10),
            pady=10,
            fill="both",
            expand=True
        )

        employee_columns = (
            "ID",
            "ПІБ",
            "Посада",
            "Зарплата"
        )

        self.employees_table = ttk.Treeview(
            employees_table_frame,
            columns=employee_columns,
            show="headings",
            height=3
        )

        for column in employee_columns:
            self.employees_table.heading(column, text=column)

            if column == "ID":
                self.employees_table.column(column, width=50, anchor="center")
            elif column == "ПІБ":
                self.employees_table.column(column, width=260, anchor="w")
            else:
                self.employees_table.column(column, width=150, anchor="center")

        employees_scrollbar = ttk.Scrollbar(
            employees_table_frame,
            orient="vertical",
            command=self.employees_table.yview
        )

        self.employees_table.configure(yscrollcommand=employees_scrollbar.set)

        employees_scrollbar.pack(side="right", fill="y")
        self.employees_table.pack(fill="both", expand=True)

        work_types_section = tk.LabelFrame(
            self.workers_tab,
            text="Види робіт",
            padx=10,
            pady=10
        )
        work_types_section.pack(fill="x", padx=10, pady=5)

        work_type_form = tk.Frame(work_types_section)
        work_type_form.pack(side="left", padx=10, pady=5, anchor="n")

        tk.Label(work_type_form, text="Назва:").grid(row=0, column=0, sticky="w", pady=3)
        self.work_name_entry = tk.Entry(work_type_form, width=25)
        self.work_name_entry.grid(row=0, column=1, pady=3)

        tk.Label(work_type_form, text="Опис:").grid(row=1, column=0, sticky="w", pady=3)
        self.work_description_entry = tk.Entry(work_type_form, width=25)
        self.work_description_entry.grid(row=1, column=1, pady=3)

        tk.Label(work_type_form, text="Вартість:").grid(row=2, column=0, sticky="w", pady=3)
        self.work_cost_entry = tk.Entry(work_type_form, width=25)
        self.work_cost_entry.grid(row=2, column=1, pady=3)

        self.add_work_type_button = ttk.Button(
            work_type_form,
            text="Додати вид роботи",
            width=25,
            command=self.add_work_type
        )
        self.add_work_type_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.delete_work_type_button = ttk.Button(
            work_type_form,
            text="Видалити вид роботи",
            width=25,
            command=self.delete_work_type
        )
        self.delete_work_type_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.show_work_types_button = ttk.Button(
            work_types_section,
            text="Показати види робіт",
            width=25,
            command=self.show_work_types
        )
        self.show_work_types_button.pack(side="left", padx=10, pady=5, anchor="n")

        work_types_table_frame = tk.Frame(work_types_section)
        work_types_table_frame.pack(
            side="left",
            padx=(20, 10),
            pady=10,
            fill="both",
            expand=True
        )

        work_type_columns = (
            "ID",
            "Назва",
            "Опис",
            "Вартість"
        )

        self.work_types_table = ttk.Treeview(
            work_types_table_frame,
            columns=work_type_columns,
            show="headings",
            height=3
        )

        for column in work_type_columns:
            self.work_types_table.heading(column, text=column)

            if column == "ID":
                self.work_types_table.column(column, width=50, anchor="center")
            elif column == "Назва":
                self.work_types_table.column(column, width=220, anchor="w")
            elif column == "Опис":
                self.work_types_table.column(column, width=420, anchor="w")
            else:
                self.work_types_table.column(column, width=120, anchor="center")

        work_types_scrollbar = ttk.Scrollbar(
            work_types_table_frame,
            orient="vertical",
            command=self.work_types_table.yview
        )

        self.work_types_table.configure(yscrollcommand=work_types_scrollbar.set)

        work_types_scrollbar.pack(side="right", fill="y")
        self.work_types_table.pack(fill="both", expand=True)

        materials_table_frame = tk.Frame(self.materials_tab)
        materials_table_frame.pack(pady=10, fill="both", expand=True)

        material_columns = (
            "Вид роботи",
            "Матеріал",
            "Одиниця",
            "Ціна",
            "Кількість",
            "Постачальник",
            "Загальна вартість"
        )

        self.materials_table = ttk.Treeview(
            materials_table_frame,
            columns=material_columns,
            show="headings",
            height=12
        )

        for column in material_columns:
            self.materials_table.heading(column, text=column)

            if column == "Вид роботи":
                self.materials_table.column(column, width=180, anchor="w")
            elif column == "Матеріал":
                self.materials_table.column(column, width=180, anchor="w")
            elif column == "Постачальник":
                self.materials_table.column(column, width=180, anchor="w")
            elif column == "Загальна вартість":
                self.materials_table.column(column, width=150, anchor="center")
            else:
                self.materials_table.column(column, width=100, anchor="center")

        materials_scrollbar = ttk.Scrollbar(
            materials_table_frame,
            orient="vertical",
            command=self.materials_table.yview
        )

        self.materials_table.configure(yscrollcommand=materials_scrollbar.set)

        materials_scrollbar.pack(side="right", fill="y")
        self.materials_table.pack(fill="both", expand=True)

        self.total_materials_cost_label = tk.Label(
            self.materials_tab,
            text="Загальна вартість матеріалів: 0 грн",
            font=("Segoe UI", 10, "bold")
        )
        self.total_materials_cost_label.pack(pady=5)

        order_works_section = tk.LabelFrame(
            self.workers_tab,
            text="Роботи замовлення",
            padx=10,
            pady=10
        )
        order_works_section.pack(fill="x", padx=10, pady=5)

        order_work_frame = tk.Frame(order_works_section)
        order_work_frame.pack(
            side="left",
            padx=10,
            pady=5,
            anchor="n"
        )

        tk.Label(order_work_frame, text="Замовлення:").grid(row=0, column=0, sticky="w", pady=3)

        self.order_combo = ttk.Combobox(
            order_work_frame,
            width=35,
            state="readonly"
        )
        self.order_combo.grid(row=1, column=0, pady=3)

        tk.Label(order_work_frame, text="Вид роботи:").grid(row=2, column=0, sticky="w", pady=3)

        self.work_type_order_combo = ttk.Combobox(
            order_work_frame,
            width=35,
            state="readonly"
        )
        self.work_type_order_combo.grid(row=3, column=0, pady=3)

        order_buttons_frame = tk.Frame(order_works_section)
        order_buttons_frame.pack(
            side="left",
            padx=10,
            pady=5,
            anchor="n"
        )

        self.add_work_to_order_button = ttk.Button(
            order_buttons_frame,
            text="Додати роботу до замовлення",
            width=25,
            command=self.add_work_type_to_order
        )
        self.add_work_to_order_button.pack(pady=3)

        self.show_order_works_button = ttk.Button(
            order_buttons_frame,
            text="Показати роботи замовлення",
            width=25,
            command=self.show_order_works
        )
        self.show_order_works_button.pack(pady=3)

        order_works_table_frame = tk.Frame(order_works_section)
        order_works_table_frame.pack(pady=10, fill="both", expand=True)

        order_work_columns = (
            "Назва роботи",
            "Опис",
            "Вартість",
            "Працівник",
            "Посада",
            "Роль"
        )

        self.order_works_table = ttk.Treeview(
            order_works_table_frame,
            columns=order_work_columns,
            show="headings",
            height=2
        )

        for column in order_work_columns:
            self.order_works_table.heading(column, text=column)

            if column == "Назва роботи":
                self.order_works_table.column(column, width=180, anchor="w")
            elif column == "Опис":
                self.order_works_table.column(column, width=300, anchor="w")
            elif column == "Вартість":
                self.order_works_table.column(column, width=100, anchor="center")
            elif column == "Роль":
                self.order_works_table.column(column, width=120, anchor="center")
            else:
                self.order_works_table.column(column, width=150, anchor="center")

        order_works_scrollbar = ttk.Scrollbar(
            order_works_table_frame,
            orient="vertical",
            command=self.order_works_table.yview
        )

        self.order_works_table.configure(yscrollcommand=order_works_scrollbar.set)

        order_works_scrollbar.pack(side="right", fill="y")
        self.order_works_table.pack(fill="both", expand=True)

        self.total_works_cost_label = tk.Label(
            order_works_section,
            text="Загальна вартість робіт: 0 грн",
            font=("Segoe UI", 10, "bold")
        )
        self.total_works_cost_label.pack(pady=2)

        self.estimate_total_label = tk.Label(
            order_works_section,
            text="Загальний кошторис: 0 грн",
            font=("Segoe UI", 11, "bold")
        )
        self.estimate_total_label.pack(pady=2)

        assignments_section = tk.LabelFrame(
            self.workers_tab,
            text="Призначення працівників",
            padx=10,
            pady=10
        )
        assignments_section.pack(fill="x", padx=10, pady=5)

        assign_frame = tk.Frame(assignments_section)
        assign_frame.pack(pady=5)

        tk.Label(assign_frame, text="Вид роботи:").grid(row=0, column=0, padx=5)
        self.work_type_combo = ttk.Combobox(
            assign_frame,
            width=30,
            state="readonly"
        )
        self.work_type_combo.grid(row=0, column=1, padx=5)

        tk.Label(assign_frame, text="Працівник:").grid(row=0, column=2, padx=5)
        self.employee_combo = ttk.Combobox(
            assign_frame,
            width=30,
            state="readonly"
        )
        self.employee_combo.grid(row=0, column=3, padx=5)

        tk.Label(assign_frame, text="Роль у роботі:").grid(row=0, column=4, padx=5)
        self.role_in_work_combo = ttk.Combobox(
            assign_frame,
            values=[
                "Керівник робіт",
                "Архітектор проєкту",
                "Виконроб",
                "Будівельник",
                "Монтажник",
                "Електрик",
                "Сантехнік",
                "Оздоблювальник"
            ],
            width=20,
            state="readonly"
        )
        self.role_in_work_combo.grid(row=0, column=5, padx=5)

        self.assign_employee_button = ttk.Button(
            assignments_section,
            text="Призначити працівника",
            width=25,
            command=self.assign_employee
        )
        self.assign_employee_button.pack(pady=5)

        self.show_assignments_button = ttk.Button(
            assignments_section,
            text="Показати призначення",
            width=25,
            command=self.show_assignments
        )
        self.show_assignments_button.pack(pady=5)

        assignments_table_frame = tk.Frame(assignments_section)
        assignments_table_frame.pack(pady=10, fill="both", expand=True)

        assignment_columns = (
            "Вид роботи",
            "Працівник",
            "Посада",
            "Роль"
        )

        self.assignments_table = ttk.Treeview(
            assignments_table_frame,
            columns=assignment_columns,
            show="headings",
            height=5
        )

        for column in assignment_columns:
            self.assignments_table.heading(column, text=column)

            if column == "Вид роботи":
                self.assignments_table.column(column, width=260, anchor="w")
            elif column == "Працівник":
                self.assignments_table.column(column, width=220, anchor="w")
            elif column == "Посада":
                self.assignments_table.column(column, width=160, anchor="center")
            else:
                self.assignments_table.column(column, width=140, anchor="center")

        assignments_scrollbar = ttk.Scrollbar(
            assignments_table_frame,
            orient="vertical",
            command=self.assignments_table.yview
        )

        self.assignments_table.configure(yscrollcommand=assignments_scrollbar.set)

        assignments_scrollbar.pack(side="right", fill="y")
        self.assignments_table.pack(fill="both", expand=True)

        self.load_work_and_employee_lists()

        self.load_orders_and_work_types()

        payment_frame = tk.Frame(self.payments_tab)
        payment_frame.pack(pady=5)

        tk.Label(payment_frame, text="Дата платежу:").grid(row=0, column=0, padx=5)
        self.payment_date_entry = tk.Entry(payment_frame, width=15)
        self.payment_date_entry.grid(row=0, column=1, padx=5)

        tk.Label(payment_frame, text="Сума:").grid(row=0, column=2, padx=5)
        self.payment_amount_entry = tk.Entry(payment_frame, width=15)
        self.payment_amount_entry.grid(row=0, column=3, padx=5)

        tk.Label(payment_frame, text="Тип платежу:").grid(row=0, column=4, padx=5)
        self.payment_type_combo = ttk.Combobox(
            payment_frame,
            values=["Передоплата", "Часткова оплата", "Повна оплата", "Остаточний розрахунок"],
            width=20,
            state="readonly"
        )
        self.payment_type_combo.grid(row=0, column=5, padx=5)

        self.add_payment_button = ttk.Button(
            self.payments_tab,
            text="Додати платіж",
            width=25,
            command=self.add_payment
        )
        self.add_payment_button.pack(pady=5)

        payments_table_frame = tk.Frame(self.payments_tab)
        payments_table_frame.pack(pady=10, fill="both", expand=True)

        payment_columns = (
            "ID платежу",
            "Дата",
            "Сума",
            "Тип платежу"
        )

        self.payments_table = ttk.Treeview(
            payments_table_frame,
            columns=payment_columns,
            show="headings",
            height=10
        )

        for column in payment_columns:
            self.payments_table.heading(column, text=column)

            if column == "ID платежу":
                self.payments_table.column(column, width=80, anchor="center")
            elif column == "Тип платежу":
                self.payments_table.column(column, width=220, anchor="w")
            else:
                self.payments_table.column(column, width=140, anchor="center")

        payments_scrollbar = ttk.Scrollbar(
            payments_table_frame,
            orient="vertical",
            command=self.payments_table.yview
        )

        self.payments_table.configure(yscrollcommand=payments_scrollbar.set)

        payments_scrollbar.pack(side="right", fill="y")
        self.payments_table.pack(fill="both", expand=True)

        self.total_payments_label = tk.Label(
            self.payments_tab,
            text="Всього сплачено: 0 грн",
            font=("Segoe UI", 10, "bold")
        )
        self.total_payments_label.pack(pady=5)

        self.balance_label = tk.Label(
            self.payments_tab,
            text="Залишок до оплати: 0 грн",
            font=("Segoe UI", 10, "bold")
        )
        self.balance_label.pack(pady=5)

        table_frame = tk.Frame(self.orders_tab)
        table_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        columns = (
            "ID",
            "Замовник",
            "Адреса",
            "Площа",
            "Тип проєкту",
            "Статус",
            "Дата початку",
            "Дата завершення"
        )
        self.orders_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        self.orders_table.tag_configure("new", background="#e7f1ff")
        self.orders_table.tag_configure("in_progress", background="#fff3cd")
        self.orders_table.tag_configure("completed", background="#d1e7dd")
        self.orders_table.tag_configure("cancelled", background="#f8d7da")

        for column in columns:
            self.orders_table.heading(column, text=column)
            self.orders_table.column(column, width=120, anchor="center")

        self.orders_table.column("ID", width=35, anchor="center")
        self.orders_table.column("Замовник", width=170, anchor="w")
        self.orders_table.column("Адреса", width=280, anchor="w")
        self.orders_table.column("Площа", width=80)
        self.orders_table.column("Тип проєкту", width=130)
        self.orders_table.column("Статус", width=100)
        self.orders_table.column("Дата початку", width=110)
        self.orders_table.column("Дата завершення", width=120)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.orders_table.yview
        )

        self.orders_table.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.orders_table.pack(fill="both", expand=True)
        self.orders_table.bind("<<TreeviewSelect>>", self.on_order_select)
        #self.window.bind("<Button-1>", self.clear_selection)

        self.show_assignments()

        analytics_frame = tk.Frame(self.analytics_tab)
        analytics_frame.pack(fill="both", expand=True, padx=20, pady=20)

        analytics_title = tk.Label(
            analytics_frame,
            text="Аналітика системи",
            font=("Segoe UI", 16, "bold")
        )
        analytics_title.pack(pady=10)

        self.total_orders_label = tk.Label(
            analytics_frame,
            text="Кількість замовлень: 0",
            font=("Segoe UI", 12)
        )
        self.total_orders_label.pack(pady=5)

        self.total_orders_cost_label = tk.Label(
            analytics_frame,
            text="Загальна вартість замовлень: 0 грн",
            font=("Segoe UI", 12)
        )
        self.total_orders_cost_label.pack(pady=5)

        self.total_paid_label = tk.Label(
            analytics_frame,
            text="Загальна сума оплат: 0 грн",
            font=("Segoe UI", 12)
        )
        self.total_paid_label.pack(pady=5)

        self.total_debt_label = tk.Label(
            analytics_frame,
            text="Загальна заборгованість: 0 грн",
            font=("Segoe UI", 12)
        )
        self.total_debt_label.pack(pady=5)

        self.status_statistics_label = tk.Label(
            analytics_frame,
            text="Статистика статусів:",
            font=("Segoe UI", 12, "bold"),
            justify="left"
        )
        self.status_statistics_label.pack(pady=10)
        self.update_analytics()

    def create_contract(self):
        try:
            address = self.address_entry.get().strip()
            land_area_text = self.land_area_entry.get().strip()

            if not land_area_text:
                messagebox.showerror(
                    "Помилка введення",
                    "Введіть площу ділянки."
                )
                return

            land_area = float(land_area_text)

            if land_area <= 0:
                messagebox.showerror(
                    "Помилка введення",
                    "Площа ділянки має бути числом більшим за 0."
                )
                return

            project_type = self.project_type_combo.get()
            price_segment = self.price_segment_combo.get()
            material_type = self.material_type_combo.get()
            status = self.status_combo.get()
            start_date = self.start_date_entry.get().strip()
            end_date = self.end_date_entry.get().strip()
            prepayment = 0
            customer_name = self.customer_name_entry.get().strip()
            customer_contact = self.customer_contact_entry.get().strip()

            if not customer_name or not customer_contact:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть ПІБ замовника та контактні дані."
                )
                return

            if not self.is_text_min_length(customer_name, 10):
                messagebox.showerror(
                    "Помилка введення",
                    "ПІБ замовника має містити не менше 10 символів."
                )
                return

            if not self.is_text_min_length(customer_contact, 7):
                messagebox.showerror(
                    "Помилка введення",
                    "Контактні дані мають містити не менше 7 символів."
                )
                return

            if not self.is_text_min_length(address, 12):
                messagebox.showerror(
                    "Помилка введення",
                    "Адреса об'єкта має містити не менше 12 символів."
                )
                return

            if not address or not project_type or not price_segment or not material_type or not status or not start_date or not end_date:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть адресу, тип проєкту, ціновий сегмент, тип матеріалів, статус, дату початку та дату завершення."
                )
                return

            if not self.is_valid_date(start_date) or not self.is_valid_date(end_date):
                messagebox.showerror(
                    "Помилка введення",
                    "Дата має бути у форматі РРРР-ММ-ДД, наприклад 2026-03-01."
                )
                return

            if not self.is_valid_date_period(start_date, end_date):
                messagebox.showerror(
                    "Помилка введення",
                    "Дата завершення не може бути раніше дати початку."
                )
                return

            order = self.controller.create_order(
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

            self.controller.calculate_cost(order)

            self.set_total_cost(order.cost)

            self.controller.save_order(
                customer_name,
                customer_contact,
                order
            )
            self.controller.create_contract(order)

            orders = self.controller.get_all_orders()
            self.fill_orders_table(orders)
            self.load_orders_and_work_types()
            self.update_analytics()

            self.clear_fields()

            messagebox.showinfo(
                "Успішно",
                "Контракт сформовано, а дані збережено в базі даних."
            )

        except ValueError:
            messagebox.showerror(
                "Помилка введення",
                "Площа ділянки має бути числом."
            )

    def show_orders(self):
        orders = self.controller.get_all_orders()
        self.fill_orders_table(orders)

    def search_orders(self):
        customer_name = self.customer_name_entry.get().strip()

        if not customer_name:
            messagebox.showerror(
                "Помилка пошуку",
                "Введіть ПІБ замовника для пошуку."
            )
            return

        if len(customer_name) < 3:
            messagebox.showerror(
                "Помилка пошуку",
                "Для пошуку введіть не менше 3 символів."
            )
            return

        orders = self.controller.search_orders_by_customer(customer_name)

        if not orders:
            messagebox.showinfo(
                "Результат пошуку",
                "Замовлення за таким ПІБ не знайдено."
            )
            return

        self.fill_orders_table(orders)

    def fill_orders_table(self, orders):
        for row in self.orders_table.get_children():
            self.orders_table.delete(row)

        for order in orders:
            status = order[5]

            if status == "Нове":
                tag = "new"
            elif status == "У роботі":
                tag = "in_progress"
            elif status == "Завершено":
                tag = "completed"
            elif status == "Скасовано":
                tag = "cancelled"
            else:
                tag = ""

            self.orders_table.insert("", "end", values=order, tags=(tag,))

    def clear_fields(self):
        self.customer_name_entry.delete(0, tk.END)
        self.customer_contact_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.land_area_entry.delete(0, tk.END)
        self.project_type_combo.set("")
        self.price_segment_combo.set("")
        self.material_type_combo.set("")
        self.status_combo.set("Нове")

        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
        self.set_total_cost("")
        self.original_order_data = None

    def set_total_cost(self, value):
        self.prepayment_entry.config(state="normal")
        self.prepayment_entry.delete(0, tk.END)
        self.prepayment_entry.insert(0, str(value))
        self.prepayment_entry.config(state="readonly")

    def is_valid_date(self, date_text):
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def is_valid_date_period(self, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return end >= start

    def is_text_min_length(self, text, min_length):
        return len(text.strip()) >= min_length

    def on_order_select(self, _event):
        selected_item = self.orders_table.selection()

        if not selected_item:
            return

        order_values = self.orders_table.item(
            selected_item[0],
            "values"
        )

        order_id = int(order_values[0])
        self.selected_order_id = order_id
        order_details = self.controller.get_order_details_by_id(order_id)

        if not order_details:
            return

        def value(data):
            return "" if data is None else str(data)

        self.customer_name_entry.delete(0, tk.END)
        self.customer_name_entry.insert(0, value(order_details[0]))

        self.customer_contact_entry.delete(0, tk.END)
        self.customer_contact_entry.insert(0, value(order_details[1]))

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, value(order_details[2]))

        self.land_area_entry.delete(0, tk.END)
        self.land_area_entry.insert(0, value(order_details[3]))

        self.project_type_combo.set(value(order_details[4]))
        self.price_segment_combo.set(value(order_details[5]))
        self.material_type_combo.set(value(order_details[6]))

        self.status_combo.set(value(order_details[7]))

        self.start_date_entry.delete(0, tk.END)
        self.start_date_entry.insert(0, value(order_details[8]))

        self.end_date_entry.delete(0, tk.END)
        self.end_date_entry.insert(0, value(order_details[9]))

        self.set_total_cost(value(order_details[10]))
        self.original_order_data = (
            value(order_details[0]),
            value(order_details[1]),
            value(order_details[2]),
            f"{float(order_details[3]):.2f}",
            value(order_details[4]),
            value(order_details[5]),
            value(order_details[6]),
            value(order_details[7]),
            value(order_details[8]),
            value(order_details[9])
        )

        self.order_combo.set(
            f"{order_id} - {order_values[1]}"
        )

        try:
            self.show_payments()
        except Exception:
            pass

        try:
            self.show_materials()
        except Exception:
            pass

        try:
            self.show_order_works()
        except Exception:
            pass

    def delete_order(self):
        try:
            order_id = self.selected_order_id

            if order_id is None:
                messagebox.showwarning(
                    "Помилка",
                    "Будь ласка, виберіть замовлення в таблиці."
                )
                return

            confirm = messagebox.askyesno(
                "Підтвердження видалення",
                f"Ви дійсно хочете видалити замовлення з ID {order_id}?"
            )

            if not confirm:
                return

            self.controller.delete_order(order_id)

            messagebox.showinfo(
                "Успішно",
                f"Замовлення з ID {order_id} видалено."
            )

            orders = self.controller.get_all_orders()
            self.fill_orders_table(orders)
            if not orders:
                self.selected_order_id = None
                self.clear_form()
            self.load_orders_and_work_types()
            self.update_analytics()


        except Exception as error:
            messagebox.showerror(
                "Помилка видалення",
                f"Не вдалося видалити замовлення: {error}"
            )

    def update_order(self):
        try:
            selected_item = self.orders_table.selection()

            if not selected_item:
                messagebox.showwarning(
                    "Помилка",
                    "Будь ласка, виберіть замовлення в таблиці."
                )
                return

            order_values = self.orders_table.item(selected_item[0], "values")
            order_id = int(order_values[0])

            address = self.address_entry.get().strip()
            land_area_text = self.land_area_entry.get().strip()

            if not land_area_text:
                messagebox.showerror(
                    "Помилка введення",
                    "Введіть площу ділянки."
                )
                return

            land_area = float(land_area_text)

            if land_area <= 0:
                messagebox.showerror(
                    "Помилка введення",
                    "Площа ділянки має бути числом більшим за 0."
                )
                return

            project_type = self.project_type_combo.get()
            price_segment = self.price_segment_combo.get()
            material_type = self.material_type_combo.get()
            status = self.status_combo.get()
            start_date = self.start_date_entry.get().strip()
            end_date = self.end_date_entry.get().strip()
            prepayment = 0

            customer_name = self.customer_name_entry.get().strip()
            customer_contact = self.customer_contact_entry.get().strip()
            current_data = (
                customer_name,
                customer_contact,
                address,
                f"{land_area:.2f}",
                project_type,
                price_segment,
                material_type,
                status,
                start_date,
                end_date
            )

            if current_data == self.original_order_data:
                messagebox.showinfo(
                    "Без змін",
                    "Ви не внесли жодних змін у замовлення."
                )
                return

            if not address or not project_type or not price_segment or not material_type or not status or not start_date or not end_date:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть адресу, тип проєкту, ціновий сегмент, тип матеріалів, статус, дату початку та дату завершення."
                )
                return

            if not customer_name or not customer_contact:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть ПІБ замовника та контактні дані."
                )
                return

            if not self.is_text_min_length(customer_name, 10):
                messagebox.showerror(
                    "Помилка введення",
                    "ПІБ замовника має містити не менше 10 символів."
                )
                return

            if not self.is_text_min_length(customer_contact, 7):
                messagebox.showerror(
                    "Помилка введення",
                    "Контактні дані мають містити не менше 7 символів."
                )
                return

            if not self.is_text_min_length(address, 12):
                messagebox.showerror(
                    "Помилка введення",
                    "Адреса об'єкта має містити не менше 12 символів."
                )
                return

            if not self.is_valid_date(start_date) or not self.is_valid_date(end_date):
                messagebox.showerror(
                    "Помилка введення",
                    "Дата має бути у форматі РРРР-ММ-ДД, наприклад 2026-03-01."
                )
                return

            if not self.is_valid_date_period(start_date, end_date):
                messagebox.showerror(
                    "Помилка введення",
                    "Дата завершення не може бути раніше дати початку."
                )
                return

            order = self.controller.create_order(
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

            self.controller.calculate_cost(order)

            self.set_total_cost(order.cost)

            self.controller.update_order(order_id, order)

            self.controller.update_customer_by_order(
                order_id,
                customer_name,
                customer_contact
            )

            orders = self.controller.get_all_orders()
            self.fill_orders_table(orders)
            self.load_orders_and_work_types()
            self.update_analytics()

            messagebox.showinfo(
                "Успішно",
                f"Замовлення з ID {order_id} оновлено."
            )

        except ValueError:
            messagebox.showerror(
                "Помилка введення",
                "Площа ділянки має бути числом."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка оновлення",
                f"Не вдалося оновити замовлення: {error}"
            )

    def clear_form(self):
        self.customer_name_entry.delete(0, tk.END)
        self.customer_contact_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.land_area_entry.delete(0, tk.END)

        self.project_type_combo.set("")
        self.price_segment_combo.set("")
        self.material_type_combo.set("")
        self.status_combo.set("Нове")

        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)

        self.prepayment_entry.config(state="normal")
        self.prepayment_entry.delete(0, tk.END)
        self.prepayment_entry.config(state="readonly")

        self.current_works_cost = 0
        self.current_materials_cost = 0

        self.selected_order_id = None
        self.original_order_data = None

        self.order_combo.set("")
        self.work_type_order_combo.set("")

        for row in self.payments_table.get_children():
            self.payments_table.delete(row)

        for row in self.materials_table.get_children():
            self.materials_table.delete(row)

        for row in self.order_works_table.get_children():
            self.order_works_table.delete(row)

        self.total_payments_label.config(
            text="Всього сплачено: 0 грн"
        )

        self.balance_label.config(
            text="Залишок до оплати: 0 грн"
        )

        self.total_materials_cost_label.config(
            text="Загальна вартість матеріалів: 0 грн"
        )

        self.total_works_cost_label.config(
            text="Загальна вартість робіт: 0 грн"
        )

        self.estimate_total_label.config(
            text="Загальний кошторис: 0 грн"
        )

        if self.total_works_cost_label:
            self.total_works_cost_label.config(
                text="Загальна вартість робіт: 0 грн"
            )

        if self.total_materials_cost_label:
            self.total_materials_cost_label.config(
                text="Загальна вартість матеріалів: 0 грн"
            )

        if self.estimate_total_label:
            self.estimate_total_label.config(
                text="Загальний кошторис: 0 грн"
            )

    def clear_selection(self, event):
        widget = event.widget

        if widget == self.orders_table:
            return

        if isinstance(widget, (tk.Entry, tk.Button, ttk.Button, ttk.Combobox)):
            return

        widget_name = str(widget).lower()

        if "combobox" in widget_name or "button" in widget_name or "entry" in widget_name:
            return

        self.orders_table.selection_remove(
            self.orders_table.selection()
        )

        self.clear_form()

    def show_payments(self):
        try:
            order_id = self.selected_order_id

            if order_id is None:
                messagebox.showwarning(
                    "Помилка",
                    "Будь ласка, виберіть замовлення в таблиці."
                )
                return

            payments = self.controller.get_payments_by_order(order_id)
            total_payments = self.controller.get_total_payments(order_id)
            balance = self.controller.get_payment_balance(order_id)

            for row in self.payments_table.get_children():
                self.payments_table.delete(row)

            for payment in payments:
                self.payments_table.insert("", "end", values=payment)

            self.total_payments_label.config(
                text=f"Всього сплачено: {total_payments} грн"
            )

            self.balance_label.config(
                text=f"Залишок до оплати: {balance} грн"
            )

            if not payments:
                messagebox.showinfo(
                    "Платежі",
                    "Для цього замовлення платежі не знайдено."
                )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося показати платежі: {error}"
            )

    def add_payment(self):
        try:
            selected_item = self.orders_table.selection()

            if not selected_item:
                messagebox.showwarning(
                    "Помилка",
                    "Будь ласка, виберіть замовлення в таблиці."
                )
                return

            order_values = self.orders_table.item(selected_item[0], "values")
            order_id = int(order_values[0])

            payment_date = self.payment_date_entry.get().strip()
            payment_type = self.payment_type_combo.get()

            try:
                amount = float(self.payment_amount_entry.get())
            except ValueError:
                messagebox.showerror(
                    "Помилка введення",
                    "Сума платежу має бути числом."
                )
                return

            if amount <= 0:
                messagebox.showerror(
                    "Помилка введення",
                    "Сума платежу має бути числом більшим за 0."
                )
                return

            balance = self.controller.get_payment_balance(order_id)

            if float(balance) <= 0:
                messagebox.showinfo(
                    "Оплата завершена",
                    "За цим замовленням уже немає залишку до оплати."
                )
                return

            if amount > float(balance):
                messagebox.showerror(
                    "Помилка платежу",
                    "Сума платежу перевищує залишок до оплати."
                )
                return

            if not payment_date or not payment_type:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть дату платежу та тип платежу."
                )
                return

            if not self.is_valid_date(payment_date):
                messagebox.showerror(
                    "Помилка введення",
                    "Дата платежу має бути у форматі РРРР-ММ-ДД, наприклад 2026-03-01."
                )
                return

            order_details = self.controller.get_order_details_by_id(order_id)
            order_start_date = str(order_details[8])

            if datetime.strptime(payment_date, "%Y-%m-%d") < datetime.strptime(order_start_date, "%Y-%m-%d"):
                messagebox.showerror(
                    "Помилка введення",
                    "Дата платежу не може бути раніше дати початку замовлення."
                )
                return

            self.controller.add_payment(
                order_id,
                payment_date,
                amount,
                payment_type
            )

            self.payment_date_entry.delete(0, tk.END)
            self.payment_amount_entry.delete(0, tk.END)
            self.payment_type_combo.set("")
            self.show_payments()
            self.update_analytics()

            messagebox.showinfo(
                "Успішно",
                "Платіж додано до вибраного замовлення."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося додати платіж: {error}"
            )

    def add_employee(self):
        try:
            full_name = self.employee_name_entry.get().strip()
            position = self.employee_position_entry.get().strip()
            salary_text = self.employee_salary_entry.get().strip()
            contact_data = self.employee_contact_entry.get().strip()

            if not full_name or not position or not salary_text or not contact_data:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть ПІБ, посаду, зарплату та контакти працівника."
                )
                return

            if not self.is_text_min_length(full_name, 10):
                messagebox.showerror(
                    "Помилка введення",
                    "ПІБ працівника має містити не менше 10 символів."
                )
                return

            if not self.is_text_min_length(position, 3):
                messagebox.showerror(
                    "Помилка введення",
                    "Посада має містити не менше 3 символів."
                )
                return

            salary = float(salary_text)

            if salary <= 0:
                messagebox.showerror(
                    "Помилка введення",
                    "Зарплата має бути числом більшим за 0."
                )
                return

            self.controller.add_employee(
                full_name,
                position,
                salary,
                contact_data
            )

            self.employee_name_entry.delete(0, tk.END)
            self.employee_position_entry.delete(0, tk.END)
            self.employee_salary_entry.delete(0, tk.END)
            self.employee_contact_entry.delete(0, tk.END)

            self.show_employees()
            self.load_work_and_employee_lists()

            messagebox.showinfo(
                "Успішно",
                "Працівника додано."
            )

        except ValueError:
            messagebox.showerror(
                "Помилка введення",
                "Зарплата має бути числом."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося додати працівника: {error}"
            )

    def delete_employee(self):
        try:
            selected = self.employees_table.selection()

            if not selected:
                messagebox.showerror(
                    "Помилка",
                    "Оберіть працівника в таблиці."
                )
                return

            values = self.employees_table.item(
                selected[0],
                "values"
            )

            employee_id = int(values[0])

            answer = messagebox.askyesno(
                "Підтвердження",
                "Видалити працівника?"
            )

            if not answer:
                return

            self.controller.delete_employee(employee_id)

            self.show_employees()
            self.load_work_and_employee_lists()

            messagebox.showinfo(
                "Успішно",
                "Працівника видалено."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                str(error)
            )

    def show_employees(self):
        try:
            employees = self.controller.get_all_employees()

            for row in self.employees_table.get_children():
                self.employees_table.delete(row)

            for employee in employees:
                self.employees_table.insert("", "end", values=employee)

            if not employees:
                messagebox.showinfo(
                    "Працівники",
                    "Працівників не знайдено."
                )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося показати працівників: {error}"
            )

    def add_work_type(self):
        try:
            work_name = self.work_name_entry.get().strip()
            description = self.work_description_entry.get().strip()
            cost_text = self.work_cost_entry.get().strip()

            if not work_name or not description or not cost_text:
                messagebox.showerror(
                    "Помилка введення",
                    "Заповніть назву, опис та вартість виду роботи."
                )
                return

            if not self.is_text_min_length(work_name, 5):
                messagebox.showerror(
                    "Помилка введення",
                    "Назва виду роботи має містити не менше 5 символів."
                )
                return

            if not self.is_text_min_length(description, 10):
                messagebox.showerror(
                    "Помилка введення",
                    "Опис виду роботи має містити не менше 10 символів."
                )
                return

            cost = float(cost_text)

            if cost <= 0:
                messagebox.showerror(
                    "Помилка введення",
                    "Вартість роботи має бути числом більшим за 0."
                )
                return

            self.controller.add_work_type(work_name, description, cost)

            self.work_name_entry.delete(0, tk.END)
            self.work_description_entry.delete(0, tk.END)
            self.work_cost_entry.delete(0, tk.END)

            self.show_work_types()
            self.load_work_and_employee_lists()
            self.load_orders_and_work_types()

            messagebox.showinfo(
                "Успішно",
                "Вид роботи додано."
            )

        except ValueError:
            messagebox.showerror(
                "Помилка введення",
                "Вартість роботи має бути числом."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося додати вид роботи: {error}"
            )

    def delete_work_type(self):
        try:
            selected = self.work_types_table.selection()

            if not selected:
                messagebox.showerror(
                    "Помилка",
                    "Оберіть вид роботи в таблиці."
                )
                return

            values = self.work_types_table.item(
                selected[0],
                "values"
            )

            work_type_id = int(values[0])

            answer = messagebox.askyesno(
                "Підтвердження",
                "Видалити вид роботи?"
            )

            if not answer:
                return

            self.controller.delete_work_type(work_type_id)

            self.show_work_types()
            self.load_work_and_employee_lists()
            self.load_orders_and_work_types()

            messagebox.showinfo(
                "Успішно",
                "Вид роботи видалено."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                str(error)
            )

    def show_work_types(self):
        try:
            work_types = self.controller.get_all_work_types()

            for row in self.work_types_table.get_children():
                self.work_types_table.delete(row)

            for work_type in work_types:
                self.work_types_table.insert("", "end", values=work_type)

            if not work_types:
                messagebox.showinfo(
                    "Види робіт",
                    "Види робіт не знайдено."
                )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося показати види робіт: {error}"
            )

    def load_work_and_employee_lists(self):
        work_types = self.controller.get_all_work_types()
        employees = self.controller.get_all_employees()

        self.work_type_combo["values"] = [
            f"{work_type[0]} - {work_type[1]}"
            for work_type in work_types
        ]

        self.employee_combo["values"] = [
            f"{employee[0]} - {employee[1]}"
            for employee in employees
        ]

    def load_orders_and_work_types(self):
        orders = self.controller.get_all_orders()
        work_types = self.controller.get_all_work_types()

        self.order_combo["values"] = [
            f"{order[0]} - {order[1]}"
            for order in orders
        ]

        self.work_type_order_combo["values"] = [
            f"{work_type[0]} - {work_type[1]}"
            for work_type in work_types
        ]

    def assign_employee(self):
        try:
            selected_work_type = self.work_type_combo.get()
            selected_employee = self.employee_combo.get()
            role_in_work = self.role_in_work_combo.get().strip()

            selected_order = self.order_combo.get()

            if selected_order:
                order_id = int(selected_order.split(" - ")[0])
                order_details = self.controller.get_order_details_by_id(order_id)
                order_status = str(order_details[7])

                if order_status == "Завершено" or order_status == "Скасовано":
                    messagebox.showerror(
                        "Помилка",
                        "Не можна призначати працівників для завершеного або скасованого замовлення."
                    )
                    return

            if not selected_work_type or not selected_employee or not role_in_work:
                messagebox.showerror(
                    "Помилка введення",
                    "Оберіть вид роботи, працівника та роль у роботі."
                )
                return

            work_type_id = int(selected_work_type.split(" - ")[0])
            employee_id = int(selected_employee.split(" - ")[0])

            existing_assignments = self.controller.get_assigned_employees()

            selected_work_name = selected_work_type.split(" - ")[1].strip().lower()
            selected_employee_name = selected_employee.split(" - ")[1].strip().lower()

            for assignment in existing_assignments:
                existing_work_name = str(assignment[0]).strip().lower()
                existing_employee_name = str(assignment[1]).strip().lower()

                if existing_work_name == selected_work_name and existing_employee_name == selected_employee_name:
                    messagebox.showerror(
                        "Помилка",
                        "Цього працівника вже призначено на цей вид роботи."
                    )
                    return

            self.controller.assign_employee_to_work_type(
                work_type_id,
                employee_id,
                role_in_work
            )

            self.work_type_combo.set("")
            self.employee_combo.set("")
            self.role_in_work_combo.set("")

            if self.order_combo.get():
                self.show_order_works()

            self.show_assignments()

            messagebox.showinfo(
                "Успішно",
                "Працівника призначено на виконання роботи."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося призначити працівника: {error}"
            )

    def show_assignments(self):
        try:
            assignments = self.controller.get_assigned_employees()

            for row in self.assignments_table.get_children():
                self.assignments_table.delete(row)

            for assignment in assignments:
                self.assignments_table.insert("", "end", values=assignment)

            if not assignments:
                messagebox.showinfo(
                    "Призначення",
                    "Призначених працівників не знайдено."
                )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося показати призначення: {error}"
            )

    def show_materials(self):
        try:
            order_id = self.selected_order_id

            if order_id is None:
                messagebox.showwarning(
                    "Помилка",
                    "Будь ласка, виберіть замовлення в таблиці."
                )
                return

            materials = self.controller.get_materials_by_order(order_id)

            for row in self.materials_table.get_children():
                self.materials_table.delete(row)

            total_materials_cost = 0

            for material in materials:
                self.materials_table.insert("", "end", values=material)

                if material[6] is not None:
                    total_materials_cost += float(material[6])

            self.total_materials_cost_label.config(
                text=f"Загальна вартість матеріалів: {total_materials_cost} грн"
            )
            self.current_materials_cost = total_materials_cost
            self.update_estimate_total()

            if not materials:
                messagebox.showinfo(
                    "Матеріали",
                    "Для цього замовлення матеріали не знайдено."
                )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося показати матеріали замовлення: {error}"
            )

    def add_work_type_to_order(self):
        try:
            selected_order = self.order_combo.get()
            selected_work_type = self.work_type_order_combo.get()

            if not selected_order or not selected_work_type:
                messagebox.showerror(
                    "Помилка введення",
                    "Оберіть замовлення та вид роботи."
                )
                return

            order_id = int(selected_order.split(" - ")[0])

            order_details = self.controller.get_order_details_by_id(order_id)
            order_status = str(order_details[7])

            if order_status == "Завершено" or order_status == "Скасовано":
                messagebox.showerror(
                    "Помилка",
                    "Не можна додавати роботи до завершеного або скасованого замовлення."
                )
                return

            work_type_id = int(selected_work_type.split(" - ")[0])

            existing_works = self.controller.get_work_types_by_order(order_id)

            for work in existing_works:
                existing_work_name = str(work[0]).strip().lower()

                selected_work_name = selected_work_type.split(" - ")[1].strip().lower()

                if existing_work_name == selected_work_name:
                    messagebox.showerror(
                        "Помилка",
                        "Цей вид роботи вже додано до замовлення."
                    )
                    return

            self.controller.add_work_type_to_order(
                order_id,
                work_type_id
            )

            self.show_order_works()

            self.work_type_order_combo.set("")

            messagebox.showinfo(
                "Успішно",
                "Вид роботи додано до замовлення."
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося додати роботу до замовлення: {error}"
            )

    def show_order_works(self):
        try:
            selected_order = self.order_combo.get()

            if not selected_order:
                messagebox.showerror(
                    "Помилка",
                    "Оберіть замовлення."
                )
                return

            order_id = int(selected_order.split(" - ")[0])

            work_types = self.controller.get_work_types_by_order(order_id)

            for row in self.order_works_table.get_children():
                self.order_works_table.delete(row)

            total_works_cost = 0

            for work in work_types:
                employee_name = work[3] if work[3] else "Працівника ще не призначено"
                employee_position = work[4] if work[4] else "-"
                role_in_work = work[5] if work[5] else "-"

                self.order_works_table.insert(
                    "",
                    "end",
                    values=(
                        work[0],
                        work[1],
                        work[2],
                        employee_name,
                        employee_position,
                        role_in_work
                    )
                )

                if work[2] is not None:
                    total_works_cost += float(work[2])

            self.total_works_cost_label.config(
                text=f"Загальна вартість робіт: {total_works_cost} грн"
            )
            self.current_works_cost = total_works_cost
            self.update_estimate_total()

            if not work_types:
                messagebox.showinfo(
                    "Роботи замовлення",
                    "Для цього замовлення роботи не знайдено."
                )

        except Exception as error:
            messagebox.showerror(
                "Помилка",
                f"Не вдалося показати роботи замовлення: {error}"
            )

    def update_estimate_total(self):
        estimate_total = self.current_works_cost + self.current_materials_cost

        self.estimate_total_label.config(
            text=f"Загальний кошторис: {estimate_total} грн"
        )

    def update_analytics(self):
        try:
            orders = self.controller.get_all_orders()

            total_orders = len(orders)

            total_cost = 0
            total_paid = 0
            total_debt = 0

            new_count = 0
            in_progress_count = 0
            completed_count = 0
            cancelled_count = 0

            for order in orders:
                order_id = order[0]
                status = order[5]

                balance = self.controller.get_payment_balance(order_id)
                paid = self.controller.get_total_payments(order_id)

                total_paid += float(paid)
                total_debt += float(balance)

                order_details = self.controller.get_order_details_by_id(order_id)

                if order_details and order_details[10]:
                    total_cost += float(order_details[10])

                if status == "Нове":
                    new_count += 1
                elif status == "У роботі":
                    in_progress_count += 1
                elif status == "Завершено":
                    completed_count += 1
                elif status == "Скасовано":
                    cancelled_count += 1

            self.total_orders_label.config(
                text=f"Кількість замовлень: {total_orders}"
            )

            self.total_orders_cost_label.config(
                text=f"Загальна вартість замовлень: {total_cost:.2f} грн"
            )

            self.total_paid_label.config(
                text=f"Загальна сума оплат: {total_paid:.2f} грн"
            )

            self.total_debt_label.config(
                text=f"Загальна заборгованість: {total_debt:.2f} грн"
            )

            self.status_statistics_label.config(
                text=(
                    "Статистика статусів:\n\n"
                    f"Нове: {new_count}\n"
                    f"У роботі: {in_progress_count}\n"
                    f"Завершено: {completed_count}\n"
                    f"Скасовано: {cancelled_count}"
                )
            )

        except Exception as error:
            messagebox.showerror(
                "Помилка аналітики",
                f"Не вдалося оновити аналітику: {error}"
            )

    def on_tab_changed(self, _event):
        selected_tab = self.notebook.tab(
            self.notebook.select(),
            "text"
        )

        if selected_tab == "Аналітика":
            self.update_analytics()

        if selected_tab == "Матеріали":
            self.show_materials()

        if selected_tab == "Платежі":
            self.show_payments()

    def run(self):
        self.window.mainloop()