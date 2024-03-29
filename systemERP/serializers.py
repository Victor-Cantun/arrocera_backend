from dataclasses import fields
from rest_framework import serializers
from systemERP.models import (
    BankAccountsCustomer,
    BankAccountsEmployee,
    BankAccountsProvider,
    BillOfLading,
    BilledIncome,
    BillsPaidPlugins,
    Binnacle,
    Category,
    ChargerSalary,
    Company,
    Conciliation,
    CreditNote,
    Customer,
    Department,
    DepositControl,
    Diesel,
    DoubleDays,
    Driver,
    DriverSalary,
    Employee,
    ExtraHours,
    FileProducer,
    FileQuotation,
    FileUnit,
    FuelDump,
    FuelType,
    Fueling,
    Gasoline,
    Income,
    IncomeCreditNotes,
    IncomeInvoices,
    InitialCash,
    LandRent,
    Loans,
    LoansChargers,
    LoansDrivers,
    Location,
    MainPresentation,
    MainProduct,
    Output,
    OutputProduct,
    Outputreview,
    PaidPlugins,
    Parcel,
    PaymentOrderProducer,
    PaymentProducer,
    Payments,
    PaymentsChargers,
    PaymentsDrivers,
    Payroll,
    PettyCash,
    Plate,
    Presentation,
    Producer,
    Product,
    ProductBI,
    ProductCN,
    ProductPO,
    ProductQuotation,
    ProductRequisition,
    ProductShopping,
    ProductW,
    Production,
    Props,
    Provider,
    PurchaseOrder,
    Quotation,
    Requisition,
    Rowoutputreview,
    Rowticketreview,
    Sale,
    SegalmexParcel,
    SegalmexReception,
    Shopping,
    Silo,
    Society,
    Ticketreview,
    Unit,
    User,
    Bank,
    BankAccount,
    UploadImage,
    Variety,
    VehicleType,
    Warehouse,
    Payroll,
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class BankAccountListSerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        model = BankAccount
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        return response


class EmployeeListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["department"] = (
            instance.department.name if instance.department != None else ""
        )
        response["category"] = (
            instance.category.name if instance.category != None else ""
        )
        response["department_id"] = (
            instance.department.id if instance.department != None else ""
        )
        response["category_id"] = (
            instance.category.id if instance.category != None else ""
        )
        response["nombre_completo"] = (
            instance.name + " " + instance.surname + " " + instance.second_surname
        )

        return response


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = "__all__"


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = "__all__"


class UnitListSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Unit
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class FileUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUnit
        fields = "__all__"


class FilePaidPluginsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidPlugins
        fields = "__all__"


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = "__all__"


class FuelingListSerializer(serializers.ModelSerializer):
    fuel_type = FuelTypeSerializer(many=False, read_only=True)
    unit = UnitSerializer(many=False, read_only=True)

    class Meta:
        model = Fueling
        fields = "__all__"


class FuelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fueling
        fields = "__all__"


class FuelDumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelDump
        fields = "__all__"


class FuelDumpListSerializer(serializers.ModelSerializer):
    fuel_type = FuelTypeSerializer(many=False, read_only=True)
    unit = UnitSerializer(many=False, read_only=True)

    class Meta:
        model = FuelDump
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["unidad"] = instance.unit.unit if instance.unit != None else ""
        response["unidad_id"] = instance.unit.id if instance.unit != None else ""
        response["combustible"] = (
            instance.fuel_type.name if instance.fuel_type != None else ""
        )
        response["combustible_id"] = (
            instance.fuel_type.id if instance.fuel_type != None else ""
        )
        return response


class DieselListSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=False, read_only=True)

    class Meta:
        model = Diesel
        fields = "__all__"


class DieselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diesel
        fields = "__all__"


class GasolineListSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=False, read_only=True)

    class Meta:
        model = Gasoline
        fields = "__all__"


class GasolineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasoline
        fields = "__all__"


class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = "__all__"


class FileQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileQuotation
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRequisition
        fields = "__all__"


class RequisitionListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    applicant = EmployeeListSerializer(many=False, read_only=True)
    products = ProductRequisitionSerializer(many=True, read_only=True)

    class Meta:
        model = Requisition
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class MainProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProduct
        fields = "__all__"


class MainPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPresentation
        fields = "__all__"


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = "__all__"


class WarehouseListSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)

    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductsPOSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductPO
        fields = "__all__"


class PurchaseOrderListSerializer(serializers.ModelSerializer):
    products = ProductsPOSerializer(many=True, read_only=True)
    business_name = CustomerSerializer(many=False, read_only=True)
    auxiliary_sales = EmployeeSerializer(many=False, read_only=True)
    storekeeper = EmployeeSerializer(many=False, read_only=True)
    qa = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["business_name"] = (
            instance.business_name.name if instance.business_name != None else ""
        )
        response["auxiliardeventas"] = (
            instance.auxiliary_sales.name
            + " "
            + instance.auxiliary_sales.surname
            + " "
            + instance.auxiliary_sales.second_surname
            if instance.auxiliary_sales != None
            else ""
        )
        response["almacenista"] = (
            instance.storekeeper.name
            + " "
            + instance.storekeeper.surname
            + " "
            + instance.storekeeper.second_surname
            if instance.storekeeper != None
            else ""
        )
        response["controldecalidad"] = (
            instance.qa.name
            + " "
            + instance.qa.surname
            + " "
            + instance.qa.second_surname
            if instance.qa != None
            else ""
        )
        response["id_business"] = (
            instance.business_name.id if instance.business_name != None else ""
        )
        response["id_auxiliar"] = (
            instance.auxiliary_sales.id if instance.auxiliary_sales != None else ""
        )
        response["id_almacenista"] = (
            instance.storekeeper.id if instance.storekeeper != None else ""
        )
        response["id_qa"] = instance.qa.id if instance.qa != None else ""

        return response


class ListPurchaseOrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class ProductsQuotationSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductQuotation
        fields = "__all__"


