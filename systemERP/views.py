from cgi import print_arguments
from ipaddress import summarize_address_range
#from msilib.schema import ListView
from django.views.generic import ListView, View, TemplateView
from urllib import request
from django.shortcuts import render, redirect
from .models import BankAccountsCustomer, BankAccountsEmployee, BankAccountsProvider, BillOfLading, BilledIncome, BillsPaidPlugins, ChargerSalary, Company, ConceptPayment, CreditNote, Customer, Department, DepositControl, DoubleDays, DriverSalary, ExtraHours, FileProducer, FileQuotation, FileUnit, FuelDump, FuelType, Fueling, Gasoline, LandRent, Loans, LoansChargers, LoansDrivers, Location, MainProduct, Output, OutputProduct, Outputreview, PaidPlugins, Parcel, PaymentOrderProducer, PaymentProducer, PaymentSchedule, PaymentsChargers, PaymentsDrivers, Payroll, PettyCash, Presentation, Producer, Product, ProductCN, ProductQuotation, ProductRequisition, ProductShopping, ProductW, Props, Provider, Category, Employee, Quotation, Requisition, Rowoutputreview, SegalmexParcel, SegalmexReception, Shopping, Society, User, Bank, BankAccount, UploadImage, Unit, Variety, VehicleType, Warehouse, Ticketreview, Rowticketreview, Binnacle
#RestFramework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BankAccountsCustomerSerializer, BankAccountsEmployeeSerializer, BankAccountsProviderSerializer, BillOfLadingSerializer, BilledIncomeSerializer, BinnacleSerializer, ChargerSalarySerializer, CompanySerializer, CreditNoteListSerializer, CustomerSerializer, DepositControlSerializer, DieselSerializer, DoubleDaysSerializer, DriverSalarySerializer, ExtraHoursSerializer, FileProducerSerializer, FileQuotationSerializer, FileUnitSerializer, FuelDumpListSerializer, FuelDumpSerializer, FuelTypeSerializer, FuelingListSerializer, FuelingListSerializer, FuelingSerializer, LandRentSerializer, ListBankAccountsCustomerSerializer, ListBankAccountsEmployeeSerializer, ListBankAccountsProviderSerializer, ListBillOfLadingSerializer, ListBilledIncomeSerializer, ListChargerSalarySerializer, ListDepositControlSerializer, ListDoubleDaysSerializer, ListDriverSalarySerializer, ListExtraHoursSerializer, ListLandRentSerializer, ListLoansChargersSerializer, ListLoansDriversSerializer, ListLoansSerializer, ListPaymentOrderProducerSerializer, ListPaymentProducerSerializer, ListPaymentScheduleSerializer, ListPaymentsChargersSerializer, ListPaymentsDriversSerializer, ListPayrollSerializer, ListPettyCashSerializer, ListPropsSerializer, ListQuotationSerializer, ListSegalmexParcelSerializer, ListSegalmexReceptionSerializer, ListTotalDepositControlSerializer, LoansChargersSerializer, LoansDriversSerializer, LoansSerializer, LocationSerializer, MainProductSerializer, OutputListSerializer, OutputreviewListSerializer, PaidPluginsSerializer, ParcelListSerializer, ParcelSerializer, PaymentOrderProducerSerializer, PaymentProducerSerializer, PaymentsChargersSerializer, PaymentsDriversSerializer, PayrollSerializer, PettyCashSerializer, PresentationSerializer, ProductSerializer, PropsSerializer, RequisitionListSerializer, RequisitionSerializer, SegalmexParcelSerializer, SegalmexReceptionSerializer, ShoppingListSerializer, SocietyListSerializer, SocietySerializer, UnitListSerializer, UserSerializer, DepartmentSerializer, BankSerializer,BankAccountSerializer, EmployeeSerializer, EmployeeListSerializer, ProducerSerializer, ProviderSerializer, CategorySerializer, BankAccountListSerializer, UploadImageSerializer, UnitSerializer, VarietySerializer, VehicleTypeSerializer, WarehouseListSerializer, WarehouseSerializer, TicketreviewListSerializer
#FORMS
from .forms import EmployeeForm
from django.http import HttpResponse, JsonResponse
from .utils import render_to_pdf
import openpyxl
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from werkzeug.security import generate_password_hash, check_password_hash
from django.db.models import Sum
# Create your views here.
def home(request):
	return render(request, 'home.html')

# *? USUARIOS
@api_view(['POST'])
def RegisterUser(request):
	data = request.data
	password = data['password']
	clave = generate_password_hash(password)
	new_user = User.objects.create(
		name=data["name"],
		lastname=data["lastname"],
		cellphone=data["cellphone"],
		email = data["email"],
		password = clave
		)
	new_user.save()
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})        

@api_view(['POST'])
def LoginUser(request):
	data = request.data
	clave = data['password']
	users = User.objects.filter(email=data["email"]).first()
	if not users:
		return Response({"message":"No existe coincidencias con su correo electrónico!","status":400})
	if check_password_hash(users.password, clave):
		serializer = UserSerializer(users, many=False)
		return Response(serializer.data)
	return Response({"message":"No existe coincidencias!","status":400})

@api_view(['POST'])
def CreateUser(request):
	data = request.data
	password = data['password']
	clave = generate_password_hash(password)
	new_user = User.objects.create(
		name=data["name"],
		lastname=data["lastname"],
		cellphone=data["cellphone"],
		email = data["email"],
		password = clave,

		users = data["users"],
		companies = data["companies"],
		departments = data["departments"],
		categories = data["categories"],

		societies = data["societies"],
		parcels = data["parcels"],
		producers = data["producers"],
		reception = data["reception"],

		binnacle = data["binnacle"],
		units = data["units"],
		fuels = data["fuels"],
		requisitions = data["requisitions"],
		shoppings = data["shoppings"],
		providers = data["providers"],

		quotes = data["quotes"],
		purchase_orders = data["purchase_orders"],
		products = data["products"],
		outputs = data["outputs"],
		CreditNotes = data['CreditNotes'],
		BillOfLading = data['BillOfLading'],
		PaymentSchedule = data['PaymentSchedule'],
		PettyCash = data['PettyCash'],
		drivers = data['drivers'],
		chargers = data['chargers'],
		LandRent = data['LandRent'],
		PaymentOrderProducer = data['PaymentOrderProducer'],
		payments = data['payments'],

		banks = data["banks"],
		customers = data["customers"],
		BilledIncome = data["BilledIncome"],
		PaidPlugins = data['PaidPlugins'],
		DepositControl = data['DepositControl'],

		employees = data["employees"],
		payroll = data['payroll'],
		ExtraHours = data['ExtraHours'],
		DoubleDays = data['DoubleDays'],
		props = data['props'],
		loans = data['loans'],
		
		watch =  data["watch"],
		write =  data["write"],
		edit =  data["edit"],
		delete =  data["delete"],
		export =  data["export"],
		status =  data["status"],
		role = data['role']
	)
	new_user.save()
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})

