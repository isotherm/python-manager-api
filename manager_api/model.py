# -*- coding: utf-8 -*-
# Do not edit. Automatically generated from Manager v23.1.11.592.

from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel

from . import enums
from .enums import *
from .object import Object


CustomFieldsAttribute = Union["Employee", "FixedAsset", "PayslipDeductionItem", "DepreciationEntry", "RecurringSalesOrder", "Folder", "PurchaseInvoice", "RecurringPurchaseInvoice", "InventoryWriteOff", "SalesOrder", "TaxCode", "RecurringSalesInvoice", "DeliveryNote", "Project", "DebitNote", "WithholdingTaxReceipt", "IntangibleAsset", "RecurringJournalEntry", "Payslip", "Payment", "RecurringPayslip", "InventoryTransfer", "InventoryItem", "RecurringInterAccountTransfer", "Receipt", "PayslipContributionItem", "Supplier", "PurchaseOrder", "BankOrCashAccount", "SalesInvoice", "GoodsReceipt", "RecurringPurchaseOrder", "ExpenseClaim", "SalesQuote", "CapitalAccount", "BusinessDetails", "Customer", "InterAccountTransfer", "PurchaseQuote", "BillableTime", "CreditNote", "NonInventoryItem", "SpecialAccount", "RecurringPayment", "RecurringReceipt", "JournalEntry", "PayslipEarningsItem", "InventoryKit", "RecurringSalesQuote", "ProductionOrder", "AmortizationEntry"]
BalanceSheetAbstractGroup = Union["Assets", "BalanceSheetGroup", "Equity", "Liabilities"]
ChartOfAccountsGroup = Union["BalanceSheetAbstractGroup", "ProfitAndLossStatementGroup"]
IGeneralLedgerAccount = Union["BalanceSheetBillableExpensesAccount", "ProfitAndLossStatementAccountLatePaymentFees", "BalanceSheetEmployeeClearingAccount", "BalanceSheetInventoryOnHandAccount", "ControlAccountForIntangibleAssetsAccumulatedAmortization", "BalanceSheetBillableTimeAccount", "BalanceSheetProductionInProgressAccount", "ControlAccountForInventoryItems", "BalanceSheetAccountsPayableAccount", "ProfitAndLossStatementAccountBillableTimeInvoiced", "ProfitAndLossStatementAccountFixedAssetDepreciation", "BalanceSheetWithholdingTaxReceivableAccount", "ProfitAndLossStatementAccountIntangibleAssetsAmortization", "ProfitAndLossStatementCapitalGainsOnInvestments", "ProfitAndLossStatementAccount", "BalanceSheetTaxPayableAccount", "ControlAccountForSuppliers", "BalanceSheetFixedAssetsAtCostAccount", "ControlAccountForEmployees", "BalanceSheetSpecialAccountsAccount", "ControlAccountForBankAccounts", "BalanceSheetWithholdingTaxAccount", "ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal", "BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount", "BalanceSheetInterdivisionalLoan", "BalanceSheetInvestmentsAccount", "BalanceSheetWithholdingTaxPayableAccount", "ControlAccountForInvestments", "ProfitAndLossStatementAccountBillableExpensesInvoiced", "ControlAccountForFixedAssets", "ControlAccountForIntangibleAssets", "ProfitAndLossStatementAccountBillableTimeMovement", "ProfitAndLossStatementAccountInventoryPurchases", "BalanceSheetFixedAssetsAccumulatedDepreciationAccount", "ProfitAndLossStatementAccountCurrencyGainsLosses", "BalanceSheetExpenseClaimsAccount", "BalanceSheetCapitalAccountsAccount", "ControlAccountForFixedAssetsAccumulatedDepreciation", "ProfitAndLossStatementAccountBillableExpensesCost", "BalanceSheetIntangibleAssetsAtCostAccount", "ProfitAndLossStatementAccountFixedAssetLossOnDisposal", "BalanceSheetCashAtBankAccount", "ControlAccountForCustomers", "BalanceSheetAccountsReceivableAccount", "ControlAccountForSpecialAccounts", "ProfitAndLossStatementAccountInventorySales", "BalanceSheetAccount", "ProfitAndLossStatementAccountRoundingExpense", "ControlAccountForCapitalAccounts", "BalanceSheetRetainedEarningsAccount", "BalanceSheetSuspenseAccount"]
ICustomGeneralLedgerAccount = Union["BalanceSheetAccount", "ProfitAndLossStatementAccount"]
IInventoryWriteOffAccount = Union["BalanceSheetFixedAssetsAtCostAccount", "BalanceSheetAccount", "ControlAccountForFixedAssets", "ProfitAndLossStatementAccount"]
IJournalEntryAccount = Union["BalanceSheetBillableExpensesAccount", "ProfitAndLossStatementAccountLatePaymentFees", "BalanceSheetEmployeeClearingAccount", "BalanceSheetInventoryOnHandAccount", "ControlAccountForInventoryItems", "BalanceSheetAccountsPayableAccount", "ProfitAndLossStatementAccountBillableTimeInvoiced", "ProfitAndLossStatementAccountFixedAssetDepreciation", "ProfitAndLossStatementAccountIntangibleAssetsAmortization", "ProfitAndLossStatementCapitalGainsOnInvestments", "ProfitAndLossStatementAccount", "ControlAccountForSuppliers", "BalanceSheetFixedAssetsAtCostAccount", "ControlAccountForEmployees", "BalanceSheetSpecialAccountsAccount", "BalanceSheetWithholdingTaxAccount", "ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal", "BalanceSheetInvestmentsAccount", "BalanceSheetWithholdingTaxPayableAccount", "ProfitAndLossStatementAccountBillableExpensesInvoiced", "ControlAccountForInvestments", "ProfitAndLossStatementAccountBillableTimeMovement", "ControlAccountForFixedAssets", "ControlAccountForIntangibleAssets", "ProfitAndLossStatementAccountInventoryPurchases", "BalanceSheetExpenseClaimsAccount", "BalanceSheetCapitalAccountsAccount", "ProfitAndLossStatementAccountBillableExpensesCost", "BalanceSheetIntangibleAssetsAtCostAccount", "ProfitAndLossStatementAccountFixedAssetLossOnDisposal", "ControlAccountForCustomers", "BalanceSheetAccountsReceivableAccount", "ControlAccountForSpecialAccounts", "ProfitAndLossStatementAccountInventorySales", "BalanceSheetAccount", "ControlAccountForCapitalAccounts", "BalanceSheetRetainedEarningsAccount"]
INonInventoryItemAccount = Union["BalanceSheetAccount", "ProfitAndLossStatementAccount"]
IPurchaseInvoiceAccount = Union["BalanceSheetIntangibleAssetsAtCostAccount", "BalanceSheetBillableExpensesAccount", "ControlAccountForInvestments", "BalanceSheetEmployeeClearingAccount", "ControlAccountForFixedAssets", "ControlAccountForIntangibleAssets", "ProfitAndLossStatementAccount", "BalanceSheetFixedAssetsAtCostAccount", "ControlAccountForEmployees", "BalanceSheetSpecialAccountsAccount", "ControlAccountForSpecialAccounts", "BalanceSheetAccount", "ControlAccountForCapitalAccounts", "BalanceSheetCapitalAccountsAccount", "BalanceSheetRetainedEarningsAccount"]
ISalesInvoiceAccount = Union["BalanceSheetIntangibleAssetsAtCostAccount", "ProfitAndLossStatementAccountBillableExpensesInvoiced", "ControlAccountForInvestments", "ControlAccountForFixedAssets", "ControlAccountForIntangibleAssets", "ProfitAndLossStatementAccount", "BalanceSheetFixedAssetsAtCostAccount", "BalanceSheetSpecialAccountsAccount", "ControlAccountForSpecialAccounts", "BalanceSheetAccount", "ProfitAndLossStatementAccountBillableTimeInvoiced", "ControlAccountForCapitalAccounts", "BalanceSheetCapitalAccountsAccount", "BalanceSheetRetainedEarningsAccount"]
IBankOrCashAccount = Union["BankOrCashAccount"]
IReportingCategory = Union["EmployeeEmailField", "RoundDownReportingCategory", "BusinessDetailsNameField", "PayslipDeductionItemReportingCategory", "ReportTranformationFromDate", "ReportTransformationTaxSales", "ReportTransformationTaxAmounts", "TaxAmountReportingCategory", "EmployeeNameField", "ReverseSignReportingCategory", "PayslipEarningsItemReportingCategory", "TaxCodeReversedReportingCategory", "DateCustomField", "CustomField", "SupplierNameField", "ReportTransformationLabel", "PayslipContributionItemReportingCategory", "ReportTransformationFromDateLastJuly", "ReportTransformationNetAmounts", "MultipleValueCustomField", "SetZeroIfNegativeReportingCategory", "TaxCodeReportingCategory", "CheckboxCustomField", "HideIfEmptyReportingCategory", "ReportTranformationToDate", "ReportTransformationTaxPurchases", "NumberCustomField", "TextCustomField", "TaxAmountReversedReportingCategory"]
IExpenseClaimPayer = Union["Employee", "CapitalAccount", "ExpenseClaimsPayer"]
ICustomField = Union["CheckboxCustomField", "DateCustomField", "NumberCustomField", "MultipleValueCustomField", "TextCustomField"]
IPurchaseItem = Union["FreightInItem", "NonInventoryItem", "InventoryItem"]
ISaleItem = Union["InventoryKit", "NonInventoryItem", "InventoryItem"]
IProfitAndLossAccount = Union["ProfitAndLossStatementAccountBillableExpensesInvoiced", "ProfitAndLossStatementAccountFixedAssetLossOnDisposal", "ProfitAndLossStatementAccountBillableTimeMovement", "ProfitAndLossStatementAccountLatePaymentFees", "ProfitAndLossStatementCapitalGainsOnInvestments", "ProfitAndLossStatementAccount", "ProfitAndLossStatementAccountInventoryPurchases", "ProfitAndLossStatementAccountCurrencyGainsLosses", "ProfitAndLossStatementAccountInventorySales", "ProfitAndLossStatementAccountRoundingExpense", "ProfitAndLossStatementAccountFixedAssetDepreciation", "ProfitAndLossStatementAccountBillableTimeInvoiced", "ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal", "ProfitAndLossStatementAccountBillableExpensesCost", "ProfitAndLossStatementAccountIntangibleAssetsAmortization"]


class AgedPayables(Object):
    Guid: ClassVar[UUID] = "6abe86ec-a6c9-46a8-a9c9-7104056a2730"
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Division: Optional[Division]
    SortBy: Optional[SortBy]
    Description: Optional[str]
    ShowInvoices: Optional[bool]


class AgedReceivables(Object):
    Guid: ClassVar[UUID] = "39f00628-27a7-4924-9030-5bc655ee234f"
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Division: Optional[Division]
    SortBy: Optional[SortBy]
    Description: Optional[str]
    ShowInvoices: Optional[bool]


class AmortizationCalculationWorksheet(Object):
    Guid: ClassVar[UUID] = "011cf167-ff32-49e7-b0f3-ac12a3fe43ed"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class AmortizationEntry(Object):
    Guid: ClassVar[UUID] = "d33519a3-e8e0-4556-9833-b744a58dd2f7"
    class Line(BaseModel):
        IntangibleAsset: Optional[IntangibleAsset]
        Division: Optional[Division]
        Amount: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class Amount(Object):
    pass


class Assets(Object):
    Key = UUID("4c05c221-ca57-4c7c-be62-115669302ed4")


class Attachment(Object):
    Guid: ClassVar[UUID] = "2e541a82-94d7-42fc-a388-26bdc0803455"
    Date: Optional[date]
    Name: Optional[str]
    ContentType: Optional[str]
    Size: Optional[int]
    Object: Optional[Object]


class BalanceSheet(Object):
    Guid: ClassVar[UUID] = "7b4f463a-470d-44c4-9e75-fafc630b5851"
    class Period(BaseModel):
        Date: Optional[date]
        Division: Optional[Division]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    AccountingMethod: Optional[AccountingBasis]
    Rounding: Optional[Rounding]
    Layout: Optional[BalanceSheetLayout]
    GroupsToCollapse: Optional[List[BalanceSheetAbstractGroup]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class BalanceSheetAbstractGroup(Object):
    pass


class BalanceSheetAccount(Object):
    Guid: ClassVar[UUID] = "6ef13e42-ad89-4d42-9480-546e0c04a411"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[CashFlowStatementInvestingActivityGroup]
    Division: Optional[Division]
    Position: Optional[int]
    StartingBalance: Optional[Decimal]
    StartingBalanceType: Optional[DebitCredit]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    Inactive: Optional[bool]


class BalanceSheetAccountsPayableAccount(Object):
    Key = UUID("dac7ba37-0ccd-45e5-906e-548e6c50df37")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]


class BalanceSheetAccountsReceivableAccount(Object):
    Key = UUID("d1489e95-bb28-4f5d-b42e-67d3291b3893")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]


class BalanceSheetBillableExpensesAccount(Object):
    Key = UUID("059dbfb9-1c80-4043-887f-0fc441099fe0")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    Position: Optional[int]