class ListQuotationSerializer(serializers.ModelSerializer):
    products = ProductsQuotationSerializer(many=True, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    generator = EmployeeSerializer(many=False, read_only=True)
    authorizer = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = Quotation
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["genera"] = (
            instance.generator.name
            + " "
            + instance.generator.surname
            + " "
            + instance.generator.second_surname
            if instance.generator != None
            else ""
        )
        response["autoriza"] = (
            instance.authorizer.name
            + " "
            + instance.authorizer.surname
            + " "
            + instance.authorizer.second_surname
            if instance.authorizer != None
            else ""
        )
        response["id_customer"] = (
            instance.customer.id if instance.customer != None else ""
        )
        response["id_genera"] = (
            instance.generator.id if instance.generator != None else ""
        )
        response["id_autoriza"] = (
            instance.authorizer.id if instance.authorizer != None else ""
        )

        return response


class RowticketreviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    bigbags = PresentationSerializer(many=False, read_only=True)
    packages = PresentationSerializer(many=False, read_only=True)

    class Meta:
        model = Rowticketreview
        fields = "__all__"


class TicketreviewListSerializer(serializers.ModelSerializer):
    rows = RowticketreviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ticketreview
        fields = "__all__"


class RowoutputreviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    bigbags = PresentationSerializer(many=False, read_only=True)
    packages = PresentationSerializer(many=False, read_only=True)

    class Meta:
        model = Rowoutputreview
        fields = "__all__"


class OutputreviewListSerializer(serializers.ModelSerializer):
    rows = RowticketreviewSerializer(many=True, read_only=True)

    class Meta:
        model = Outputreview
        fields = "__all__"


class OutputProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    presentation = PresentationSerializer(many=False, read_only=True)

    class Meta:
        model = OutputProduct
        fields = "__all__"


class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = "__all__"


class OutputListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    driver = EmployeeSerializer(many=False, read_only=True)
    plate = UnitSerializer(many=False, read_only=True)
    bank_account = BankAccountListSerializer(many=False, read_only=True)
    delivered = EmployeeSerializer(many=False, read_only=True)
    products = OutputProductSerializer(many=True, read_only=True)

    class Meta:
        model = Output
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["company"] = (
            instance.company.name if instance.company != None else "",
        )
        response["id_company"] = (
            instance.company.id if instance.company != None else "",
        )
        response["customer"] = (
            instance.customer.name if instance.customer != None else ""
        )
        response["driver"] = (
            instance.driver.name
            + " "
            + instance.driver.surname
            + " "
            + instance.driver.second_surname
            if instance.driver != None
            else ""
        )
        response["plate"] = instance.plate.plate_no if instance.plate != None else ""
        response["bank_account"] = (
            instance.bank_account.number if instance.bank_account != None else ""
        )
        response["delivered"] = (
            instance.delivered.name
            + " "
            + instance.delivered.surname
            + " "
            + instance.delivered.second_surname
            if instance.delivered != None
            else ""
        )
        response["id_customer"] = (
            instance.customer.id if instance.customer != None else ""
        )
        response["id_driver"] = instance.driver.id if instance.driver != None else ""
        response["id_plate"] = instance.plate.id if instance.plate != None else ""
        response["id_bank_account"] = (
            instance.bank_account.id if instance.bank_account != None else ""
        )
        response["id_delivered"] = (
            instance.delivered.id if instance.delivered != None else ""
        )
        return response


class BinnacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Binnacle
        fields = "__all__"


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = "__all__"


class ParcelListSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(many=False, read_only=True)

    class Meta:
        model = Parcel
        fields = "__all__"


class ListLandRentSerializer(serializers.ModelSerializer):
    # parcel = ParcelSerializer(many=False, read_only=True)
    # bank_account = BankAccountListSerializer(many=False, read_only=True)
    class Meta:
        model = LandRent
        fields = "__all__"


class ListPettyCashSerializer(serializers.ModelSerializer):
    responsible = EmployeeSerializer(many=False, read_only=True)
    area = DepartmentSerializer(many=False, read_only=True)

    class Meta:
        model = PettyCash
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "description": instance.description,
            "responsible": instance.responsible.name,
            "area": instance.area.name,
            "cash": instance.cash,
            "discount": instance.discount,
            "responsible_id": instance.responsible.id
            if instance.responsible_id != None
            else "",
            "area_id": instance.area.id if instance.area_id != None else "",
        }


class PettyCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCash
        fields = "__all__"


class InitialCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialCash
        fields = "__all__"


class LandRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRent
        fields = "__all__"


class ProductShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShopping
        fields = "__all__"


class ShoppingListSerializer(serializers.ModelSerializer):
    products = ProductShoppingSerializer(many=True, read_only=True)
    requisition = RequisitionListSerializer(many=False, read_only=True)
    provider = ProviderSerializer(many=False, read_only=True)
    department = DepartmentSerializer(many=False, read_only=True)
    applicant = EmployeeSerializer(many=False, read_only=True)
    verify = EmployeeSerializer(many=False, read_only=True)
    authorizes = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = Shopping
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["requisition"] = (
            instance.requisition.folio if instance.requisition != None else ""
        )
        response["provider"] = (
            instance.provider.name if instance.provider != None else ""
        )
        response["department"] = (
            instance.department.name if instance.department != None else ""
        )
        response["requisition_id"] = (
            instance.requisition.id if instance.requisition != None else ""
        )
        response["provider_id"] = (
            instance.provider.id if instance.provider != None else ""
        )
        response["department_id"] = (
            instance.department.id if instance.department != None else ""
        )
        response["applicant"] = (
            instance.applicant.name
            + " "
            + instance.applicant.surname
            + " "
            + instance.applicant.second_surname
            if instance.applicant != None
            else ""
        )
        response["verify"] = (
            instance.verify.name
            + " "
            + instance.verify.surname
            + " "
            + instance.verify.second_surname
            if instance.verify != None
            else ""
        )
        response["authorizes"] = (
            instance.authorizes.name
            + " "
            + instance.authorizes.surname
            + " "
            + instance.authorizes.second_surname
            if instance.authorizes != None
            else ""
        )

        return response