@api_view(['GET'])
def ListUser(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def DetailUser(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(user, many=False)
	return Response(serializer.data)	

@api_view(['POST'])
def UpdateUser(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(instance=user, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó la actualización!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteUser(request, pk):
	row = User.objects.filter(id=pk)
	row.delete()   
	return Response({"message":"Registro eliminado satisfactoriamente!","status":200}) 

#*? COMPAÑIAS
@api_view(['GET'])
def ListCompany(request):
	company = Company.objects.all()
	serializer = CompanySerializer(company, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateCompany(request):
	serializer = CompanySerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteCompany(request, pk):
	company = Company.objects.get(id=pk)
	company.delete()    
	return Response({"message":"Registro eliminado satisfactoriamente!","status":200})

@api_view(['GET'])
def DetailCompany(request, pk):
	company = Company.objects.get(id=pk)
	serializer = CompanySerializer(company, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateCompany(request, pk):
	company = Company.objects.get(id=pk)
	serializer = DepartmentSerializer(instance=company, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó la actualización!","errors":serializer.errors,"status":400})


#*? DEPARTAMENTOS

@api_view(['GET'])
def DepartmentList(request):
	department = Department.objects.all().order_by("id")
	serializer = DepartmentSerializer(department, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def DepartmentDetail(request, pk):
	department = Department.objects.get(id=pk)
	serializer = DepartmentSerializer(department, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateDepartment(request):
	serializer = DepartmentSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateDepartment(request, pk):
	department = Department.objects.get(id=pk)
	serializer = DepartmentSerializer(instance=department, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó la actualización!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteDepartment(request, pk):
	department = Department.objects.get(id=pk)
	department.delete()    
	return Response({"message":"Registro eliminado satisfactoriamente!","status":200})

class ReportDepartmentsPDF(View):
	def get(self, request, *args, **kwargs):
		departments = Department.objects.all()
		data = {'departments': departments}
		pdf = render_to_pdf('paginas/ReportDepartments.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportDepartmentsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		departments = Department.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Categorias'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Departamento'

		cont = 7
		pos = 1
		for department in departments:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=department.name

			pos+=1
			cont+=1

		nombre_archivo = "Reporte_departamentos.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? CATEGORIAS

@api_view(['GET'])
def CategoryList(request):
	category = Category.objects.all().order_by("id")
	serializer = CategorySerializer(category, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def CategoryDetail(request, pk):
	category = Category.objects.get(id=pk)
	serializer = CategorySerializer(category, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateCategory(request):
	serializer = CategorySerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateCategory(request, pk):
	category = Category.objects.get(id=pk)
	serializer = CategorySerializer(instance=category, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó la actualización!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteCategory(request, pk):
	category = Category.objects.get(id=pk)
	category.delete()
	return Response({"message":"Registro eliminado satisfactoriamente!","status":200})

class ReportCategoriesPDF(View):
	def get(self, request, *args, **kwargs):
		categories = Category.objects.all()
		data = {'categories': categories}
		pdf = render_to_pdf('paginas/ReportCategories.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportCategoriesXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		categories = Category.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Categorias'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Categoria'

		cont = 7
		pos = 1
		for category in categories:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=category.name

			pos+=1
			cont+=1

		nombre_archivo = "Reporte_categorias.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? BANCOS

@api_view(['GET'])
def BankList(request):
	banks = Bank.objects.all().order_by("id")
	serializer = BankSerializer(banks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def BankDetail(request, pk):
	bank = Bank.objects.get(id=pk)
	serializer = BankSerializer(bank, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def BankCreate(request):
	serializer = BankSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def BankUpdate(request, pk):
	bank = Bank.objects.get(id=pk)
	serializer = BankSerializer(instance=bank, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó la actualización!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def BankDelete(request, pk):
	bank = Bank.objects.get(id=pk)
	bank.delete()
	return Response({"message":"Registro eliminado satisfactoriamente!","status":200})

class ReportBanksPDF(View):
	def get(self, request, *args, **kwargs):
		banks = Bank.objects.all()
		data = {'banks': banks}
		pdf = render_to_pdf('paginas/ReportBanks.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportBanksXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		banks = Bank.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Bancos'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Banco'

		cont = 7
		pos = 1
		for bank in banks:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=bank.name

			pos+=1
			cont+=1

		nombre_archivo = "Reporte_bancos.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? CUENTAS DE BANCOS

@api_view(['GET'])
def BankAccountList(request):
	banksaccount = BankAccount.objects.all().order_by("id")
	serializer = BankAccountListSerializer(banksaccount, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def BankAccountDetail(request, pk):
	bankaccount = BankAccount.objects.get(id=pk)
	serializer = BankAccountSerializer(bankaccount, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def BankAccountCreate(request):
	serializer = BankAccountSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def BankAccountUpdate(request, pk):
	bankaccount = BankAccount.objects.get(id=pk)
	serializer = BankAccountSerializer(instance=bankaccount, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})        
	return Response({"message":"No se realizó la actualización!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def BankAccountDelete(request, pk):
	bankaccount = BankAccount.objects.get(id=pk)
	bankaccount.delete()
	return Response({"message":"Registro eliminado satisfactoriamente!","status":200})

class ReportBankAccountsPDF(View):
	def get(self, request, *args, **kwargs):
		bankaccounts = BankAccount.objects.all()
		data = {'bankaccounts': bankaccounts}
		pdf = render_to_pdf('paginas/ReportBankAccounts.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportBankAccountsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		bankaccounts = BankAccount.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Bancos'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Banco'
		ws['E6'] = 'No. Cuenta'
		ws['F6'] = 'Clave interbancaria'

		cont = 7
		pos = 1
		for bankaccount in bankaccounts:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=bankaccount.bank.name
			ws.cell(row = cont, column = 5).value=bankaccount.number
			ws.cell(row = cont, column = 6).value=bankaccount.interbank_key

			pos+=1
			cont+=1

		nombre_archivo = "Reporte_cuentas_de_banco.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? PRODUCTORES

@api_view(['GET'])
def ProducerList(request):
	producer = Producer.objects.all()
	serializer = ProducerSerializer(producer, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ProducerDetail(request, pk):
	producer = Producer.objects.get(id=pk)
	serializer = ProducerSerializer(producer, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateProducer(request):
	serializer = ProducerSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateProducer(request, pk):
	producer = Producer.objects.get(id=pk)
	serializer = ProducerSerializer(instance=producer, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteProducer(request, pk):
	producer = Producer.objects.get(id=pk)
	producer.delete()
	return Response('Registro eliminado satisfactoriamente!')

# *? PDF PRODUCTORES
class ReportProducersPDF(View):
	def get(self, request, *args, **kwargs):
		producers = Producer.objects.all()
		
		data = {
			'producers': producers
		}
		pdf = render_to_pdf('paginas/ReportProducer.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

# *? XLSX PRODUCTORES
class ReportProducersXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		producers = Producer.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Productores'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'
		ws['E6'] = 'RFC'
		ws['F6'] = 'Teléfono'
		ws['G6'] = 'Correo electrónico'
		ws['H6'] = 'Código Postal'
		ws['I6'] = 'Pais'
		ws['J6'] = 'Estado'
		ws['K6'] = 'Ciudad'
		ws['L6'] = 'Localidad'
		ws['M6'] = 'Colonia'
		ws['N6'] = 'Calle'
		ws['O6'] = 'No. Interior'
		ws['P6'] = 'No. Exterior'
		ws['Q6'] = 'Representante legal'
		

		cont = 7

		for producer in producers:
			ws.cell(row = cont, column = 3).value=producer.id
			ws.cell(row = cont, column = 4).value=producer.name
			ws.cell(row = cont, column = 5).value=producer.rfc
			ws.cell(row = cont, column = 6).value=producer.phone
			ws.cell(row = cont, column = 7).value=producer.email
			ws.cell(row = cont, column = 8).value=producer.postal_code
			ws.cell(row = cont, column = 9).value=producer.country
			ws.cell(row = cont, column = 10).value=producer.state
			ws.cell(row = cont, column = 11).value=producer.city
			ws.cell(row = cont, column = 12).value=producer.location
			ws.cell(row = cont, column = 13).value=producer.suburb
			ws.cell(row = cont, column = 14).value=producer.street
			ws.cell(row = cont, column = 15).value=producer.int_no
			ws.cell(row = cont, column = 16).value=producer.ext_no
			ws.cell(row = cont, column = 17).value=producer.representative
			
			cont+=1

		nombre_archivo = "Reporte_Productores.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? PROVEEDORES

@api_view(['GET'])
def ProviderList(request):
	provider = Provider.objects.all()
	serializer = ProviderSerializer(provider, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ProviderListForUser(request, pk):
	provider = Provider.objects.filter(user_id=pk)
	serializer = ProviderSerializer(provider, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ProviderDetail(request, pk):
	provider = Provider.objects.get(id=pk)
	serializer = ProviderSerializer(provider, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateProvider(request):
	serializer = ProviderSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateProvider(request, pk):
	provider = Provider.objects.get(id=pk)
	serializer = ProviderSerializer(instance=provider, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteProvider(request, pk):
	provider = Provider.objects.get(id=pk)
	provider.delete()
	return Response('Registro eliminado satisfactoriamente!')

class ReportProvidersPDF(View):
	def get(self, request, *args, **kwargs):
		providers = Provider.objects.all()
		
		data = {
			'providers': providers
		}
		pdf = render_to_pdf('paginas/ReportProviders.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class  ReportProvidersXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		providers = Provider.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Proveedores'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'
		ws['E6'] = 'RFC'
		ws['F6'] = 'Teléfono'
		ws['G6'] = 'Correo electrónico'
		ws['H6'] = 'Representante'
		ws['I6'] = 'Codigo Postal'
		ws['J6'] = 'Pais'
		ws['K6'] = 'Estado'
		ws['L6'] = 'Ciudad'
		ws['M6'] = 'Localidad'
		ws['N6'] = 'Colonia'
		ws['O6'] = 'Calle'
		ws['P6'] = 'No. Interior'
		ws['Q6'] = 'No. Exterior'

		cont = 7
		pos = 1

		for provider in providers:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=provider.name
			ws.cell(row = cont, column = 5).value=provider.rfc
			ws.cell(row = cont, column = 6).value=provider.phone
			ws.cell(row = cont, column = 7).value=provider.email
			ws.cell(row = cont, column = 8).value=provider.representative
			ws.cell(row = cont, column = 9).value=provider.postal_code
			ws.cell(row = cont, column = 10).value=provider.country
			ws.cell(row = cont, column = 11).value=provider.state
			ws.cell(row = cont, column = 12).value=provider.city
			ws.cell(row = cont, column = 13).value=provider.location
			ws.cell(row = cont, column = 14).value=provider.suburb
			ws.cell(row = cont, column = 15).value=provider.street
			ws.cell(row = cont, column = 16).value=provider.int_no
			ws.cell(row = cont, column = 17).value=provider.ext_no
			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Proveedores.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? EMPLEADOS

@api_view(['GET'])
def ListEmployee(request):
	employee = Employee.objects.all()
	serializer = EmployeeListSerializer(employee, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def EmployeeListForUser(request, pk):
	employee = Employee.objects.filter(user_id=pk)
	serializer = EmployeeListSerializer(employee, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def EmployeeDetail(request, pk):
	employee = Employee.objects.get(id=pk)
	serializer = EmployeeListSerializer(employee, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateEmployee(request):  
	if request.method == 'POST':
		serializer = EmployeeSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
		return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateEmployee(request, pk):
	employee = Employee.objects.get(id=pk)
	serializer = EmployeeSerializer(instance=employee, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdatePhotoEmployee(request, pk):
	data = request.data
	employee = Employee.objects.get(id=pk)
	employee.imagen = data['imagen']
	employee.save()
	return Response({"message":"Registro actualizado satisfactoriamente!","status":200}) 

@api_view(['DELETE'])
def DeleteEmployee(request, pk):
	employee = Employee.objects.get(id=pk)
	employee.delete()
	return Response('Registro eliminado satisfactoriamente!')

def CrearEmpleado(request):
	formulario = EmployeeForm(request.POST or None, request.FILES or None)    
	if formulario.is_valid():
		formulario.save()
		return redirect('home')
	return render(request, 'paginas/CreateEmployee.html' , {'formulario':formulario})
				
class EmpleadoList(generics.ListCreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class ReportEmployee(ListView):
	model = Employee
	template_name = "paginas/ReportEmployee.html"
	context_object_name = 'employees'

class ReportEmployeesPDF(View):
	def get(self, request, *args, **kwargs):
		employees = Employee.objects.all()
		
		data = {
			'employees': employees
		}
		pdf = render_to_pdf('paginas/ReportEmployees.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportEmployeesXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		employees = Employee.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Empleados'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'
		ws['E6'] = 'Apellido paterno'
		ws['F6'] = 'Appllido materno'
		ws['G6'] = 'Departamento'
		ws['H6'] = 'Categoria'
		ws['I6'] = 'Correo electrónico'
		ws['J6'] = 'Celular'

		cont = 7
		pos = 1

		for empleado in employees:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=empleado.name
			ws.cell(row = cont, column = 5).value=empleado.surname
			ws.cell(row = cont, column = 6).value=empleado.second_surname
			ws.cell(row = cont, column = 7).value=empleado.department.name
			ws.cell(row = cont, column = 8).value=empleado.category.name
			ws.cell(row = cont, column = 9).value=empleado.personal_email
			ws.cell(row = cont, column = 10).value=empleado.cell_phone
			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Empleados.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? UNIDADES
@api_view(['GET'])
def VehicleTypeList(request):
	vehicles = VehicleType.objects.all()
	serializer = VehicleTypeSerializer(vehicles, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateVehicleType(request):
	serializer = VehicleTypeSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def UnitList(request):
	units = Unit.objects.all()
	serializer = UnitListSerializer(units, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def UnitListForUser(request,pk):
	units = Unit.objects.filter(user_id=pk)
	serializer = UnitListSerializer(units, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def UnitDetail(request, pk):
	units = Unit.objects.get(id=pk)
	serializer = UnitListSerializer(units, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateUnit(request):
	serializer = UnitSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateUnit(request, pk):
	unit = Unit.objects.get(id=pk)
	serializer = UnitSerializer(instance=unit, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdatePhotoUnit(request, pk):
	data = request.data
	unit = Unit.objects.get(id=pk)
	unit.imagen = data['imagen']
	unit.save()
	return Response({"message":"Registro actualizado satisfactoriamente!","status":200}) 
	#return Response({"message":"No se realizó el Registro!","status":400})

@api_view(['DELETE'])
def DeleteUnit(request, pk):
	unit = Unit.objects.get(id=pk)
	unit.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['POST'])
def UploadFileUnit(request):
	serializer = FileUnitSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200}) 
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def DetailFileUnit(request, pk):	
	documents = FileUnit.objects.filter(unit_id=pk)
	serializer = FileUnitSerializer(documents, many=True)
	return Response(serializer.data)

class ReportUnitsPDF(View):
	def get(self, request, *args, **kwargs):
		units = Unit.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'units': units
		}
		pdf = render_to_pdf('paginas/ReportUnit.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportUnitsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		units = Unit.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Empleados'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Unidad'
		ws['E6'] = 'Tipo de vehículo'
		ws['F6'] = 'Kilometraje inicial'
		ws['G6'] = 'Kilometraje Actual'
		ws['H6'] = 'Marca'
		ws['I6'] = 'Modelo'
		ws['J6'] = 'Color'
		ws['K6'] = 'Bastidor'
		ws['L6'] = 'Motor'
		ws['M6'] = 'Precio'
		ws['N6'] = 'No. de permiso'
		ws['O6'] = 'No. de placas'
		ws['P6'] = 'Vigencia'
		ws['Q6'] = 'Aseguradora'
		ws['R6'] = 'No. de poliza'
		ws['S6'] = 'Inicio de vigencia'
		ws['T6'] = 'Final de vigencia'
		ws['U6'] = 'No. de Tarjeta de circulación'
		ws['V6'] = 'No. de Identificación'
		ws['W6'] = 'Estado'

		cont = 7
		pos = 1

		for item in units:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.unit
			ws.cell(row = cont, column = 5).value=item.vehicle_type.vehicle_type
			ws.cell(row = cont, column = 6).value=item.initial_mileage
			ws.cell(row = cont, column = 7).value=item.current_mileage			
			ws.cell(row = cont, column = 8).value=item.brand
			ws.cell(row = cont, column = 9).value=item.model
			ws.cell(row = cont, column = 10).value=item.color
			ws.cell(row = cont, column = 11).value=item.frame
			ws.cell(row = cont, column = 12).value=item.engine
			ws.cell(row = cont, column = 13).value=item.price
			ws.cell(row = cont, column = 14).value=item.permit_no
			ws.cell(row = cont, column = 15).value=item.plate_no
			ws.cell(row = cont, column = 16).value=item.validity
			ws.cell(row = cont, column = 17).value=item.insurance_carrier
			ws.cell(row = cont, column = 18).value=item.policy_no
			ws.cell(row = cont, column = 19).value=item.start_validity
			ws.cell(row = cont, column = 20).value=item.end_validity
			ws.cell(row = cont, column = 21).value=item.circulation_card_no
			ws.cell(row = cont, column = 22).value=item.identification_no
			ws.cell(row = cont, column = 23).value=item.state
			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Unidades.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response	

# *? COMBUSTIBLE
@api_view(['GET'])
def ListFuelType(request):
	fuel = FuelType.objects.all()
	serializer = FuelTypeSerializer(fuel, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def ListFueling(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	fuel_type = data['fuel_type']
	rows = Fueling.objects.filter(date__range=[fecha1, fecha2]).filter(fuel_type_id=fuel_type)
	#rows = FuelDump.objects.all()
	serializer = FuelDumpListSerializer(rows, many=True)


@api_view(['POST'])
def CreateFueling(request):
	serializer = FuelingSerializer(data = request.data)
	data=request.data
	unit = Unit.objects.filter(id=data["unit"]).update(current_mileage = data["mileage"])
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def DetailFueling(request, pk):
	fuel = Fueling.objects.get(id=pk)
	serializer = FuelingListSerializer(fuel, many=False)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteFueling(request, pk):
	fuel = Fueling.objects.get(id=pk)
	fuel.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['POST'])
def UpdateFueling(request, pk):
	fuel = Fueling.objects.get(id=pk)
	serializer = DieselSerializer(instance=fuel, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

#*? DESCARGA DE COMBUSTIBLE

@api_view(['POST'])
def CreateFuelDump(request):
	serializer = FuelDumpSerializer(data = request.data)
	data=request.data
	#unit = Unit.objects.filter(id=data["unit"]).update(current_mileage = data["mileage"])
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListFuelDump(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	fuel_type = data['fuel_type']
	rows = FuelDump.objects.filter(date__range=[fecha1, fecha2]).filter(fuel_type_id=fuel_type)
	#rows = FuelDump.objects.all()
	serializer = FuelDumpListSerializer(rows, many=True)
	return Response(serializer.data)

# *? Requisición
@api_view(['GET'])
def ListRequisition(request):
	requisition = Requisition.objects.all()
	serializer = RequisitionListSerializer(requisition, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ListAuthorizedRequisitions(request):
	requisition = Requisition.objects.filter(status='Autorizada')
	serializer = RequisitionListSerializer(requisition, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateRequisition(request):
	data = request.data
	new_requisition = Requisition.objects.create(
		date=data["date"],
		folio = data["folio"],
		applicant_id=data["applicant"],
		description=data["description"],
		observation = data["observation"],
		department_id = data["department"],
		status = data['status'],
		user_id=data["user"]
		)
	new_requisition.save()

	for product in data["products"]:
		new_product = ProductRequisition.objects.create(
			amount=product["amount"],
			unit=product["unit"],
			product=product["product"],
			code=data["code"])
		new_product.save()		
		product_obj = ProductRequisition.objects.filter(product=product["product"], code=data["code"]).get(product=product["product"])
		new_requisition.products.add(product_obj)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  

@api_view(['DELETE'])
def DeleteRequisition(request, pk):
	requisition = Requisition.objects.get(id=pk)
	requisition.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def RequisitionDetail(request, pk):
	requisition = Requisition.objects.get(id=pk)
	serializer = RequisitionListSerializer(requisition, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateStatusRequisition(request, pk):
	data=request.data
	requisitions = Requisition.objects.filter(id=pk).update(status= data["status"])
	return Response({"message":"Registro actualizado satisfactoriamente!","status":data})  
	#requisitions = Requisition.objects.get(id=pk)
	#serializer = RequisitionSerializer(instance=requisitions, data=request.data)
	#if requisitions:
		#serializer.save()
		#return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UploadFileQuotation(request):
	serializer = FileQuotationSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200}) 
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def DetailFileQuotation(request, pk):	
	documents = FileQuotation.objects.filter(requisition_id=pk)
	serializer = FileQuotationSerializer(documents, many=True)
	return Response(serializer.data)


# *? CLIENTES
@api_view(['GET'])
def ListCustomer(request):
	customer = Customer.objects.all()
	serializer = CustomerSerializer(customer, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def CustomerList(request, pk):
	customer = Customer.objects.filter(user_id=pk)
	serializer = CustomerSerializer(customer, many=True)
	return Response(serializer.data)
@api_view(['GET'])
def CustomerDetail(request, pk):
	customer = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(customer, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateCustomer(request):
	serializer = CustomerSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def UpdateCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(instance=customer, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['POST'])
def UpdatePhotoCustomer(request, pk):
	data = request.data
	customer = Customer.objects.get(id=pk)
	customer.imagen = data['imagen']
	customer.save()
	return Response({"message":"Registro actualizado satisfactoriamente!","status":200}) 


class ReportCustomersPDF(View):
	def get(self, request, *args, **kwargs):
		customers = Customer.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'customers': customers
		}
		pdf = render_to_pdf('paginas/ReportCustomers.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportCustomersXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		customers = Customer.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')

		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:I2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:I3')
		ws['C5'] = 'Reporte de Empleados'
		ws.merge_cells('C5:I5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'
		ws['E6'] = 'RFC'
		ws['F6'] = 'Teléfono'
		ws['G6'] = 'Correo electrónico'
		ws['H6'] = 'Representante'
		ws['I6'] = 'Codigo Postal'
		ws['J6'] = 'Estado'
		ws['K6'] = 'Ciudad'
		ws['L6'] = 'Localidad'
		ws['M6'] = 'Colonia'
		ws['N6'] = 'Calle'
		ws['O6'] = 'No. Interior'
		ws['P6'] = 'No. Exterior'
		


		cont = 7
		pos = 1

		for customer in customers:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=customer.name
			ws.cell(row = cont, column = 5).value=customer.rfc
			ws.cell(row = cont, column = 6).value=customer.phone
			ws.cell(row = cont, column = 7).value=customer.email
			ws.cell(row = cont, column = 8).value=customer.representative
			ws.cell(row = cont, column = 9).value=customer.postal_code
			ws.cell(row = cont, column = 10).value=customer.country
			ws.cell(row = cont, column = 11).value=customer.state
			ws.cell(row = cont, column = 12).value=customer.city
			ws.cell(row = cont, column = 13).value=customer.location
			ws.cell(row = cont, column = 14).value=customer.suburb
			ws.cell(row = cont, column = 15).value=customer.int_no
			ws.cell(row = cont, column = 16).value=customer.ext_no
			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Clientes.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

# *? NOTAS DE CREDITO
@api_view(['GET'])
def CreditNoteList(request):
	creditnote = CreditNote.objects.all()
	serializer = CreditNoteListSerializer(creditnote, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteCreditNote(request, pk):
	creditnote = CreditNote.objects.get(id=pk)
	creditnote.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def CreditNoteDetail(request, pk):
	creditnote = CreditNote.objects.get(id=pk)
	serializer = CreditNoteListSerializer(creditnote, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateCreditNote(request):
	data = request.data
	new_creditnote = CreditNote.objects.create(
		date=data["date"], 
		purchase_order=data["purchase_order"],
		date_delivery=data["date_delivery"],
		business_name_id=data["business_name"],
		order_number=data ["order_number"],
		place_delivery=data["place_delivery"],
		sale_condition = data["sale_condition"],
		invoice = data["invoice"],
		observation = data["observation"],
		auxiliary_sales_id = data["auxiliary_sales"],
		storekeeper_id = data["storekeeper"],
		qa_id = data["qa"],
		iva=data['iva'],
		subtotal=data['subtotal'],
		total=data['total'],
		user_id=data['user']
		)
	new_creditnote.save()

	for product in data["products"]:
		new_product = ProductCN.objects.create(amount=product["amount"], unit=product["unit"], presentation_id=product["presentation"], product_id=product["product"], price=product["price"], subtotal = product["subtotal"], code=data["code"])
		new_product.save()
		
		product_obj = ProductCN.objects.filter(amount=product["amount"], unit=product["unit"], presentation_id=product["presentation"], product_id=product["product"], price=product["price"], subtotal = product["subtotal"], code=data["code"]).get(code=data["code"])
		new_creditnote.creditnote_products.add(product_obj)

	#serializer = RequisitionSerializer(new_creditnote)
	#return Response(serializer.data)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})
#*? COTIZACIONES
@api_view(['GET'])
def ListQuotation(request):
	quotation = Quotation.objects.all()
	serializer = ListQuotationSerializer(quotation, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteQuotation(request, pk):
	quotation = Quotation.objects.get(id=pk)
	quotation.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailQuotation(request, pk):
	quotation = Quotation.objects.get(id=pk)
	serializer = ListQuotationSerializer(quotation, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateQuotation(request):
	data = request.data
	new_quotation = Quotation.objects.create(
		date=data["date"], 
		invoice=data["invoice"],
		period=data["period"],
		source=data["source"],
		customer_id=data["customer"],
		introduction=data["introduction"],
		iva=data['iva'],
		subtotal=data['subtotal'],
		total=data['total'],
		generator_id=data['generator'],
		authorizer_id=data['authorizer'],
		comment=data['comment'],
		user_id=data['user']
		)
	new_quotation.save()

	for product in data["products"]:
		new_product = ProductQuotation.objects.create(amount=product["amount"], unit=product["unit"], presentation_id=product["presentation"], product_id=product["product"], price=product["price"], subtotal = product["subtotal"], code=data["code"])
		new_product.save()
		
		product_obj = ProductQuotation.objects.filter(amount=product["amount"], unit=product["unit"], presentation_id=product["presentation"], product_id=product["product"], price=product["price"], subtotal = product["subtotal"], code=data["code"]).get(code=data["code"])
		new_quotation.products.add(product_obj)

	#serializer = RequisitionSerializer(new_creditnote)
	#return Response(serializer.data)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

#*? ALMACÉN
@api_view(['GET'])
def WarehouseList(request):
	warehouse = Warehouse.objects.all()
	serializer = WarehouseListSerializer(warehouse, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateWarehouse(request):
	serializer = WarehouseSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

#*? PRESENTACIÓN ALMACÉN
@api_view(['GET'])
def PresentationList(request):
	presentation = Presentation.objects.all()
	serializer = PresentationSerializer(presentation, many = True)
	return Response(serializer.data)

@api_view(['POST'])
def CreatePresentation(request):
	serializer = PresentationSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeletePresentation(request, pk):
	presentation = Presentation.objects.get(id=pk)
	presentation.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def PresentationDetail(request, pk):	
	presentation = Presentation.objects.get(id=pk)
	serializer = PresentationSerializer(presentation, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdatePresentation(request, pk):
	presentation = Presentation.objects.get(id=pk)
	serializer = PresentationSerializer(instance=presentation, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})	

class ReportPresentationsPDF(View):
	def get(self, request, *args, **kwargs):
		presentations = Presentation.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'presentations': presentations
		}
		pdf = render_to_pdf('paginas/ReportPresentations.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportPresentationsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		presentations = Presentation.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')

		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:I2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:I3')
		ws['C5'] = 'Reporte de Presentaciones'
		ws.merge_cells('C5:I5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'

		cont = 7
		pos = 1

		for item in presentations:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.name

			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Presentaciones.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response
#*? PRODUCTOS PRINCIPALES
@api_view(['POST'])
def CreateMainProduct(request):
	serializer = MainProductSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def ListMainProduct(request):
	product = MainProduct.objects.all()
	serializer = MainProductSerializer(product, many = True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteMainProduct(request, pk):
	product = MainProduct.objects.get(id=pk)
	product.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailMainProduct(request, pk):	
	product = MainProduct.objects.get(id=pk)
	serializer = MainProductSerializer(product, many=False)
	return Response(serializer.data)

#*? PRODUCTOS ALMACÉN
@api_view(['GET'])
def ListProduct(request):
	product = Product.objects.all()
	serializer = ProductSerializer(product, many = True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
	serializer = ProductSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	product.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailProduct(request, pk):	
	product = Product.objects.get(id=pk)
	serializer = ProductSerializer(product, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=product, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

class ReportProductsPDF(View):
	def get(self, request, *args, **kwargs):
		products = Product.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'products': products
		}
		pdf = render_to_pdf('paginas/ReportProducts.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportProductsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		products = Product.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')

		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:I2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:I3')
		ws['C5'] = 'Reporte de Productos'
		ws.merge_cells('C5:I5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'

		cont = 7
		pos = 1

		for item in products:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.name

			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Productos.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response


#*? REPORTE DE REPASO DE ENTRADAS

@api_view(['POST'])
def CreateTicketReview(request):
	data = request.data
	new_ticket = Ticketreview.objects.create(date=data["date"], variety=data["variety"], total=data["total"], observation=data["observation"])
	new_ticket.save()

	for row in data["rows"]:
		new_product = Rowticketreview.objects.create(product_id=row["product"], bigbags_id=row["bigbags"], kgsxbigbags=row["kgsxbigbags"], packages_id=row["packages"], kgsxpackages=row["kgsxpackages"], subtotal=row["subtotal"], code=data["code"])
		new_product.save()
		
		row_obj = Rowticketreview.objects.filter(product_id=row["product"], code=data["code"]).get(product_id=row["product"])
		new_ticket.rows.add(row_obj)

	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  

@api_view(['GET'])
def TicketReviewList(request):
	ticketreview = Ticketreview.objects.all()
	serializer = TicketreviewListSerializer(ticketreview, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def TicketReviewDetail(request, pk):
	ticketreview = Ticketreview.objects.get(id=pk)
	serializer = TicketreviewListSerializer(ticketreview, many=False)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTicketReview(request, pk):
	ticketreview = Ticketreview.objects.get(id=pk)
	ticketreview.delete()
	return Response('Registro eliminado satisfactoriamente!')

#*? SALIDAS

@api_view(['POST'])
def CreateOutput(request):
	data = request.data
	new_output = Output.objects.create(
		user_id=data['user'],
		company_id=data['company'],
		date=data['date'],
		invoice=data['invoice'],
		customer_id=data['customer'],
		destiny = data['destiny'],
		gross_weight=data['gross_weight'],
		tare=data['tare'],
		net_weight=data['net_weight'],
		driver_id=data['driver'],
		plate_id = data['plate'],
		payment_method=data['payment_method'],
		bank_account_id=data['bank_account'],		
		subtotal=data['subtotal'],
		iva=data['iva'],
		total=data['total'],
		delivered_id = data['delivered'],
		received = data['received'],
		comment=data['comment']
		)
	new_output.save()

	for row in data["rows"]:
		new_product = OutputProduct.objects.create(amount=row["amount"], unit=row["unit"], presentation_id=row["presentation"], product_id=row["product"], price=row["price"], subtotal = row["subtotal"], code=data["code"])
		
		new_product.save()
		
		row_obj = OutputProduct.objects.filter(product_id=row["product"], code=data["code"]).get(product_id=row["product"])
		new_output.products.add(row_obj)

	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  

@api_view(['POST'])
def OutputList(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	company = data['company']
	output = Output.objects.filter(date__range=[fecha1, fecha2]).filter(company_id=company)
	serializer = OutputListSerializer(output, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def OutputDetail(request, pk):
	output = Output.objects.get(id=pk)
	serializer = OutputListSerializer(output, many=False)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteOutput(request, pk):
	output = Output.objects.get(id=pk)
	output.delete()
	return Response('Registro eliminado satisfactoriamente!')


#? BITACORA
@api_view(['GET'])
def ListBinnacle(request,pk):
	binnacle = Binnacle.objects.filter(user_id=pk)
	serializer = BinnacleSerializer(binnacle, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateBinnacle(request):
	serializer = BinnacleSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteBinnacle(request, pk):
	binnacle = Binnacle.objects.get(id=pk)
	binnacle.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailBinnacle(request, pk):	
	binnacle = Binnacle.objects.get(id=pk)
	serializer = BinnacleSerializer(binnacle, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateBinnacle(request, pk):
	binnacle = Binnacle.objects.get(id=pk)
	serializer = BinnacleSerializer(instance=binnacle, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

class ReportBinnaclesPDF(View):
	def get(self, request, *args, **kwargs):
		binnacles = Binnacle.objects.all()
		data = {'binnacles': binnacles}
		pdf = render_to_pdf('paginas/ReportBinnacles.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportBinnaclesXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		binnacles = Binnacle.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')
		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:J2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:J3')
		ws['C5'] = 'Reporte de Bitacoras'
		ws.merge_cells('C5:J5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Fecha'
		ws['E6'] = 'Labores'
		ws['F6'] = 'Lotes'
		ws['G6'] = 'HA'
		ws['H6'] = 'Faena'
		ws['I6'] = 'Total aplicado'
		ws['J6'] = 'medida'
		ws['K6'] = 'Acurate'
		ws['L6'] = 'Total aplicado'
		ws['M6'] = 'medida'
		ws['N6'] = 'Prolux'
		ws['O6'] = 'Total aplicado'
		ws['P6'] = 'medida'
		ws['Q6'] = 'Aderente'
		ws['R6'] = 'Total aplicado'
		ws['S6'] = 'medida'
		ws['T6'] = 'Sulfato de amonio'
		ws['U6'] = 'Total aplicado'
		ws['V6'] = 'medida'
		ws['W6'] = 'Nomolt'
		ws['X6'] = 'Total aplicado'
		ws['Y6'] = 'medida'
		ws['Z6'] = 'Metarrizium'
		ws['AA6'] = 'Total aplicado'
		ws['AB6'] = 'medida'
		ws['AC6'] = 'Beauberian'
		ws['AD6'] = 'Total aplicado'
		ws['AE6'] = 'medida'
		ws['AF6'] = 'Abland'
		ws['AG6'] = 'Total aplicado'
		ws['AH6'] = 'medida'
		ws['AI6'] = 'aura'
		ws['AJ6'] = 'Total aplicado'
		ws['AK6'] = 'medida'
		ws['AL6'] = 'Urea'
		ws['AM6'] = 'Total aplicado'
		ws['AN6'] = 'medida'
		ws['AO6'] = 'Dash'
		ws['AP6'] = 'Total aplicado'
		ws['AQ6'] = 'medida'
		ws['AR6'] = 'Cipermetrina'
		ws['AS6'] = 'Total aplicado'
		ws['AT6'] = 'medida'


		cont = 7
		pos = 1
		for item in binnacles:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.fecha
			ws.cell(row = cont, column = 5).value=item.labores
			ws.cell(row = cont, column = 6).value=item.lotes
			ws.cell(row = cont, column = 7).value=item.ha
			ws.cell(row = cont, column = 8).value=item.faena
			ws.cell(row = cont, column = 9).value=item.ta_ha_faena
			ws.cell(row = cont, column = 10).value=item.medida_faena
			ws.cell(row = cont, column = 11).value=item.acurate
			ws.cell(row = cont, column = 12).value=item.ta_ha_acurate
			ws.cell(row = cont, column = 13).value=item.medida_acurate
			ws.cell(row = cont, column = 14).value=item.prolux
			ws.cell(row = cont, column = 15).value=item.ta_ha_prolux
			ws.cell(row = cont, column = 16).value=item.medida_prolux
			ws.cell(row = cont, column = 17).value=item.aderente
			ws.cell(row = cont, column = 18).value=item.ta_ha_aderente
			ws.cell(row = cont, column = 19).value=item.medida_aderente
			ws.cell(row = cont, column = 20).value=item.sulfato
			ws.cell(row = cont, column = 21).value=item.ta_ha_sulfato
			ws.cell(row = cont, column = 22).value=item.medida_sulfato
			ws.cell(row = cont, column = 23).value=item.nomolt
			ws.cell(row = cont, column = 24).value=item.ta_ha_nomolt
			ws.cell(row = cont, column = 25).value=item.medida_nomolt
			ws.cell(row = cont, column = 26).value=item.metarrizium
			ws.cell(row = cont, column = 27).value=item.ta_ha_metarrizium
			ws.cell(row = cont, column = 28).value=item.medida_metarrizium
			ws.cell(row = cont, column = 29).value=item.beauberian
			ws.cell(row = cont, column = 30).value=item.ta_ha_beauberian
			ws.cell(row = cont, column = 31).value=item.medida_beauberian
			ws.cell(row = cont, column = 32).value=item.abland
			ws.cell(row = cont, column = 33).value=item.ta_ha_abland
			ws.cell(row = cont, column = 34).value=item.medida_abland
			ws.cell(row = cont, column = 35).value=item.aura
			ws.cell(row = cont, column = 36).value=item.ta_ha_aura
			ws.cell(row = cont, column = 37).value=item.medida_aura
			ws.cell(row = cont, column = 38).value=item.urea
			ws.cell(row = cont, column = 39).value=item.ta_ha_urea
			ws.cell(row = cont, column = 40).value=item.medida_urea
			ws.cell(row = cont, column = 41).value=item.dash
			ws.cell(row = cont, column = 42).value=item.ta_ha_dash
			ws.cell(row = cont, column = 43).value=item.medida_dash
			ws.cell(row = cont, column = 44).value=item.cipermetrina
			ws.cell(row = cont, column = 45).value=item.ta_ha_cipermetrina
			ws.cell(row = cont, column = 46).value=item.medida_cipermetrina

			pos+=1
			cont+=1

		nombre_archivo = "Reporte_bitacoras.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

#? PARCELAS

@api_view(['GET'])
def ListParcel(request):
	parcel = Parcel.objects.all()
	serializer = ParcelListSerializer(parcel, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateParcel(request):
	serializer = ParcelSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteParcel(request, pk):
	parcel = Parcel.objects.get(id=pk)
	parcel.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailParcel(request, pk):	
	parcel = Parcel.objects.get(id=pk)
	serializer = ParcelSerializer(parcel, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateParcel(request, pk):
	parcel = Parcel.objects.get(id=pk)
	serializer = ParcelSerializer(instance=parcel, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

class ReportParcelsPDF(View):
	def get(self, request, *args, **kwargs):
		parcels = Parcel.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'parcels': parcels
		}
		pdf = render_to_pdf('paginas/ReportParcel.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportParcelsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		parcels = Parcel.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')

		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:I2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:I3')
		ws['C5'] = 'Reporte de Parcelas'
		ws.merge_cells('C5:I5')

		ws['C6'] = 'ID'
		ws['D6'] = 'No. Parcela'
		ws['E6'] = 'Georeferencia'
		ws['F6'] = 'Hectareas'
		ws['G6'] = 'Certificado'
		ws['H6'] = 'RAN'
		ws['I6'] = 'Propietario'
		ws['J6'] = 'Ubicación'
		ws['K6'] = 'Comentario'

		cont = 7
		pos = 1

		for item in parcels:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.no_parcel
			ws.cell(row = cont, column = 5).value=item.georeferences
			ws.cell(row = cont, column = 6).value=item.hectares
			ws.cell(row = cont, column = 7).value=item.certificate
			ws.cell(row = cont, column = 8).value=item.ran
			ws.cell(row = cont, column = 9).value=item.owner
			ws.cell(row = cont, column = 10).value=item.location
			ws.cell(row = cont, column = 11).value=item.comment

			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Sociedades.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

#? RENTA DE PREDIOS

@api_view(['POST'])
def ListLandRent(request):
	data = request.data
	rent_year = data['rent_year']
	reason_rent = data['reason_rent']
	landrent = LandRent.objects.filter(rent_year=rent_year).filter(reason_rent=reason_rent)
	serializer = ListLandRentSerializer(landrent, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateLandRent(request):
	serializer = LandRentSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteLandRent(request, pk):
	landrent = LandRent.objects.get(id=pk)
	landrent.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailLandRent(request, pk):	
	landrent = LandRent.objects.get(id=pk)
	serializer = ListLandRentSerializer(landrent, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateLandRent(request, pk):
	landrent = LandRent.objects.get(id=pk)
	serializer = LandRentSerializer(instance=landrent, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

#*? CAJA CHICA
@api_view(['POST'])
def CreatePettyCash(request):
	serializer = PettyCashSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListPettyCash(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	pettycash = PettyCash.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListPettyCashSerializer(pettycash, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeletePettyCash(request, pk):
	pettycash = PettyCash.objects.get(id=pk)
	pettycash.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailPettyCash(request, pk):	
	pettycash = PettyCash.objects.get(id=pk)
	serializer = ListPettyCashSerializer(pettycash, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdatePettyCash(request, pk):
	pettycash = PettyCash.objects.get(id=pk)
	serializer = PettyCashSerializer(instance=pettycash, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListCash(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	pettycash = Output.objects.filter(date__range=[fecha1, fecha2]).aggregate(Sum('total'))
	return Response(pettycash)
	#serializer = OutputListSerializer(pettycash, many=True)
	#return Response(serializer.data)
@api_view(['POST'])
def ListDiscount(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	discount = PettyCash.objects.filter(date__range=[fecha1, fecha2]).aggregate(Sum('cash'))
	return Response(discount)



# *? COMPRAS
@api_view(['GET'])
def ListShopping(request):
	shopping = Shopping.objects.all()
	serializer = ShoppingListSerializer(shopping, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteShopping(request, pk):
	shopping = Shopping.objects.get(id=pk)
	shopping.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailShopping(request, pk):
	shopping = Shopping.objects.get(id=pk)
	serializer = ShoppingListSerializer(shopping, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def CreateShopping(request):
	data = request.data
	new_shopping = Shopping.objects.create(
		date=data['date'],
		provider_id=data['provider'],
		requisition_id=data['requisition'],
		department_id=data['department'],
		payment_type=data['payment_type'],
		iva=data['iva'],
		subtotal=data['subtotal'],
		total=data['total'],
		observation=data['observation'],
		applicant_id=data['applicant'],
		verify_id=data['verify'],
		authorizes_id=data['authorizes'],
		user_id=data['user']
		)
	new_shopping.save()

	for product in data["products"]:
		new_product = ProductShopping.objects.create(
			product_name=product["product_name"],
			amount=product["amount"],
			unit=product["unit"], 
			price=product["price"], 
			subtotal = product["subtotal"], 
			code=data["code"])
		new_product.save()
		
		product_obj = ProductShopping.objects.filter(product_name=product["product_name"], code=data["code"]).get(product_name=product["product_name"])
		new_shopping.products.add(product_obj)

	#serializer = RequisitionSerializer(new_shopping)
	#return Response(serializer.data)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})
#*? SOCIEDAD
@api_view(['POST'])
def CreateSociety(request):
	data = request.data
	new_society = Society.objects.create(
		name=data["name"],
		cycle = data["cycle"],
		year = data["year"]
		)
	new_society.save()

	for producer in data["producers"]:

		
		producer_obj = Producer.objects.get(id=producer)
		new_society.producers.add(producer_obj)

	#serializer = RequisitionSerializer(new_society)
	#return Response(serializer.data)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def ListSociety(request):
	society = Society.objects.all()
	serializer = SocietySerializer(society, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteSociety(request, pk):
	society = Society.objects.get(id=pk)
	society.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailSociety(request, pk):
	society = Society.objects.get(id=pk)
	serializer = SocietyListSerializer(society, many=False)
	return Response(serializer.data)

class ReportSocietiesPDF(View):
	def get(self, request, *args, **kwargs):
		societies = Society.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'societies': societies
		}
		pdf = render_to_pdf('paginas/ReportSocieties.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportSocietiesXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		societies = Society.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')

		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:I2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:I3')
		ws['C5'] = 'Reporte de Sociedades'
		ws.merge_cells('C5:I5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Nombre'
		ws['E6'] = 'Ciclo'
		ws['F6'] = 'Año'

		cont = 7
		pos = 1

		for item in societies:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.name
			ws.cell(row = cont, column = 5).value=item.cycle
			ws.cell(row = cont, column = 6).value=item.year

			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Sociedades.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

#*? SEGALMEX PARCELAS

@api_view(['GET'])
def ListSegalmexParcel(request):
	parcel = SegalmexParcel.objects.all()
	serializer = ListSegalmexParcelSerializer(parcel, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateSegalmexParcel(request):
	serializer = SegalmexParcelSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteSegalmexParcel(request, pk):
	parcel = SegalmexParcel.objects.get(id=pk)
	parcel.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailSegalmexParcel(request, pk):
	parcel = SegalmexParcel.objects.get(id=pk)
	serializer = ListSegalmexParcelSerializer(parcel, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateSegalmexParcel(request, pk):
	parcel = SegalmexParcel.objects.get(id=pk)
	serializer = SegalmexParcelSerializer(instance=parcel, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

class ReportSegalmexParcelsPDF(View):
	def get(self, request, *args, **kwargs):
		parcels = SegalmexParcel.objects.all()
		#serializer = EmployeeListSerializer(employees, many=True)
		data = {
			'parcels': parcels
		}
		pdf = render_to_pdf('paginas/ReportSegalmexParcel.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

class ReportSegalmexParcelsXLSX(TemplateView):
	def get(self, request, *args, **kwargs):
		parcels = SegalmexParcel.objects.all()
		wb = Workbook()
		ws = wb.active
		imag = openpyxl.drawing.image.Image('imagenes/logo_empresa_chica.png')

		ws.add_image(imag, 'A1')
		ws['C2'] = 'CAMPESINOS PRODUCTORES CAMPECHANOS'
		ws.merge_cells('C2:I2')
		ws['C3'] = 'SPR DE RL DE CV'
		ws.merge_cells('C3:I3')
		ws['C5'] = 'Reporte de Distribución de parcelas'
		ws.merge_cells('C5:I5')

		ws['C6'] = 'ID'
		ws['D6'] = 'Sociedad'
		ws['E6'] = 'Ciclo PV'
		ws['F6'] = 'Ciclo OI'
		ws['G6'] = 'Año'
		ws['H6'] = 'Comentario'

		cont = 7
		pos = 1

		for item in parcels:
			ws.cell(row = cont, column = 3).value=pos
			ws.cell(row = cont, column = 4).value=item.society.name
			ws.cell(row = cont, column = 5).value=item.cyclepv.no_parcel
			ws.cell(row = cont, column = 6).value=item.cycleoi.no_parcel
			ws.cell(row = cont, column = 7).value=item.year
			ws.cell(row = cont, column = 8).value=item.comment

			cont+=1
			pos+=1

		nombre_archivo = "Reporte_Sociedades.xlsx"
		response = HttpResponse(content_type = "application/ms-excel")
		content = "attachment; filename = {0}".format(nombre_archivo)
		response['Content-Disposition'] = content
		wb.save(response)
		return response

@api_view(['POST'])
def UploadDocProducer(request):
	serializer = FileProducerSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200}) 
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def DetailFileProducer(request, pk):	
	documents = FileProducer.objects.filter(producer_id=pk)
	serializer = FileProducerSerializer(documents, many=True)
	return Response(serializer.data)

#*? SEGALMEX RECEPCIÓN
@api_view(['POST'])
def SearchReception(request):
	try:
		data = request.data
		fecha1 = data['start_date']
		fecha2 = data['end_date']
		productor = data['producer']
		reception = SegalmexReception.objects.filter(checkin_date__range=[fecha1, fecha2]).filter(producer_id=productor)
		serializer = ListSegalmexReceptionSerializer(reception, many=True)
		return Response(serializer.data)

	except KeyError:
		reception = SegalmexReception.objects.filter(checkin_date__range=[fecha1, fecha2])
		serializer = ListSegalmexReceptionSerializer(reception, many=True)
		return Response(serializer.data)	
		
@api_view(['GET'])
def ListSegalmexReception(request):
	reception = SegalmexReception.objects.all()
	serializer = ListSegalmexReceptionSerializer(reception, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreateSegalmexReception(request):
	serializer = SegalmexReceptionSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteSegalmexReception(request, pk):
	reception = SegalmexReception.objects.get(id=pk)
	reception.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailSegalmexReception(request, pk):
	reception = SegalmexReception.objects.get(id=pk)
	serializer = ListSegalmexReceptionSerializer(reception, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateSegalmexReception(request, pk):
	reception = SegalmexReception.objects.get(id=pk)
	serializer = SegalmexReceptionSerializer(instance=reception, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def ListLocation(request):
	location = Location.objects.all()
	serializer = LocationSerializer(location, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ListVariety(request):
	variety = Variety.objects.all()
	serializer = VarietySerializer(variety, many=True)
	return Response(serializer.data)

# *? PDF CLIENTES
class PDF_Boleta(View):
	#@api_view(['GET'])
	def get(self, request, pk):
		boleta = SegalmexReception.objects.get(id=pk)
		#serializer = ListSegalmexReceptionSerializer(boleta, many=False)
		data = {
			'boleta': boleta.id
		}
		pdf = render_to_pdf('paginas/Boleta.html', data)
		return HttpResponse(pdf, content_type = 'application/pdf')

#*? orden de pago de productores

@api_view(['GET'])
def ListPaymentOrderProducer(request):
	order = PaymentOrderProducer.objects.all()
	serializer = ListPaymentOrderProducerSerializer(order, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreatePaymentOrderProducer(request):
	serializer = PaymentOrderProducerSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeletePaymentOrderProducer(request, pk):
	order = PaymentOrderProducer.objects.get(id=pk)
	order.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailPaymentOrderProducer(request, pk):
	order = PaymentOrderProducer.objects.get(id=pk)
	serializer = ListPaymentOrderProducerSerializer(order, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdatePaymentOrderProducer(request, pk):
	order = PaymentOrderProducer.objects.get(id=pk)
	serializer = PaymentOrderProducerSerializer(instance=order, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

#*? BUSCAR TICKET DE RECEPCIÓN
@api_view(['POST'])
def SearchTicketReception(request):
	try:
		data = request.data
		ticket = data
		reception = SegalmexReception.objects.get(ticket=ticket)
		serializer = ListSegalmexReceptionSerializer(reception, many=False)
		return Response(serializer.data)
	except SegalmexReception.DoesNotExist:
		#raise Exception("Could not find a burger")	
		return Response({"message":"No se encontro coincidencia!","status":400})

#*? BUSCAR ORDEN DE PAGO DE PRODUCTOR
@api_view(['POST'])
def SearchPaymentOrderProducer(request):
	try:
		data = request.data
		ticket = data
		orden = PaymentOrderProducer.objects.get(id=ticket)
		serializer = ListPaymentOrderProducerSerializer(orden, many=False)
		return Response(serializer.data)
	except PaymentOrderProducer.DoesNotExist:
		#raise Exception("Could not find a burger")	
		return Response({"message":"No se encontro coincidencia!","status":400})

#*? pago de productores

@api_view(['GET'])
def ListPaymentProducer(request):
	order = PaymentProducer.objects.all()
	serializer = ListPaymentProducerSerializer(order, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def CreatePaymentProducer(request):
	serializer = PaymentProducerSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeletePaymentProducer(request, pk):
	order = PaymentProducer.objects.get(id=pk)
	order.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailPaymentProducer(request, pk):
	order = PaymentProducer.objects.get(id=pk)
	serializer = ListPaymentProducerSerializer(order, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdatePaymentProducer(request, pk):
	order = PaymentProducer.objects.get(id=pk)
	serializer = PaymentProducerSerializer(instance=order, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})



#*? SALARIO DE CHOFERES
@api_view(['POST'])
def ListDriverSalary(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	driver = data['driver']
	driver = DriverSalary.objects.filter(date__range=[fecha1, fecha2]).filter(driver_id = driver)
	serializer = ListDriverSalarySerializer(driver, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def CreateDriverSalary(request):
	serializer = DriverSalarySerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteDriverSalary(request, pk):
	driversalary = DriverSalary.objects.get(id=pk)
	driversalary.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailDriverSalary(request, pk):
	driversalary = DriverSalary.objects.get(id=pk)
	serializer = ListDriverSalarySerializer(driversalary, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateDriverSalary(request, pk):
	driversalary = DriverSalary.objects.get(id=pk)
	serializer = DriverSalarySerializer(instance=driversalary, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})	
#*? SALARIO DE CARGADORES
@api_view(['POST'])
def ListChargerSalary(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	#charger = data['charger']
	salaries = ChargerSalary.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListChargerSalarySerializer(salaries, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def CreateChargerSalary(request):
	serializer = ChargerSalarySerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['DELETE'])
def DeleteChargerSalary(request, pk):
	chargersalary = ChargerSalary.objects.get(id=pk)
	chargersalary.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['GET'])
def DetailChargerSalary(request, pk):
	chargersalary = ChargerSalary.objects.get(id=pk)
	serializer = ListChargerSalarySerializer(chargersalary, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def UpdateChargerSalary(request, pk):
	chargersalary = ChargerSalary.objects.get(id=pk)
	serializer = ChargerSalarySerializer(instance=chargersalary, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro actualizado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})	
#*? NOMINA
@api_view(['POST'])
def CreatePayroll(request):
	serializer = PayrollSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListPayroll(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	charger = Payroll.objects.filter(start_date__range=[fecha1, fecha2]).filter(end_date__range=[fecha1, fecha2])
	serializer = ListPayrollSerializer(charger, many=True)
	return Response(serializer.data)
#*? HORAS EXTRAS
@api_view(['POST'])
def CreateExtraHours(request):
	serializer = ExtraHoursSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListExtraHours(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	extrahours = ExtraHours.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListExtraHoursSerializer(extrahours, many=True)
	return Response(serializer.data)	

@api_view(['DELETE'])
def DeleteExtraHours(request, pk):
	extrahours = ExtraHours.objects.get(id=pk)
	extrahours.delete()
	return Response('Registro eliminado satisfactoriamente!')	
#*? DIAS DOBLES
@api_view(['POST'])
def CreateDoubleDays(request):
	serializer = DoubleDaysSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListDoubleDays(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	doubledays = DoubleDays.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListDoubleDaysSerializer(doubledays, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteDoubleDays(request, pk):
	doubledays = DoubleDays.objects.get(id=pk)
	doubledays.delete()
	return Response('Registro eliminado satisfactoriamente!')
#*? APOYOS
@api_view(['POST'])
def CreateProps(request):
	serializer = PropsSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListProps(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	props = Props.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListPropsSerializer(props, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteProps(request, pk):
	props = Props.objects.get(id=pk)
	props.delete()
	return Response('Registro eliminado satisfactoriamente!')
#*? PRESTAMOS
@api_view(['POST'])
def CreateLoans(request):
	serializer = LoansSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListLoans(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	loans = Loans.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListLoansSerializer(loans, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteLoans(request, pk):
	loans = Loans.objects.get(id=pk)
	loans.delete()
	return Response('Registro eliminado satisfactoriamente!')

#*? PRESTAMOS
@api_view(['POST'])
def CreateLoansChargers(request):
	serializer = LoansChargersSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListLoansChargers(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	loans = LoansChargers.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListLoansChargersSerializer(loans, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteLoansChargers(request, pk):
	loans = LoansChargers.objects.get(id=pk)
	loans.delete()
	return Response('Registro eliminado satisfactoriamente!')

#*? ABONO CARGADORES
@api_view(['POST'])
def CreatePaymentsChargers(request):
	serializer = PaymentsChargersSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListPaymentsChargers(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	loans = PaymentsChargers.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListPaymentsChargersSerializer(loans, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeletePaymentsChargers(request, pk):
	loans = PaymentsChargers.objects.get(id=pk)
	loans.delete()
	return Response('Registro eliminado satisfactoriamente!')



#*? PRESTAMOS
@api_view(['POST'])
def CreateLoansDrivers(request):
	serializer = LoansDriversSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListLoansDrivers(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	loans = LoansDrivers.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListLoansDriversSerializer(loans, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteLoansDrivers(request, pk):
	loans = LoansDrivers.objects.get(id=pk)
	loans.delete()
	return Response('Registro eliminado satisfactoriamente!')

#*? ABONO CHOFERES
@api_view(['POST'])
def CreatePaymentsDrivers(request):
	serializer = PaymentsDriversSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListPaymentsDrivers(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	loans = PaymentsDrivers.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListPaymentsDriversSerializer(loans, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeletePaymentsDrivers(request, pk):
	loans = PaymentsDrivers.objects.get(id=pk)
	loans.delete()
	return Response('Registro eliminado satisfactoriamente!')



#*? CARTA PORTE
@api_view(['POST'])
def CreateBillOfLading(request):
	serializer = BillOfLadingSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListBillOfLading(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	bill = BillOfLading.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListBillOfLadingSerializer(bill, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeleteBillOfLading(request, pk):
	bill = BillOfLading.objects.get(id=pk)
	bill.delete()
	return Response('Registro eliminado satisfactoriamente!')

@api_view(['POST'])
def CreatePaymentSchedule(request):
	data = request.data
	new_payment = PaymentSchedule.objects.create(
		date=data["date"], 
		company_id=data["company"],
		bank_account_id=data["bank_account"],
		description=data["description"],
		total=data["total"],
		code=data["code"],
		user_id=data['user']
		)
	new_payment.save()

	for product in data["concepts"]:
		new_product = ConceptPayment.objects.create( concept=product["concept"], amount=product["amount"], code=data["code"])
		new_product.save()
		
		product_obj = ConceptPayment.objects.filter(concept=product["concept"], amount=product["amount"], code=data["code"]).get(code=data["code"])
		new_payment.concepts.add(product_obj)

	#serializer = RequisitionSerializer(new_creditnote)
	#return Response(serializer.data)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListPaymentSchedule(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	paymentschedule = PaymentSchedule.objects.filter(date__range=[fecha1, fecha2])
	serializer = ListPaymentScheduleSerializer(paymentschedule, many=True)
	return Response(serializer.data)

@api_view(['DELETE'])
def DeletePaymentSchedule(request, pk):
	payment = PaymentSchedule.objects.get(id=pk)
	payment.delete()
	return Response('Registro eliminado satisfactoriamente!')
#*? CUENTAS DE BANCOS DE CLIENTES

@api_view(['POST'])
def CreateBankAccountsCustomer(request):
	serializer = BankAccountsCustomerSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def ListBankAccountsCustomer(request, pk):
	list = BankAccountsCustomer.objects.filter(customer_id=pk)
	serializer = ListBankAccountsCustomerSerializer(list, many=True)
	return Response(serializer.data)	

#*? CUENTAS DE BANCOS DE EMPLEADOS	

@api_view(['POST'])
def CreateBankAccountsEmployee(request):
	serializer = BankAccountsEmployeeSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def ListBankAccountsEmployee(request, pk):
	list = BankAccountsEmployee.objects.filter(employee_id=pk)
	serializer = ListBankAccountsEmployeeSerializer(list, many=True)
	return Response(serializer.data)	

#*? CUENTAS DE BANCOS DE PROVEEDORES	

@api_view(['POST'])
def CreateBankAccountsProvider(request):
	serializer = BankAccountsProviderSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['GET'])
def ListBankAccountsProvider(request, pk):
	list = BankAccountsProvider.objects.filter(provider_id=pk)
	serializer = ListBankAccountsProviderSerializer(list, many=True)
	return Response(serializer.data)


#*? INGRESOS FACTURADOS

@api_view(['POST'])
def CreateBilledIncome(request):
	serializer = BilledIncomeSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListBilledIncome(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	company = data['company']
	list = BilledIncome.objects.filter(date__range=[fecha1, fecha2]).filter(company_id = company)
	serializer = ListBilledIncomeSerializer(list, many=True)
	return Response(serializer.data)	

@api_view(['GET'])
def ListBills(request):
	list = BilledIncome.objects.all()
	serializer = ListBilledIncomeSerializer(list, many=True)
	return Response(serializer.data)	

#*? CONTROL DE DEPOSITOS

@api_view(['POST'])
def CreateDepositControl(request):
	serializer = DepositControlSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

@api_view(['POST'])
def ListDepositControl(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	account = data['account']
	list = DepositControl.objects.filter(date__range=[fecha1, fecha2]).filter(account_id = account)
	serializer = ListDepositControlSerializer(list, many=True)
	return Response(serializer.data)	

@api_view(['POST'])
def ListTotalDepositControl(request):
	data = request.data
	fecha1 = data['start_date']
	fecha2 = data['end_date']
	
	list = DepositControl.objects.filter(date__range=[fecha1, fecha2]).values('account__tax_regime','account__company','account__deposit_limit').order_by('account__tax_regime','account','account__deposit_limit').annotate(TotalAmount=Sum('amount'))
	#serializer = ListTotalDepositControlSerializer(list, many=True)
	#return Response(serializer.data)
	return Response (list)

#*? COMPLEMENTOS DE PAGO

@api_view(['POST'])
def CreatePaidPlugins(request):
	data = request.data
	new_paid = PaidPlugins.objects.create(
		invoice = data['invoice'],
		payment_date=data['payment_date'],
		date_issue = data['date_issue'],
		company_id = data['company'],
		customer_id = data['customer'],
		account_id = data['account'],
		code = data['code'],
		user_id=data['user']
		)
	new_paid.save()

	for row in data["bills"]:
		new_invoice = BillsPaidPlugins.objects.create(invoice=row["invoice"],customer_id=data["customer"], code=data["code"])
		new_invoice.save()
		
		invoice_obj = BillsPaidPlugins.objects.filter(invoice=row["invoice"],customer_id=data["customer"], code=data["code"]).get(code=data["code"])
		new_paid.bills.add(invoice_obj)

	#serializer = RequisitionSerializer(new_creditnote)
	#return Response(serializer.data)
	return Response({"message":"Registro agregado satisfactoriamente!","status":200})  
	#return Response({"message":"No se realizó el Registro!","errors":serializer.errors,"status":400})

