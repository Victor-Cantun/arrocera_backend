from dataclasses import fields
from rest_framework import serializers
from systemERP.models import BankAccountsCustomer, BankAccountsEmployee, BankAccountsProvider, BillOfLading, BilledIncome, Binnacle, Category, ChargerSalary, Company, CreditNote, Customer, Department, DepositControl, Diesel, DoubleDays, DriverSalary, Employee, ExtraHours, FileProducer, FileQuotation, FileUnit, FuelDump, FuelType, Fueling, Gasoline, LandRent, Loans, LoansChargers, LoansDrivers, Location, MainProduct, Output, OutputProduct, Outputreview, PaidPlugins, Parcel, PaymentOrderProducer, PaymentProducer, PaymentsChargers, PaymentsDrivers, Payroll, PettyCash, Presentation, Producer, Product, ProductCN, ProductQuotation, ProductRequisition, ProductShopping, ProductW, Props, Provider, Quotation, Requisition, Rowoutputreview, Rowticketreview, SegalmexParcel, SegalmexReception, Shopping, Society, Ticketreview, Unit, User, Bank, BankAccount, UploadImage, Variety, VehicleType, Warehouse, Payroll

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
              
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BankAccountListSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = BankAccount
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    category= CategorySerializer(many=False, read_only=True)
    bank= BankSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['department'] = instance.department.name if instance.department != None else '',
        response['category'] = instance.category.name if instance.department != None else '',       
        return response        

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class UnitListSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer(many=False, read_only=True)
    class Meta:
        model = Unit
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class FileUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUnit
        fields = '__all__'        

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'

class FuelingListSerializer(serializers.ModelSerializer):
    fuel_type = FuelTypeSerializer(many=False, read_only=True)
    unit = UnitSerializer(many=False, read_only=True)
    class Meta:
        model = Fueling
        fields = '__all__'

class FuelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fueling
        fields = '__all__'        

class FuelDumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelDump
        fields = '__all__'

class FuelDumpListSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=False, read_only=True)
    class Meta:
        model = FuelDump
        fields = '__all__'

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['unit'] = instance.unit.unit if instance.unit != None else '',
        return response


class DieselListSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=False, read_only=True)
    class Meta:
        model = Diesel
        fields = '__all__'

class DieselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diesel
        fields = '__all__'

class GasolineListSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(many=False, read_only=True)
    class Meta:
        model = Gasoline
        fields = '__all__'

class GasolineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasoline
        fields = '__all__'

class RequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisition
        fields = '__all__'

class FileQuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileQuotation
        fields = '__all__'           

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductRequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRequisition
        fields = '__all__'        

class RequisitionListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    applicant = EmployeeListSerializer(many=False, read_only=True)
    products = ProductRequisitionSerializer(many=True, read_only=True)
    class Meta:
        model = Requisition
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ListCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class MainProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProduct
        fields = '__all__'

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'

class WarehouseListSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    class Meta:
        model = Warehouse
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductsCNSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    class Meta:
        model = ProductCN
        fields = '__all__'

class CreditNoteListSerializer(serializers.ModelSerializer):

    creditnote_products = ProductsCNSerializer(many=True, read_only=True)
    business_name = CustomerSerializer(many=False, read_only=True)
    auxiliary_sales = EmployeeSerializer(many=False, read_only=True)
    storekeeper =  EmployeeSerializer(many=False, read_only=True)
    qa = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = CreditNote
        fields = '__all__'

class ProductsQuotationSerializer(serializers.ModelSerializer):
    presentation = PresentationSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    class Meta:
        model = ProductQuotation
        fields = '__all__'