class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = "__all__"


class SocietyListSerializer(serializers.ModelSerializer):
    producers = ProducerSerializer(many=True, read_only=True)

    class Meta:
        model = Society
        fields = "__all__"


class SegalmexParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegalmexParcel
        fields = "__all__"


class ListSegalmexParcelSerializer(serializers.ModelSerializer):
    society = SocietySerializer(many=False, read_only=True)
    cyclepv = ParcelSerializer(many=False, read_only=True)
    cycleoi = ParcelSerializer(many=False, read_only=True)

    class Meta:
        model = SegalmexParcel
        fields = "__all__"


class FileProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileProducer
        fields = "__all__"


class SegalmexReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegalmexReception
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class VarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Variety
        fields = "__all__"


class SiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silo
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = "__all__"


class ListSegalmexReceptionSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(many=False, read_only=True)
    driver = DriverSerializer(many=False, read_only=True)
    plate = PlateSerializer(many=False, read_only=True)
    variety = VarietySerializer(many=False, read_only=True)
    receive = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = SegalmexReception
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["company"] = instance.company.name if instance.company != None else ""
        response["producer"] = (
            instance.producer.name if instance.producer != None else ""
        )
        response["driver"] = instance.driver.name if instance.driver != None else ""
        # response["brand"] = instance.plate.brand if instance.plate != None else ""
        # response["model"] = instance.plate.model if instance.plate != None else ""
        response["plate"] = instance.plate.plate if instance.plate != None else ""
        response["variety"] = instance.variety.name if instance.variety != None else ""
        response["receive"] = instance.receive.name if instance.receive != None else ""

        response["company_id"] = instance.company.id if instance.company != None else ""
        response["producer_id"] = (
            instance.producer.id if instance.producer != None else ""
        )
        response["driver_id"] = instance.driver.id if instance.driver != None else ""
        response["plate_id"] = instance.plate.id if instance.plate != None else ""
        response["variety_id"] = instance.variety.id if instance.variety != None else ""
        response["receive_id"] = instance.receive.id if instance.receive != None else ""

        return response


class PaymentOrderProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOrderProducer
        fields = "__all__"


class ListPaymentOrderProducerSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(many=False, read_only=True)
    generate_order = EmployeeSerializer(many=False, read_only=True)
    authorize_order = EmployeeSerializer(many=False, read_only=True)
    ticket = ListSegalmexReceptionSerializer(many=False, read_only=True)

    class Meta:
        model = PaymentOrderProducer
        fields = "__all__"


class PaymentProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProducer
        fields = "__all__"


class ListPaymentProducerSerializer(serializers.ModelSerializer):
    pay_order = ListPaymentOrderProducerSerializer(many=False, read_only=True)
    bank_account = BankAccountSerializer(many=False, read_only=True)

    class Meta:
        model = PaymentProducer
        fields = "__all__"


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class DriverSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverSalary
        fields = "__all__"


class ListDriverSalarySerializer(serializers.ModelSerializer):
    driver = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = DriverSalary
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "product": instance.product,
            "invoice": instance.invoice,
            "source": instance.source,
            "destination": instance.destination,
            "tonnage": instance.tonnage,
            "price": instance.price,
            "freight": instance.freight,
            "percentage": instance.percentage,
            "advance": instance.advance,
            "balance": instance.balance,
            "driver_id": instance.driver.id if instance.driver_id != None else "",
        }


class ChargerSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargerSalary
        fields = "__all__"


class ListChargerSalarySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=True)
    charger = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = ChargerSalary
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "product": instance.product,
            "customer": instance.customer.name if instance.custumer != None else "",
            "invoice": instance.invoice,
            "tonnage": instance.tonnage,
            "packaging": instance.packaging,
            "rate": instance.rate,
            "pay": instance.pay,
            "customer_id": instance.customer.id if instance.customer_id != None else "",
        }


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = "__all__"


class ListPayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = "__all__"


class ListCalculatePayrollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    nombre_completo = serializers.CharField()
    department = serializers.CharField()
    sr = serializers.DecimalField(max_digits=8, decimal_places=2)
    TotalAbono = serializers.DecimalField(max_digits=8, decimal_places=2)
    TotalHorasExtras = serializers.DecimalField(max_digits=8, decimal_places=2)
    TotalApoyo = serializers.DecimalField(max_digits=8, decimal_places=2)
    TotalDiasDobles = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Employee
        fields = [
            "id",
            "nombre_completo",
            "department",
            "sr",
            "TotalAbono",
            "TotalHorasExtras",
            "TotalApoyo",
            "TotalDiasDobles",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["id"] = response["id"]
        response["nombre_completo"] = response["nombre_completo"]
        response["department"] = response["department"]
        response["sr"] = response["sr"] if response["sr"] != None else 0
        response["TotalApoyo"] = (
            response["TotalApoyo"] if response["TotalApoyo"] != None else 0
        )
        response["TotalHorasExtras"] = (
            response["TotalHorasExtras"] if response["TotalHorasExtras"] != None else 0
        )
        response["TotalDiasDobles"] = (
            response["TotalDiasDobles"] if response["TotalDiasDobles"] != None else 0
        )
        response["TotalAbono"] = (
            response["TotalAbono"] if response["TotalAbono"] != None else 0
        )

        return response


class ExtraHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraHours
        fields = "__all__"


class ListExtraHoursSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = ExtraHours
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "hours": instance.hours,
            "comment": instance.comment,
        }


class DoubleDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubleDays
        fields = "__all__"


class ListDoubleDaysSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = DoubleDays
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "days": instance.days,
            "comment": instance.comment,
        }


class PropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Props
        fields = "__all__"


class ListPropsSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = Props
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "amount": instance.amount,
            "comment": instance.comment,
        }


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class EmployeeLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("name",)


class ListLoansSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.CharField()
    employee = serializers.IntegerField()
    nombre_completo = serializers.CharField()
    loan = serializers.DecimalField(max_digits=8, decimal_places=2)
    TotalPayment = serializers.DecimalField(max_digits=8, decimal_places=2)
    TotalSaldo = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Loans
        # fields = '__all__'
        fields = [
            "id",
            "date",
            "employee",
            "nombre_completo",
            "loan",
            "TotalPayment",
            "TotalSaldo",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["id"] = response["id"]
        response["date"] = response["date"]
        response["employee"] = response["employee"]
        response["nombre_completo"] = response["nombre_completo"]
        response["loan"] = response["loan"]
        response["TotalPayment"] = (
            response["TotalPayment"] if response["TotalPayment"] != None else 0
        )
        response["TotalSaldo"] = (
            response["TotalSaldo"] if response["TotalSaldo"] != None else 0
        )

        return response


class LoansChargersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansChargers
        fields = "__all__"


class PaymentsChargersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsChargers
        fields = "__all__"


class LoansDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansDrivers
        fields = "__all__"


class PaymentsDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsDrivers
        fields = "__all__"


class ListLoansChargersSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = LoansChargers
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "loan": instance.loan,
            "comment": instance.comment,
        }


class ListPaymentsChargersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsChargers
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "payment": instance.payment,
            "comment": instance.comment,
        }


class ListLoansDriversSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = LoansDrivers
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "loan": instance.loan,
            "comment": instance.comment,
        }


class ListPaymentsDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsDrivers
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "date": instance.date,
            "employee": instance.employee.name + " " + instance.employee.surname
            if instance.employee != None
            else "",
            "payment": instance.payment,
            "comment": instance.comment,
        }


class BillOfLadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfLading
        fields = "__all__"


