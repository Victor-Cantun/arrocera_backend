from email.policy import default
from django.db import models

# Create your models here.


class User(models.Model):
    status = (("", ""), ("Activo", "Activo"), ("Inactivo", "Inactivo"))
    role = (
        ("", ""),
        ("Invitado", "Invitado"),
        ("Empleado", "Empleado"),
        ("Administrador", "Administrador"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre", null=True)
    lastname = models.CharField(max_length=200, verbose_name="Apellido", null=True)
    cellphone = models.BigIntegerField(verbose_name="Celular", null=True, unique=True)
    email = models.EmailField(verbose_name="Correo electrónico", null=True, unique=True)
    password = models.CharField(max_length=500, verbose_name="Contraseña", null=True)
    status = models.CharField(
        choices=status, max_length=50, null=True, verbose_name="Estado"
    )
    role = models.CharField(choices=role, max_length=50, null=True, verbose_name="Rol")
    creation = models.DateTimeField(auto_now=True)

    users = models.BooleanField(null=True, verbose_name="usuarios", default=False)
    companies = models.BooleanField(null=True, verbose_name="compañias", default=False)
    departments = models.BooleanField(
        null=True, verbose_name="departamentos", default=False
    )
    categories = models.BooleanField(
        null=True, verbose_name="categorias", default=False
    )

    societies = models.BooleanField(null=True, verbose_name="sociedades", default=False)
    parcels = models.BooleanField(null=True, verbose_name="parcelas", default=False)
    producers = models.BooleanField(
        null=True, verbose_name="productores", default=False
    )
    reception = models.BooleanField(null=True, verbose_name="reception", default=False)

    binnacle = models.BooleanField(null=True, verbose_name="bitacora", default=False)
    units = models.BooleanField(null=True, verbose_name="unidades", default=False)
    fuels = models.BooleanField(null=True, verbose_name="combustible", default=False)
    requisitions = models.BooleanField(
        null=True, verbose_name="requisiciones", default=False
    )
    shoppings = models.BooleanField(null=True, verbose_name="compras", default=False)
    providers = models.BooleanField(
        null=True, verbose_name="proveedores", default=False
    )

    quotes = models.BooleanField(null=True, verbose_name="cotizaciones", default=False)
    purchase_orders = models.BooleanField(
        null=True, verbose_name="orden de venta", default=False
    )
    products = models.BooleanField(null=True, verbose_name="productos", default=False)
    outputs = models.BooleanField(null=True, verbose_name="salidas", default=False)
    CreditNotes = models.BooleanField(
        null=True, verbose_name="Notas de credito", default=False
    )
    BillOfLading = models.BooleanField(
        null=True, verbose_name="Carta porte", default=False
    )
    PaymentSchedule = models.BooleanField(
        null=True, verbose_name="Programación de pagos", default=False
    )
    PettyCash = models.BooleanField(null=True, verbose_name="Caja chica", default=False)
    drivers = models.BooleanField(
        null=True, verbose_name="Sueldo choferes", default=False
    )
    chargers = models.BooleanField(
        null=True, verbose_name="Sueldo cargadores", default=False
    )
    LandRent = models.BooleanField(
        null=True, verbose_name="Reta de tierras", default=False
    )
    PaymentOrderProducer = models.BooleanField(
        null=True, verbose_name="Orden de pago", default=False
    )
    payments = models.BooleanField(null=True, verbose_name="Pagos", default=False)

    banks = models.BooleanField(null=True, verbose_name="bancos", default=False)
    customers = models.BooleanField(null=True, verbose_name="clientes", default=False)
    BilledIncome = models.BooleanField(
        null=True, verbose_name="Ingresos Facturados", default=False
    )
    PaidPlugins = models.BooleanField(
        null=True, verbose_name="Complementos de pago", default=False
    )
    DepositControl = models.BooleanField(
        null=True, verbose_name="Control de depositos", default=False
    )
    Income = models.BooleanField(null=True, verbose_name="Ingresos", default=False)
    Conciliation = models.BooleanField(
        null=True, verbose_name="Conciliaciones", default=False
    )

    employees = models.BooleanField(null=True, verbose_name="empleados", default=False)
    payroll = models.BooleanField(null=True, verbose_name="Nomina", default=False)
    ExtraHours = models.BooleanField(
        null=True, verbose_name="Horas extras", default=False
    )
    DoubleDays = models.BooleanField(
        null=True, verbose_name="Dias dobles", default=False
    )
    props = models.BooleanField(null=True, verbose_name="Apoyos", default=False)
    loans = models.BooleanField(null=True, verbose_name="prestamos", default=False)

    # inputs = models.BooleanField(null=True, verbose_name="entradas")
    watch = models.BooleanField(null=True, verbose_name="Visualizar", default=False)
    write = models.BooleanField(null=True, verbose_name="Escribir", default=False)
    edit = models.BooleanField(null=True, verbose_name="Editar", default=False)
    delete = models.BooleanField(null=True, verbose_name="Eliminar", default=False)
    export = models.BooleanField(null=True, verbose_name="Exportar", default=False)
    photo = models.ImageField(
        upload_to="employees/",
        verbose_name="Foto de perfil",
        null=True,
        default="users/NoPhoto.png",
    )


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, verbose_name="Nombre", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Departamento", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Departamento: " + self.name
        return fila


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Categoria", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Categoria: " + self.name
        return fila


class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Banco", unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="BankUser"
    )
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Banco: " + self.name
        return fila


class TaxRegime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, verbose_name="Régimen fiscal", unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class BankAccount(models.Model):
    id = models.AutoField(primary_key=True)
    bank = models.ForeignKey(
        Bank, verbose_name="Banco", on_delete=models.CASCADE, null=True
    )
    tax_regime = models.CharField(
        max_length=500, verbose_name="Régimen fiscal", null=True
    )
    company = models.CharField(max_length=500, verbose_name="Empresa", null=True)
    number = models.BigIntegerField(verbose_name="Número de cuenta", unique=True)
    interbank_key = models.BigIntegerField(
        verbose_name="Clave interbancaria", null=True
    )
    deposit_limit = models.BigIntegerField(
        verbose_name="Límite de depósito", null=True, default=0
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = (
            "banco: "
            + self.bank
            + " number:"
            + self.number
            + " interbank_key:"
            + self.interbank_key
        )
        return fila


class Producer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Proveedor", unique=True)
    rfc = models.CharField(max_length=50, verbose_name="RFC", null=True)
    phone = models.BigIntegerField(verbose_name="Teléfono", null=True)
    email = models.EmailField(verbose_name="Correo Electrónico", null=True)
    postal_code = models.IntegerField(verbose_name="Codigo postal", null=True)
    country = models.CharField(max_length=100, verbose_name="Pais", null=True)
    state = models.CharField(max_length=100, verbose_name="Estado", null=True)
    city = models.CharField(max_length=100, verbose_name="Ciudad", null=True)
    location = models.CharField(max_length=100, verbose_name="Localidad", null=True)
    suburb = models.CharField(max_length=50, verbose_name="Colonia", null=True)
    street = models.CharField(max_length=50, verbose_name="Calle", null=True)
    int_no = models.CharField(max_length=50, verbose_name="Número interior", null=True)
    ext_no = models.CharField(max_length=50, verbose_name="Número exterior", null=True)
    representative = models.CharField(
        max_length=100, verbose_name="Representante legal", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        # fila = "Nombre: "+self.name
        return self.name


class FileProducer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, verbose_name="Nombre del Archivo", null=True
    )
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)
    document = models.FileField(
        upload_to="documentos_productores/", verbose_name="Documento", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Proveedor", unique=True)
    rfc = models.CharField(max_length=50, verbose_name="RFC", null=True)
    phone = models.BigIntegerField(verbose_name="Teléfono", null=True)
    email = models.EmailField(verbose_name="Correo Electrónico", null=True)
    postal_code = models.IntegerField(verbose_name="Codigo postal", null=True)
    country = models.CharField(max_length=100, verbose_name="Pais", null=True)
    state = models.CharField(max_length=100, verbose_name="Estado", null=True)
    city = models.CharField(max_length=100, verbose_name="Ciudad", null=True)
    location = models.CharField(max_length=100, verbose_name="Localidad", null=True)
    suburb = models.CharField(max_length=50, verbose_name="Colonia", null=True)
    street = models.CharField(max_length=50, verbose_name="Calle", null=True)
    int_no = models.CharField(max_length=50, verbose_name="Número interior", null=True)
    ext_no = models.CharField(max_length=50, verbose_name="Número exterior", null=True)
    representative = models.CharField(
        max_length=100, verbose_name="Representante legal", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Nombre: " + self.name
        return fila


class UploadImage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Nombre")
    imagen = models.ImageField(
        upload_to="imagenes/",
        verbose_name="Foto de perfil",
        blank=True,
        null=True,
        default="",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    sex = (("", ""), ("Masculino", "Masculino"), ("Femenino", "Femenino"))

    maritalstatus = (
        ("", ""),
        ("Soltero", "Soltero"),
        ("Casado", "Casado"),
        ("Divorciado", "Divorciado"),
        ("Viudo", "Viudo"),
    )

    liveswith = (
        ("", ""),
        ("Solo", "Solo"),
        ("Padres", "Padres"),
        ("Conyugue", "Conyugue"),
        ("Familia", "Familia"),
        ("Parientes", "Parientes"),
    )

    peoplewhodepend = (
        ("", ""),
        ("Hijos", "Hijos"),
        ("Conyugue", "Conyugue"),
        ("Padres", "Padres"),
        ("Nadie", "Nadie"),
        ("Otros", "Otros"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    surname = models.CharField(max_length=100, verbose_name="Apellido Paterno")
    second_surname = models.CharField(
        max_length=100, verbose_name="Apellido Materno", null=True
    )
    date_birth = models.DateField(verbose_name="Fecha de nacimiento", null=True)
    age = models.IntegerField(verbose_name="Edad", null=True)
    postal_code = models.IntegerField(verbose_name="Codigo postal", null=True)
    country = models.CharField(max_length=100, verbose_name="Pais", null=True)
    state = models.CharField(max_length=100, verbose_name="Estado", null=True)
    city = models.CharField(max_length=100, verbose_name="Ciudad", null=True)
    location = models.CharField(max_length=100, verbose_name="Localidad", null=True)
    suburb = models.CharField(max_length=50, verbose_name="Colonia", null=True)
    street = models.CharField(max_length=50, verbose_name="Calle", null=True)
    int_no = models.CharField(max_length=50, verbose_name="Número interior", null=True)
    ext_no = models.CharField(max_length=50, verbose_name="Número exterior", null=True)
    height = models.DecimalField(
        verbose_name="Estatura", decimal_places=2, max_digits=20, null=True
    )
    weight = models.DecimalField(
        verbose_name="Peso", decimal_places=2, max_digits=20, null=True
    )
    curp = models.CharField(max_length=50, verbose_name="CURP", null=True)
    rfc = models.CharField(max_length=50, verbose_name="RFC", null=True)
    nss = models.CharField(max_length=50, verbose_name="NSS", null=True)
    gender = models.CharField(
        max_length=20, verbose_name="Género", choices=sex, null=True
    )
    civil_status = models.CharField(
        max_length=20, verbose_name="Estado civil", choices=maritalstatus, null=True
    )
    lives_with = models.CharField(
        max_length=20, verbose_name="Vive con", choices=liveswith, null=True
    )
    depends_him = models.CharField(
        max_length=20, verbose_name="Dependen de el", choices=peoplewhodepend, null=True
    )
    date_admission = models.DateField(verbose_name="Fecha de ingreso", null=True)
    employee_no = models.CharField(
        max_length=50, verbose_name="Número de empleado", null=True
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    sr = models.DecimalField(
        verbose_name="Estatura", decimal_places=2, max_digits=20, null=True
    )
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, verbose_name="Banco", null=True
    )
    bank_account = models.BigIntegerField(
        verbose_name="Numero de cuenta bancaria", null=True
    )
    interbank_key = models.BigIntegerField(
        verbose_name="Clave interbancaria", null=True
    )
    personal_email = models.EmailField(
        max_length=50, verbose_name="Email personal", null=True
    )
    cell_phone = models.BigIntegerField(verbose_name="Celular", null=True)
    home_phone = models.BigIntegerField(verbose_name="Teléfono de casa", null=True)
    corporate_email = models.EmailField(
        max_length=50, verbose_name="Email corporativo", null=True
    )
    corporate_cellphone = models.BigIntegerField(
        verbose_name="Celular corporativo", null=True
    )
    corporate_phone = models.BigIntegerField(
        verbose_name="Teléfono corporativo", null=True
    )
    imagen = models.ImageField(
        upload_to="employees/",
        verbose_name="Foto de perfil",
        null=True,
        default="employees/NoPhoto.png",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(
        max_length=100, verbose_name="Tipo de vehículo", unique=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Tipo de vehiculo: " + self.vehicle_type
        return fila


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", unique=True)
    vehicle_type = models.ForeignKey(
        VehicleType, on_delete=models.CASCADE, default="", blank=True, null=True
    )
    initial_mileage = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometraje Inicial",
        default="0.0",
        blank=True,
        null=True,
    )
    current_mileage = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometraje Actual",
        default="0.0",
        blank=True,
        null=True,
    )
    hours_worked = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Horas Trabajadas",
        default="0.0",
        blank=True,
        null=True,
    )
    brand = models.CharField(
        max_length=50, verbose_name="Marca", null=True, default="", blank=True
    )
    model = models.CharField(
        max_length=50, verbose_name="Modelo", null=True, default="", blank=True
    )
    color = models.CharField(
        max_length=50, verbose_name="Color", null=True, default="", blank=True
    )
    frame = models.CharField(
        max_length=50, verbose_name="Bastidor", null=True, default="", blank=True
    )
    engine = models.CharField(
        max_length=50, verbose_name="Motor", null=True, default="", blank=True
    )
    price = models.CharField(
        max_length=50, verbose_name="Precio", null=True, default="", blank=True
    )
    permit_no = models.CharField(
        max_length=50,
        verbose_name="Numero de permiso",
        null=True,
        default="",
        blank=True,
    )
    plate_no = models.CharField(
        max_length=50,
        verbose_name="Número de placas",
        null=True,
        unique=True,
        default="",
        blank=True,
    )
    validity = models.CharField(
        max_length=50, verbose_name="Vigencia", null=True, default="", blank=True
    )
    insurance_carrier = models.CharField(
        max_length=50, verbose_name="Aseguradora", null=True, default="", blank=True
    )
    policy_no = models.CharField(
        max_length=50,
        verbose_name="Número de poliza",
        null=True,
        default="",
        blank=True,
    )
    C_VerificationNo = models.CharField(
        max_length=50,
        verbose_name="Numeor de verificacion contaminantes",
        null=True,
        default="",
        blank=True,
    )
    PM_VerificationNo = models.CharField(
        max_length=50,
        verbose_name="Numero de verificacion fisicomecanico",
        null=True,
        default="",
        blank=True,
    )
    start_validity = models.DateField(
        max_length=50,
        verbose_name="Inicio de vigencia",
        null=True,
        default="",
        blank=True,
    )
    end_validity = models.DateField(
        max_length=50,
        verbose_name="Final de vigencia",
        null=True,
        default="",
        blank=True,
    )
    circulation_card_no = models.CharField(
        max_length=50,
        verbose_name="Número de tarjeta de circulación",
        null=True,
        default="",
        blank=True,
    )
    identification_no = models.CharField(
        max_length=50,
        verbose_name="Número de identificación",
        null=True,
        default="",
        blank=True,
    )
    state = models.CharField(
        max_length=50, verbose_name="Estado", null=True, default="", blank=True
    )
    imagen = models.ImageField(
        upload_to="units/",
        verbose_name="Foto",
        blank=True,
        null=True,
        default="units/NoPhoto.png",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Unit: " + self.unit
        return fila


class FileUnit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, verbose_name="Nombre del Archivo", null=True
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    document = models.FileField(
        upload_to="documentos_unidades/", verbose_name="Documento", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class FuelType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, verbose_name="Tipo de combustible", unique=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Combustible: " + self.name
        return fila


class Fueling(models.Model):
    documenttype = (
        ("Ticket", "Ticket"),
        ("Recibo", "Recibo"),
        ("Factura", "Factura"),
        ("Otro", "Otro"),
    )
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha")
    last_mileage = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Ultimo Kilometraje",
        default="0",
        blank=True,
        null=True,
    )
    mileage = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Kilometraje", null=True
    )
    fuel_capacity = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Capacidad de combustible",
        null=True,
    )
    liters = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Litros", null=True
    )
    hours = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Horas Trabajadas", null=True
    )
    last_hours = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Ultimas Horas Trabajadas",
        null=True,
    )
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    km_traveled = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros recorridos",
        default="0",
        blank=True,
        null=True,
    )
    gallon = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Galon",
        default="0",
        blank=True,
        null=True,
    )
    purchase_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Precio de compra",
        default="0",
        blank=True,
        null=True,
    )
    km_gallon = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Galon",
        default="0",
        blank=True,
        null=True,
    )
    document_type = models.CharField(
        max_length=20,
        verbose_name="Tipo de Documento",
        choices=documenttype,
        default="",
    )
    km_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Precio",
        default="0",
        blank=True,
        null=True,
    )
    document_no = models.IntegerField(
        verbose_name="Número de documento", blank=True, null=True
    )
    comment = models.CharField(
        max_length=100, verbose_name="Comentario", default="", blank=True, null=True
    )
    km_liters = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Litros",
        default="0",
        blank=True,
        null=True,
    )
    liters_hours = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Litros/Horas",
        default="0",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class FuelDump(models.Model):
    id = models.AutoField(primary_key=True)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, null=True)
    date = models.DateField(max_length=50, verbose_name="Fecha")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    capacity = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Capacidad",
        default="0",
        blank=True,
        null=True,
    )
    current_content = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Capacidad",
        default="0",
        blank=True,
        null=True,
    )
    liters_discharged = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Capacidad",
        default="0",
        blank=True,
        null=True,
    )
    comment = models.CharField(
        max_length=100, verbose_name="Comentario", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Diesel(models.Model):
    documenttype = (
        ("Ticket", "Ticket"),
        ("Recibo", "Recibo"),
        ("Factura", "Factura"),
        ("Otro", "Otro"),
    )
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha")
    last_mileage = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Ultimo Kilometraje",
        default="0",
        blank=True,
        null=True,
    )
    mileage = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Kilometraje"
    )
    liters = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Litros")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    km_traveled = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros recorridos",
        default="0",
        blank=True,
        null=True,
    )
    gallon = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Galon",
        default="0",
        blank=True,
        null=True,
    )
    purchase_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Precio de compra",
        default="0",
        blank=True,
        null=True,
    )
    km_gallon = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Galon",
        default="0",
        blank=True,
        null=True,
    )
    document_type = models.CharField(
        max_length=20,
        verbose_name="Tipo de Documento",
        choices=documenttype,
        default="",
    )
    km_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Precio",
        default="0",
        blank=True,
        null=True,
    )
    document_no = models.IntegerField(
        verbose_name="Número de documento", blank=True, null=True
    )
    comment = models.CharField(
        max_length=100, verbose_name="Comentario", default="", blank=True, null=True
    )
    km_liters = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Litros",
        default="0",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Gasoline(models.Model):
    gasolinetype = (("Magna", "Magna"), ("Premium", "Premium"))
    documenttype = (
        ("Ticket", "Ticket"),
        ("Recibo", "Recibo"),
        ("Factura", "Factura"),
        ("Otro", "Otro"),
    )
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha")
    last_mileage = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Ultimo Kilometraje",
        default="0",
        blank=True,
        null=True,
    )
    mileage = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Kilometraje"
    )
    liters = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Litros")
    type = models.CharField(
        max_length=20, verbose_name="Tipo de Gasolina", choices=gasolinetype, default=""
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    km_traveled = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros recorridos",
        default="0",
        blank=True,
        null=True,
    )
    gallon = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Galon",
        default="0",
        blank=True,
        null=True,
    )
    purchase_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Precio de compra",
        default="0",
        blank=True,
        null=True,
    )
    km_gallon = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Galon",
        default="0",
        blank=True,
        null=True,
    )
    document_type = models.CharField(
        max_length=20,
        verbose_name="Tipo de Documento",
        choices=documenttype,
        default="",
    )
    km_price = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Precio",
        default="0",
        blank=True,
        null=True,
    )
    document_no = models.IntegerField(
        verbose_name="Número de documento", blank=True, null=True
    )
    comment = models.CharField(
        max_length=100, verbose_name="Comentario", default="", blank=True, null=True
    )
    km_liters = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kilometros/Litros",
        default="0",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class MainProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, verbose_name="Producto", unique=True, default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Producto: " + self.name
        return fila