class ListQuotationSerializer(serializers.ModelSerializer):
    products = ProductsQuotationSerializer(many=True, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    generator = EmployeeSerializer(many=False, read_only=True)
    authorizer =  EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = Quotation
        fields = '__all__'

class RowticketreviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    bigbags = PresentationSerializer(many=False, read_only=True)
    packages = PresentationSerializer(many=False, read_only=True)
    class Meta:
        model = Rowticketreview
        fields = '__all__'

class TicketreviewListSerializer(serializers.ModelSerializer):
    rows = RowticketreviewSerializer(many=True, read_only=True)
    class Meta:
        model = Ticketreview
        fields = '__all__'

class RowoutputreviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    bigbags = PresentationSerializer(many=False, read_only=True)
    packages = PresentationSerializer(many=False, read_only=True)
    class Meta:
        model = Rowoutputreview
        fields = '__all__'

class OutputreviewListSerializer(serializers.ModelSerializer):
    rows = RowticketreviewSerializer(many=True, read_only=True)
    class Meta:
        model = Outputreview
        fields = '__all__'

class OutputProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    presentation = PresentationSerializer(many=False, read_only=True)
    
    class Meta:
        model = OutputProduct
        fields = '__all__'

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'        

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
        fields = ['id','company','date','invoice','customer','destiny','gross_weight','tare','net_weight', 'driver', 'plate','payment_method','bank_account','subtotal', 'iva', 'total', 'delivered', 'received','comment','products']   

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['company'] = instance.company.name if instance.company != None else '',
        response['customer'] = instance.customer.name if instance.customer != None else '',
        response['driver'] = instance.driver.name if instance.driver != None else '',
        response['plate'] = instance.plate.plate_no if instance.plate != None else '',
        response['bank_account'] = instance.bank_account.number if instance.bank_account != None else '',
        response['delivered'] = instance.delivered.name if instance.delivered != None else ''
        
        return response

class BinnacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Binnacle
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

class ParcelListSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(many=False, read_only=True)
    class Meta:
        model = Parcel
        fields = '__all__'

class ListLandRentSerializer(serializers.ModelSerializer):
    parcel = ParcelSerializer(many=False, read_only=True)
    bank_account = BankAccountListSerializer(many=False, read_only=True)
    class Meta:
        model = LandRent
        fields = '__all__'        

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'rent_year':instance.rent_year,
            'reason_rent':instance.reason_rent,
            'lessor':instance.parcel.owner if instance.parcel != None else '',
            'location':instance.parcel.location if instance.parcel != None else '',
            'parcel_no':instance.parcel.no_parcel if instance.parcel != None else '',
            'hectares':instance.parcel.hectares if instance.parcel != None else '',
            'price_hectare':instance.parcel.price_hectare if instance.parcel != None else '',
            'rental_value':instance.parcel.rental_value if instance.parcel != None else '',
            'advances':instance.advances,
            'amount':instance.amount,
            'payment':instance.payment,
            'balance_against':instance.balance_against,
            'payment_method':instance.payment_method if instance.payment_method != None else '',
            'payment_date':instance.payment_date if instance.payment_date != None else '',
            'bank_account':instance.bank_account.number if instance.bank_account != None else '',
            'parcel_id':instance.parcel.id if instance.parcel != None else '',
            'bank_account_id':instance.bank_account.id  if instance.bank_account_id != None else '',     
        }   

class ListPettyCashSerializer(serializers.ModelSerializer):
    responsible = EmployeeSerializer(many=False, read_only=True)
    area = DepartmentSerializer(many=False, read_only=True)
    class Meta:
        model = PettyCash
        fields = '__all__'
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'description':instance.description,
            'responsible':instance.responsible.name,
            'area':instance.area.name,
            'cash':instance.cash,
            'discount':instance.discount,
            'responsible_id':instance.responsible.id if instance.responsible_id != None else '', 
            'area_id':instance.area.id if instance.area_id != None else '', 
        }

class PettyCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCash
        fields = '__all__'

class LandRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRent
        fields = '__all__'     

class ProductShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShopping
        fields = '__all__'

class ShoppingListSerializer(serializers.ModelSerializer):

    products = ProductShoppingSerializer(many=True, read_only=True)
    requisition = RequisitionListSerializer(many=False, read_only=True)
    provider = ProviderSerializer(many=False, read_only=True)
    department = DepartmentSerializer(many=False, read_only=True)
    applicant = EmployeeSerializer(many=False, read_only=True)
    verify =  EmployeeSerializer(many=False, read_only=True)
    authorizes = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = Shopping
        fields = '__all__'

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = '__all__'

class SocietyListSerializer(serializers.ModelSerializer):
    producers = ProducerSerializer(many=True, read_only=True)
    class Meta:
        model = Society
        fields = '__all__'

class SegalmexParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegalmexParcel
        fields = '__all__'

class ListSegalmexParcelSerializer(serializers.ModelSerializer):
    society = SocietySerializer(many=False, read_only=True)
    cyclepv = ParcelSerializer(many=False, read_only=True)
    cycleoi = ParcelSerializer(many=False, read_only=True)
    class Meta:
        model = SegalmexParcel
        fields = '__all__'

class FileProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileProducer
        fields = '__all__'

class SegalmexReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegalmexReception
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class VarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Variety
        fields = '__all__'

class ListSegalmexReceptionSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(many=False, read_only=True)
    location = LocationSerializer(many=False, read_only=True)
    driver = EmployeeSerializer(many=False, read_only=True)
    plate = UnitSerializer(many=False, read_only=True)
    variety = VarietySerializer(many=False, read_only=True)
    receive = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = SegalmexReception
        fields = '__all__'

class PaymentOrderProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOrderProducer
        fields = '__all__'

class ListPaymentOrderProducerSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer(many=False, read_only=True)
    generate_order = EmployeeSerializer(many=False, read_only=True)
    authorize_order = EmployeeSerializer(many=False, read_only=True)
    ticket = ListSegalmexReceptionSerializer(many=False, read_only=True)
    class Meta:
        model = PaymentOrderProducer
        fields = '__all__'

class PaymentProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProducer
        fields = '__all__'

class ListPaymentProducerSerializer(serializers.ModelSerializer):
    pay_order = ListPaymentOrderProducerSerializer(many=False, read_only=True)
    bank_account = BankAccountSerializer(many=False, read_only=True)
    class Meta:
        model = PaymentProducer
        fields = '__all__'

class DriverSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverSalary
        fields = '__all__'

class ListDriverSalarySerializer(serializers.ModelSerializer):
    driver = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = DriverSalary
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'product':instance.product,
            'invoice':instance.invoice,
            'source':instance.source,
            'destination':instance.destination,
            'tonnage':instance.tonnage,
            'price':instance.price,
            'freight':instance.freight,
            'percentage':instance.percentage,
            'advance':instance.advance,
            'balance':instance.balance,
            'driver_id':instance.driver.id  if instance.driver_id != None else '',     
        }          

class ChargerSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargerSalary
        fields = '__all__'

class ListChargerSalarySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=True)
    charger = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = ChargerSalary
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'product':instance.product,
            'customer':instance.customer.name if instance.custumer != None else '',
            'invoice':instance.invoice,
            'tonnage':instance.tonnage,
            'packaging':instance.packaging,
            'rate':instance.rate,
            'pay':instance.pay,
            'customer_id':instance.customer.id  if instance.customer_id != None else '',  
        }   

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'

class ListPayrollSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = Payroll
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'start_date':instance.start_date,
            'end_date':instance.end_date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'worked_days':instance.worked_days,
            'sr':instance.sr,
            'payroll':instance.payroll,
            'props':instance.props,
            'extra_hours':instance.extra_hours,
            'double_days':instance.double_days,
            'discounts_loan':instance.discounts_loan,
            'total_pay':instance.total_pay
        } 

class ExtraHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraHours
        fields = '__all__'

class ListExtraHoursSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = ExtraHours
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'hours':instance.hours,
            'comment':instance.comment
        } 

class DoubleDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubleDays
        fields = '__all__'

class ListDoubleDaysSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = DoubleDays
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'days':instance.days,
            'comment':instance.comment
        } 

class PropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Props
        fields = '__all__'

class ListPropsSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = Props
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'amount':instance.amount,
            'comment':instance.comment
        } 

class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'

class ListLoansSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = Loans
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'loan':instance.loan,
            'weeks':instance.weeks,
            'payment':instance.payment,
            'comment':instance.comment
        } 

class LoansChargersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansChargers
        fields = '__all__'

class PaymentsChargersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsChargers
        fields = '__all__'

class LoansDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansDrivers
        fields = '__all__'

class PaymentsDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsDrivers
        fields = '__all__'

class ListLoansChargersSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = LoansChargers
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'loan':instance.loan,
            'comment':instance.comment
        } 

class ListPaymentsChargersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsChargers
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'payment':instance.payment,
            'comment':instance.comment
        } 

class ListLoansDriversSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        model = LoansDrivers
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'loan':instance.loan,
            'comment':instance.comment
        } 

class ListPaymentsDriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsDrivers
        fields = '__all__'
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'employee':instance.employee.name+" "+instance.employee.surname if instance.employee != None else '',
            'payment':instance.payment,
            'comment':instance.comment
        } 

class BillOfLadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfLading
        fields = '__all__'

class ListBillOfLadingSerializer(serializers.ModelSerializer):
    driver = EmployeeSerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    class Meta:
        model = BillOfLading
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'date':instance.date,
            'invoice':instance.invoice,
            'customer':instance.customer.name if instance.customer != None else '',
            'code':instance.code,
            'destination':instance.destination,
            'km':instance.km,
            'sat_code':instance.sat_code,
            'product':instance.product,
            'kg':instance.kg,
            'unit_price_1':instance.unit_price_1,
            'total_value':instance.total_value,
            'driver':instance.driver.name+" "+instance.driver.surname if instance.driver != None else '',
            'tract':instance.tract,
            'cage':instance.cage,
            'amount':instance.amount,
            'unit_price_2':instance.unit_price_2,
            'subtotal':instance.subtotal,
            'iva':instance.iva,
            'retention':instance.retention,
            'total':instance.total,
            'to_program':instance.to_program,
        } 

class ListPaymentScheduleSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    bank_account = BankAccountSerializer(many=False, read_only=True)
    class Meta:
        model = BillOfLading
        fields = '__all__'

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['company'] = instance.company.name if instance.company != None else '',
        response['bank_account'] = instance.bank_account.number if instance.bank_account != None else '',
        response['customer'] = instance.customer.name if instance.customer != None else '',
        response['rfc'] = instance.customer.rfc if instance.customer != None else '',
        response['description'] = instance.description
        response['total'] = instance.total
        
        return response

class BankAccountsCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountsCustomer
        fields = '__all__'

class ListBankAccountsCustomerSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)
    class Meta:
        model = BankAccountsCustomer
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'customer':instance.customer.name if instance.customer != None else '',
            'bank':instance.bank.name if instance.bank != None else '',
            'account_number':instance.account_number,
            'interbank_key':instance.interbank_key,
            'owner':instance.owner
        } 

class BankAccountsProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountsProvider
        fields = '__all__'

class ListBankAccountsProviderSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)
    class Meta:
        model = BankAccountsProvider
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'provider':instance.provider.name if instance.provider != None else '',
            'bank':instance.bank.name if instance.bank != None else '',
            'account_number':instance.account_number,
            'interbank_key':instance.interbank_key,
            'owner':instance.owner
        } 


class BankAccountsEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountsEmployee
        fields = '__all__'

class ListBankAccountsEmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=False, read_only=True)
    bank = BankSerializer(many=False, read_only=True)
    class Meta:
        model = BankAccountsEmployee
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'employee':instance.employee.name if instance.employee != None else '',
            'bank':instance.bank.name if instance.bank != None else '',
            'account_number':instance.account_number,
            'interbank_key':instance.interbank_key,
        }         

class BilledIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilledIncome
        fields = '__all__'

class ListBilledIncomeSerializer(serializers.ModelSerializer):
    product = MainProductSerializer(many=False, read_only=True)
    company = CompanySerializer(many=False, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    class Meta:
        model = BilledIncome
        fields = '__all__'
    
    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['company'] = instance.company.name if instance.company != None else '',
        response['product'] = instance.product.name if instance.product != None else '',
        response['customer'] = instance.customer.name if instance.customer != None else '',
        
        return response

class DepositControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositControl
        fields = '__all__'

class ListDepositControlSerializer(serializers.ModelSerializer):
    account = MainProductSerializer(many=False, read_only=True)
    
    class Meta:
        model = DepositControl
        fields = '__all__'

class ListTotalDepositControlSerializer(serializers.ModelSerializer):
    account = BankAccountSerializer(many=False, read_only=True)
    
    class Meta:
        model = DepositControl
        fields = '__all__'

class PaidPluginsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidPlugins
        fields = '__all__'