class ListBillOfLadingSerializer(serializers.ModelSerializer):
    driver = EmployeeSerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = BillOfLading
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["customer"] = (
            instance.customer.name if instance.customer != None else ""
        )
        response["driver"] = (
            instance.driver.name
            + " "
            + instance.driver.surname
            + " "
            + instance.driver.second_surname
            if instance.driver != None
            else ""
        )
        response["id_customer"] = (
            instance.customer.id if instance.customer != None else ""
        )
        response["id_driver"] = instance.driver.id if instance.driver != None else ""
        return response


class ListPaymentScheduleSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    bank_account = BankAccountSerializer(many=False, read_only=True)

    class Meta:
        model = BillOfLading
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["company"] = (
            instance.company.name if instance.company != None else "",
        )
        response["bank_account"] = (
            instance.bank_account.number if instance.bank_account != None else "",
        )
        response["customer"] = (
            instance.customer.name if instance.customer != None else "",
        )
        response["rfc"] = (instance.customer.rfc if instance.customer != None else "",)
        response["description"] = instance.description
        response["total"] = instance.total

        return response


class BankAccountsCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountsCustomer
        fields = "__all__"


class ListBankAccountsCustomerSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)

    class Meta:
        model = BankAccountsCustomer
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "customer": instance.customer.name if instance.customer != None else "",
            "bank": instance.bank.name if instance.bank != None else "",
            "account_number": instance.account_number,
            "interbank_key": instance.interbank_key,
            "owner": instance.owner,
        }


class BankAccountsProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountsProvider
        fields = "__all__"


class ListBankAccountsProviderSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)

    class Meta:
        model = BankAccountsProvider
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "provider": instance.provider.name if instance.provider != None else "",
            "bank": instance.bank.name if instance.bank != None else "",
            "account_number": instance.account_number,
            "interbank_key": instance.interbank_key,
            "owner": instance.owner,
        }


class BankAccountsEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountsEmployee
        fields = "__all__"


class ListBankAccountsEmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)

    class Meta:
        model = BankAccountsEmployee
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "employee": instance.employee.name if instance.employee != None else "",
            "bank": instance.bank.name if instance.bank != None else "",
            "account_number": instance.account_number,
            "interbank_key": instance.interbank_key,
        }


class BilledIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilledIncome
        fields = "__all__"


class ProductsBilledSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductBI
        fields = "__all__"