class MainPresentation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, verbose_name="Presentation", unique=True, default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Presentación: " + self.name
        return fila


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, verbose_name="Producto", unique=True, default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Presentation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, verbose_name="Presentación", unique=True, default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ProductRequisition(models.Model):
    amount = models.IntegerField(verbose_name="Cantidad", null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    product = models.CharField(max_length=500, verbose_name="Product", null=True)
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )


class Requisition(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    folio = models.IntegerField(unique=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    description = models.CharField(
        max_length=100, verbose_name="Descripción", default="", blank=True, null=True
    )
    observation = models.CharField(
        max_length=100, verbose_name="Observación", default="", blank=True, null=True
    )
    status = models.CharField(
        max_length=50, verbose_name="status", default="Pendiente", null=True
    )
    products = models.ManyToManyField(ProductRequisition, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class FileQuotation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200, verbose_name="Nombre del Archivo", null=True
    )
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, null=True)
    document = models.FileField(
        upload_to="cotizaciones/", verbose_name="Documento", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, default=""
    )
    name = models.CharField(max_length=150, verbose_name="Cliente", unique=True)
    rfc = models.CharField(max_length=50, verbose_name="RFC")
    phone = models.BigIntegerField(verbose_name="Teléfono", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo Electrónico", blank=True, null=True)
    postal_code = models.IntegerField(
        verbose_name="Codigo postal", default="0", blank=True, null=True
    )
    country = models.CharField(
        max_length=100, verbose_name="Pais", default="", blank=True, null=True
    )
    state = models.CharField(
        max_length=100, verbose_name="Estado", default="", blank=True, null=True
    )
    city = models.CharField(
        max_length=100, verbose_name="Ciudad", default="", blank=True, null=True
    )
    location = models.CharField(
        max_length=100, verbose_name="Localidad", default="", blank=True, null=True
    )
    suburb = models.CharField(
        max_length=50, verbose_name="Colonia", blank=True, null=True
    )
    street = models.CharField(
        max_length=50, verbose_name="Calle", blank=True, null=True
    )
    int_no = models.CharField(
        max_length=50, verbose_name="Número interior", blank=True, null=True
    )
    ext_no = models.CharField(
        max_length=50, verbose_name="Número exterior", blank=True, null=True
    )
    representative = models.CharField(
        max_length=100, verbose_name="Representante legal", blank=True, null=True
    )
    imagen = models.ImageField(
        upload_to="customers/",
        verbose_name="Foto de perfil",
        null=True,
        default="customers/NoPhoto.png",
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Nombre: " + self.name
        return fila


class ProductW(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100, verbose_name="Producto", unique=True, default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ProductwPresentation(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductW, on_delete=models.CASCADE, null=True)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["product", "presentation"]]


class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(
        max_length=200, verbose_name="Producto", default="", blank=True, null=True
    )
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = "Producto: " + self.product
        return fila


class ProductPO(models.Model):
    amount = models.IntegerField(verbose_name="Cantidad", null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    purchase_order = models.IntegerField(verbose_name="Orden de pedido", null=True)
    date_delivery = models.DateField(
        max_length=50, verbose_name="Fecha de entrega", null=True
    )
    business_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_number = models.IntegerField(verbose_name="Orden de pedido", null=True)
    place_delivery = models.CharField(
        max_length=100,
        verbose_name="Lugar de entrega",
        default="",
        blank=True,
        null=True,
    )
    sale_condition = models.CharField(
        max_length=100,
        verbose_name="Condición de venta",
        default="",
        blank=True,
        null=True,
    )
    invoice = models.IntegerField(verbose_name="No. de Factura", null=True)
    iva = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Iva", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", blank=True, null=True
    )
    observation = models.CharField(
        max_length=200, verbose_name="Observación", default="", blank=True, null=True
    )
    auxiliary_sales = models.ForeignKey(
        Employee,
        verbose_name="Auxiliar de ventas",
        related_name="POauxiliary",
        on_delete=models.CASCADE,
        null=True,
    )
    storekeeper = models.ForeignKey(
        Employee,
        verbose_name="Almacenista",
        related_name="POstorekeeper",
        on_delete=models.CASCADE,
        null=True,
    )
    qa = models.ForeignKey(
        Employee,
        verbose_name="Control de calidad",
        related_name="POQA",
        on_delete=models.CASCADE,
        null=True,
    )
    products = models.ManyToManyField(ProductPO, blank=True)
    voucher = status = models.CharField(
        max_length=50, verbose_name="Comprobante", default="", blank=True, null=True
    )
    status = models.CharField(
        max_length=50, verbose_name="status", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ProductBI(models.Model):
    amount = models.IntegerField(verbose_name="Cantidad", null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    net_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso neto", blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )


class BilledIncome(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    due_date = models.DateField(
        max_length=50, verbose_name="Fecha de vencimiento", null=True
    )
    invoice = models.IntegerField(null=True, verbose_name="Factura")
    products = models.ManyToManyField(ProductBI, blank=True)
    net_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="peso", null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="total", null=True
    )
    status = models.CharField(
        max_length=50, verbose_name="Status", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ProductCN(models.Model):
    amount = models.IntegerField(verbose_name="Cantidad", null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class CreditNote(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    no_creditnote = models.IntegerField(verbose_name="No. Nota de credito", null=True)
    purchase_order = models.IntegerField(verbose_name="Orden de pedido", null=True)
    date_delivery = models.DateField(
        max_length=50, verbose_name="Fecha de entrega", null=True
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_number = models.IntegerField(verbose_name="Orden de pedido", null=True)
    place_delivery = models.CharField(
        max_length=100,
        verbose_name="Lugar de entrega",
        default="",
        blank=True,
        null=True,
    )
    sale_condition = models.CharField(
        max_length=100,
        verbose_name="Condición de venta",
        default="",
        blank=True,
        null=True,
    )
    invoice = models.ForeignKey(BilledIncome, on_delete=models.CASCADE, null=True)
    iva = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Iva", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", blank=True, null=True
    )
    observation = models.CharField(
        max_length=200, verbose_name="Observación", default="", blank=True, null=True
    )
    auxiliary_sales = models.ForeignKey(
        Employee,
        verbose_name="Auxiliar de ventas",
        related_name="auxiliary",
        on_delete=models.CASCADE,
        null=True,
    )
    storekeeper = models.ForeignKey(
        Employee,
        verbose_name="Almacenista",
        related_name="storekeeper",
        on_delete=models.CASCADE,
        null=True,
    )
    qa = models.ForeignKey(
        Employee,
        verbose_name="Control de calidad",
        related_name="QA",
        on_delete=models.CASCADE,
        null=True,
    )
    products = models.ManyToManyField(ProductCN, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ProductQuotation(models.Model):
    amount = models.IntegerField(verbose_name="Cantidad", null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Quotation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    invoice = models.IntegerField(verbose_name="Folio", null=True)
    period = models.CharField(max_length=500, verbose_name="Periodo", null=True)
    source = models.CharField(max_length=500, verbose_name="Origen", null=True)
    attention = models.CharField(
        max_length=500, verbose_name="Atención", null=True, blank=True
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    introduction = models.CharField(
        max_length=500, verbose_name="Introducción", null=True
    )
    iva = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Iva", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", blank=True, null=True
    )
    generator = models.ForeignKey(
        Employee,
        verbose_name="Genera",
        related_name="GeneraCotizacion",
        on_delete=models.CASCADE,
        null=True,
    )
    authorizer = models.ForeignKey(
        Employee,
        verbose_name="Autoriza",
        related_name="AutorizaCotizacion",
        on_delete=models.CASCADE,
        null=True,
    )
    comment = models.CharField(max_length=1000, verbose_name="Observaciones", null=True)
    products = models.ManyToManyField(ProductQuotation, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Rowticketreview(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        ProductW,
        verbose_name="Producto de Almacen",
        on_delete=models.CASCADE,
        null=True,
    )
    bigbags = models.ForeignKey(
        Presentation,
        verbose_name="Presentación de producto",
        related_name="entry_presentation_bigbags",
        on_delete=models.CASCADE,
        null=True,
    )
    kgsxbigbags = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kgs X BigBags",
        default="",
        blank=True,
        null=True,
    )
    packages = models.ForeignKey(
        Presentation,
        verbose_name="Presentación de producto",
        related_name="entry_presentation_packages",
        on_delete=models.CASCADE,
        null=True,
    )
    kgsxpackages = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kgs X Bultos",
        default="",
        blank=True,
        null=True,
    )
    subtotal = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Subtotal",
        default="",
        blank=True,
        null=True,
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Ticketreview(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha")
    variety = models.CharField(max_length=100, verbose_name="Variedad")
    total = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Total")
    observation = models.CharField(
        max_length=100, verbose_name="Observación", default="", blank=True, null=True
    )
    rows = models.ManyToManyField(Rowticketreview, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Rowoutputreview(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        ProductW,
        verbose_name="Producto de Almacen",
        on_delete=models.CASCADE,
        null=True,
    )
    bigbags = models.ForeignKey(
        Presentation,
        verbose_name="Presentación de producto",
        related_name="output_presentation_bigbags",
        on_delete=models.CASCADE,
        null=True,
    )
    kgsxbigbags = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kgs X BigBags",
        default="",
        blank=True,
        null=True,
    )
    packages = models.ForeignKey(
        Presentation,
        verbose_name="Presentación de producto",
        related_name="output_presentation_packages",
        on_delete=models.CASCADE,
        null=True,
    )
    kgsxpackages = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Kgs X Bultos",
        default="",
        blank=True,
        null=True,
    )
    subtotal = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Subtotal",
        default="",
        blank=True,
        null=True,
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Outputreview(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha")
    variety = models.CharField(max_length=100, verbose_name="Variedad")
    total = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Total")
    observation = models.CharField(
        max_length=100, verbose_name="Observación", default="", blank=True, null=True
    )
    rows = models.ManyToManyField(Rowoutputreview, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class OutputProduct(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(verbose_name="Cantidad", null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    presentation = models.ForeignKey(
        Presentation, on_delete=models.CASCADE, default="", null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, default="", null=True
    )
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    no = models.IntegerField(verbose_name="No", null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Output(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    invoice = models.IntegerField(verbose_name="Folio", null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    destiny = models.CharField(max_length=200, verbose_name="Destino", null=True)
    gross_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso bruto"
    )
    tare = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Tara")
    net_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso neto"
    )
    driver = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        related_name="salidas_chofer",
    )
    plate = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(
        max_length=200, verbose_name="Metodo de pago", null=True
    )
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    iva = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Iva", null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", null=True
    )
    delivered = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        related_name="salidas_entrego",
    )
    received = models.CharField(max_length=200, verbose_name="Recibió", null=True)
    comment = models.CharField(max_length=200, verbose_name="Comentatio", null=True)
    products = models.ManyToManyField(OutputProduct, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Binnacle(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(max_length=50, verbose_name="Fecha")
    labores = models.CharField(max_length=1000, verbose_name="Labores")
    lotes = models.CharField(max_length=500, verbose_name="Lotes", null=True)
    ha = models.IntegerField(verbose_name="Ha", null=True)
    faena = models.IntegerField(verbose_name="Faena", default="", blank=True, null=True)
    ta_ha_faena = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_faena = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    acurate = models.IntegerField(
        verbose_name="Acurate", default="", blank=True, null=True
    )
    ta_ha_acurate = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_acurate = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    prolux = models.IntegerField(
        verbose_name="Prolux", default="", blank=True, null=True
    )
    ta_ha_prolux = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_prolux = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    aderente = models.IntegerField(
        verbose_name="Aderente", default="", blank=True, null=True
    )
    ta_ha_aderente = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_aderente = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    sulfato = models.IntegerField(
        verbose_name="Sulfato de amonio", default="", blank=True, null=True
    )
    ta_ha_sulfato = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_sulfato = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    nomolt = models.IntegerField(
        verbose_name="Nomolt", default="", blank=True, null=True
    )
    ta_ha_nomolt = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_nomolt = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    metarrizium = models.IntegerField(
        verbose_name="Metarrizim", default="", blank=True, null=True
    )
    ta_ha_metarrizium = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_metarrizium = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    beauberian = models.IntegerField(
        verbose_name="Beauberian", default="", blank=True, null=True
    )
    ta_ha_beauberian = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_beauberian = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    abland = models.IntegerField(
        verbose_name="abland", default="", blank=True, null=True
    )
    ta_ha_abland = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_abland = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    aura = models.IntegerField(verbose_name="aura", default="", blank=True, null=True)
    ta_ha_aura = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_aura = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    urea = models.IntegerField(verbose_name="urea", default="", blank=True, null=True)
    ta_ha_urea = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_urea = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    dash = models.IntegerField(verbose_name="dash", default="", blank=True, null=True)
    ta_ha_dash = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_dash = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    cipermetrina = models.IntegerField(
        verbose_name="cipermetrina", default="", blank=True, null=True
    )
    ta_ha_cipermetrina = models.IntegerField(
        verbose_name="Total aplicado", default="", blank=True, null=True
    )
    medida_cipermetrina = models.CharField(
        max_length=20, verbose_name="Medida", default="", blank=True, null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="binnacle_user"
    )
    creation = models.DateTimeField(auto_now=True)


class ProductShopping(models.Model):
    product_name = models.CharField(max_length=200)
    amount = models.IntegerField(verbose_name="Cantidad", blank=True, null=True)
    unit = models.CharField(max_length=50, verbose_name="Unidad", blank=True, null=True)
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Shopping(models.Model):
    payment_type = (("", ""), ("Contado", "Contado"), ("Credito", "Credito"))

    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    provider = models.ForeignKey(
        Provider, verbose_name="Departamento", on_delete=models.CASCADE, null=True
    )
    requisition = models.ForeignKey(
        Requisition, verbose_name="Id Requisition", on_delete=models.CASCADE, null=True
    )
    department = models.ForeignKey(
        Department, verbose_name="Departamento", on_delete=models.CASCADE, null=True
    )
    payment_type = models.CharField(
        max_length=50, verbose_name="Forma de pago", null=True, choices=payment_type
    )
    iva = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Iva", blank=True, null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", blank=True, null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", blank=True, null=True
    )
    observation = models.CharField(
        max_length=200, verbose_name="Observación", default="", blank=True, null=True
    )
    applicant = models.ForeignKey(
        Employee,
        verbose_name="Solicita",
        related_name="solicita",
        on_delete=models.CASCADE,
        null=True,
    )
    verify = models.ForeignKey(
        Employee,
        verbose_name="Verifica",
        related_name="verifica",
        on_delete=models.CASCADE,
        null=True,
    )
    authorizes = models.ForeignKey(
        Employee,
        verbose_name="Autoriza",
        related_name="autoriza",
        on_delete=models.CASCADE,
        null=True,
    )
    products = models.ManyToManyField(ProductShopping, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Society(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    cycle = models.CharField(max_length=100, verbose_name="Ciclo")
    year = models.IntegerField(verbose_name="Año")
    producers = models.ManyToManyField(Producer, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class SocietyProducers(models.Model):
    id = models.AutoField(primary_key=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, null=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)


class Parcel(models.Model):
    id = models.AutoField(primary_key=True)
    no_parcel = models.CharField(
        max_length=100, verbose_name="Número de parcela", null=True, unique=True
    )
    georeferences = models.CharField(
        max_length=200, verbose_name="Georeferencias", null=True
    )
    hectares = models.CharField(max_length=200, verbose_name="Hectareas", null=True)
    certificate = models.CharField(
        max_length=200, verbose_name="Certificado", null=True
    )
    ran = models.CharField(max_length=200, verbose_name="RAN", null=True)
    owner = models.CharField(max_length=200, verbose_name="Propietario", null=True)
    location = models.CharField(max_length=500, verbose_name="Ubicación", null=True)
    price_hectare = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Precio por hectarea",
        blank=True,
        null=True,
    )
    rental_value = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Valor de la renta",
        blank=True,
        null=True,
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class LandRent(models.Model):
    reasonrent = (
        ("", ""),
        ("Solo tierra", "Tierra"),
        ("Almacenamiento de agua", "Almacenamiento de agua"),
    )
    id = models.AutoField(primary_key=True)
    rent_year = models.IntegerField(verbose_name="Año de renta", null=True)
    reason_rent = models.CharField(
        max_length=100, verbose_name="Motivo de renta", null=True, choices=reasonrent
    )
    lessor = models.CharField(
        max_length=200, verbose_name="Propietario", null=True, blank=True
    )
    location = models.CharField(
        max_length=200, verbose_name="Ubicación", null=True, blank=True
    )
    parcel = models.CharField(
        max_length=200, verbose_name="Parcelas", null=True, blank=True
    )
    hectares = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Superficie",
        blank=True,
        null=True,
    )
    price_hectare = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Precio por hectarea",
        blank=True,
        null=True,
    )
    rental_value = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Valor de renta",
        blank=True,
        null=True,
    )
    advances = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Anticipo", blank=True, null=True
    )
    amount = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Importe a pagar",
        blank=True,
        null=True,
    )
    payment = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Importe pagado",
        blank=True,
        null=True,
    )
    balance_against = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Balance en contra",
        blank=True,
        null=True,
    )
    payment_method = models.CharField(
        max_length=200, verbose_name="Metodo de pago", null=True
    )
    payment_date = models.DateField(
        max_length=50, verbose_name="Fecha de pago", null=True
    )
    bank_account = models.CharField(
        max_length=200, verbose_name="Cuenta bancaria", null=True, blank=True
    )
    status = models.CharField(max_length=50, verbose_name="Metodo de pago", null=True)
    comment = models.CharField(max_length=200, verbose_name="Metodo de pago", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class SegalmexParcel(models.Model):
    id = models.AutoField(primary_key=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, null=True)
    cyclepv = models.ForeignKey(
        Parcel, on_delete=models.CASCADE, related_name="CicloPV", null=True
    )
    cycleoi = models.ForeignKey(
        Parcel, on_delete=models.CASCADE, related_name="CicloOI", null=True
    )
    year = models.IntegerField(verbose_name="Año", null=True)
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Población", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Variety(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Variedad", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class InitialCash(models.Model):
    id = models.AutoField(primary_key=True)
    cash = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Importe", null=True
    )


class PettyCash(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    description = models.CharField(
        max_length=500, verbose_name="Descripcion de pago", null=True
    )
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    cash = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Importe", null=True
    )
    discount = models.BooleanField(null=True, verbose_name="Descuento")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Plate(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=100, verbose_name="Placa")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Charger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class DriverSalary(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    product = models.CharField(max_length=500, verbose_name="Producto", null=True)
    invoice = models.IntegerField(null=True, verbose_name="Folio")
    source = models.CharField(max_length=500, verbose_name="Origen", null=True)
    destination = models.CharField(max_length=500, verbose_name="Destino", null=True)
    tonnage = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Tonelaje", null=True
    )
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio unitario", null=True
    )
    freight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Flete", null=True
    )
    percentage = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Porcentaje", null=True
    )
    advance = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Anticipo", null=True
    )
    balance = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Saldo", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ChargerSalary(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    product = models.CharField(max_length=500, verbose_name="Producto", null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    invoice = models.IntegerField(null=True, verbose_name="Folio")
    tonnage = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Tonelaje", null=True
    )
    packaging = models.CharField(max_length=500, verbose_name="Embalaje", null=True)
    rate = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Tarifa", null=True
    )
    pay = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Pago", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Payroll(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(max_length=50, verbose_name="Fecha Incio", null=True)
    end_date = models.DateField(max_length=50, verbose_name="Fecha Fnal", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    monday = models.IntegerField(null=True, verbose_name="Lunes")
    tuesday = models.IntegerField(null=True, verbose_name="Martes")
    wednesday = models.IntegerField(null=True, verbose_name="Miercoles")
    thursday = models.IntegerField(null=True, verbose_name="Jueves")
    friday = models.IntegerField(null=True, verbose_name="Viernes")
    saturday = models.IntegerField(null=True, verbose_name="Sabado")
    sunday = models.IntegerField(null=True, verbose_name="Domingo")
    worked_days = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Dias trabajados", null=True
    )
    hours_worked = models.IntegerField(null=True, verbose_name="Horas trabajadas")
    sr = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="sr", null=True
    )
    payroll = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Nomina", null=True
    )
    props = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="apoyos", null=True
    )
    extra_hours = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="horas extras", null=True
    )
    double_days = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="dias dobles", null=True
    )
    discounts_loan = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="descuentos", null=True
    )
    total_pay = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Totales", null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="PayrollUser"
    )
    creation = models.DateTimeField(auto_now=True)


