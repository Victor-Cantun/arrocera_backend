from django.contrib import admin
from .models import Binnacle, Category, Company, CreditNote, Customer, Department, Diesel, Employee, FileProducer, FuelType, Fueling, Gasoline, Location, MainProduct, Parcel, Presentation, Producer, Product, ProductCN, ProductW, Provider, Requisition, SegalmexParcel, SegalmexReception, Shopping, Unit, User, Bank, BankAccount, Variety, VehicleType, Warehouse
# Register your models here.
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Bank)
admin.site.register(BankAccount)
admin.site.register(Employee)
admin.site.register(Producer)
admin.site.register(Provider)
admin.site.register(VehicleType)
admin.site.register(Unit)
admin.site.register(FuelType)
admin.site.register(Fueling)
admin.site.register(Diesel)
admin.site.register(Gasoline)
admin.site.register(Product)
admin.site.register(Requisition)
admin.site.register(Customer)
admin.site.register(ProductCN)
admin.site.register(CreditNote)
admin.site.register(ProductW)
admin.site.register(Presentation)
admin.site.register(Warehouse)
admin.site.register(Binnacle)
admin.site.register(Parcel)
admin.site.register(Shopping)
admin.site.register(FileProducer)
admin.site.register(Location)
admin.site.register(Variety)
admin.site.register(SegalmexReception)
admin.site.register(SegalmexParcel)
admin.site.register(Company)
admin.site.register(MainProduct)



#admin.site.register(ProductRequisition)

#class ProductRequisitionInline(admin.TabularInline):
    #model = ProductRequisition
    #extra = 1

#class RequisitionAdmin(admin.ModelAdmin):
   # inlines = [ProductRequisitionInline]

#admin.site.register(Requisition,RequisitionAdmin)

