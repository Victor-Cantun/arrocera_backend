from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("home", views.home, name="home"),
    # *? USUARIOS
    path("LoginUser", views.LoginUser, name="LoginUser"),
    path("RegisterUser", views.RegisterUser, name="RegisterUser"),
    path("CreateUser", views.CreateUser, name="CreateUser"),
    path("ListUser", views.ListUser, name="ListUser"),
    path("DeleteUser/<str:pk>", views.DeleteUser, name="DeleteUser"),
    path("UpdateUser/<str:pk>", views.UpdateUser, name="UpdateUser"),
    path("DetailUser/<str:pk>", views.DetailUser, name="DetailUser"),
    # *? MIS COMPAÑIAS
    path("CreateCompany", views.CreateCompany, name="CreateCompany"),
    path("ListCompany", views.ListCompany, name="ListCompany"),
    path("DeleteCompany/<str:pk>", views.DeleteCompany, name="DeleteCompany"),
    path("DetailCompany/<str:pk>", views.DetailCompany, name="DetailCompany"),
    path("UpdateCompany/<str:pk>", views.UpdateCompany, name="UpdateCompany"),
    # *? DEPARTAMENTOS
    path("DepartmentList", views.DepartmentList, name="DepartmentList"),
    path("DepartmentDetail/<str:pk>", views.DepartmentDetail, name="DepartmentDetail"),
    path("CreateDepartment", views.CreateDepartment, name="CreateDepartment"),
    path("UpdateDepartment/<str:pk>", views.UpdateDepartment, name="UpdateDepartment"),
    path("DeleteDepartment/<str:pk>", views.DeleteDepartment, name="DeleteDepartment"),
    path(
        "ReportDepartmentsPDF",
        views.ReportDepartmentsPDF.as_view(),
        name="ReportDepartmentsPDF",
    ),
    path(
        "ReportDepartmentsXLSX",
        views.ReportDepartmentsXLSX.as_view(),
        name="ReportDepartmentsXLSX",
    ),
    # *? CATEGORIAS
    path("CategoryList", views.CategoryList, name="CategoryList"),
    path("CategoryDetail/<str:pk>", views.CategoryDetail, name="CategoryDetail"),
    path("CreateCategory", views.CreateCategory, name="CreateCategory"),
    path("UpdateCategory/<str:pk>", views.UpdateCategory, name="UpdateCategory"),
    path("DeleteCategory/<str:pk>", views.DeleteCategory, name="DeleteCategory"),
    path(
        "ReportCategoriesPDF",
        views.ReportCategoriesPDF.as_view(),
        name="ReportCategoriesPDF",
    ),
    path(
        "ReportCategoriesXLSX",
        views.ReportCategoriesXLSX.as_view(),
        name="ReportCategoriesXLSX",
    ),
    # *? BANCOS
    path("BankList", views.BankList, name="BankList"),
    path("BankDetail/<str:pk>", views.BankDetail, name="BankDetail"),
    path("BankCreate", views.BankCreate, name="BankCreate"),
    path("BankUpdate/<str:pk>", views.BankUpdate, name="BankUpdate"),
    path("BankDelete/<str:pk>", views.BankDelete, name="BankDelete"),
    path("ReportBanksPDF", views.ReportBanksPDF.as_view(), name="ReportBanksPDF"),
    path("ReportBanksXLSX", views.ReportBanksXLSX.as_view(), name="ReportBanksXLSX"),
    # *? CUENTAS DE BANCOS
    path("BankAccountList", views.BankAccountList, name="BankAccountList"),
    path(
        "BankAccountDetail/<str:pk>", views.BankAccountDetail, name="BankAccountDetail"
    ),
    path("BankAccountCreate", views.BankAccountCreate, name="BankAccountCreate"),
    path(
        "BankAccountUpdate/<str:pk>", views.BankAccountUpdate, name="BankAccountUpdate"
    ),
    path(
        "BankAccountDelete/<str:pk>", views.BankAccountDelete, name="BankAccountDelete"
    ),
    path(
        "ReportBankAccountsPDF",
        views.ReportBankAccountsPDF.as_view(),
        name="ReportBankAccountsPDF",
    ),
    path(
        "ReportBankAccountsXLSX",
        views.ReportBankAccountsXLSX.as_view(),
        name="ReportBankAccountsXLSX",
    ),
    # *? PRODUCTORES
    path("Producers", views.Producers, name="Producers"),
    path("ProducerList", views.ProducerList, name="ProducerList"),
    path("ProducerDetail/<str:pk>", views.ProducerDetail, name="ProducerDetail"),
    path("CreateProducer", views.CreateProducer, name="CreateProducer"),
    path("UpdateProducer/<str:pk>", views.UpdateProducer, name="UpdateProducer"),
    path("DeleteProducer/<str:pk>", views.DeleteProducer, name="DeleteProducer"),
    path("UploadDocProducer", views.UploadDocProducer, name="UploadDocProducer"),
    path(
        "DetailFileProducer/<str:pk>",
        views.DetailFileProducer,
        name="DetailFileProducer",
    ),
    path(
        "ReportProducersPDF/<str:user>",
        views.ReportProducersPDF,
        name="ReportProducersPDF",
    ),
    path(
        "ReportProducersXLSX/<str:user>",
        views.ReportProducersXLSX.as_view(),
        name="ReportProducersXLSX",
    ),
    # *? PROVEEDORES
    path("Providers", views.Providers, name="Providers"),
    path("ProviderList", views.ProviderList, name="ProviderList"),
    path(
        "ProviderListForUser/<str:pk>", views.ProviderListForUser, name="ProviderList"
    ),
    path("ProviderDetail/<str:pk>", views.ProviderDetail, name="ProviderDetail"),
    path("CreateProvider", views.CreateProvider, name="CreateProvider"),
    path("UpdateProvider/<str:pk>", views.UpdateProvider, name="UpdateProvider"),
    path("DeleteProvider/<str:pk>", views.DeleteProvider, name="DeleteProvider"),
    path(
        "ReportProvidersPDF/<str:user>",
        views.ReportProvidersPDF,
        name="ReportProvidersPDF",
    ),
    path(
        "ReportProvidersXLSX/<str:user>",
        views.ReportProvidersXLSX.as_view(),
        name="ReportProvidersXLSX",
    ),
    # *? EMPLEADOS
    path("Empleado", views.EmpleadoList.as_view(), name="Empleado"),
    path("Employees", views.Employees, name="Employees"),
    path("ListEmployee", views.ListEmployee, name="ListEmployee"),
    path(
        "EmployeeListForUser/<str:pk>", views.EmployeeListForUser, name="EmployeeList"
    ),
    path("EmployeeDetail/<str:pk>", views.EmployeeDetail, name="EmployeeDetail"),
    path("CreateEmployee", views.CreateEmployee, name="CreateEmployee"),
    path("CrearEmpleado", views.CrearEmpleado, name="CrearEmpleado"),
    path("UpdateEmployee/<str:pk>", views.UpdateEmployee, name="UpdateEmployee"),
    path(
        "UpdatePhotoEmployee/<str:pk>",
        views.UpdatePhotoEmployee,
        name="UpdatePhotoEmployee",
    ),
    path("DeleteEmployee/<str:pk>", views.DeleteEmployee, name="DeleteEmployee"),
    path(
        "ReportEmployeesPDF/<str:department>/<str:user>",
        views.ReportEmployeesPDF,
        name="ReportEmployeesPDF",
    ),
    path(
        "ReportEmployeesXLSX/<str:department>/<str:user>",
        views.ReportEmployeesXLSX.as_view(),
        name="ReportEmployeesXLSX",
    ),
    # *? UNIDADES
    path("Units", views.Units, name="Units"),
    path("VehicleTypeList", views.VehicleTypeList, name="VehicleTypeList"),
    path("CreateVehicleType", views.CreateVehicleType, name="CreateVehicleType"),
    path("UnitList", views.UnitList, name="UnitList"),
    path("UnitListForUser/<str:pk>", views.UnitListForUser, name="UnitList"),
    path("UnitDetail/<str:pk>", views.UnitDetail, name="UnitDetail"),
    path("CreateUnit", views.CreateUnit, name="CreateUnit"),
    path("UpdateUnit/<str:pk>", views.UpdateUnit, name="UpdateUnit"),
    path("DeleteUnit/<str:pk>", views.DeleteUnit, name="DeleteUnit"),
    path("UpdatePhotoUnit/<str:pk>", views.UpdatePhotoUnit, name="UpdatePhotoUnit"),
    path("ReportUnitsPDF/<str:user>", views.ReportUnitsPDF, name="ReportUnitsPDF"),
    path(
        "ReportUnitsXLSX/<str:user>",
        views.ReportUnitsXLSX.as_view(),
        name="ReportUnitsXLSX",
    ),
    path("UploadFileUnit", views.UploadFileUnit, name="UploadFileUnit"),
    path("DetailFileUnit/<str:pk>", views.DetailFileUnit, name="DetailFileUnit"),
    # *? COMBUSTIBLE
    path("ListFuelType", views.ListFuelType, name="ListFuelType"),
    path("ListFueling", views.ListFueling, name="ListFueling"),
    path("DetailFueling/<str:pk>", views.DetailFueling, name="DetailFueling"),
    path("CreateFueling", views.CreateFueling, name="CreateFueling"),
    path("UpdateFueling/<str:pk>", views.UpdateFueling, name="UpdateFueling"),
    path("DeleteFueling/<str:pk>", views.DeleteFueling, name="DeleteFueling"),
    path(
        "ReportFuelLoadPDF/<str:start_date>/<str:end_date>/<str:fuel_type>/<str:user>",
        views.ReportFuelLoadPDF,
        name="ReportFuelLoadPDF",
    ),
    path(
        "ReportFuelLoadXLSX/<str:start_date>/<str:end_date>/<str:fuel_type>/<str:user>",
        views.ReportFuelLoadXLSX.as_view(),
        name="ReportFuelLoadXLSX",
    ),
    path("ObtainLoads/<str:pk>", views.ObtainLoads, name="ObtainLoads"),
    # *? DESCARGA DE COMBUSTIBLE
    path("CreateFuelDump", views.CreateFuelDump, name="CreateFuelDump"),
    path("ListFuelDump", views.ListFuelDump, name="ListFuelDump"),
    path("DeleteFuelDump/<str:pk>", views.DeleteFuelDump, name="DeleteFuelDump"),
    path("DetailFuelDump/<str:pk>", views.DetailFuelDump, name="DetailFuelDump"),
    path("UpdateFuelDump/<str:pk>", views.UpdateFuelDump, name="UpdateFuelDump"),
    # *? REQUISITION
    path("Requisitions", views.Requisitions, name="Requisitions"),
    path("ListRequisition", views.ListRequisition, name="ListRequisition"),
    path(
        "ListAuthorizedRequisitions",
        views.ListAuthorizedRequisitions,
        name="ListAuthorizedRequisitions",
    ),
    path("CreateRequisition", views.CreateRequisition, name="CreateRequisition"),
    path(
        "DeleteRequisition/<str:pk>", views.DeleteRequisition, name="DeleteRequisition"
    ),
    path(
        "RequisitionDetail/<str:pk>", views.RequisitionDetail, name="RequisitionDetail"
    ),
    path("UploadFileQuotation", views.UploadFileQuotation, name="UploadFileQuotation"),
    path(
        "DetailFileQuotation/<str:pk>",
        views.DetailFileQuotation,
        name="DetailFileQuotation",
    ),
    path(
        "UpdateStatusRequisition/<str:pk>",
        views.UpdateStatusRequisition,
        name="UpdateStatusRequisition",
    ),
    # *? CLIENTES
    path("CustomersBalance", views.CustomersBalance, name="CustomersBalance"),
    path("Customers", views.Customers, name="Customers"),
    path("ListCustomer", views.ListCustomer, name="ListCustomer"),
    path("CustomerList/<str:pk>", views.CustomerList, name="CustomerList"),
    path("CustomerDetail/<str:pk>", views.CustomerDetail, name="CustomerDetail"),
    path("CreateCustomer", views.CreateCustomer, name="CreateCustomer"),
    path("UpdateCustomer/<str:pk>", views.UpdateCustomer, name="UpdateCustomer"),
    path("DeleteCustomer/<str:pk>", views.DeleteCustomer, name="DeleteCustomer"),
    path(
        "ReportCustomersPDF/<str:user>",
        views.ReportCustomersPDF,
        name="ReportCustomersPDF",
    ),
    path(
        "ReportCustomersXLSX",
        views.ReportCustomersXLSX.as_view(),
        name="ReportCustomersXLSX",
    ),
    path(
        "UpdatePhotoCustomer/<str:pk>",
        views.UpdatePhotoCustomer,
        name="UpdatePhotoCustomer",
    ),
    path("AccountStatus", views.AccountStatus, name="AccountStatus"),
    # *? ORDEN DE PEDIDO
    path("PurchaseOrders", views.PurchaseOrders, name="PurchaseOrders"),
    path("ListPurchaseOrders", views.ListPurchaseOrders, name="ListPurchaseOrders"),
    path("CreatePurchaseOrder", views.CreatePurchaseOrder, name="CreatePurchaseOrder"),
    path(
        "DeletePurchaseOrder/<str:pk>",
        views.DeletePurchaseOrder,
        name="DeletePurchaseOrder",
    ),
    path(
        "DetailPurchaseOrder/<str:pk>",
        views.DetailPurchaseOrder,
        name="DetailPurchaseOrder",
    ),
    path(
        "UpdatePurchaseOrder/<str:pk>",
        views.UpdatePurchaseOrder,
        name="UpdatePurchaseOrder",
    ),
    path(
        "ReportPurchaseOrderPDF/<str:pk>",
        views.ReportPurchaseOrderPDF,
        name="ReportPurchaseOrderPDF",
    ),
    # *? NOTAS DE CREDITO
    path("CreditNotes", views.CreditNotes, name="CreditNotes"),
    path("CreditNoteList", views.CreditNoteList, name="CreditNoteList"),
    path("CreateCreditNote", views.CreateCreditNote, name="CreateCreditNote"),
    path("DeleteCreditNote/<str:pk>", views.DeleteCreditNote, name="DeleteCreditNote"),
    path("CreditNoteDetail/<str:pk>", views.CreditNoteDetail, name="CreditNoteDetail"),
    path(
        "ReportCreditNotePDF/<str:pk>",
        views.ReportCreditNotePDF,
        name="ReportCreditNotePDF",
    ),
    path("DetailCreditNote/<str:pk>", views.DetailCreditNote, name="DetailCreditNote"),
    path("UpdateCreditNote/<str:pk>", views.UpdateCreditNote, name="UpdateCreditNote"),
    # *? COTIZACIONES
    path("Quotes", views.Quotes, name="Quotes"),
    path("ListQuotation", views.ListQuotation, name="ListQuotation"),
    path("CreateQuotation", views.CreateQuotation, name="CreateQuotation"),
    path("DeleteQuotation/<str:pk>", views.DeleteQuotation, name="DeleteQuotation"),
    path("DetailQuotation/<str:pk>", views.DetailQuotation, name="DetailQuotation"),
    path(
        "ReportQuotationPDF/<str:pk>",
        views.ReportQuotationPDF,
        name="ReportQuotationPDF",
    ),
    path("UpdateQuotation/<str:pk>", views.UpdateQuotation, name="UpdateQuotation"),
    # *? PRODUCTOS PRINCIPALES
    path("CreateMainProduct", views.CreateMainProduct, name="CreateMainProduct"),
    path("ListMainProduct", views.ListMainProduct, name="ListMainProduct"),
    path(
        "DeleteMainProduct/<str:pk>", views.DeleteMainProduct, name="DeleteMainProduct"
    ),
    path(
        "DetailMainProduct/<str:pk>", views.DetailMainProduct, name="DetailMainProduct"
    ),
    # *? PRESENTATION
    path(
        "ListMainPresentation", views.ListMainPresentation, name="ListMainPresentation"
    ),
    # *? PRODUCTOS
    path("ListProduct", views.ListProduct, name="ListProduct"),
    path("CreateProduct", views.CreateProduct, name="CreateProduct"),
    path("DeleteProduct/<str:pk>", views.DeleteProduct, name="DeleteProduct"),
    path("DetailProduct/<str:pk>", views.DetailProduct, name="DetailProduct"),
    path("UpdateProduct/<str:pk>", views.UpdateProduct, name="UpdateProduct"),
    path(
        "ReportProductsPDF", views.ReportProductsPDF.as_view(), name="ReportProductsPDF"
    ),
    path(
        "ReportProductsXLSX",
        views.ReportProductsXLSX.as_view(),
        name="ReportProductsXLSX",
    ),
    # *? PRESENTACIONES
    path("PresentationList", views.PresentationList, name="PresentationList"),
    path("CreatePresentation", views.CreatePresentation, name="CreatePresentation"),
    path(
        "DeletePresentation/<str:pk>",
        views.DeletePresentation,
        name="DeletePresentation",
    ),
    path(
        "PresentationDetail/<str:pk>",
        views.PresentationDetail,
        name="PresentationDetail",
    ),
    path(
        "UpdatePresentation/<str:pk>",
        views.UpdatePresentation,
        name="UpdatePresentation",
    ),
    path(
        "ReportPresentationsPDF",
        views.ReportPresentationsPDF.as_view(),
        name="ReportPresentationsPDF",
    ),
    path(
        "ReportPresentationsXLSX",
        views.ReportPresentationsXLSX.as_view(),
        name="ReportPresentationsXLSX",
    ),
    # *? ALMACÉN
    path("CreateWarehouse", views.CreateWarehouse, name="CreateWarehouse"),
    # *? ENTRADA REPASO
    path("CreateTicketReview", views.CreateTicketReview, name="CreateTicketReview"),
    path("TicketReviewList", views.TicketReviewList, name="TicketReviewList"),
    path(
        "TicketReviewDetail/<str:pk>",
        views.TicketReviewDetail,
        name="TicketReviewDetail",
    ),
    # *? SALIDAS REPASO
    path("Outputs", views.Outputs, name="Outputs"),
    path("CreateOutput", views.CreateOutput, name="CreateOutput"),
    path("OutputList", views.OutputList, name="OutputList"),
    path("OutputDetail/<str:pk>", views.OutputDetail, name="OutputDetail"),
    path("DeleteOutput/<str:pk>", views.DeleteOutput, name="DeleteOutput"),
    path("UpdateOutput/<str:pk>", views.UpdateOutput, name="UpdateOutput"),
    # *? BITACORA
    path("Binnacles", views.Binnacles, name="Binnacles"),
    path("ListBinnacle/<str:pk>", views.ListBinnacle, name="ListBinnacle"),
    path("DetailBinnacle/<str:pk>", views.DetailBinnacle, name="DetailBinnacle"),
    path("CreateBinnacle", views.CreateBinnacle, name="CreateBinnacle"),
    path("UpdateBinnacle/<str:pk>", views.UpdateBinnacle, name="UpdateBinnacle"),
    path("DeleteBinnacle/<str:pk>", views.DeleteBinnacle, name="DeleteBinnacle"),
    path(
        "ReportBinnaclesPDF/<str:start_date>/<str:end_date>/<str:user>",
        views.ReportBinnaclesPDF,
        name="ReportBinnaclesPDF",
    ),
    path(
        "ReportBinnaclesXLSX/<str:start_date>/<str:end_date>/<str:user>",
        views.ReportBinnaclesXLSX.as_view(),
        name="ReportBinnaclesXLSX",
    ),
    # *? PARCELAS
    path("Parcels", views.Parcels, name="Parcels"),
    path("ListParcel", views.ListParcel, name="ListParcel"),
    path("DetailParcel/<str:pk>", views.DetailParcel, name="DetailParcel"),
    path("CreateParcel", views.CreateParcel, name="CreateParcel"),
    path("UpdateParcel/<str:pk>", views.UpdateParcel, name="UpdateParcel"),
    path("DeleteParcel/<str:pk>", views.DeleteParcel, name="DeleteParcel"),
    path(
        "ReportParcelsPDF/<str:user>", views.ReportParcelsPDF, name="ReportParcelsPDF"
    ),
    path(
        "ReportParcelsXLSX/<str:user>",
        views.ReportParcelsXLSX.as_view(),
        name="ReportParcelsXLSX",
    ),
    # *? RENTA DE TIERRAS
    path("ListLandRent", views.ListLandRent, name="ListLandRent"),
    path("CreateLandRent", views.CreateLandRent, name="CreateLandRent"),
    path("DeleteLandRent/<str:pk>", views.DeleteLandRent, name="DeleteLandRent"),
    path("DetailLandRent/<str:pk>", views.DetailLandRent, name="DetailLandRent"),
    path("UpdateLandRent/<str:pk>", views.UpdateLandRent, name="UpdateLandRent"),
    # *? CAJA CHICA
    path("ListPettyCash", views.ListPettyCash, name="ListPettyCash"),
    path("CreatePettyCash", views.CreatePettyCash, name="CreatePettyCash"),
    path("DeletePettyCash/<str:pk>", views.DeletePettyCash, name="DeletePettyCash"),
    path("DetailPettyCash/<str:pk>", views.DetailPettyCash, name="DetailPettyCash"),
    path("UpdatePettyCash/<str:pk>", views.UpdatePettyCash, name="UpdatePettyCash"),
    path("ListCash", views.ListCash, name="ListCash"),
    path("ListDiscount", views.ListDiscount, name="ListDiscount"),
    path("UpdateInitialCash", views.UpdateInitialCash, name="UpdateInitialCash"),
    path("ListInitialCash", views.ListInitialCash, name="ListInitialCash"),
    # *? COMPRAS
    path("Shoppings", views.Shoppings, name="Shoppings"),
    path("ListShopping", views.ListShopping, name="ListShopping"),
    path("DetailShopping/<str:pk>", views.DetailShopping, name="DetailShopping"),
    path("CreateShopping", views.CreateShopping, name="CreateShopping"),
    # path('UpdateShopping/<str:pk>',views.UpdateShopping, name="UpdateShopping"),
    path("DeleteShopping/<str:pk>", views.DeleteShopping, name="DeleteShopping"),
    # *? SOCIEDADES
    path("Societies", views.Societies, name="Societies"),
    path("CreateSociety", views.CreateSociety, name="CreateSociety"),
    path("ListSociety", views.ListSociety, name="ListSociety"),
    path("DeleteSociety/<str:pk>", views.DeleteSociety, name="DeleteSociety"),
    path("DetailSociety/<str:pk>", views.DetailSociety, name="DetailSociety"),
    path("UpdateSociety/<str:pk>", views.UpdateSociety, name="UpdateSociety"),
    path(
        "ReportSocietiesPDF/<str:user>",
        views.ReportSocietiesPDF,
        name="ReportSocietiesPDF",
    ),
    path(
        "ReportSocietiesXLSX/<str:user>",
        views.ReportSocietiesXLSX.as_view(),
        name="ReportSocietiesXLSX",
    ),
    # *? SEGALMEX parcelas
    path("ListSegalmexParcel", views.ListSegalmexParcel, name="ListSegalmexParcel"),
    path(
        "CreateSegalmexParcel", views.CreateSegalmexParcel, name="CreateSegalmexParcel"
    ),
    path(
        "DeleteSegalmexParcel/<str:pk>",
        views.DeleteSegalmexParcel,
        name="DeleteSegalmexParcel",
    ),
    path(
        "DetailSegalmexParcel/<str:pk>",
        views.DetailSegalmexParcel,
        name="DetailSegalmexParcel",
    ),
    path(
        "UpdateSegalmexParcel/<str:pk>",
        views.UpdateSegalmexParcel,
        name="UpdateSegalmexParcel",
    ),
    path(
        "ReportSegalmexParcelsPDF",
        views.ReportSegalmexParcelsPDF.as_view(),
        name="ReportSegalmexParcelsPDF",
    ),
    path(
        "ReportSegalmexParcelsXLSX",
        views.ReportSegalmexParcelsXLSX.as_view(),
        name="ReportSegalmexParcelsXLSX",
    ),
    # *? SEGALMEX recepción
    path(
        "ListSegalmexReception",
        views.ListSegalmexReception,
        name="ListSegalmexReception",
    ),
    path(
        "CreateSegalmexReception",
        views.CreateSegalmexReception,
        name="CreateSegalmexReception",
    ),
    path(
        "DeleteSegalmexReception/<str:pk>",
        views.DeleteSegalmexReception,
        name="DeleteSegalmexReception",
    ),
    path(
        "DetailSegalmexReception/<str:pk>",
        views.DetailSegalmexReception,
        name="DetailSegalmexReception",
    ),
    path(
        "UpdateSegalmexReception/<str:pk>",
        views.UpdateSegalmexReception,
        name="UpdateSegalmexReception",
    ),
    # path('BoletaPDF/<str:pk>', views.PDF_Boleta.as_view(), name='BoletaPDF'),
    path("SearchReception", views.SearchReception, name="SearchReception"),
    path(
        "ReportReceptionsXLSX/<str:start_date>/<str:end_date>/<str:producer>/<str:user>",
        views.ReportReceptionsXLSX.as_view(),
        name="ReportReceptionsXLSX",
    ),
    # *? Locatidades
    path("ListLocation", views.ListLocation, name="ListLocation"),
    # *? Variedades de arroz
    path("ListVariety", views.ListVariety, name="ListVariety"),
    # *? ORDEN DE PAGO DE PROVEEDORES
    path(
        "SearchTicketReception",
        views.SearchTicketReception,
        name="SearchTicketReception",
    ),
    path(
        "ListPaymentOrderProducer",
        views.ListPaymentOrderProducer,
        name="ListPaymentOrderProducer",
    ),
    path(
        "CreatePaymentOrderProducer",
        views.CreatePaymentOrderProducer,
        name="CreatePaymentOrderProducer",
    ),
    path(
        "DeletePaymentOrderProducer/<str:pk>",
        views.DeletePaymentOrderProducer,
        name="DeletePaymentOrderProducer",
    ),
    path(
        "DetailPaymentOrderProducer/<str:pk>",
        views.DetailPaymentOrderProducer,
        name="DetailPaymentOrderProducer",
    ),
    path(
        "UpdatePaymentOrderProducer/<str:pk>",
        views.UpdatePaymentOrderProducer,
        name="UpdatePaymentOrderProducer",
    ),
    # *? PAGO DE PROVEEDORES
    path(
        "SearchPaymentOrderProducer",
        views.SearchPaymentOrderProducer,
        name="SearchPaymentOrderProducer",
    ),
    path("ListPaymentProducer", views.ListPaymentProducer, name="ListPaymentProducer"),
    path(
        "CreatePaymentProducer",
        views.CreatePaymentProducer,
        name="CreatePaymentProducer",
    ),
    path(
        "DeletePaymentProducer/<str:pk>",
        views.DeletePaymentProducer,
        name="DeletePaymentProducer",
    ),
    path(
        "DetailPaymentProducer/<str:pk>",
        views.DetailPaymentProducer,
        name="DetailPaymentProducer",
    ),
    path(
        "UpdatePaymentProducer/<str:pk>",
        views.UpdatePaymentProducer,
        name="UpdatePaymentProducer",
    ),
    # *? Salario de choferes
    path("ListDriverSalary", views.ListDriverSalary, name="ListDriverSalary"),
    path("CreateDriverSalary", views.CreateDriverSalary, name="CreateDriverSalary"),
    path(
        "DeleteDriverSalary/<str:pk>",
        views.DeleteDriverSalary,
        name="DeleteDriverSalary",
    ),
    path(
        "DetailDriverSalary/<str:pk>",
        views.DetailDriverSalary,
        name="DetailDriverSalary",
    ),
    path(
        "UpdateDriverSalary/<str:pk>",
        views.UpdateDriverSalary,
        name="UpdateDriverSalary",
    ),
    # *? Salario de cargadores
    path("ListChargerSalary", views.ListChargerSalary, name="ListChargerSalary"),
    path("CreateChargerSalary", views.CreateChargerSalary, name="CreateChargerSalary"),
    path(
        "DeleteChargerSalary/<str:pk>",
        views.DeleteChargerSalary,
        name="DeleteChargerSalary",
    ),
    path(
        "DetailChargerSalary/<str:pk>",
        views.DetailChargerSalary,
        name="DetailChargerSalary",
    ),
    path(
        "UpdateChargerSalary/<str:pk>",
        views.UpdateChargerSalary,
        name="UpdateChargerSalary",
    ),
    # *? NOMINA
    path("ListPayroll", views.ListPayroll, name="ListPayroll"),
    path("CreatePayroll", views.CreatePayroll, name="CreatePayroll"),
    path("CalculatePayroll", views.CalculatePayroll, name="CalculatePayroll"),
    # *? Horas Extra
    path("ListExtraHours", views.ListExtraHours, name="ListExtraHours"),
    path("CreateExtraHours", views.CreateExtraHours, name="CreateExtraHours"),
    path("DeleteExtraHours/<str:pk>", views.DeleteExtraHours, name="DeleteExtraHours"),
    # *? Horas Extra
    path("ListDoubleDays", views.ListDoubleDays, name="ListDoubleDays"),
    path("CreateDoubleDays", views.CreateDoubleDays, name="CreateDoubleDays"),
    path("DeleteDoubleDays/<str:pk>", views.DeleteDoubleDays, name="DeleteDoubleDays"),
    # *? Apoyos
    path("ListProps", views.ListProps, name="ListProps"),
    path("CreateProps", views.CreateProps, name="CreateProps"),
    path("DeleteProps/<str:pk>", views.DeleteProps, name="DeleteProps"),
    # *? Prestamos
    path("ListLoans", views.ListLoans, name="ListLoans"),
    path("CreateLoans", views.CreateLoans, name="CreateLoans"),
    path("DeleteLoans/<str:pk>", views.DeleteLoans, name="DeleteLoans"),
    path("AddPaymentLoan", views.AddPaymentLoan, name="AddPaymentLoan"),
    # *? Prestamos Cargadores
    path("ListLoansChargers", views.ListLoansChargers, name="ListLoansChargers"),
    path("CreateLoansChargers", views.CreateLoansChargers, name="CreateLoansChargers"),
    path(
        "DeleteLoansChargers/<str:pk>",
        views.DeleteLoansChargers,
        name="DeleteLoansChargers",
    ),
    # *? Abono Cargadores
    path(
        "ListPaymentsChargers", views.ListPaymentsChargers, name="ListPaymentsChargers"
    ),
    path(
        "CreatePaymentsChargers",
        views.CreatePaymentsChargers,
        name="CreatePaymentsChargers",
    ),
    path(
        "DeletePaymentsChargers/<str:pk>",
        views.DeletePaymentsChargers,
        name="DeletePaymentsChargers",
    ),
    # *? Drivers/ CHOFERES
    # *? Chargers/ Cargadores
    # *? Prestamos Choferes
    path("ListLoansDrivers", views.ListLoansDrivers, name="ListLoansDrivers"),
    path("CreateLoansDrivers", views.CreateLoansDrivers, name="CreateLoansDrivers"),
    path(
        "DeleteLoansDrivers/<str:pk>",
        views.DeleteLoansDrivers,
        name="DeleteLoansDrivers",
    ),
    # *? Abonos Choferes
    path("ListPaymentsDrivers", views.ListPaymentsDrivers, name="ListPaymentsDrivers"),
    path(
        "CreatePaymentsDrivers",
        views.CreatePaymentsDrivers,
        name="CreatePaymentsDrivers",
    ),
    path(
        "DeletePaymentsDrivers/<str:pk>",
        views.DeletePaymentsDrivers,
        name="DeletePaymentsDrivers",
    ),
    # *? Carta PORTE
    path("BillOfLadings", views.BillOfLadings, name="BillOfLadings"),
    path("ListBillOfLading", views.ListBillOfLading, name="ListBillOfLading"),
    path("CreateBillOfLading", views.CreateBillOfLading, name="CreateBillOfLading"),
    path(
        "DeleteBillOfLading/<str:pk>",
        views.DeleteBillOfLading,
        name="DeleteBillOfLading",
    ),
    path(
        "DetailBillOfLading/<str:pk>",
        views.DetailBillOfLading,
        name="DetailBillOfLading",
    ),
    path(
        "UpdateBillOfLading/<str:pk>",
        views.UpdateBillOfLading,
        name="UpdateBillOfLading",
    ),
    # *? Progración de pagos
    path("PaymentsSchedule", views.PaymentsSchedule, name="PaymentsSchedule"),
    path("ListPaymentSchedule", views.ListPaymentSchedule, name="ListPaymentSchedule"),
    path(
        "CreatePaymentSchedule",
        views.CreatePaymentSchedule,
        name="CreatePaymentSchedule",
    ),
    path(
        "DeletePaymentSchedule/<str:pk>",
        views.DeletePaymentSchedule,
        name="DeletePaymentSchedule",
    ),
    # *? Crear Cuuenta de Banco de clientes
    path(
        "CreateBankAccountsCustomer",
        views.CreateBankAccountsCustomer,
        name="CreateBankAccountsCustomer",
    ),
    path(
        "ListBankAccountsCustomer/<str:pk>",
        views.ListBankAccountsCustomer,
        name="ListBankAccountsCustomer",
    ),
    # *? Crear Cuuenta de Banco de Empleados
    path(
        "CreateBankAccountsEmployee",
        views.CreateBankAccountsEmployee,
        name="CreateBankAccountsEmployee",
    ),
    path(
        "ListBankAccountsEmployee/<str:pk>",
        views.ListBankAccountsEmployee,
        name="ListBankAccountsEmployee",
    ),
    # *? Crear Cuuenta de Banco de Proveedores
    path(
        "CreateBankAccountsProvider",
        views.CreateBankAccountsProvider,
        name="CreateBankAccountsProvider",
    ),
    path(
        "ListBankAccountsProvider/<str:pk>",
        views.ListBankAccountsProvider,
        name="ListBankAccountsProvider",
    ),
    # *? VENTAS
    path("CreateSale", views.CreateSale, name="CreateSale"),
    path("ListSales", views.ListSales, name="ListSales"),
    path("DeleteSale/<str:pk>", views.DeleteSale, name="DeleteSale"),
    path("DetailSale/<str:pk>", views.DetailSale, name="DetailSale"),
    path("UpdateSale/<str:pk>", views.UpdateSale, name="UpdateSale"),
    # *? FACTURAS
    path("CreateBilledIncome", views.CreateBilledIncome, name="CreateBilledIncome"),
    path("ListBilledIncome", views.ListBilledIncome, name="ListBilledIncome"),
    path("ListBills", views.ListBills, name="ListBills"),
    path(
        "DeleteBilledIncome/<str:pk>",
        views.DeleteBilledIncome,
        name="DeleteBilledIncome",
    ),
    path(
        "DetailBilledIncome/<str:pk>",
        views.DetailBilledIncome,
        name="DetailBilledIncome",
    ),
    path(
        "UpdateBilledIncome/<str:pk>",
        views.UpdateBilledIncome,
        name="UpdateBilledIncome",
    ),
    path("ListFactura", views.ListFactura, name="ListFactura"),
    # *? INGRESOS
    path("CreateIncome", views.CreateIncome, name="CreateIncome"),
    path("ListIncome", views.ListIncome, name="ListIncome"),
    path("DeleteIncome/<str:pk>", views.DeleteIncome, name="DeleteIncome"),
    path("DetailIncome/<str:pk>", views.DetailIncome, name="DetailIncome"),
    path("UpdateIncome/<str:pk>", views.UpdateIncome, name="UpdateIncome"),
    # *? CONTROL DE DEPOSITOS
    path(
        "CreateDepositControl", views.CreateDepositControl, name="CreateDepositControl"
    ),
    path("ListDepositControl", views.ListDepositControl, name="ListDepositControl"),
    # *? Total de depositos
    path(
        "ListTotalDepositControl",
        views.ListTotalDepositControl,
        name="ListTotalDepositControl",
    ),
    # *? CONCILIACIONES
    path("CreateConciliation", views.CreateConciliation, name="CreateConciliation"),
    path("ListConciliation", views.ListConciliation, name="ListConciliation"),
    path(
        "PreviousLedgerBalance/<str:pk>",
        views.PreviousLedgerBalance,
        name="PreviousLedgerBalance",
    ),
    path(
        "PreviousAccountBalance/<str:pk>",
        views.PreviousAccountBalance,
        name="PreviousAccountBalance",
    ),
    path(
        "DeleteConciliation/<str:pk>",
        views.DeleteConciliation,
        name="DeleteConciliation",
    ),
    path(
        "ListConciliationForMonth",
        views.ListConciliationForMonth,
        name="ListConciliationForMonth",
    ),
    # *? COMPLEMENTOS DE PAGO
    path("ListPlugins", views.ListPlugins, name="ListPlugins"),
    path("CreatePaidPlugins", views.CreatePaidPlugins, name="CreatePaidPlugins"),
    path("ListPaidPlugins", views.ListPaidPlugins, name="ListPaidPlugins"),
    path(
        "DeletePaidPlugins/<str:pk>", views.DeletePaidPlugins, name="DeletePaidPlugins"
    ),
    path(
        "DetailPaidPlugins/<str:pk>", views.DetailPaidPlugins, name="DetailPaidPlugins"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