class BalanceSheetBillableTimeAccount(Object):
    Key = UUID("9f3c0a1a-dd0b-4b5c-ba50-3e4939a0e90c")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetCapitalAccountsAccount(Object):
    Key = UUID("054dfae1-c34a-475e-abde-49e0385ffc9a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetCashAtBankAccount(Object):
    Key = UUID("6d4af96a-0959-4bb2-9160-fa825ec67c43")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetEmployeeClearingAccount(Object):
    Key = UUID("650a36fe-801f-4031-8d5b-ab422d061fca")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetExpenseClaimsAccount(Object):
    Key = UUID("f728124f-c6b6-4dad-82c5-22fc0d8d0571")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetFixedAssetsAccumulatedDepreciationAccount(Object):
    Key = UUID("f813a6c8-1ead-46bd-8911-f12714be193c")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetFixedAssetsAtCostAccount(Object):
    Key = UUID("4a0e8917-fee2-4033-9161-48dd513fdb73")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetGroup(Object):
    Guid: ClassVar[UUID] = "c03d1921-7a45-4eda-8742-a2d9082dcf4f"
    Name: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount(Object):
    Key = UUID("aa12d048-bfbd-47dc-a5b8-03e35c417996")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetIntangibleAssetsAtCostAccount(Object):
    Key = UUID("31d369e3-32c7-4bd2-bb83-9c1c58010c1a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetInterdivisionalLoan(Object):
    Key = UUID("ac4ab22b-0fbd-485f-8434-d25745b9be22")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetInventoryOnHandAccount(Object):
    Key = UUID("0fb45a62-fc42-43a8-a776-782e8b5ffc96")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetInvestmentsAccount(Object):
    Key = UUID("352897d1-e7fe-462e-9965-458ed9e27b82")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatementInvestingActivityGroup: Optional[CashFlowStatementInvestingActivityGroup]
    Position: Optional[int]


class BalanceSheetProductionInProgressAccount(Object):
    Key = UUID("30a1b83c-68a8-4f2c-ae70-25b0acc2d12a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetRetainedEarningsAccount(Object):
    Key = UUID("74dfd025-d68e-4a99-9c78-5d43e17c0e09")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetSpecialAccountsAccount(Object):
    Key = UUID("ef49facb-203b-4b45-aebd-99af4645700b")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[CashFlowStatementInvestingActivityGroup]
    Position: Optional[int]


class BalanceSheetSuspenseAccount(Object):
    Key = UUID("11211c9e-0988-4d16-8bf2-fa39487123aa")


class BalanceSheetTaxPayableAccount(Object):
    Key = UUID("30c697fa-4196-438a-ab5a-1957478034b1")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetWithholdingTaxAccount(Object):
    Key = UUID("8f75a810-abd0-4d89-a6a2-66c9003a60e2")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetWithholdingTaxPayableAccount(Object):
    Key = UUID("a4dffac2-35d1-47e1-a4bd-b6de15975fdb")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetWithholdingTaxReceivableAccount(Object):
    Key = UUID("c66de1bf-6f63-4bc8-9452-0b019e41c47f")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]


class BankAccountSummary(Object):
    Guid: ClassVar[UUID] = "77afd97c-51d7-484b-8192-b7eb006daadb"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
    BankAccount: Optional[BankOrCashAccount]
    Periods: Optional[List[Period]]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class BankOrCashAccount(Object):
    Guid: ClassVar[UUID] = "1408c33b-6284-4f50-9e31-48cbea21f3cf"
    Name: Optional[str]
    Code: Optional[str]
    Currency: Optional[ForeignCurrency]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForBankAccounts]
    StartingBalance: Optional[Decimal]
    HasInternationalBankAccountNumber: Optional[bool]
    InternationalBankAccountNumber: Optional[str]
    CanHavePendingTransactions: Optional[bool]
    HasCreditLimit: Optional[bool]
    CreditLimit: Optional[Decimal]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    IsBankAccount: Optional[bool]


class BankReconciliation(Object):
    Guid: ClassVar[UUID] = "a3b1d610-b5e8-4f17-8e97-e53e69b78bb5"
    Date: Optional[date]
    BankAccount: Optional[BankOrCashAccount]
    StatementBalance: Optional[Decimal]


class BaseCurrency(Object):
    Key = UUID("39dde4fc-7af8-44cc-8572-3b1ff4cfb918")
    Code: Optional[str]
    Name: Optional[str]
    Symbol: Optional[str]
    DecimalPlaces: Optional[int]


class BillableExpenses(Object):
    Guid: ClassVar[UUID] = "e3ea8ce1-4fa4-43df-aec6-38ef5b574b1b"
    Enabled: Optional[bool]


class BillableTime(Object):
    Guid: ClassVar[UUID] = "6bfb652c-11cb-46fa-9e5a-c5950ccbae15"
    Date: Optional[date]
    Customer: Optional[Customer]
    Description: Optional[str]
    HourlyRate: Optional[Decimal]
    TimeSpent: Optional[int]
    TimeSpentMinutes: Optional[int]
    Division: Optional[Division]
    Status: Optional[BillableTimeStatus]
    SalesInvoice: Optional[SalesInvoice]
    WrittenOffDate: Optional[date]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class BillableTimeSummary(Object):
    Guid: ClassVar[UUID] = "5516d6e5-d1fe-4271-8625-f7f0acc7f961"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class BusinessDetails(Object):
    Key = UUID("38cf4712-6e95-4ce1-b53a-bff03edad273")
    Name: Optional[str]
    Address: Optional[str]
    Country: Optional[str]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class BusinessDetailsNameField(Object):
    Key = UUID("ce6302f8-0b02-42d8-b6b7-850063e4bbe0")


class BusinessLogo(Object):
    Key = UUID("096d0af9-df72-425d-aae8-d59c0497f119")
    ContentType: Optional[str]
    Content: Optional[bytes]


class CapitalAccount(Object):
    Guid: ClassVar[UUID] = "b9c4cd62-7569-44f0-bc62-9df3007a6a5c"
    Name: Optional[str]
    Code: Optional[str]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForCapitalAccounts]
    StartingBalance: Optional[StartingBalanceType]
    StartingBalanceAmount: Optional[Decimal]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    Inactive: Optional[bool]


class CashFlowStatement(Object):
    Guid: ClassVar[UUID] = "2a9a4b8e-8b06-4819-adee-4b766a55119c"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Method: Optional[CashFlowStatementMethod]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    RoundDecimals: Optional[bool]


class CashFlowStatementFinancingActivityGroup(Object):
    Guid: ClassVar[UUID] = "da08116a-6fe3-47c2-805c-d5a81a03931a"
    Name: Optional[str]


class CashFlowStatementInvestingActivityGroup(Object):
    Guid: ClassVar[UUID] = "a9cf8675-afb3-42d6-9440-f5efedef55b8"
    Name: Optional[str]


class CashFlowStatementOperatingActivityGroup(Object):
    Guid: ClassVar[UUID] = "25299eaa-3460-4a62-bd5d-8bc65b24375d"
    Name: Optional[str]


class ChartOfAccountsGroup(Object):
    pass


class CheckboxCustomField(Object):
    Guid: ClassVar[UUID] = "ccad5339-206e-4145-aa3d-3bd8d785b2fb"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[CustomFieldsAttribute]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]


class Column(Object):
    pass


class ControlAccount(Object):
    pass


class ControlAccountForBankAccounts(Object):
    Guid: ClassVar[UUID] = "c97264e3-eed6-4afd-8d2c-e1c1a00b4dc1"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForCapitalAccounts(Object):
    Guid: ClassVar[UUID] = "95b9d17d-f5f8-4722-a89d-456fa0906e13"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForCustomers(Object):
    Guid: ClassVar[UUID] = "7a57978e-583d-4997-86c7-c557de0e7fdd"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForEmployees(Object):
    Guid: ClassVar[UUID] = "fb804fba-df12-4628-ae54-df7a67d67f1b"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForFixedAssets(Object):
    Guid: ClassVar[UUID] = "014742b2-fc31-4ded-90b5-2e0d437a1589"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForFixedAssetsAccumulatedDepreciation(Object):
    Guid: ClassVar[UUID] = "c2e88cf8-4d05-4bec-8c42-fdef424faf1a"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForIntangibleAssets(Object):
    Guid: ClassVar[UUID] = "8ed99282-8ec3-4505-8846-0507bd0d0f70"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForIntangibleAssetsAccumulatedAmortization(Object):
    Guid: ClassVar[UUID] = "47995ee3-b2c9-4799-ace3-768f7514c644"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForInventoryItems(Object):
    Guid: ClassVar[UUID] = "acc019f7-9bb9-4d8e-ba66-0956916b4247"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForInvestments(Object):
    Guid: ClassVar[UUID] = "fb2c120e-6b30-47cb-a61e-14f0189bec06"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForSpecialAccounts(Object):
    Guid: ClassVar[UUID] = "6af7e809-1de3-4a09-923f-27ad786ed837"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[CashFlowStatementInvestingActivityGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForSuppliers(Object):
    Guid: ClassVar[UUID] = "78e7aefb-9dff-4ae5-981e-4165b14fd963"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class CreditNote(Object):
    Guid: ClassVar[UUID] = "245e5943-0092-409d-96ae-e2ee10eac75b"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        Account: Optional[ISalesInvoiceAccount]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        SalesUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    IssueDate: Optional[date]
    Reference: Optional[str]
    Customer: Optional[Customer]
    SalesInvoice: Optional[SalesInvoice]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    SalesInventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsIncludeTax: Optional[bool]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxAmount: Optional[Decimal]
    WithholdingTaxRate: Optional[Decimal]
    HasCreditNoteCustomTheme: Optional[bool]
    CreditNoteCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasCreditNoteFooters: Optional[bool]
    CreditNoteFooters: Optional[List[CreditNoteFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    Type: Optional[CreditNoteType]


class CreditNoteFooter(Object):
    Guid: ClassVar[UUID] = "90f7ba80-5666-49a2-af1b-908cf9a651cd"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Currency(Object):
    pass


class Customer(Object):
    Guid: ClassVar[UUID] = "ec37c11e-2b67-49c6-8a58-6eccb7dd75ee"
    Name: Optional[str]
    Code: Optional[str]
    CreditLimit: Optional[Decimal]
    Currency: Optional[ForeignCurrency]
    BillingAddress: Optional[str]
    DeliveryAddress: Optional[str]
    Email: Optional[str]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForCustomers]
    StartingBalance: Optional[Decimal]
    HasDefaultDueDateDays: Optional[bool]
    DefaultDueDateDays: Optional[int]
    HasDefaultHourlyRate: Optional[bool]
    DefaultHourlyRate: Optional[Decimal]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultBillingAddress: Optional[bool]


class CustomerPortal(Object):
    Guid: ClassVar[UUID] = "18048748-7c70-49e6-bed4-b9d310736956"
    Customer: Optional[Customer]
    SalesQuotes: Optional[bool]
    SalesOrders: Optional[bool]
    SalesInvoices: Optional[bool]
    CreditNotes: Optional[bool]
    DeliveryNotes: Optional[bool]


class CustomerStatementsTransactions(Object):
    Guid: ClassVar[UUID] = "c81ede5f-141e-4eb3-a586-1b0ab079cae6"
    FromDate: Optional[date]
    ToDate: Optional[DateType]
    ToCustomDate: Optional[date]
    Theme: Optional[Theme]


class CustomerStatementsUnpaidInvoices(Object):
    Guid: ClassVar[UUID] = "b9b3d678-a743-46e1-aaf5-fd1b27b5e20b"
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Theme: Optional[Theme]


class CustomerSummary(Object):
    Guid: ClassVar[UUID] = "b8583039-fa11-441a-a727-40aa2311e74c"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Division: Optional[Division]


class CustomField(Object):
    Guid: ClassVar[UUID] = "dcb382dc-a4e0-4354-a845-b7d647f610f7"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[CustomFieldsAttribute]]
    Type: Optional[CustomFieldStyle]
    OptionsForDropdownList: Optional[str]
    Size: Optional[CustomFieldSize]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class CustomFields(Object):
    Strings: Optional[Dict[ICustomField, str]]
    Decimals: Optional[Dict[ICustomField, Decimal]]
    Dates: Optional[Dict[ICustomField, date]]
    Booleans: Optional[Dict[ICustomField, bool]]
    StringArrays: Optional[Dict[ICustomField, List[str]]]


class CustomReport(Object):
    Guid: ClassVar[UUID] = "7df43b64-9aea-4b19-a60a-a56f2e390df4"
    class SelectElement(BaseModel):
        SelectPrimaryField: Optional[MemberInfo]
        SelectSecondaryField: Optional[MemberInfo]
        SelectCustomField: Optional[CustomField]
        DisplayName: Optional[str]
    class OrderByElement(BaseModel):
        OrderByPrimaryField: Optional[MemberInfo]
        OrderBySecondaryField: Optional[MemberInfo]
        OrderByCustomField: Optional[CustomField]
        SortOrder: Optional[SortOrder]
    class GroupByElement(BaseModel):
        GroupByPrimaryField: Optional[MemberInfo]
        GroupBySecondaryField: Optional[MemberInfo]
        GroupByCustomField: Optional[CustomField]
    class WhereElement(BaseModel):
        WherePrimaryField: Optional[MemberInfo]
        WhereSecondaryField: Optional[MemberInfo]
        WhereCustomField: Optional[CustomField]
        StringOperator: Optional[StringOperator]
        String: Optional[str]
        DecimalOperator: Optional[DecimalOperator]
        Decimal: Optional[Decimal]
        BooleanOperator: Optional[BooleanOperator]
        ObjectOperator: Optional[ObjectOperator]
        Object: Optional[Object]
        DateOperator: Optional[DateOperator]
        StartDate: Optional[date]
        EndDate: Optional[date]
    Name: Optional[str]
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Select: Optional[List[SelectElement]]
    HasWhere: Optional[bool]
    Where: Optional[List[WhereElement]]
    HasOrderBy: Optional[bool]
    OrderBy: Optional[List[OrderByElement]]
    HasGroupBy: Optional[bool]
    GroupBy: Optional[List[GroupByElement]]
    GroupsToCollapse: Optional[bool]


class DateAndNumberFormat(Object):
    Key = UUID("a56e89d1-7bee-4509-8b84-c9ebc3808b0c")
    class NumberFormatParts(BaseModel):
        DecimalSeparator: Optional[str]
        GroupSeparator: Optional[str]
        GroupSizes: Optional[List[int]]
    DateFormat: Optional[str]
    TimeFormat: Optional[str]
    FirstDayOfWeek: Optional[enums.FirstDayOfWeek]
    NumberFormat: Optional[str]


class DateCustomField(Object):
    Guid: ClassVar[UUID] = "6c564f4c-380c-432e-af3b-2d6514c1891c"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[CustomFieldsAttribute]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]