class ListBilledIncomeSerializer(serializers.ModelSerializer):
    products = ProductsBilledSerializer(many=True, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = BilledIncome
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["customer"] = (
            instance.customer.name if instance.customer != None else ""
        )

        response["customer_id"] = (
            instance.customer.id if instance.customer != None else ""
        )

        return response


class ProductsCNSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductCN
        fields = "__all__"


class CreditNoteListSerializer(serializers.ModelSerializer):
    products = ProductsCNSerializer(many=True, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    auxiliary_sales = EmployeeSerializer(many=False, read_only=True)
    storekeeper = EmployeeSerializer(many=False, read_only=True)
    qa = EmployeeSerializer(many=False, read_only=True)
    invoice = BilledIncomeSerializer(many=False, read_only=True)

    class Meta:
        model = CreditNote
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["business_name"] = (
            instance.customer.name if instance.customer != None else ""
        )
        response["auxiliardeventas"] = (
            instance.auxiliary_sales.name
            + " "
            + instance.auxiliary_sales.surname
            + " "
            + instance.auxiliary_sales.second_surname
            if instance.auxiliary_sales != None
            else ""
        )
        response["almacenista"] = (
            instance.storekeeper.name
            + " "
            + instance.storekeeper.surname
            + " "
            + instance.storekeeper.second_surname
            if instance.storekeeper != None
            else ""
        )
        response["controldecalidad"] = (
            instance.qa.name
            + " "
            + instance.qa.surname
            + " "
            + instance.qa.second_surname
            if instance.qa != None
            else ""
        )
        response["id_business"] = (
            instance.customer.id if instance.customer != None else ""
        )
        response["id_auxiliar"] = (
            instance.auxiliary_sales.id if instance.auxiliary_sales != None else ""
        )
        response["id_almacenista"] = (
            instance.storekeeper.id if instance.storekeeper != None else ""
        )
        response["id_qa"] = instance.qa.id if instance.qa != None else ""
        response["id_invoice"] = instance.invoice.id if instance.invoice != None else ""

        return response


class FacturaSerializer(serializers.ModelSerializer):
    invoice = BilledIncomeSerializer(many=False, read_only=True)

    # income = serializers.IntegerField()
    class Meta:
        model = IncomeInvoices
        fields = "__all__"


class NotasSerializer(serializers.ModelSerializer):
    creditnote = CreditNoteListSerializer(many=False, read_only=True)

    class Meta:
        model = IncomeCreditNotes
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


# *? COMPLEMENTOS DE PAGO
class FacturaComplementoSerializer(serializers.ModelSerializer):
    invoice = BilledIncomeSerializer(many=False, read_only=True)

    # income = serializers.IntegerField()
    class Meta:
        model = BillsPaidPlugins
        fields = "__all__"


class ListPaidPluginsSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=True)
    account = BankAccountSerializer(many=False, read_only=True)
    bills = FacturaComplementoSerializer(many=True, read_only=True)

    # creditnotes = NotasSerializer(many=True, read_only=True)
    class Meta:
        model = PaidPlugins
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["customer_id"] = (
            instance.customer.id if instance.customer != None else ""
        )
        response["account_id"] = instance.account.id if instance.account != None else ""

        return response


class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    presentation = PresentationSerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = Sale
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["presentation_id"] = (
            instance.presentation.id if instance.presentation != None else ""
        )
        response["product_id"] = instance.product.id if instance.product != None else ""
        response["customer_id"] = (
            instance.customer.id if instance.customer != None else ""
        )

        return response


class ListSalesSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    presentation = PresentationSerializer(many=False, read_only=True)
    # company = CompanySerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = Sale
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response["product"] = (
            instance.product.name if instance.product != None else "",
        )
        response["presentation"] = (
            instance.presentation.name if instance.presentation != None else "",
        )
        response["customer"] = (
            instance.customer.name if instance.customer != None else "",
        )

        return response


class DepositControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositControl
        fields = "__all__"


class ListDepositControlSerializer(serializers.ModelSerializer):
    account = MainProductSerializer(many=False, read_only=True)

    class Meta:
        model = DepositControl
        fields = "__all__"


class ConciliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conciliation
        fields = "__all__"


class ListConciliationSerializer(serializers.ModelSerializer):
    account = MainProductSerializer(many=False, read_only=True)

    class Meta:
        model = Conciliation
        fields = "__all__"


class ListTotalDepositControlSerializer(serializers.ModelSerializer):
    account = BankAccountSerializer(many=False, read_only=True)

    class Meta:
        model = DepositControl
        fields = "__all__"


class PaidPluginsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidPlugins
        fields = "__all__"


class ListAccountStatusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    customer = serializers.CharField()
    invoice = serializers.CharField()
    date = serializers.CharField()
    total = serializers.DecimalField(max_digits=8, decimal_places=2)
    ImporteNC = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = BilledIncome
        fields = ["id", "customer", "invoice", "date", "total", "ImporteNC"]


class ListIncomeSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=True)
    bank_account = BankAccountSerializer(many=False, read_only=True)
    invoices = FacturaSerializer(many=True, read_only=True)
    creditnotes = NotasSerializer(many=True, read_only=True)
    payment_plugin = ListPaidPluginsSerializer(many=False, read_only=True)

    class Meta:
        model = Income
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["id_customer"] = (
            instance.customer.id if instance.customer != None else ""
        )
        response["id_account"] = (
            instance.bank_account.id if instance.bank_account != None else ""
        )
        response["id_plugin"] = (
            instance.payment_plugin.id if instance.payment_plugin != None else ""
        )

        return response


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = "__all__"