class ExtraHours(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    hours = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="horas extras", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class DoubleDays(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    days = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Dias dobles", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Props(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Dias dobles", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="PropsUser"
    )
    creation = models.DateTimeField(auto_now=True)


class Loans(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, related_name="employee"
    )
    loan = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Prestamo", null=True, default=0
    )
    weeks = models.IntegerField(null=True, verbose_name="Semanas")
    payment = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Abonos", null=True, default=0
    )
    status = models.CharField(max_length=500, verbose_name="Estado", null=True)
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="LoansUser"
    )
    creation = models.DateTimeField(auto_now=True)


class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    loan = models.ForeignKey(
        Loans, on_delete=models.CASCADE, null=True, verbose_name="Prestamo"
    )
    payment = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Abono", null=True, default=0
    )


class LoansChargers(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    loan = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Prestamo", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class PaymentsChargers(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    payment = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Pago", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class LoansDrivers(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    loan = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Prestamo", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class PaymentsDrivers(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    payment = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Pago", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class BillOfLading(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    invoice = models.CharField(max_length=100, verbose_name="Factura", null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=100, verbose_name="Código", null=True)
    destination = models.CharField(max_length=100, verbose_name="destino", null=True)
    km = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="KM", null=True
    )
    sat_code = models.CharField(max_length=100, verbose_name="Código SAT", null=True)
    product = models.CharField(max_length=100, verbose_name="Producto", null=True)
    kg = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="KG", null=True
    )
    unit_price_1 = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="P.U", null=True
    )
    total_value = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total value", null=True
    )
    driver = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    tract = models.IntegerField(null=True, verbose_name="Tracto")
    cage = models.CharField(max_length=100, verbose_name="Jaula", null=True)
    amount = models.IntegerField(null=True, verbose_name="Cantidad")
    unit_price_2 = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="P.U", null=True
    )
    subtotal = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Subtotal", null=True
    )
    iva = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="IVA", null=True
    )
    retention = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Retención", null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", null=True
    )
    to_program = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="A programar", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class ConceptPayment(models.Model):
    concept = models.CharField(max_length=50, verbose_name="Unidad", null=True)
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Importe", blank=True, null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )


class PaymentSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    description = models.CharField(
        max_length=500, verbose_name="Descripción", null=True
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", null=True
    )
    code = models.CharField(max_length=500, verbose_name="Code", null=True)
    concepts = models.ManyToManyField(ConceptPayment, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class BankAccountsCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    bank = models.ForeignKey(
        Bank, verbose_name="Banco", on_delete=models.CASCADE, null=True
    )
    account_number = models.BigIntegerField(
        verbose_name="Número de cuenta", unique=True
    )
    interbank_key = models.BigIntegerField(
        verbose_name="Clave interbancaria", unique=True
    )
    owner = models.CharField(max_length=500, verbose_name="Propietario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class BankAccountsEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    bank = models.ForeignKey(
        Bank, verbose_name="Banco", on_delete=models.CASCADE, null=True
    )
    account_number = models.BigIntegerField(
        verbose_name="Número de cuenta", unique=True
    )
    interbank_key = models.BigIntegerField(
        verbose_name="Clave interbancaria", unique=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class BankAccountsProvider(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    bank = models.ForeignKey(
        Bank, verbose_name="Banco", on_delete=models.CASCADE, null=True
    )
    account_number = models.BigIntegerField(
        verbose_name="Número de cuenta", unique=True
    )
    interbank_key = models.BigIntegerField(
        verbose_name="Clave interbancaria", unique=True
    )
    owner = models.CharField(max_length=500, verbose_name="Propietario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class DepositControl(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    reference = models.BigIntegerField(verbose_name="Referencia bancaria", null=True)
    beneficiary = models.CharField(
        max_length=200, verbose_name="Beneficiario", null=True
    )
    concept = models.CharField(max_length=200, verbose_name="Concepto", null=True)
    amount = models.IntegerField(null=True, verbose_name="Importe")
    invoice = models.IntegerField(null=True, verbose_name="Factura")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class BillsPaidPlugins(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, verbose_name="Cliente"
    )
    invoice = models.ForeignKey(
        BilledIncome, on_delete=models.CASCADE, null=True, verbose_name="Cliente"
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )


class PaidPlugins(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.CharField(max_length=200, verbose_name="Folio", null=True)
    payment_date = models.DateField(
        max_length=50, verbose_name="Fecha de pago", null=True
    )
    date_issue = models.DateField(
        max_length=50, verbose_name="Fecha de emision", null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    bills = models.ManyToManyField(BillsPaidPlugins, blank=True)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Importe", null=True
    )
    code = models.CharField(
        max_length=20, verbose_name="Codigo", default="", blank=True, null=True
    )
    document = models.FileField(
        upload_to="PaidPlugins/", verbose_name="Complementos de Pago", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Conciliation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    reference = models.CharField(
        max_length=200, verbose_name="Referencia bancaria", null=True
    )
    beneficiary = models.CharField(
        max_length=500, verbose_name="Beneficiario", null=True
    )
    concept = models.CharField(max_length=200, verbose_name="Concepto", null=True)
    deposit = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Deposito", null=True
    )
    charge = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Cargo", null=True
    )
    pending_charge = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Cargo Pendiente", null=True
    )
    countable_balance = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Saldo Contable", null=True
    )
    account_balance = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Saldo Bancario", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_order = models.IntegerField(null=True, verbose_name="Orden de pedido")
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    deadline = models.DateField(
        max_length=50, verbose_name="Fecha de entrega", null=True
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE, null=True)
    net_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso neto", null=True
    )
    unit_price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio unitario", null=True
    )
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Importe", null=True
    )
    status = status = models.CharField(max_length=500, verbose_name="Estado", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class IncomeInvoices(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(BilledIncome, on_delete=models.CASCADE, null=True)
    income = models.IntegerField(null=True, verbose_name="Income")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class IncomeCreditNotes(models.Model):
    id = models.AutoField(primary_key=True)
    creditnote = models.ForeignKey(CreditNote, on_delete=models.CASCADE, null=True)
    income = models.IntegerField(null=True, verbose_name="Income")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    invoices = models.ManyToManyField(
        IncomeInvoices, blank=True, related_name="facturas"
    )
    creditnotes = models.ManyToManyField(
        IncomeCreditNotes, blank=True, related_name="notas"
    )
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=True)
    payment_plugin = models.ForeignKey(PaidPlugins, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Importe", null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class SegalmexReception(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Compañia",
        null=True,
        default="",
    )
    period = models.CharField(
        max_length=100, verbose_name="Periodo", null=True, default=""
    )
    year = models.IntegerField(verbose_name="Año", null=True)
    checkin_date = models.DateField(
        max_length=50, verbose_name="Fecha de ingreso", null=True, default=""
    )
    checkin_time = models.TimeField(
        max_length=50, verbose_name="Hora de ingreso", null=True, default=""
    )
    checkout_date = models.DateField(
        max_length=50, verbose_name="Fecha de salida", null=True, default=""
    )
    checkout_time = models.TimeField(
        max_length=50, verbose_name="Hora de salida", null=True, default=""
    )
    ticket = models.IntegerField(verbose_name="No. de Boleta", null=True, default="")
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        verbose_name="Productor",
        null=True,
        default="",
    )
    location = models.CharField(
        max_length=200, verbose_name="Localidad", null=True, default=""
    )
    driver = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="Chofer", null=True, default=""
    )
    plate = models.ForeignKey(
        Plate, on_delete=models.CASCADE, verbose_name="Unidad", null=True, default=""
    )
    lot = models.CharField(max_length=100, verbose_name="Lote", null=True, default="")
    observation = models.CharField(
        max_length=500, verbose_name="Observacion", null=True, default=""
    )
    contract = models.CharField(
        max_length=100, verbose_name="contrato", null=True, default=""
    )
    variety = models.ForeignKey(
        Variety,
        on_delete=models.CASCADE,
        verbose_name="variedad",
        null=True,
        default="",
    )
    municipality = models.CharField(
        max_length=100, verbose_name="municipio", null=True, default=""
    )
    action = models.CharField(
        max_length=50, verbose_name="accion", null=True, default=""
    )
    gross_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso bruto", null=True, default=0
    )
    tare_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso tara", null=True, default=0
    )
    field_weight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Peso campo", null=True, default=0
    )
    h_d = models.DecimalField(
        verbose_name="humedad y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    h_t = models.DecimalField(
        verbose_name="humedad y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    h_da = models.DecimalField(
        verbose_name="humedad y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    i_d = models.DecimalField(
        verbose_name="impurezas y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    i_t = models.DecimalField(
        verbose_name="impurezas y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    i_da = models.DecimalField(
        verbose_name="impurezas y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gq_d = models.DecimalField(
        verbose_name="grano quebrado y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gq_t = models.DecimalField(
        verbose_name="grano quebrado y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gq_da = models.DecimalField(
        verbose_name="grano quebrado y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gv_d = models.DecimalField(
        verbose_name="grano verde y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gv_t = models.DecimalField(
        verbose_name="grano verde y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gv_da = models.DecimalField(
        verbose_name="grano verde y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gm_d = models.DecimalField(
        verbose_name="grano manchado y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gm_t = models.DecimalField(
        verbose_name="grano manchado y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    gm_da = models.DecimalField(
        verbose_name="grano manchado y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    ge_d = models.DecimalField(
        verbose_name="grano estrellado y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    ge_t = models.DecimalField(
        verbose_name="grano estrellado y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    ge_da = models.DecimalField(
        verbose_name="grano estrellado y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    cr_d = models.DecimalField(
        verbose_name="cuticula roja y dictaminado",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    cr_t = models.DecimalField(
        verbose_name="cuticula roja y tolerancia",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    cr_da = models.DecimalField(
        verbose_name="cuticula roja y deduccion aplicable",
        max_digits=19,
        decimal_places=2,
        null=True,
        default=0,
    )
    discount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Descuento", null=True, default=0
    )
    discounted_weight = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Peso con descuento",
        null=True,
        default=0,
    )
    net_analyzed = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Neto analizado",
        null=True,
        default=0,
    )
    balance = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name="Saldo a liquidar",
        null=True,
        default=0,
    )
    balance_letters = models.CharField(
        max_length=500, verbose_name="Comentario", null=True, default=0
    )
    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Precio", null=True, default=0
    )
    freight = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Flete", null=True, default=0
    )
    total = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", null=True, default=0
    )
    receive = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="Recibio",
        null=True,
        default="",
    )
    comment = models.CharField(
        max_length=500, verbose_name="Comentario", null=True, default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class PaymentOrderProducer(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    description = models.CharField(
        max_length=500, verbose_name="Descripcion de pago", null=True
    )
    producer = models.ForeignKey(
        Producer, on_delete=models.CASCADE, verbose_name="Productor", null=True
    )
    ticket = models.ForeignKey(
        SegalmexReception,
        on_delete=models.CASCADE,
        verbose_name="No. Boleta",
        null=True,
    )
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    generate_order = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="GeneraOrdenPago_proveedor",
        null=True,
    )
    authorize_order = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="AutorizaOrdenPago_proveedor",
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)


class PaymentProducer(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(max_length=50, verbose_name="Fecha", null=True)
    pay_order = models.ForeignKey(
        PaymentOrderProducer,
        on_delete=models.CASCADE,
        verbose_name="Orden de Pago",
        null=True,
    )
    description = models.CharField(
        max_length=500, verbose_name="Descripcion de pago", null=True
    )
    payment_method = models.CharField(
        max_length=50, verbose_name="Metodo de pago", null=True
    )
    amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Total", null=True
    )
    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, verbose_name="Cuenta de banco", null=True
    )
    comment = models.CharField(max_length=500, verbose_name="Comentario", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    creation = models.DateTimeField(auto_now=True)