class DebitNote(Object):
    Guid: ClassVar[UUID] = "274fc6d0-2eac-43d0-8286-79c856e644aa"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        Account: Optional[IPurchaseInvoiceAccount]
        BillableExpenseCustomer: Optional[Customer]
        BillableExpenseSalesInvoice: Optional[SalesInvoice]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        Employee: Optional[Employee]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        PurchaseUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    IssueDate: Optional[date]
    Reference: Optional[str]
    Supplier: Optional[Supplier]
    PurchaseInvoice: Optional[PurchaseInvoice]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    PurchaseInventoryLocation: Optional[InventoryLocation]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    HasDebitNoteCustomTheme: Optional[bool]
    DebitNoteCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasDebitNoteFooters: Optional[bool]
    DebitNoteFooters: Optional[List[DebitNoteFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class DebitNoteFooter(Object):
    Guid: ClassVar[UUID] = "ae399a2e-95c0-4ef5-a32d-5cd8217d885a"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class DeliveryNote(Object):
    Guid: ClassVar[UUID] = "a0f6a539-f6a4-4a38-a69a-546a608a1f6d"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
    DeliveryDate: Optional[date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    InvoiceNumber: Optional[str]
    InventoryLocation: Optional[InventoryLocation]
    Customer: Optional[Customer]
    SalesOrder: Optional[SalesOrder]
    SalesInvoice: Optional[SalesInvoice]
    DeliveryAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    HasLineNumber: Optional[bool]
    CustomTitle: Optional[bool]
    DeliveryNoteCustomTitle: Optional[str]
    HasDeliveryNoteCustomTheme: Optional[bool]
    DeliveryNoteCustomTheme: Optional[Theme]
    HasDeliveryNoteFooters: Optional[bool]
    DeliveryNoteFooters: Optional[List[DeliveryNoteFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class DeliveryNoteColumns(Object):
    Guid: ClassVar[UUID] = "8e82c77b-b894-4df8-939d-9c6983eb58d4"
    class Column(BaseModel):
        Name: Optional[enums.DeliveryNoteColumns]
        CustomField: Optional[ICustomField]
        ClassicCustomField: Optional[CustomField]
    CustomColumns: Optional[bool]
    Columns: Optional[List[Column]]


class DeliveryNoteFooter(Object):
    Guid: ClassVar[UUID] = "fd737085-d270-4749-9274-7b458a2ec740"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class DepreciationCalculationWorksheet(Object):
    Guid: ClassVar[UUID] = "105604f5-5bc1-4bfa-a101-3c339c22989a"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class DepreciationEntry(Object):
    Guid: ClassVar[UUID] = "75cdc055-6dec-4381-bc40-b670366e6abc"
    class Line(BaseModel):
        FixedAsset: Optional[FixedAsset]
        Division: Optional[Division]
        Amount: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class Division(Object):
    Guid: ClassVar[UUID] = "cc7fc110-e3e4-4b3b-823d-86c4a4cdabbc"
    Name: Optional[str]
    Inactive: Optional[bool]


class DivisionExceptionReport(Object):
    Guid: ClassVar[UUID] = "0e7711f8-1db1-4bcd-ac91-020d74a06dab"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class EinvoiceMe(Object):
    Guid: ClassVar[UUID] = "12e0885e-65c0-4a5c-85d6-98b4b3865518"
    Enabled: Optional[bool]
    Authorization: Optional[str]
    LastSync: Optional[int]


class EmailSettings(Object):
    Key = UUID("a4ddb0e3-b207-4fee-aa01-f104b6c09932")
    SmtpServer: Optional[str]
    Port: Optional[SmtpPort]
    SmtpCredentials: Optional[str]
    EmailAddress: Optional[str]
    Password: Optional[str]
    SendCopy: Optional[bool]
    SendCopyEmail: Optional[str]
    ReceiveRepliesAtADifferentAddressThanYouSendFrom: Optional[bool]
    ReplyTo: Optional[str]
    DoNotVerifyTLSCertificate: Optional[bool]
    DoNotUseInternationalDeliveryFormat: Optional[bool]


class EmailTemplateForCreditNote(Object):
    Key = UUID("85bf4dd0-fd18-4d03-b106-460839d2e3f7")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForCustomerStatement(Object):
    Key = UUID("aacecb53-f501-4db7-9879-f03d3304e08a")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForDebitNote(Object):
    Key = UUID("252d164a-90fc-45a3-bd35-b84f6d08d3e2")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForDeliveryNote(Object):
    Key = UUID("4768f2b1-4388-4cc3-ac50-c00284434dd6")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPayment(Object):
    Key = UUID("fe8baa5b-5737-4852-b520-cb9a590f3a94")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPayslip(Object):
    Key = UUID("61648ae7-4613-459a-aca6-9913928f776f")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPurchaseInvoice(Object):
    Key = UUID("21129fc9-26db-4cab-a70b-b42802f7017d")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPurchaseOrder(Object):
    Key = UUID("a45a2ffe-2c07-4564-8a98-431032a3387f")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPurchaseQuote(Object):
    Key = UUID("ff22d093-a191-47eb-acad-4ed0b439dc43")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForReceipt(Object):
    Key = UUID("b5d1faec-e726-4700-8666-8197b8681984")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForSalesInvoice(Object):
    Key = UUID("48279506-e1bc-4011-bb47-97c0336401a0")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForSalesOrder(Object):
    Key = UUID("3087728d-7fd5-42a4-b92c-8c0a4c87ab0c")
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForSalesQuote(Object):
    Key = UUID("cc707d1f-5a8d-43f1-84a4-22732fb0ccd6")
    Subject: Optional[str]
    MessageBody: Optional[str]


class Employee(Object):
    Guid: ClassVar[UUID] = "dadb7f95-a5dd-45c0-945d-6ad4ee28776e"
    Name: Optional[str]
    Code: Optional[str]
    Address: Optional[str]
    Email: Optional[str]
    Currency: Optional[ForeignCurrency]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForEmployees]
    StartingBalance: Optional[StartingBalanceType]
    StartingBalanceAmount: Optional[Decimal]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    Inactive: Optional[bool]


class EmployeeEmailField(Object):
    Key = UUID("f66ab672-c1c6-4280-9439-bdb0a72b7619")


class EmployeeNameField(Object):
    Key = UUID("db71c44c-ec5a-4701-aa54-67ada72aff1a")


class EmployeeSummary(Object):
    Guid: ClassVar[UUID] = "e7b3a4f4-35d7-4f92-a8fc-e9eadbc140a8"
    Employee: Optional[Employee]
    FromDate: Optional[date]
    ToDate: Optional[date]
    ExcludeZeroBalances: Optional[bool]


class Equity(Object):
    Key = UUID("9275ff4c-4cff-41d0-b7b5-f31c783f03d8")
    Name: Optional[str]


class ExchangeRate(Object):
    Guid: ClassVar[UUID] = "14240c19-3d08-4fe6-94bb-6dd17c4bcda6"
    Date: Optional[date]
    Currency: Optional[ForeignCurrency]
    Type: Optional[ExchangeRateType]
    BaseRate: Optional[Decimal]
    CounterRate: Optional[Decimal]


class ExpenseClaim(Object):
    Guid: ClassVar[UUID] = "02572e0c-0167-4dbd-a392-08d8f67f3fe4"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        Account: Optional[IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[Customer]
        AccountsReceivableSalesInvoice: Optional[SalesInvoice]
        BillableExpenseCustomer: Optional[Customer]
        BillableExpenseSalesInvoice: Optional[SalesInvoice]
        AccountsPayableSupplier: Optional[Supplier]
        PurchaseInvoice: Optional[PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[Supplier]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        Employee: Optional[Employee]
        InventoryItem: Optional[InventoryItem]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        LineDescription: Optional[str]
        Qty: Optional[Decimal]
        PurchaseUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    Date: Optional[date]
    Reference: Optional[str]
    PaidBy: Optional[IExpenseClaimPayer]
    Payee: Optional[str]
    Currency: Optional[ForeignCurrency]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[InventoryLocation]
    AmountsIncludeTax: Optional[bool]
    HasLineDescription: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class ExpenseClaimsPayer(Object):
    Guid: ClassVar[UUID] = "563d7f9e-d64c-49ec-a938-e5531e72f4d8"
    Name: Optional[str]
    StartingBalance: Optional[StartingBalanceType]
    StartingBalanceAmount: Optional[Decimal]
    Division: Optional[Division]
    Inactive: Optional[bool]


class ExpenseClaimsSummary(Object):
    Guid: ClassVar[UUID] = "faa1756c-5aaf-4646-9f33-555e45e37efb"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class Extension(Object):
    Guid: ClassVar[UUID] = "9a8fc328-7553-469f-88ed-dc533f2160b2"
    Name: Optional[str]
    Script: Optional[str]
    Location: Optional[LocationType]
    CustomLocation: Optional[str]
    Inactive: Optional[bool]


class FixedAsset(Object):
    Guid: ClassVar[UUID] = "00082353-9fca-4ab4-91ae-20505479cbda"
    ItemCode: Optional[str]
    ItemName: Optional[str]
    DepreciationRate: Optional[Decimal]
    Description: Optional[str]
    Division: Optional[Division]
    ControlAccountForFixedAssets: Optional[ControlAccountForFixedAssets]
    ControlAccountForFixedAssetsAccumulatedDepreciation: Optional[ControlAccountForFixedAssetsAccumulatedDepreciation]
    StartingBalance: Optional[Decimal]
    StartingBalanceAccumulatedDepreciation: Optional[Decimal]
    CustomDepreciationExpenseAccount: Optional[bool]
    CustomDepreciationExpenseAccountSelection: Optional[ProfitAndLossStatementAccount]
    DisposedFixedAsset: Optional[bool]
    DisposalDate: Optional[date]
    CustomExpenseAccountForDisposal: Optional[ProfitAndLossStatementAccount]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class FixedAssetSummary(Object):
    Guid: ClassVar[UUID] = "0dbf7789-7a6f-4182-b641-6b8e561b4a9c"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class Folder(Object):
    Guid: ClassVar[UUID] = "5d6fae1e-ff34-4870-80e9-8a755842d46e"
    Description: Optional[str]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class Forecast(Object):
    Guid: ClassVar[UUID] = "821030a6-9820-4cba-8879-eda07853b9a6"
    class Line(BaseModel):
        Account: Optional[IJournalEntryAccount]
        Amount: Optional[Decimal]
    Date: Optional[date]
    Repeat: Optional[Repeat]
    Growth: Optional[Decimal]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    Inactive: Optional[bool]


class ForecastProfitAndLossStatement(Object):
    Guid: ClassVar[UUID] = "a513a0b4-24f2-49ac-a820-d116ab9d198a"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class ForeignCurrency(Object):
    Guid: ClassVar[UUID] = "6116531b-cb3d-4f85-b239-745972943a6b"
    Code: Optional[str]
    Name: Optional[str]
    Symbol: Optional[str]
    DecimalPlaces: Optional[int]
    StartingExchangeRate: Optional[Decimal]
    Inactive: Optional[bool]


class FreightInItem(Object):
    Key = UUID("3458c24f-2a5f-4dcf-9de7-7340b1463d9c")


class GeneralLedgerSummary(Object):
    Guid: ClassVar[UUID] = "6c1d3132-7978-45c8-a6e2-2387c7de46b0"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class GeneralLedgerTransactions(Object):
    Guid: ClassVar[UUID] = "a3283b79-76be-44b6-9639-fa22d9b63246"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    Account: Optional[IGeneralLedgerAccount]


class GoodsReceipt(Object):
    Guid: ClassVar[UUID] = "866217a4-f841-47de-a4e6-87152405c88d"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    InvoiceNumber: Optional[str]
    Supplier: Optional[Supplier]
    PurchaseOrder: Optional[PurchaseOrder]
    PurchaseInvoice: Optional[PurchaseInvoice]
    InventoryLocation: Optional[InventoryLocation]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    HasLineNumber: Optional[bool]
    HasGoodsReceiptCustomTheme: Optional[bool]
    GoodsReceiptCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    HasGoodsReceiptFooters: Optional[bool]
    GoodsReceiptFooters: Optional[List[GoodsReceiptFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class GoodsReceiptFooter(Object):
    Guid: ClassVar[UUID] = "6db45d4f-ef92-4cb8-916f-a7c8645384be"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class HideIfEmptyReportingCategory(Object):
    Key = UUID("c9d0844e-7628-4bf4-899c-155be1577983")


class IntangibleAsset(Object):
    Guid: ClassVar[UUID] = "94d5307e-4332-4545-ab1e-1528c9032b7d"
    ItemCode: Optional[str]
    ItemName: Optional[str]
    AmortizationRate: Optional[Decimal]
    Description: Optional[str]
    Division: Optional[Division]
    ControlAccountForIntangibleAssets: Optional[ControlAccountForIntangibleAssets]
    ControlAccountForIntangibleAssetsAccumulatedAmortization: Optional[ControlAccountForIntangibleAssetsAccumulatedAmortization]
    StartingBalance: Optional[Decimal]
    StartingBalanceAccumulatedAmortization: Optional[Decimal]
    CustomAmortizationExpenseAccount: Optional[bool]
    CustomAmortizationExpenseAccountSelection: Optional[ProfitAndLossStatementAccount]
    DisposedIntangibleAsset: Optional[bool]
    DisposalDate: Optional[date]
    CustomExpenseAccountForDisposal: Optional[ProfitAndLossStatementAccount]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class IntangibleAssetSummary(Object):
    Guid: ClassVar[UUID] = "d76b3a1a-bb37-4767-9f65-f0389ec9d5df"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class InterAccountTransfer(Object):
    Guid: ClassVar[UUID] = "dea4f923-c498-4504-b3ef-30be3c33175e"
    Date: Optional[date]
    Reference: Optional[str]
    description: Optional[str]
    paidFrom: Optional[IBankOrCashAccount]
    CreditAmount: Optional[Decimal]
    CreditClearStatus: Optional[BankAccountClearStatus]
    CreditClearDate: Optional[date]
    receivedIn: Optional[IBankOrCashAccount]
    DebitAmount: Optional[Decimal]
    DebitClearStatus: Optional[BankAccountClearStatus]
    DebitClearDate: Optional[date]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    AutomaticReference: Optional[bool]
    HasInterAccountTransferFooters: Optional[bool]
    InterAccountTransferFooters: Optional[List[InterAccountTransferFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class InterAccountTransferFooter(Object):
    Guid: ClassVar[UUID] = "12479269-1209-4684-8d6a-ccc7a447fd62"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class InternalPdfGenerator(Object):
    Key = UUID("7e9fe6d7-d3a4-4456-981f-8112184b5517")
    Enabled: Optional[bool]
    PageSize: Optional[PageSize]


class InventoryItem(Object):
    Guid: ClassVar[UUID] = "0dbdbf8a-d80c-48e6-b453-bb7862445b7c"
    class StartingBalanceQuantity(BaseModel):
        Qty: Optional[Decimal]
        InventoryLocation: Optional[InventoryLocation]
    ItemCode: Optional[str]
    ItemName: Optional[str]
    UnitName: Optional[str]
    ProductionStage: Optional[int]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForInventoryItems]
    StartingBalance: Optional[List[StartingBalanceQuantity]]
    StartingBalanceAverageCost: Optional[Decimal]
    TrackQuantityToReceive: Optional[bool]
    TrackQuantityToDeliver: Optional[bool]
    CustomIncomeAccount: Optional[bool]
    IncomeAccount: Optional[ProfitAndLossStatementAccount]
    CustomExpenseAccount: Optional[bool]
    ExpenseAccount: Optional[ProfitAndLossStatementAccount]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[Decimal]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[Decimal]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[Division]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultQty: Optional[bool]


class InventoryKit(Object):
    Guid: ClassVar[UUID] = "efc4f2cc-acf0-4815-a9a8-13bae00c6167"
    class Item(BaseModel):
        InventoryItem: Optional[InventoryItem]
        Qty: Optional[Decimal]
    ItemCode: Optional[str]
    ItemName: Optional[str]
    UnitName: Optional[str]
    BillOfMaterials: Optional[List[Item]]
    Division: Optional[Division]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[Decimal]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[Division]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    CustomIncomeAccount: Optional[bool]
    IncomeAccount: Optional[ProfitAndLossStatementAccount]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class InventoryLocation(Object):
    Guid: ClassVar[UUID] = "fae8151d-252e-45e3-b1f4-e048075b8983"
    Name: Optional[str]
    Inactive: Optional[bool]


class InventoryPriceList(Object):
    Guid: ClassVar[UUID] = "14da35e1-9b94-4403-8575-9d64ade4d7b4"
    Name: Optional[str]
    FilterByCustomField: Optional[bool]
    CustomField: Optional[CustomField]
    Filter: Optional[str]


class InventoryProfitMargin(Object):
    Guid: ClassVar[UUID] = "796da7cf-3551-4ff4-afad-942d4fc750cc"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]


class InventoryQuantityByLocation(Object):
    Guid: ClassVar[UUID] = "0e50586b-d1d0-40a3-81eb-8b6602e3050b"
    Date: Optional[date]
    Description: Optional[str]
    CustomInventoryLocations: Optional[bool]
    InventoryLocations: Optional[List[InventoryLocation]]


class InventoryQuantityMovement(Object):
    Guid: ClassVar[UUID] = "bd9e1f26-91e4-4c7b-b410-a62cb966bcfc"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    ExcludeItemsWithNoMovement: Optional[bool]


class InventoryTransfer(Object):
    Guid: ClassVar[UUID] = "7eaafddc-54c9-4235-98d2-e8a1ee438150"
    class Line(BaseModel):
        Item: Optional[InventoryItem]
        LineDescription: Optional[str]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    InventoryLocation: Optional[InventoryLocation]
    ToInventoryLocation: Optional[InventoryLocation]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    CustomFields: Optional[Dict[CustomField, str]]
    AutomaticReference: Optional[bool]
    CustomFields2: Optional[CustomFields]


class InventoryValueSummary(Object):
    Guid: ClassVar[UUID] = "7e9405f2-ed99-4891-8757-5c4c23cabdb2"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    ExcludeItemsWithNoMovement: Optional[bool]


class InventoryWriteOff(Object):
    Guid: ClassVar[UUID] = "d7ff6694-f1ef-419f-8ae2-55527a02e95f"
    class Item(BaseModel):
        InventoryItem: Optional[InventoryItem]
        Qty: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    InventoryLocation: Optional[InventoryLocation]
    Items: Optional[List[Item]]
    Allocation: Optional[IInventoryWriteOffAccount]
    FixedAsset: Optional[FixedAsset]
    TaxCode: Optional[TaxCode]
    Project: Optional[Project]
    Division: Optional[Division]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class Investment(Object):
    Guid: ClassVar[UUID] = "a8f95068-fc73-43f7-aabb-fd868e506b51"
    Code: Optional[str]
    Name: Optional[str]
    ControlAccount: Optional[ControlAccountForInvestments]
    MarketPrice: Optional[Decimal]
    StartingBalance: Optional[Decimal]
    StartingBalanceTotalCost: Optional[Decimal]
    Inactive: Optional[bool]


class JournalEntry(Object):
    Guid: ClassVar[UUID] = "5ea52bc4-90ae-4e4a-aec4-ef1224b279ad"
    class Line(BaseModel):
        Account: Optional[IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[Customer]
        AccountsReceivableSalesInvoice: Optional[SalesInvoice]
        BillableExpenseCustomer: Optional[Customer]
        BillableExpenseSalesInvoice: Optional[SalesInvoice]
        AccountsPayableSupplier: Optional[Supplier]
        PurchaseInvoice: Optional[PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[Supplier]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        Employee: Optional[Employee]
        InventoryItem: Optional[InventoryItem]
        InventoryLocation: Optional[InventoryLocation]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        ExpenseClaimPayer: Optional[ExpenseClaimsPayer]
        Investment: Optional[Investment]
        LineDescription: Optional[str]
        Qty: Optional[Decimal]
        Debit: Optional[Decimal]
        Credit: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    Date: Optional[date]
    Reference: Optional[str]
    Currency: Optional[ForeignCurrency]
    Narration: Optional[str]
    Lines: Optional[List[Line]]
    ForTaxPurposesThisIs: Optional[TaxTransactionType]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    HasJournalEntryFooters: Optional[bool]
    JournalEntryFooters: Optional[List[JournalEntryFooter]]
    CashTransactionForCashFlowStatementPurposes: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class JournalEntryFooter(Object):
    Guid: ClassVar[UUID] = "5be035ca-d96b-4e8d-b963-53340cf7f4f8"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class LatePaymentFee(Object):
    Guid: ClassVar[UUID] = "4dada073-022f-464e-bdb3-ff38c83e577f"
    Date: Optional[date]
    Customer: Optional[Customer]
    SalesInvoice: Optional[SalesInvoice]
    Amount: Optional[Decimal]


class Liabilities(Object):
    Key = UUID("ed5a19f6-12c5-45cc-b4b7-4e79f7ef50bc")


class LockDate(Object):
    Key = UUID("4c5dac8f-2d5e-4634-a51b-0bbdd021a499")
    LockAccountingPeriods: Optional[bool]
    Date: Optional[date]


class MemberInfo(Object):
    Key: Optional[str]


class MultipleValueCustomField(Object):
    Guid: ClassVar[UUID] = "f32774a9-f740-4c2b-8353-b321576f6166"
    class Option(BaseModel):
        Value: Optional[str]
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[CustomFieldsAttribute]]
    Options: Optional[List[Option]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]


class NamedObject(Object):
    pass


class NonInventoryItem(Object):
    Guid: ClassVar[UUID] = "7affe9ee-731f-4936-8acf-15cae7bcacee"
    Code: Optional[str]
    Name: Optional[str]
    UnitName: Optional[str]
    WhenSold: Optional[INonInventoryItemAccount]
    WhenPurchased: Optional[INonInventoryItemAccount]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[Decimal]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[Decimal]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[Division]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultQty: Optional[bool]


class NumberCustomField(Object):
    Guid: ClassVar[UUID] = "68e09438-7aa1-4d63-b7d3-ce2dcd052e88"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[CustomFieldsAttribute]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    HideTotalAmount: Optional[bool]
    Inactive: Optional[bool]


class Object(Object):
    pass


class Payment(Object):
    Guid: ClassVar[UUID] = "79f99d26-e43a-4ecb-a9c9-0774601a9b2e"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        Account: Optional[IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[Customer]
        AccountsReceivableSalesInvoice: Optional[SalesInvoice]
        BillableExpenseCustomer: Optional[Customer]
        BillableExpenseSalesInvoice: Optional[SalesInvoice]
        AccountsPayableSupplier: Optional[Supplier]
        PurchaseInvoice: Optional[PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[Supplier]
        Employee: Optional[Employee]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        ExpenseClaimsPayer: Optional[ExpenseClaimsPayer]
        Investment: Optional[Investment]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        PurchaseUnitPrice: Optional[Decimal]
        Amount: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    Date: Optional[date]
    Reference: Optional[str]
    PaidFrom: Optional[IBankOrCashAccount]
    Cleared: Optional[BankAccountClearStatus]
    BankClearDate: Optional[date]
    Payee: Optional[PayerPayeeType]
    Customer: Optional[Customer]
    Supplier: Optional[Supplier]
    Contact: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    FixedTotal: Optional[bool]
    FixedTotalAmount: Optional[Decimal]
    CustomTheme: Optional[bool]
    PaymentCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    PaymentCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPaymentFooters: Optional[bool]
    PaymentFooters: Optional[List[PaymentFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PaymentFooter(Object):
    Guid: ClassVar[UUID] = "6fbe0380-de89-4351-b5ac-eda06b5e7a80"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PaymentRule(Object):
    Guid: ClassVar[UUID] = "71ac4a94-6a53-4c0a-990c-e8174ab398d1"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        Account: Optional[IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[Customer]
        BillableExpenseCustomer: Optional[Customer]
        AccountsPayableSupplier: Optional[Supplier]
        WithholdingTaxPayableSupplier: Optional[Supplier]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        Employee: Optional[Employee]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        ExpenseClaimsPayer: Optional[ExpenseClaimsPayer]
        Investment: Optional[Investment]
        Description: Optional[str]
        Qty: Optional[Decimal]
        Amount: Optional[DiscountType]
        ExactAmount: Optional[Decimal]
        Percentage: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Division: Optional[Division]
    class Condition(BaseModel):
        AndDescriptionContains: Optional[str]
    IfBankAccountIs: Optional[BankOrCashAccount]
    AndAmountIs: Optional[AmountType]
    AndAmountIsAmount: Optional[Decimal]
    Conditions: Optional[List[Condition]]
    Payee: Optional[PayerPayeeType]
    Customer: Optional[Customer]
    Supplier: Optional[Supplier]
    OtherContact: Optional[str]
    Lines: Optional[List[Line]]
    DescriptionColumn: Optional[bool]
    QuantityColumn: Optional[bool]


class Payslip(Object):
    Guid: ClassVar[UUID] = "1d103fa7-6fc1-4951-811e-972968b842cc"
    class Earned(BaseModel):
        Item: Optional[PayslipEarningsItem]
        Description: Optional[str]
        Units: Optional[Decimal]
        UnitPrice: Optional[Decimal]
        Division: Optional[Division]
    class Deduction(BaseModel):
        Item: Optional[PayslipDeductionItem]
        Description: Optional[str]
        DeductionAmount: Optional[Decimal]
        Division: Optional[Division]
    class Contribution(BaseModel):
        Item: Optional[PayslipContributionItem]
        Description: Optional[str]
        ContributionAmount: Optional[Decimal]
        Division: Optional[Division]
    Date: Optional[date]
    Reference: Optional[str]
    description: Optional[str]
    employee: Optional[Employee]
    Earnings: Optional[List[Earned]]
    Deductions: Optional[List[Deduction]]
    Contributions: Optional[List[Contribution]]
    ShowTotalsForThePeriod: Optional[bool]
    TotalsPeriodStart: Optional[date]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    AutomaticReference: Optional[bool]
    HasPayslipFooters: Optional[bool]
    PayslipFooters: Optional[List[PayslipFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PayslipContributionItem(Object):
    Guid: ClassVar[UUID] = "73af4c68-c347-4088-8846-758f1e7bc5bb"
    Name: Optional[str]
    ExpenseAccount: Optional[ProfitAndLossStatementAccount]
    LiabilityAccount: Optional[BalanceSheetAccount]
    ReportingCategory: Optional[PayslipContributionItemReportingCategory]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PayslipContributionItemReportingCategory(Object):
    Guid: ClassVar[UUID] = "ad4c002b-f4ea-4bf5-85cc-f65dd4398794"
    Name: Optional[str]
    Inactive: Optional[bool]


class PayslipDeductionItem(Object):
    Guid: ClassVar[UUID] = "0444eb18-6fc5-4d1f-be8b-c114da01832c"
    Name: Optional[str]
    Account: Optional[ICustomGeneralLedgerAccount]
    ReportingCategory: Optional[PayslipDeductionItemReportingCategory]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PayslipDeductionItemReportingCategory(Object):
    Guid: ClassVar[UUID] = "1ccb2c74-e9ed-4642-9687-bdf9f3403f3b"
    Name: Optional[str]
    Inactive: Optional[bool]


class PayslipEarningsItem(Object):
    Guid: ClassVar[UUID] = "ab02f6ab-c91c-4fc2-b979-66a6682c200e"
    Name: Optional[str]
    ExpenseAccount: Optional[ProfitAndLossStatementAccount]
    ReportingCategory: Optional[PayslipEarningsItemReportingCategory]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PayslipEarningsItemReportingCategory(Object):
    Guid: ClassVar[UUID] = "3de1fae6-48ea-4901-8e1b-507483bfc4f3"
    Name: Optional[str]
    Inactive: Optional[bool]


class PayslipFooter(Object):
    Guid: ClassVar[UUID] = "9c4197b6-212a-4c22-9338-6eaa659cfe49"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PayslipSummary(Object):
    Guid: ClassVar[UUID] = "3278903e-bf63-4f6f-b04d-a9e5ebd5a055"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]


class PayslipTotalsPerItemAndEmployee(Object):
    Guid: ClassVar[UUID] = "13de6e5f-cacf-46a1-adb9-2250f76d77dd"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class ProductionOrder(Object):
    Guid: ClassVar[UUID] = "da996523-e77e-493c-b134-31c6c6ccae4a"
    class Item(BaseModel):
        BillOfMaterials: Optional[InventoryItem]
        Qty: Optional[Decimal]
    class ExpenseItem(BaseModel):
        Account: Optional[ICustomGeneralLedgerAccount]
        Amount: Optional[Decimal]
        Division: Optional[Division]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    FinishedInventoryItem: Optional[InventoryItem]
    Qty: Optional[Decimal]
    BillOfMaterials: Optional[List[Item]]
    InventoryLocation: Optional[InventoryLocation]
    AddNonInventoryCostIntoProduction: Optional[bool]
    ExpenseItems: Optional[List[ExpenseItem]]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class ProfitAndLossStatement(Object):
    Guid: ClassVar[UUID] = "165c0392-9aad-4067-b855-a2393ead5df4"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        Division: Optional[Division]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    AccountingMethod: Optional[AccountingBasis]
    Rounding: Optional[Rounding]
    GroupsToCollapse: Optional[List[ProfitAndLossStatementGroup]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class ProfitAndLossStatementAccount(Object):
    Guid: ClassVar[UUID] = "26b9e4a5-ce10-4f30-94c7-23a1ca4428f9"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[CashFlowStatementInvestingActivityGroup]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    Position: Optional[int]
    Inactive: Optional[bool]


class ProfitAndLossStatementAccountBillableExpensesCost(Object):
    Key = UUID("234d263d-cf0e-4e3e-85ca-ef899016e58a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableExpensesInvoiced(Object):
    Key = UUID("1ae41f36-c83a-428c-be23-a99714110807")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableTimeInvoiced(Object):
    Key = UUID("8d86390b-b90f-4cf6-862b-9b4050449b91")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableTimeMovement(Object):
    Key = UUID("03d41bd1-8dd4-4ce3-9b82-5ce17a40171a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountCurrencyGainsLosses(Object):
    Key = UUID("635ddd64-1176-4d35-b1c2-2d7d3bb12bb6")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    CashFlowStatementGroup: Optional[CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountFixedAssetDepreciation(Object):
    Key = UUID("fb6fdbfd-b39f-4674-8928-10c2bdd87e58")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountFixedAssetLossOnDisposal(Object):
    Key = UUID("428ea9ba-4679-4568-b05b-7fcf62504893")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal(Object):
    Key = UUID("43e14984-202e-4e9e-b843-d417dddcd3d2")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountIntangibleAssetsAmortization(Object):
    Key = UUID("83d56444-fed8-4de8-8e58-e325a370ae44")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountInventoryPurchases(Object):
    Key = UUID("aa80b662-3642-4c08-b328-2fccf132ceb1")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountInventorySales(Object):
    Key = UUID("ea44f579-9548-4954-baf0-48538aceff1e")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[TaxCode]
    Position: Optional[int]


class ProfitAndLossStatementAccountLatePaymentFees(Object):
    Key = UUID("841b2acb-8bb5-4742-864e-4226fa421f44")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountRoundingExpense(Object):
    Key = UUID("2aa99eac-faca-4017-a157-edbbbcb160ac")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementActualVsBudget(Object):
    Guid: ClassVar[UUID] = "25c7aa0e-536c-42be-a75c-1b5ac71e955a"
    class BudgetItem(BaseModel):
        Account: Optional[IProfitAndLossAccount]
        Amount: Optional[Decimal]
    Title: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Division: Optional[Division]
    Lines: Optional[List[BudgetItem]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    RoundDecimals: Optional[bool]


class ProfitAndLossStatementCapitalGainsOnInvestments(Object):
    Key = UUID("de8d014f-e862-4ab5-88cc-335d464315a6")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementGroup(Object):
    Guid: ClassVar[UUID] = "5770616c-0e01-46ca-a172-f7042275da6c"
    Name: Optional[str]
    Type: Optional[ProfitAndLossStatementGroupType]
    ParentGroup: Optional[ProfitAndLossStatementGroup]
    Position: Optional[int]


class Project(Object):
    Guid: ClassVar[UUID] = "5170f738-cfba-42e3-bb8e-a7d5c5ab66f2"
    Name: Optional[str]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PurchaseInvoice(Object):
    Guid: ClassVar[UUID] = "58b9eb90-f6b8-4abc-8ea1-12fd77b8336e"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        Account: Optional[IPurchaseInvoiceAccount]
        BillableExpenseCustomer: Optional[Customer]
        BillableExpenseSalesInvoice: Optional[SalesInvoice]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        Employee: Optional[Employee]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        PurchaseUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    IssueDate: Optional[date]
    DueDate: Optional[DueDateType]
    DueDateDays: Optional[int]
    DueDateDate: Optional[date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    Supplier: Optional[Supplier]
    PurchaseQuote: Optional[PurchaseQuote]
    PurchaseOrder: Optional[PurchaseOrder]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    PurchaseInventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsIncludeTax: Optional[bool]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    HasPurchaseInvoiceCustomTheme: Optional[bool]
    PurchaseInvoiceCustomTheme: Optional[Theme]
    HideBalanceDue: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseInvoiceFooters: Optional[bool]
    PurchaseInvoiceFooters: Optional[List[PurchaseInvoiceFooter]]
    ClosedInvoice: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PurchaseInvoiceFooter(Object):
    Guid: ClassVar[UUID] = "06205221-f856-402f-8df9-104942cf579a"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PurchaseOrder(Object):
    Guid: ClassVar[UUID] = "a26bbea1-57aa-4fd9-b7c9-e26b83114385"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        PurchaseUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
    Date: Optional[date]
    Reference: Optional[str]
    Supplier: Optional[Supplier]
    PurchaseQuote: Optional[PurchaseQuote]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    TrackQuantityToReceive: Optional[bool]
    HasPurchaseOrderCustomTheme: Optional[bool]
    PurchaseOrderCustomTheme: Optional[Theme]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseOrderFooters: Optional[bool]
    PurchaseOrderFooters: Optional[List[PurchaseOrderFooter]]
    Cancelled: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class PurchaseOrderFooter(Object):
    Guid: ClassVar[UUID] = "38104c9e-7805-47de-935e-f6b660a470de"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PurchaseQuote(Object):
    Guid: ClassVar[UUID] = "38d606f7-6358-4ace-9d1d-f6c0b9ea9d68"
    class Line(BaseModel):
        Item: Optional[IPurchaseItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        PurchaseUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
    Date: Optional[date]
    Reference: Optional[str]
    Supplier: Optional[Supplier]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    RequestForQuotation: Optional[bool]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    HasPurchaseQuoteCustomTheme: Optional[bool]
    PurchaseQuoteCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    Cancelled: Optional[bool]
    CustomTitle: Optional[bool]
    PurchaseQuoteCustomTitle: Optional[str]
    RequestForQuotationCustomTitleOption: Optional[bool]
    RequestForQuotationCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseQuoteFooters: Optional[bool]
    PurchaseQuoteFooters: Optional[List[PurchaseQuoteFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class PurchaseQuoteFooter(Object):
    Guid: ClassVar[UUID] = "072dd522-a137-4e91-8966-93f56f987cda"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Receipt(Object):
    Guid: ClassVar[UUID] = "7662b887-c8d8-486e-98fd-f9dbcd41c6dc"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        Account: Optional[IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[Customer]
        AccountsReceivableSalesInvoice: Optional[SalesInvoice]
        BillableExpenseCustomer: Optional[Customer]
        BillableExpenseSalesInvoice: Optional[SalesInvoice]
        AccountsPayableSupplier: Optional[Supplier]
        PurchaseInvoice: Optional[PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[Supplier]
        Employee: Optional[Employee]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        ExpenseClaimsPayer: Optional[ExpenseClaimsPayer]
        Investment: Optional[Investment]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        SalesUnitPrice: Optional[Decimal]
        Amount: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    Date: Optional[date]
    Reference: Optional[str]
    PaidBy: Optional[PayerPayeeType]
    Customer: Optional[Customer]
    Supplier: Optional[Supplier]
    Contact: Optional[str]
    ReceivedIn: Optional[IBankOrCashAccount]
    Cleared: Optional[BankAccountClearStatus]
    BankClearDate: Optional[date]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    FixedTotal: Optional[bool]
    FixedTotalAmount: Optional[Decimal]
    CustomTheme: Optional[bool]
    ReceiptCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    ReceiptCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasReceiptFooters: Optional[bool]
    ReceiptFooters: Optional[List[ReceiptFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class ReceiptColumns(Object):
    Guid: ClassVar[UUID] = "ab9df426-967c-4851-92e8-d45e3188fc9c"
    Columns: Optional[List[Column]]


class ReceiptFooter(Object):
    Guid: ClassVar[UUID] = "b4053b7c-b07a-45ba-aa14-1e3a624f8565"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class ReceiptRule(Object):
    Guid: ClassVar[UUID] = "72ed576f-e78b-41eb-8188-73285f32c2d2"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        Account: Optional[IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[Customer]
        BillableExpenseCustomer: Optional[Customer]
        AccountsPayableSupplier: Optional[Supplier]
        WithholdingTaxPayableSupplier: Optional[Supplier]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        Employee: Optional[Employee]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        ExpenseClaimsPayer: Optional[ExpenseClaimsPayer]
        Investment: Optional[Investment]
        Description: Optional[str]
        Qty: Optional[Decimal]
        Amount: Optional[DiscountType]
        ExactAmount: Optional[Decimal]
        Percentage: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Division: Optional[Division]
    class Condition(BaseModel):
        AndDescriptionContains: Optional[str]
    IfBankAccountIs: Optional[BankOrCashAccount]
    AndAmountIs: Optional[AmountType]
    AndAmountIsAmount: Optional[Decimal]
    Conditions: Optional[List[Condition]]
    PaidBy: Optional[PayerPayeeType]
    Customer: Optional[Customer]
    Supplier: Optional[Supplier]
    OtherContact: Optional[str]
    Lines: Optional[List[Line]]
    DescriptionColumn: Optional[bool]
    QuantityColumn: Optional[bool]


class ReceiptsAndPaymentsSummary(Object):
    Guid: ClassVar[UUID] = "fa775461-39a2-46a2-b022-adcad6c9b830"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    AccountCodes: Optional[bool]


class RecurringInterAccountTransfer(Object):
    Guid: ClassVar[UUID] = "10ac4ab8-df74-4faf-b7fc-eb343556fb1b"
    nextIssueDate: Optional[date]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    description: Optional[str]
    paidFrom: Optional[IBankOrCashAccount]
    CreditAmount: Optional[Decimal]
    CreditClearStatus: Optional[BankAccountClearStatus]
    CreditClearDate: Optional[date]
    receivedIn: Optional[IBankOrCashAccount]
    DebitAmount: Optional[Decimal]
    DebitClearStatus: Optional[BankAccountClearStatus]
    DebitClearDate: Optional[date]
    AutomaticReference: Optional[bool]
    HasInterAccountTransferFooters: Optional[bool]
    InterAccountTransferFooters: Optional[List[InterAccountTransferFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringJournalEntry(Object):
    Guid: ClassVar[UUID] = "b4c1b390-351e-4579-b43b-412b920cddaf"
    NextIssueDate: Optional[date]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    Currency: Optional[ForeignCurrency]
    Narration: Optional[str]
    Lines: Optional[List[JournalEntry.Line]]
    InventoryLocation: Optional[InventoryLocation]
    ForTaxPurposesThisIs: Optional[TaxTransactionType]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    HasJournalEntryFooters: Optional[bool]
    JournalEntryFooters: Optional[List[JournalEntryFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringPayment(Object):
    Guid: ClassVar[UUID] = "789d22dc-bc42-4952-a591-60123b344726"
    NextIssueDate: Optional[date]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    PaidFrom: Optional[IBankOrCashAccount]
    Cleared: Optional[BankAccountClearStatus]
    Payee: Optional[PayerPayeeType]
    Customer: Optional[Customer]
    Supplier: Optional[Supplier]
    Contact: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Payment.Line]]
    InventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    PaymentCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPaymentFooters: Optional[bool]
    PaymentFooters: Optional[List[PaymentFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringPayslip(Object):
    Guid: ClassVar[UUID] = "ae6e14e3-1d3d-4996-b466-ba41732a8dbe"
    nextIssueDate: Optional[date]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    employee: Optional[Employee]
    description: Optional[str]
    Earnings: Optional[List[Payslip.Earned]]
    Deductions: Optional[List[Payslip.Deduction]]
    Contributions: Optional[List[Payslip.Contribution]]
    ShowTotalsForThePeriod: Optional[bool]
    TotalsPeriodStart: Optional[date]
    CustomTheme: Optional[bool]
    Theme: Optional[Theme]
    HasPayslipFooters: Optional[bool]
    PayslipFooters: Optional[List[PayslipFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    NextIssueDate: Optional[date]


class RecurringPurchaseInvoice(Object):
    Guid: ClassVar[UUID] = "11de04ac-c448-4665-b206-8aa631e63532"
    NextIssueDate: Optional[date]
    DueDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    Supplier: Optional[Supplier]
    PurchaseOrder: Optional[PurchaseOrder]
    Description: Optional[str]
    Lines: Optional[List[PurchaseInvoice.Line]]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    AmountsIncludeTax: Optional[bool]
    AutomaticReference: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    HasPurchaseInvoiceCustomTheme: Optional[bool]
    PurchaseInvoiceCustomTheme: Optional[Theme]
    HasPurchaseInvoiceFooters: Optional[bool]
    PurchaseInvoiceFooters: Optional[List[PurchaseInvoiceFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringPurchaseOrder(Object):
    Guid: ClassVar[UUID] = "3be38758-7bf2-46f1-84a5-34e8748cade0"
    NextIssueDate: Optional[date]
    DueDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    Supplier: Optional[Supplier]
    Description: Optional[str]
    Lines: Optional[List[PurchaseOrder.Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    TrackQuantityToReceive: Optional[bool]
    HasPurchaseOrderCustomTheme: Optional[bool]
    PurchaseOrderCustomTheme: Optional[Theme]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseOrderFooters: Optional[bool]
    PurchaseOrderFooters: Optional[List[PurchaseOrderFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringReceipt(Object):
    Guid: ClassVar[UUID] = "1c7ecd01-eb32-47b1-8ccd-e85f77969b03"
    NextIssueDate: Optional[date]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    PaidBy: Optional[PayerPayeeType]
    Customer: Optional[Customer]
    Supplier: Optional[Supplier]
    Contact: Optional[str]
    ReceivedIn: Optional[IBankOrCashAccount]
    Cleared: Optional[BankAccountClearStatus]
    Description: Optional[str]
    Lines: Optional[List[Receipt.Line]]
    InventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    ReceiptCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasReceiptFooters: Optional[bool]
    ReceiptFooters: Optional[List[ReceiptFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringSalesInvoice(Object):
    Guid: ClassVar[UUID] = "81385989-81e5-48c7-a819-c344324c1c01"
    NextIssueDate: Optional[date]
    DueDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    Customer: Optional[Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[SalesInvoice.Line]]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[RoundingMethod]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxRate: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    HasSalesInvoiceCustomTheme: Optional[bool]
    SalesInvoiceCustomTheme: Optional[Theme]
    EarlyPaymentDiscount: Optional[bool]
    EarlyPaymentDiscountType: Optional[DiscountType]
    EarlyPaymentDiscountRate: Optional[Decimal]
    EarlyPaymentDiscountAmount: Optional[Decimal]
    EarlyPaymentDiscountDays: Optional[int]
    LatePaymentFees: Optional[bool]
    LatePaymentFeesPercentage: Optional[Decimal]
    CustomTitle: Optional[bool]
    SalesInvoiceCustomTitle: Optional[str]
    TotalAmountInWords: Optional[bool]
    HideDueDate: Optional[bool]
    HasSalesInvoiceFooters: Optional[bool]
    SalesInvoiceFooters: Optional[List[SalesInvoiceFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringSalesOrder(Object):
    Guid: ClassVar[UUID] = "dd7d5b17-c4be-4369-b0f5-79361525f3c2"
    NextIssueDate: Optional[date]
    ExpiryDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    Customer: Optional[Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[SalesOrder.Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    TrackQuantityToDeliver: Optional[bool]
    HasSalesOrderCustomTheme: Optional[bool]
    SalesOrderCustomTheme: Optional[Theme]
    ShowTaxAmountColumn: Optional[bool]
    CustomTitle: Optional[bool]
    SalesOrderCustomTitle: Optional[str]
    HasSalesOrderFooters: Optional[bool]
    SalesOrderFooters: Optional[List[SalesOrderFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class RecurringSalesQuote(Object):
    Guid: ClassVar[UUID] = "1ca6ee3a-3583-41d8-83b1-74ac9129e1c1"
    NextIssueDate: Optional[date]
    ExpiryDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[date]
    Customer: Optional[Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[SalesQuote.Line]]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[RoundingMethod]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    HideTotalAmount: Optional[bool]
    HasSalesQuoteCustomTheme: Optional[bool]
    SalesQuoteCustomTheme: Optional[Theme]
    CustomTitle: Optional[bool]
    SalesQuoteCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesQuoteFooters: Optional[bool]
    SalesQuoteFooters: Optional[List[SalesQuoteFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class ReportTranformationFromDate(Object):
    Key = UUID("cef33379-d1b3-4172-b090-0fc24cf978da")


class ReportTranformationToDate(Object):
    Key = UUID("8ba7e5e7-8f74-443a-b7ee-d8539b12e7e2")


class ReportTransformation2(Object):
    Guid: ClassVar[UUID] = "02c3fbc6-4473-436f-b58d-fd51937f4e77"
    class Item(BaseModel):
        Name: Optional[str]
        Column1: Optional[List[IReportingCategory]]
        Column2: Optional[List[IReportingCategory]]
        Column3: Optional[List[IReportingCategory]]
        Column4: Optional[List[IReportingCategory]]
        Column5: Optional[List[IReportingCategory]]
    class InstructionStep(BaseModel):
        Text: Optional[str]
    Name: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    Employee: Optional[Employee]
    Columns: Optional[ColumnCount]
    Items2: Optional[List[Item]]
    AccountingMethod: Optional[bool]
    AccountingMethodOption: Optional[AccountingBasis]
    Suppliers: Optional[bool]
    SupplierCustomField: Optional[CustomField]
    SupplierCustomFieldValue: Optional[str]
    ForEachSupplier: Optional[List[Item]]
    Employees: Optional[bool]
    ForEachEmployee: Optional[List[Item]]
    Script: Optional[bool]
    CustomScript: Optional[str]
    Instructions: Optional[bool]
    InstructionLines: Optional[List[InstructionStep]]
    Published: Optional[bool]


class ReportTransformationFromDateLastJuly(Object):
    Key = UUID("7d3ddc8b-49f1-4064-997a-430367e54055")


class ReportTransformationLabel(Object):
    Guid: ClassVar[UUID] = "849c558a-5f58-4779-939b-dc9d2f5ac89f"
    Name: Optional[str]


class ReportTransformationNetAmounts(Object):
    Key = UUID("928f0950-d042-46fd-9ea8-b73c947a23b7")


class ReportTransformationReport(Object):
    Guid: ClassVar[UUID] = "bbe8c088-729b-4b56-a7d7-26555270eced"
    ReportTransformation: Optional[ReportTransformation2]
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Employee: Optional[Employee]


class ReportTransformationTaxAmounts(Object):
    Key = UUID("094377dd-1f71-40cf-bb48-58daf961aa71")


class ReportTransformationTaxPurchases(Object):
    Key = UUID("89c4e9b6-f555-4243-8432-680a1cc97a61")


class ReportTransformationTaxSales(Object):
    Key = UUID("211bb6c2-9ca7-4cda-a099-99bcde19a173")


class ReverseSignReportingCategory(Object):
    Key = UUID("0b3fe333-755b-42c0-b921-2835e39e50f0")


class RoundDownReportingCategory(Object):
    Key = UUID("0846abcd-dc2a-4914-9c9b-9d7130ac99d6")


class SalesInvoice(Object):
    Guid: ClassVar[UUID] = "ad12b60b-23bf-4421-94df-8be79cef533e"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        Account: Optional[ISalesInvoiceAccount]
        CapitalAccount: Optional[CapitalAccount]
        SubAccount: Optional[SubAccount]
        SpecialAccount: Optional[SpecialAccount]
        FixedAsset: Optional[FixedAsset]
        IntangibleAsset: Optional[IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        SalesUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
        Project: Optional[Project]
        Division: Optional[Division]
    IssueDate: Optional[date]
    DueDate: Optional[DueDateType]
    DueDateDays: Optional[int]
    DueDateDate: Optional[date]
    Reference: Optional[str]
    QuoteNumber: Optional[str]
    OrderNumber: Optional[str]
    Customer: Optional[Customer]
    SalesQuote: Optional[SalesQuote]
    SalesOrder: Optional[SalesOrder]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    SalesInventoryLocation: Optional[InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[RoundingMethod]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    EarlyPaymentDiscount: Optional[bool]
    EarlyPaymentDiscountType: Optional[DiscountType]
    EarlyPaymentDiscountRate: Optional[Decimal]
    EarlyPaymentDiscountAmount: Optional[Decimal]
    EarlyPaymentDiscountDays: Optional[int]
    LatePaymentFees: Optional[bool]
    LatePaymentFeesPercentage: Optional[Decimal]
    TotalAmountInWords: Optional[bool]
    TotalAmountInBaseCurrency: Optional[bool]
    Bilingual: Optional[bool]
    CustomTitle: Optional[bool]
    SalesInvoiceCustomTitle: Optional[str]
    HasSalesInvoiceCustomTheme: Optional[bool]
    SalesInvoiceCustomTheme: Optional[Theme]
    AutomaticReference: Optional[bool]
    HideDueDate: Optional[bool]
    HideBalanceDue: Optional[bool]
    ClosedInvoice: Optional[bool]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesInvoiceFooters: Optional[bool]
    SalesInvoiceFooters: Optional[List[SalesInvoiceFooter]]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class SalesInvoiceFooter(Object):
    Guid: ClassVar[UUID] = "eaaee0ba-9c58-4f7b-a800-2857f0a675af"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class SalesInvoiceTotalsByCustomer(Object):
    Guid: ClassVar[UUID] = "997f3bd6-37ee-4b36-b066-2bb0a402ebab"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class SalesInvoiceTotalsByCustomField(Object):
    Guid: ClassVar[UUID] = "8ea7ac48-0071-4e58-8647-c1f9b17f1dc6"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Name: Optional[str]
    CustomField: Optional[CustomField]
    Periods: Optional[List[Period]]


class SalesInvoiceTotalsByItem(Object):
    Guid: ClassVar[UUID] = "c70ca645-2d2b-4536-8f81-aead1b7eba99"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class SalesOrder(Object):
    Guid: ClassVar[UUID] = "2dac5598-128d-4954-b2e4-21515047b3a7"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        SalesUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
    Date: Optional[date]
    Reference: Optional[str]
    Customer: Optional[Customer]
    SalesQuote: Optional[SalesQuote]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    TrackQuantityToDeliver: Optional[bool]
    HasSalesOrderCustomTheme: Optional[bool]
    SalesOrderCustomTheme: Optional[Theme]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    CustomTitle: Optional[bool]
    SalesOrderCustomTitle: Optional[str]
    HasSalesOrderFooters: Optional[bool]
    SalesOrderFooters: Optional[List[SalesOrderFooter]]
    Cancelled: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class SalesOrderFooter(Object):
    Guid: ClassVar[UUID] = "38bf923a-9ab8-4d86-a12a-9d2581d13fa8"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class SalesQuote(Object):
    Guid: ClassVar[UUID] = "ba89de75-cb87-4bde-b20f-314f01b31037"
    class Line(BaseModel):
        Item: Optional[ISaleItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[CustomField, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Decimal]
        SalesUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[TaxCode]
    IssueDate: Optional[date]
    ExpiryDate: Optional[int]
    Reference: Optional[str]
    Customer: Optional[Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[RoundingMethod]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[WithholdingTaxType]
    WithholdingTaxPercentage: Optional[Decimal]
    WithholdingTaxAmount: Optional[Decimal]
    HideTotalAmount: Optional[bool]
    HasSalesQuoteCustomTheme: Optional[bool]
    SalesQuoteCustomTheme: Optional[Theme]
    CustomTitle: Optional[bool]
    SalesQuoteCustomTitle: Optional[str]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesQuoteFooters: Optional[bool]
    SalesQuoteFooters: Optional[List[SalesQuoteFooter]]
    Cancelled: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class SalesQuoteFooter(Object):
    Guid: ClassVar[UUID] = "d95df676-e2cb-4be6-a9b3-86dcd79ac3bc"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Schema(Object):
    Guid: ClassVar[UUID] = "a9a71e47-82b3-49db-8aec-898adb460a80"
    Version: Optional[int]


class SetZeroIfNegativeReportingCategory(Object):
    Key = UUID("1a94b65c-4869-4138-acc1-49d16bbfeed6")


class SpecialAccount(Object):
    Guid: ClassVar[UUID] = "e495f4e8-5fad-48ac-8a66-f35049ac4ef3"
    Name: Optional[str]
    Code: Optional[str]
    Currency: Optional[ForeignCurrency]
    TaxCode: Optional[TaxCode]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForSpecialAccounts]
    StartingBalance: Optional[Decimal]
    StartingBalanceType: Optional[DebitCredit]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class CapitalAccountsSummary(Object):
    Guid: ClassVar[UUID] = "19f661de-d63c-4d25-bd00-3e05578018b1"
    Title: Optional[str]
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    Rounding: Optional[Rounding]
    ReverseSigns: Optional[bool]
    ExcludeZeroBalances: Optional[bool]
    Footer: Optional[str]


class StatementOfChangesInEquity(Object):
    Guid: ClassVar[UUID] = "06d97eb4-27de-41ee-80ef-47b8115b5b36"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    AccountingMethod: Optional[AccountingBasis]
    Rounding: Optional[Rounding]
    Periods: Optional[List[Period]]
    ExcludeZeroBalances: Optional[bool]
    Footer: Optional[str]


class SubAccount(Object):
    Guid: ClassVar[UUID] = "f361339b-932a-4436-b56e-a337c1587c72"
    Name: Optional[str]


class Subtotal(Object):
    Guid: ClassVar[UUID] = "9601ce49-6058-4dac-9405-82f35005ea90"
    Name: Optional[str]
    Position: Optional[int]


class Summary(Object):
    Guid: ClassVar[UUID] = "2631d044-861d-4710-a871-d7a11461b4ba"
    ShowBalancesForSpecifiedPeriod: Optional[bool]
    FromDate: Optional[date]
    ToDate: Optional[DateType]
    ToDateValue: Optional[date]
    ShowBalancesOnCashBasis: Optional[bool]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]
    HasGroupsToCollapse: Optional[bool]
    GroupsToCollapse: Optional[List[ChartOfAccountsGroup]]


class Supplier(Object):
    Guid: ClassVar[UUID] = "6d2dc48d-2053-4e45-8330-285ebd431242"
    Name: Optional[str]
    Code: Optional[str]
    CreditLimit: Optional[Decimal]
    Currency: Optional[ForeignCurrency]
    Address: Optional[str]
    Email: Optional[str]
    Division: Optional[Division]
    ControlAccount: Optional[ControlAccountForSuppliers]
    StartingBalance: Optional[Decimal]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]
    Inactive: Optional[bool]


class SupplierNameField(Object):
    Key = UUID("22ec22e1-8ed2-4cba-a5b9-533a1e451977")


class SupplierStatementsTransactions(Object):
    Guid: ClassVar[UUID] = "401d5f3c-92ef-47da-942a-3cd6cf64aa9c"
    FromDate: Optional[date]
    ToDate: Optional[DateType]
    ToCustomDate: Optional[date]
    Theme: Optional[Theme]


class SupplierStatementsUnpaidInvoices(Object):
    Guid: ClassVar[UUID] = "119e71a0-3ea5-4c6f-a8f2-76384b86831a"
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Theme: Optional[Theme]


class SupplierSummary(Object):
    Guid: ClassVar[UUID] = "80d4616c-d083-4f8a-9ea9-b9dd5f04360f"
    FromDate: Optional[date]
    ToDate: Optional[date]
    Division: Optional[Division]


class Tabs(Object):
    Key = UUID("ac789d1f-034f-4964-a8b5-ebfffc3511f2")
    BankAndCashAccounts: Optional[bool]
    Receipts: Optional[bool]
    Payments: Optional[bool]
    InterAccountTransfers: Optional[bool]
    BankReconciliations: Optional[bool]
    ExpenseClaims: Optional[bool]
    Customers: Optional[bool]
    SalesQuotes: Optional[bool]
    SalesOrders: Optional[bool]
    SalesInvoices: Optional[bool]
    CreditNotes: Optional[bool]
    LatePaymentFees: Optional[bool]
    BillableTime: Optional[bool]
    WithholdingTaxReceipts: Optional[bool]
    DeliveryNotes: Optional[bool]
    Suppliers: Optional[bool]
    PurchaseQuotes: Optional[bool]
    PurchaseOrders: Optional[bool]
    PurchaseInvoices: Optional[bool]
    DebitNotes: Optional[bool]
    GoodsReceipts: Optional[bool]
    Projects: Optional[bool]
    InventoryItems: Optional[bool]
    InventoryTransfers: Optional[bool]
    InventoryWriteOffs: Optional[bool]
    ProductionOrders: Optional[bool]
    Employees: Optional[bool]
    Payslips: Optional[bool]
    Investments: Optional[bool]
    FixedAssets: Optional[bool]
    DepreciationEntries: Optional[bool]
    IntangibleAssets: Optional[bool]
    AmortizationEntries: Optional[bool]
    CapitalAccounts: Optional[bool]
    SpecialAccounts: Optional[bool]
    Folders: Optional[bool]


class TaxablePurchasesPerSupplier(Object):
    Guid: ClassVar[UUID] = "1f957bf2-d198-4a9a-bb51-8d7d26b2fc5c"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TaxableSalesPerCustomer(Object):
    Guid: ClassVar[UUID] = "2623ae0a-3c13-45e7-83b7-e4c9b2b9404d"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TaxAmountReportingCategory(Object):
    Guid: ClassVar[UUID] = "f58e8724-7e63-422c-8649-a12cf77c2208"
    Name: Optional[str]
    Inactive: Optional[bool]


class TaxAmountReversedReportingCategory(Object):
    Guid: ClassVar[UUID] = "52a10ec1-0808-4641-91b8-45eb33626ae3"
    Name: Optional[str]
    Inactive: Optional[bool]


class TaxAudit(Object):
    Guid: ClassVar[UUID] = "a43c996d-707a-48cb-91c8-191feab4411f"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TaxCode(Object):
    Guid: ClassVar[UUID] = "7f368d97-8b7f-4b39-b156-dc66afd9496a"
    class Component(BaseModel):
        Name: Optional[str]
        ComponentRate: Optional[Decimal]
        ComponentAccount: Optional[BalanceSheetAccount]
        ComponentTaxAmountReportingCategory: Optional[TaxAmountReportingCategory]
        ComponentTaxAmountReversedReportingCategory: Optional[TaxAmountReversedReportingCategory]
        TaxCode: Optional[TaxCode]
    Name: Optional[str]
    Label: Optional[str]
    ReportingCategory: Optional[TaxCodeReportingCategory]
    ReportingCategoryReversed: Optional[TaxCodeReversedReportingCategory]
    TaxRate: Optional[TaxRate]
    Type: Optional[TaxRateType]
    Rate: Optional[Decimal]
    Account: Optional[BalanceSheetAccount]
    TaxAmountReportingCategory: Optional[TaxAmountReportingCategory]
    TaxAmountReversedReportingCategory: Optional[TaxAmountReversedReportingCategory]
    Components: Optional[List[Component]]
    ReverseCharged: Optional[bool]
    CustomSalesInvoiceTitle: Optional[bool]
    SalesInvoiceTitle: Optional[str]
    CustomCreditNoteTitle: Optional[bool]
    CreditNoteTitle: Optional[str]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


class TaxCodeReportingCategory(Object):
    Guid: ClassVar[UUID] = "0cb739c7-6767-4949-88a7-6415c5ec083d"
    Name: Optional[str]
    Inactive: Optional[bool]


class TaxCodeReversedReportingCategory(Object):
    Guid: ClassVar[UUID] = "6027ab88-f804-4827-beff-26b76bb94587"
    Name: Optional[str]
    Inactive: Optional[bool]


class TaxReconciliation(Object):
    Guid: ClassVar[UUID] = "82fb1232-ba69-4310-b443-22df87ef18fa"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
    Description: Optional[str]
    AccountingMethod: Optional[AccountingBasis]
    Periods: Optional[List[Period]]


class TaxSummary(Object):
    Guid: ClassVar[UUID] = "68e0d57b-4a59-453e-b8d4-6166f097eacd"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Division: Optional[Division]


class TaxTransactions(Object):
    Guid: ClassVar[UUID] = "9a441483-1a09-46d3-aecd-477c91c13ae1"
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TextCustomField(Object):
    Guid: ClassVar[UUID] = "411f5975-0376-4ba9-b7ff-5bb2baa6f69f"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[CustomFieldsAttribute]]
    Type: Optional[TextCustomFieldType]
    OptionsForDropdownList: Optional[str]
    Size: Optional[CustomFieldSize]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]


class Theme(Object):
    Guid: ClassVar[UUID] = "01e1bcb2-74c1-467d-aedc-5e8f738fe776"
    Name: Optional[str]
    Template: Optional[str]
    Inactive: Optional[bool]


class Transaction(Object):
    pass


class TrialBalance(Object):
    Guid: ClassVar[UUID] = "e5dc98ef-4662-4a68-8a9d-b3e2d12b55d6"
    class Period(BaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        Division: Optional[Division]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    AccountingMethod: Optional[AccountingBasis]
    Periods: Optional[List[Period]]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class User(Object):
    Guid: ClassVar[UUID] = "8112e1a9-fe00-47c4-9d7a-2d034f8a1f34"
    Name: Optional[str]
    Username: Optional[str]
    Password: Optional[str]
    Type: Optional[UserType]
    Businesses: Optional[List[str]]
    Sessions: Optional[List[Session]]


class Session(Object):
    Key: Optional[UUID]
    Timestamp: Optional[date]
    UserAgent: Optional[str]
    Location: Optional[str]


class UserPermissions(Object):
    Guid: ClassVar[UUID] = "c6a5d19f-6f47-4716-841d-ba06ca9fc311"
    Username: Optional[str]
    BankAndCashAccounts: Optional[List[IBankOrCashAccount]]
    AccessType: Optional[UserPermissionsAccessType]
    Namespaces: Optional[Dict[str, bool]]
    Namespaces2: Optional[Dict[str, PermittedActions]]
    FullAccess: Optional[bool]


class WithholdingTaxReceipt(Object):
    Guid: ClassVar[UUID] = "8f7510d9-a92d-4b4c-9421-fd745e198b3c"
    Date: Optional[date]
    Customer: Optional[Customer]
    Amount: Optional[Decimal]
    Description: Optional[str]
    CustomFields: Optional[Dict[CustomField, str]]
    CustomFields2: Optional[CustomFields]


AgedPayables.update_forward_refs()
AgedReceivables.update_forward_refs()
AmortizationCalculationWorksheet.update_forward_refs()
AmortizationEntry.Line.update_forward_refs()
AmortizationEntry.update_forward_refs(Line=AmortizationEntry.Line)
Amount.update_forward_refs()
Assets.update_forward_refs()
Attachment.update_forward_refs()
BalanceSheet.Period.update_forward_refs()
BalanceSheet.update_forward_refs(Period=BalanceSheet.Period)
BalanceSheetAbstractGroup.update_forward_refs()
BalanceSheetAccount.update_forward_refs()
BalanceSheetAccountsPayableAccount.update_forward_refs()
BalanceSheetAccountsReceivableAccount.update_forward_refs()
BalanceSheetBillableExpensesAccount.update_forward_refs()
BalanceSheetBillableTimeAccount.update_forward_refs()
BalanceSheetCapitalAccountsAccount.update_forward_refs()
BalanceSheetCashAtBankAccount.update_forward_refs()
BalanceSheetEmployeeClearingAccount.update_forward_refs()
BalanceSheetExpenseClaimsAccount.update_forward_refs()
BalanceSheetFixedAssetsAccumulatedDepreciationAccount.update_forward_refs()
BalanceSheetFixedAssetsAtCostAccount.update_forward_refs()
BalanceSheetGroup.update_forward_refs()
BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount.update_forward_refs()
BalanceSheetIntangibleAssetsAtCostAccount.update_forward_refs()
BalanceSheetInterdivisionalLoan.update_forward_refs()
BalanceSheetInventoryOnHandAccount.update_forward_refs()
BalanceSheetInvestmentsAccount.update_forward_refs()
BalanceSheetProductionInProgressAccount.update_forward_refs()
BalanceSheetRetainedEarningsAccount.update_forward_refs()
BalanceSheetSpecialAccountsAccount.update_forward_refs()
BalanceSheetSuspenseAccount.update_forward_refs()
BalanceSheetTaxPayableAccount.update_forward_refs()
BalanceSheetWithholdingTaxAccount.update_forward_refs()
BalanceSheetWithholdingTaxPayableAccount.update_forward_refs()
BalanceSheetWithholdingTaxReceivableAccount.update_forward_refs()
BankAccountSummary.Period.update_forward_refs()
BankAccountSummary.update_forward_refs(Period=BankAccountSummary.Period)
BankOrCashAccount.update_forward_refs()
BankReconciliation.update_forward_refs()
BaseCurrency.update_forward_refs()
BillableExpenses.update_forward_refs()
BillableTime.update_forward_refs()
BillableTimeSummary.update_forward_refs()
BusinessDetails.update_forward_refs()
BusinessDetailsNameField.update_forward_refs()
BusinessLogo.update_forward_refs()
CapitalAccount.update_forward_refs()
CashFlowStatement.Period.update_forward_refs()
CashFlowStatement.update_forward_refs(Period=CashFlowStatement.Period)
CashFlowStatementFinancingActivityGroup.update_forward_refs()
CashFlowStatementInvestingActivityGroup.update_forward_refs()
CashFlowStatementOperatingActivityGroup.update_forward_refs()
ChartOfAccountsGroup.update_forward_refs()
CheckboxCustomField.update_forward_refs()
Column.update_forward_refs()
ControlAccount.update_forward_refs()
ControlAccountForBankAccounts.update_forward_refs()
ControlAccountForCapitalAccounts.update_forward_refs()
ControlAccountForCustomers.update_forward_refs()
ControlAccountForEmployees.update_forward_refs()
ControlAccountForFixedAssets.update_forward_refs()
ControlAccountForFixedAssetsAccumulatedDepreciation.update_forward_refs()
ControlAccountForIntangibleAssets.update_forward_refs()
ControlAccountForIntangibleAssetsAccumulatedAmortization.update_forward_refs()
ControlAccountForInventoryItems.update_forward_refs()
ControlAccountForInvestments.update_forward_refs()
ControlAccountForSpecialAccounts.update_forward_refs()
ControlAccountForSuppliers.update_forward_refs()
CreditNote.Line.update_forward_refs()
CreditNote.update_forward_refs(Line=CreditNote.Line)
CreditNoteFooter.update_forward_refs()
Currency.update_forward_refs()
Customer.update_forward_refs()
CustomerPortal.update_forward_refs()
CustomerStatementsTransactions.update_forward_refs()
CustomerStatementsUnpaidInvoices.update_forward_refs()
CustomerSummary.update_forward_refs()
CustomField.update_forward_refs()
CustomFields.update_forward_refs()
CustomReport.GroupByElement.update_forward_refs()
CustomReport.WhereElement.update_forward_refs()
CustomReport.SelectElement.update_forward_refs()
CustomReport.OrderByElement.update_forward_refs()
CustomReport.update_forward_refs(GroupByElement=CustomReport.GroupByElement, WhereElement=CustomReport.WhereElement, SelectElement=CustomReport.SelectElement, OrderByElement=CustomReport.OrderByElement)
DateAndNumberFormat.NumberFormatParts.update_forward_refs()
DateAndNumberFormat.update_forward_refs(NumberFormatParts=DateAndNumberFormat.NumberFormatParts)
DateCustomField.update_forward_refs()
DebitNote.Line.update_forward_refs()
DebitNote.update_forward_refs(Line=DebitNote.Line)
DebitNoteFooter.update_forward_refs()
DeliveryNote.Line.update_forward_refs()
DeliveryNote.update_forward_refs(Line=DeliveryNote.Line)
DeliveryNoteColumns.Column.update_forward_refs()
DeliveryNoteColumns.update_forward_refs(Column=DeliveryNoteColumns.Column)
DeliveryNoteFooter.update_forward_refs()
DepreciationCalculationWorksheet.update_forward_refs()
DepreciationEntry.Line.update_forward_refs()
DepreciationEntry.update_forward_refs(Line=DepreciationEntry.Line)
Division.update_forward_refs()
DivisionExceptionReport.update_forward_refs()
EinvoiceMe.update_forward_refs()
EmailSettings.update_forward_refs()
EmailTemplateForCreditNote.update_forward_refs()
EmailTemplateForCustomerStatement.update_forward_refs()
EmailTemplateForDebitNote.update_forward_refs()
EmailTemplateForDeliveryNote.update_forward_refs()
EmailTemplateForPayment.update_forward_refs()
EmailTemplateForPayslip.update_forward_refs()
EmailTemplateForPurchaseInvoice.update_forward_refs()
EmailTemplateForPurchaseOrder.update_forward_refs()
EmailTemplateForPurchaseQuote.update_forward_refs()
EmailTemplateForReceipt.update_forward_refs()
EmailTemplateForSalesInvoice.update_forward_refs()
EmailTemplateForSalesOrder.update_forward_refs()
EmailTemplateForSalesQuote.update_forward_refs()
Employee.update_forward_refs()
EmployeeEmailField.update_forward_refs()
EmployeeNameField.update_forward_refs()
EmployeeSummary.update_forward_refs()
Equity.update_forward_refs()
ExchangeRate.update_forward_refs()
ExpenseClaim.Line.update_forward_refs()
ExpenseClaim.update_forward_refs(Line=ExpenseClaim.Line)
ExpenseClaimsPayer.update_forward_refs()
ExpenseClaimsSummary.update_forward_refs()
Extension.update_forward_refs()
FixedAsset.update_forward_refs()
FixedAssetSummary.update_forward_refs()
Folder.update_forward_refs()
Forecast.Line.update_forward_refs()
Forecast.update_forward_refs(Line=Forecast.Line)
ForecastProfitAndLossStatement.Period.update_forward_refs()
ForecastProfitAndLossStatement.update_forward_refs(Period=ForecastProfitAndLossStatement.Period)
ForeignCurrency.update_forward_refs()
FreightInItem.update_forward_refs()
GeneralLedgerSummary.update_forward_refs()
GeneralLedgerTransactions.update_forward_refs()
GoodsReceipt.Line.update_forward_refs()
GoodsReceipt.update_forward_refs(Line=GoodsReceipt.Line)
GoodsReceiptFooter.update_forward_refs()
HideIfEmptyReportingCategory.update_forward_refs()
IntangibleAsset.update_forward_refs()
IntangibleAssetSummary.update_forward_refs()
InterAccountTransfer.update_forward_refs()
InterAccountTransferFooter.update_forward_refs()
InternalPdfGenerator.update_forward_refs()
InventoryItem.StartingBalanceQuantity.update_forward_refs()
InventoryItem.update_forward_refs(StartingBalanceQuantity=InventoryItem.StartingBalanceQuantity)
InventoryKit.Item.update_forward_refs()
InventoryKit.update_forward_refs(Item=InventoryKit.Item)
InventoryLocation.update_forward_refs()
InventoryPriceList.update_forward_refs()
InventoryProfitMargin.update_forward_refs()
InventoryQuantityByLocation.update_forward_refs()
InventoryQuantityMovement.update_forward_refs()
InventoryTransfer.Line.update_forward_refs()
InventoryTransfer.update_forward_refs(Line=InventoryTransfer.Line)
InventoryValueSummary.update_forward_refs()
InventoryWriteOff.Item.update_forward_refs()
InventoryWriteOff.update_forward_refs(Item=InventoryWriteOff.Item)
Investment.update_forward_refs()
JournalEntry.Line.update_forward_refs()
JournalEntry.update_forward_refs(Line=JournalEntry.Line)
JournalEntryFooter.update_forward_refs()
LatePaymentFee.update_forward_refs()
Liabilities.update_forward_refs()
LockDate.update_forward_refs()
MemberInfo.update_forward_refs()
MultipleValueCustomField.Option.update_forward_refs()
MultipleValueCustomField.update_forward_refs(Option=MultipleValueCustomField.Option)
NamedObject.update_forward_refs()
NonInventoryItem.update_forward_refs()
NumberCustomField.update_forward_refs()
Object.update_forward_refs()
Payment.Line.update_forward_refs()
Payment.update_forward_refs(Line=Payment.Line)
PaymentFooter.update_forward_refs()
PaymentRule.Condition.update_forward_refs()
PaymentRule.Line.update_forward_refs()
PaymentRule.update_forward_refs(Condition=PaymentRule.Condition, Line=PaymentRule.Line)
Payslip.Contribution.update_forward_refs()
Payslip.Earned.update_forward_refs()
Payslip.Deduction.update_forward_refs()
Payslip.update_forward_refs(Contribution=Payslip.Contribution, Earned=Payslip.Earned, Deduction=Payslip.Deduction)
PayslipContributionItem.update_forward_refs()
PayslipContributionItemReportingCategory.update_forward_refs()
PayslipDeductionItem.update_forward_refs()
PayslipDeductionItemReportingCategory.update_forward_refs()
PayslipEarningsItem.update_forward_refs()
PayslipEarningsItemReportingCategory.update_forward_refs()
PayslipFooter.update_forward_refs()
PayslipSummary.update_forward_refs()
PayslipTotalsPerItemAndEmployee.Period.update_forward_refs()
PayslipTotalsPerItemAndEmployee.update_forward_refs(Period=PayslipTotalsPerItemAndEmployee.Period)
ProductionOrder.ExpenseItem.update_forward_refs()
ProductionOrder.Item.update_forward_refs()
ProductionOrder.update_forward_refs(ExpenseItem=ProductionOrder.ExpenseItem, Item=ProductionOrder.Item)
ProfitAndLossStatement.Period.update_forward_refs()
ProfitAndLossStatement.update_forward_refs(Period=ProfitAndLossStatement.Period)
ProfitAndLossStatementAccount.update_forward_refs()
ProfitAndLossStatementAccountBillableExpensesCost.update_forward_refs()
ProfitAndLossStatementAccountBillableExpensesInvoiced.update_forward_refs()
ProfitAndLossStatementAccountBillableTimeInvoiced.update_forward_refs()
ProfitAndLossStatementAccountBillableTimeMovement.update_forward_refs()
ProfitAndLossStatementAccountCurrencyGainsLosses.update_forward_refs()
ProfitAndLossStatementAccountFixedAssetDepreciation.update_forward_refs()
ProfitAndLossStatementAccountFixedAssetLossOnDisposal.update_forward_refs()
ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal.update_forward_refs()
ProfitAndLossStatementAccountIntangibleAssetsAmortization.update_forward_refs()
ProfitAndLossStatementAccountInventoryPurchases.update_forward_refs()
ProfitAndLossStatementAccountInventorySales.update_forward_refs()
ProfitAndLossStatementAccountLatePaymentFees.update_forward_refs()
ProfitAndLossStatementAccountRoundingExpense.update_forward_refs()
ProfitAndLossStatementActualVsBudget.BudgetItem.update_forward_refs()
ProfitAndLossStatementActualVsBudget.update_forward_refs(BudgetItem=ProfitAndLossStatementActualVsBudget.BudgetItem)
ProfitAndLossStatementCapitalGainsOnInvestments.update_forward_refs()
ProfitAndLossStatementGroup.update_forward_refs()
Project.update_forward_refs()
PurchaseInvoice.Line.update_forward_refs()
PurchaseInvoice.update_forward_refs(Line=PurchaseInvoice.Line)
PurchaseInvoiceFooter.update_forward_refs()
PurchaseOrder.Line.update_forward_refs()
PurchaseOrder.update_forward_refs(Line=PurchaseOrder.Line)
PurchaseOrderFooter.update_forward_refs()
PurchaseQuote.Line.update_forward_refs()
PurchaseQuote.update_forward_refs(Line=PurchaseQuote.Line)
PurchaseQuoteFooter.update_forward_refs()
Receipt.Line.update_forward_refs()
Receipt.update_forward_refs(Line=Receipt.Line)
ReceiptColumns.update_forward_refs()
ReceiptFooter.update_forward_refs()
ReceiptRule.Condition.update_forward_refs()
ReceiptRule.Line.update_forward_refs()
ReceiptRule.update_forward_refs(Condition=ReceiptRule.Condition, Line=ReceiptRule.Line)
ReceiptsAndPaymentsSummary.Period.update_forward_refs()
ReceiptsAndPaymentsSummary.update_forward_refs(Period=ReceiptsAndPaymentsSummary.Period)
RecurringInterAccountTransfer.update_forward_refs()
RecurringJournalEntry.update_forward_refs()
RecurringPayment.update_forward_refs()
RecurringPayslip.update_forward_refs()
RecurringPurchaseInvoice.update_forward_refs()
RecurringPurchaseOrder.update_forward_refs()
RecurringReceipt.update_forward_refs()
RecurringSalesInvoice.update_forward_refs()
RecurringSalesOrder.update_forward_refs()
RecurringSalesQuote.update_forward_refs()
ReportTranformationFromDate.update_forward_refs()
ReportTranformationToDate.update_forward_refs()
ReportTransformation2.InstructionStep.update_forward_refs()
ReportTransformation2.Item.update_forward_refs()
ReportTransformation2.update_forward_refs(InstructionStep=ReportTransformation2.InstructionStep, Item=ReportTransformation2.Item)
ReportTransformationFromDateLastJuly.update_forward_refs()
ReportTransformationLabel.update_forward_refs()
ReportTransformationNetAmounts.update_forward_refs()
ReportTransformationReport.update_forward_refs()
ReportTransformationTaxAmounts.update_forward_refs()
ReportTransformationTaxPurchases.update_forward_refs()
ReportTransformationTaxSales.update_forward_refs()
ReverseSignReportingCategory.update_forward_refs()
RoundDownReportingCategory.update_forward_refs()
SalesInvoice.Line.update_forward_refs()
SalesInvoice.update_forward_refs(Line=SalesInvoice.Line)
SalesInvoiceFooter.update_forward_refs()
SalesInvoiceTotalsByCustomer.Period.update_forward_refs()
SalesInvoiceTotalsByCustomer.update_forward_refs(Period=SalesInvoiceTotalsByCustomer.Period)
SalesInvoiceTotalsByCustomField.Period.update_forward_refs()
SalesInvoiceTotalsByCustomField.update_forward_refs(Period=SalesInvoiceTotalsByCustomField.Period)
SalesInvoiceTotalsByItem.Period.update_forward_refs()
SalesInvoiceTotalsByItem.update_forward_refs(Period=SalesInvoiceTotalsByItem.Period)
SalesOrder.Line.update_forward_refs()
SalesOrder.update_forward_refs(Line=SalesOrder.Line)
SalesOrderFooter.update_forward_refs()
SalesQuote.Line.update_forward_refs()
SalesQuote.update_forward_refs(Line=SalesQuote.Line)
SalesQuoteFooter.update_forward_refs()
Schema.update_forward_refs()
SetZeroIfNegativeReportingCategory.update_forward_refs()
SpecialAccount.update_forward_refs()
CapitalAccountsSummary.update_forward_refs()
StatementOfChangesInEquity.Period.update_forward_refs()
StatementOfChangesInEquity.update_forward_refs(Period=StatementOfChangesInEquity.Period)
SubAccount.update_forward_refs()
Subtotal.update_forward_refs()
Summary.update_forward_refs()
Supplier.update_forward_refs()
SupplierNameField.update_forward_refs()
SupplierStatementsTransactions.update_forward_refs()
SupplierStatementsUnpaidInvoices.update_forward_refs()
SupplierSummary.update_forward_refs()
Tabs.update_forward_refs()
TaxablePurchasesPerSupplier.update_forward_refs()
TaxableSalesPerCustomer.update_forward_refs()
TaxAmountReportingCategory.update_forward_refs()
TaxAmountReversedReportingCategory.update_forward_refs()
TaxAudit.update_forward_refs()
TaxCode.Component.update_forward_refs()
TaxCode.update_forward_refs(Component=TaxCode.Component)
TaxCodeReportingCategory.update_forward_refs()
TaxCodeReversedReportingCategory.update_forward_refs()
TaxReconciliation.Period.update_forward_refs()
TaxReconciliation.update_forward_refs(Period=TaxReconciliation.Period)
TaxSummary.update_forward_refs()
TaxTransactions.update_forward_refs()
TextCustomField.update_forward_refs()
Theme.update_forward_refs()
Transaction.update_forward_refs()
TrialBalance.Period.update_forward_refs()
TrialBalance.update_forward_refs(Period=TrialBalance.Period)
User.update_forward_refs()
Session.update_forward_refs()
UserPermissions.update_forward_refs()
WithholdingTaxReceipt.update_forward_refs()
