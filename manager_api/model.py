# -*- coding: utf-8 -*-
# Do not edit. Automatically generated from Manager v23.1.11.592.

from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID

from . import enums
from .enums import *
from .object import ManagerBaseModel, Object


CustomFieldsAttribute = Union["model.AmortizationEntry", "model.BankOrCashAccount", "model.BillableTime", "model.BusinessDetails", "model.CapitalAccount", "model.CreditNote", "model.Customer", "model.DebitNote", "model.DeliveryNote", "model.DepreciationEntry", "model.Employee", "model.ExpenseClaim", "model.FixedAsset", "model.Folder", "model.GoodsReceipt", "model.IntangibleAsset", "model.InterAccountTransfer", "model.InventoryItem", "model.InventoryKit", "model.InventoryTransfer", "model.InventoryWriteOff", "model.JournalEntry", "model.NonInventoryItem", "model.Payment", "model.Payslip", "model.PayslipContributionItem", "model.PayslipDeductionItem", "model.PayslipEarningsItem", "model.ProductionOrder", "model.Project", "model.PurchaseInvoice", "model.PurchaseOrder", "model.PurchaseQuote", "model.Receipt", "model.RecurringInterAccountTransfer", "model.RecurringJournalEntry", "model.RecurringPayment", "model.RecurringPayslip", "model.RecurringPurchaseInvoice", "model.RecurringPurchaseOrder", "model.RecurringReceipt", "model.RecurringSalesInvoice", "model.RecurringSalesOrder", "model.RecurringSalesQuote", "model.SalesInvoice", "model.SalesOrder", "model.SalesQuote", "model.SpecialAccount", "model.Supplier", "model.TaxCode", "model.WithholdingTaxReceipt"]
BalanceSheetAbstractGroup = Union["model.Assets", "model.BalanceSheetGroup", "model.Equity", "model.Liabilities"]
ChartOfAccountsGroup = Union["model.BalanceSheetAbstractGroup", "model.ProfitAndLossStatementGroup"]
IGeneralLedgerAccount = Union["model.BalanceSheetAccount", "model.BalanceSheetAccountsPayableAccount", "model.BalanceSheetAccountsReceivableAccount", "model.BalanceSheetBillableExpensesAccount", "model.BalanceSheetBillableTimeAccount", "model.BalanceSheetCapitalAccountsAccount", "model.BalanceSheetCashAtBankAccount", "model.BalanceSheetEmployeeClearingAccount", "model.BalanceSheetExpenseClaimsAccount", "model.BalanceSheetFixedAssetsAccumulatedDepreciationAccount", "model.BalanceSheetFixedAssetsAtCostAccount", "model.BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount", "model.BalanceSheetIntangibleAssetsAtCostAccount", "model.BalanceSheetInterdivisionalLoan", "model.BalanceSheetInventoryOnHandAccount", "model.BalanceSheetInvestmentsAccount", "model.BalanceSheetProductionInProgressAccount", "model.BalanceSheetRetainedEarningsAccount", "model.BalanceSheetSpecialAccountsAccount", "model.BalanceSheetSuspenseAccount", "model.BalanceSheetTaxPayableAccount", "model.BalanceSheetWithholdingTaxAccount", "model.BalanceSheetWithholdingTaxPayableAccount", "model.BalanceSheetWithholdingTaxReceivableAccount", "model.ControlAccountForBankAccounts", "model.ControlAccountForCapitalAccounts", "model.ControlAccountForCustomers", "model.ControlAccountForEmployees", "model.ControlAccountForFixedAssets", "model.ControlAccountForFixedAssetsAccumulatedDepreciation", "model.ControlAccountForIntangibleAssets", "model.ControlAccountForIntangibleAssetsAccumulatedAmortization", "model.ControlAccountForInventoryItems", "model.ControlAccountForInvestments", "model.ControlAccountForSpecialAccounts", "model.ControlAccountForSuppliers", "model.ProfitAndLossStatementAccount", "model.ProfitAndLossStatementAccountBillableExpensesCost", "model.ProfitAndLossStatementAccountBillableExpensesInvoiced", "model.ProfitAndLossStatementAccountBillableTimeInvoiced", "model.ProfitAndLossStatementAccountBillableTimeMovement", "model.ProfitAndLossStatementAccountCurrencyGainsLosses", "model.ProfitAndLossStatementAccountFixedAssetDepreciation", "model.ProfitAndLossStatementAccountFixedAssetLossOnDisposal", "model.ProfitAndLossStatementAccountIntangibleAssetsAmortization", "model.ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal", "model.ProfitAndLossStatementAccountInventoryPurchases", "model.ProfitAndLossStatementAccountInventorySales", "model.ProfitAndLossStatementAccountLatePaymentFees", "model.ProfitAndLossStatementAccountRoundingExpense", "model.ProfitAndLossStatementCapitalGainsOnInvestments"]
ICustomGeneralLedgerAccount = Union["model.BalanceSheetAccount", "model.ProfitAndLossStatementAccount"]
IInventoryWriteOffAccount = Union["model.BalanceSheetAccount", "model.BalanceSheetFixedAssetsAtCostAccount", "model.ControlAccountForFixedAssets", "model.ProfitAndLossStatementAccount"]
IJournalEntryAccount = Union["model.BalanceSheetAccount", "model.BalanceSheetAccountsPayableAccount", "model.BalanceSheetAccountsReceivableAccount", "model.BalanceSheetBillableExpensesAccount", "model.BalanceSheetCapitalAccountsAccount", "model.BalanceSheetEmployeeClearingAccount", "model.BalanceSheetExpenseClaimsAccount", "model.BalanceSheetFixedAssetsAtCostAccount", "model.BalanceSheetIntangibleAssetsAtCostAccount", "model.BalanceSheetInventoryOnHandAccount", "model.BalanceSheetInvestmentsAccount", "model.BalanceSheetRetainedEarningsAccount", "model.BalanceSheetSpecialAccountsAccount", "model.BalanceSheetWithholdingTaxAccount", "model.BalanceSheetWithholdingTaxPayableAccount", "model.ControlAccountForCapitalAccounts", "model.ControlAccountForCustomers", "model.ControlAccountForEmployees", "model.ControlAccountForFixedAssets", "model.ControlAccountForIntangibleAssets", "model.ControlAccountForInventoryItems", "model.ControlAccountForInvestments", "model.ControlAccountForSpecialAccounts", "model.ControlAccountForSuppliers", "model.ProfitAndLossStatementAccount", "model.ProfitAndLossStatementAccountBillableExpensesCost", "model.ProfitAndLossStatementAccountBillableExpensesInvoiced", "model.ProfitAndLossStatementAccountBillableTimeInvoiced", "model.ProfitAndLossStatementAccountBillableTimeMovement", "model.ProfitAndLossStatementAccountFixedAssetDepreciation", "model.ProfitAndLossStatementAccountFixedAssetLossOnDisposal", "model.ProfitAndLossStatementAccountIntangibleAssetsAmortization", "model.ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal", "model.ProfitAndLossStatementAccountInventoryPurchases", "model.ProfitAndLossStatementAccountInventorySales", "model.ProfitAndLossStatementAccountLatePaymentFees", "model.ProfitAndLossStatementCapitalGainsOnInvestments"]
INonInventoryItemAccount = Union["model.BalanceSheetAccount", "model.ProfitAndLossStatementAccount"]
IPurchaseInvoiceAccount = Union["model.BalanceSheetAccount", "model.BalanceSheetBillableExpensesAccount", "model.BalanceSheetCapitalAccountsAccount", "model.BalanceSheetEmployeeClearingAccount", "model.BalanceSheetFixedAssetsAtCostAccount", "model.BalanceSheetIntangibleAssetsAtCostAccount", "model.BalanceSheetRetainedEarningsAccount", "model.BalanceSheetSpecialAccountsAccount", "model.ControlAccountForCapitalAccounts", "model.ControlAccountForEmployees", "model.ControlAccountForFixedAssets", "model.ControlAccountForIntangibleAssets", "model.ControlAccountForInvestments", "model.ControlAccountForSpecialAccounts", "model.ProfitAndLossStatementAccount"]
ISalesInvoiceAccount = Union["model.BalanceSheetAccount", "model.BalanceSheetCapitalAccountsAccount", "model.BalanceSheetFixedAssetsAtCostAccount", "model.BalanceSheetIntangibleAssetsAtCostAccount", "model.BalanceSheetRetainedEarningsAccount", "model.BalanceSheetSpecialAccountsAccount", "model.ControlAccountForCapitalAccounts", "model.ControlAccountForFixedAssets", "model.ControlAccountForIntangibleAssets", "model.ControlAccountForInvestments", "model.ControlAccountForSpecialAccounts", "model.ProfitAndLossStatementAccount", "model.ProfitAndLossStatementAccountBillableExpensesInvoiced", "model.ProfitAndLossStatementAccountBillableTimeInvoiced"]
IBankOrCashAccount = Union["model.BankOrCashAccount"]
IReportingCategory = Union["model.BusinessDetailsNameField", "model.CheckboxCustomField", "model.CustomField", "model.DateCustomField", "model.EmployeeEmailField", "model.EmployeeNameField", "model.HideIfEmptyReportingCategory", "model.MultipleValueCustomField", "model.NumberCustomField", "model.PayslipContributionItemReportingCategory", "model.PayslipDeductionItemReportingCategory", "model.PayslipEarningsItemReportingCategory", "model.ReportTranformationFromDate", "model.ReportTranformationToDate", "model.ReportTransformationFromDateLastJuly", "model.ReportTransformationLabel", "model.ReportTransformationNetAmounts", "model.ReportTransformationTaxAmounts", "model.ReportTransformationTaxPurchases", "model.ReportTransformationTaxSales", "model.ReverseSignReportingCategory", "model.RoundDownReportingCategory", "model.SetZeroIfNegativeReportingCategory", "model.SupplierNameField", "model.TaxAmountReportingCategory", "model.TaxAmountReversedReportingCategory", "model.TaxCodeReportingCategory", "model.TaxCodeReversedReportingCategory", "model.TextCustomField"]
IExpenseClaimPayer = Union["model.CapitalAccount", "model.Employee", "model.ExpenseClaimsPayer"]
ICustomField = Union["model.CheckboxCustomField", "model.DateCustomField", "model.MultipleValueCustomField", "model.NumberCustomField", "model.TextCustomField"]
IPurchaseItem = Union["model.FreightInItem", "model.InventoryItem", "model.NonInventoryItem"]
ISaleItem = Union["model.InventoryItem", "model.InventoryKit", "model.NonInventoryItem"]
IProfitAndLossAccount = Union["model.ProfitAndLossStatementAccount", "model.ProfitAndLossStatementAccountBillableExpensesCost", "model.ProfitAndLossStatementAccountBillableExpensesInvoiced", "model.ProfitAndLossStatementAccountBillableTimeInvoiced", "model.ProfitAndLossStatementAccountBillableTimeMovement", "model.ProfitAndLossStatementAccountCurrencyGainsLosses", "model.ProfitAndLossStatementAccountFixedAssetDepreciation", "model.ProfitAndLossStatementAccountFixedAssetLossOnDisposal", "model.ProfitAndLossStatementAccountIntangibleAssetsAmortization", "model.ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal", "model.ProfitAndLossStatementAccountInventoryPurchases", "model.ProfitAndLossStatementAccountInventorySales", "model.ProfitAndLossStatementAccountLatePaymentFees", "model.ProfitAndLossStatementAccountRoundingExpense", "model.ProfitAndLossStatementCapitalGainsOnInvestments"]


class AgedPayables(Object):
    Guid: ClassVar[UUID] = "6abe86ec-a6c9-46a8-a9c9-7104056a2730"
    Date: Optional[model.DateType]
    CustomDate: Optional[model.date]
    Division: Optional[model.Division]
    SortBy: Optional[model.SortBy]
    Description: Optional[str]
    ShowInvoices: Optional[bool]


class AgedReceivables(Object):
    Guid: ClassVar[UUID] = "39f00628-27a7-4924-9030-5bc655ee234f"
    Date: Optional[model.DateType]
    CustomDate: Optional[model.date]
    Division: Optional[model.Division]
    SortBy: Optional[model.SortBy]
    Description: Optional[str]
    ShowInvoices: Optional[bool]


class AmortizationCalculationWorksheet(Object):
    Guid: ClassVar[UUID] = "011cf167-ff32-49e7-b0f3-ac12a3fe43ed"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class AmortizationEntry(Object):
    Guid: ClassVar[UUID] = "d33519a3-e8e0-4556-9833-b744a58dd2f7"
    class Line(ManagerBaseModel):
        IntangibleAsset: Optional[model.IntangibleAsset]
        Division: Optional[model.Division]
        Amount: Optional[model.Decimal]
    Date: Optional[model.date]
    Reference: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    AutomaticReference: Optional[bool]


class Assets(Object):
    Key = UUID("4c05c221-ca57-4c7c-be62-115669302ed4")


class Attachment(Object):
    Guid: ClassVar[UUID] = "2e541a82-94d7-42fc-a388-26bdc0803455"
    Date: Optional[model.date]
    Name: Optional[str]
    ContentType: Optional[str]
    Size: Optional[int]
    Object: Optional[model.Object]


class BalanceSheet(Object):
    Guid: ClassVar[UUID] = "7b4f463a-470d-44c4-9e75-fafc630b5851"
    class Period(ManagerBaseModel):
        Date: Optional[model.date]
        Division: Optional[model.Division]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    AccountingMethod: Optional[model.AccountingBasis]
    Rounding: Optional[model.Rounding]
    Layout: Optional[model.BalanceSheetLayout]
    GroupsToCollapse: Optional[List[model.BalanceSheetAbstractGroup]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class BalanceSheetAbstractGroup(Object):
    pass


class BalanceSheetAccount(Object):
    Guid: ClassVar[UUID] = "6ef13e42-ad89-4d42-9480-546e0c04a411"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatement: Optional[model.CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[model.CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[model.CashFlowStatementInvestingActivityGroup]
    Division: Optional[model.Division]
    Position: Optional[int]
    StartingBalance: Optional[model.Decimal]
    StartingBalanceType: Optional[model.DebitCredit]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    Inactive: Optional[bool]


class BalanceSheetAccountsPayableAccount(Object):
    Key = UUID("dac7ba37-0ccd-45e5-906e-548e6c50df37")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]


class BalanceSheetAccountsReceivableAccount(Object):
    Key = UUID("d1489e95-bb28-4f5d-b42e-67d3291b3893")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]


class BalanceSheetBillableExpensesAccount(Object):
    Key = UUID("059dbfb9-1c80-4043-887f-0fc441099fe0")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    Position: Optional[int]


class BalanceSheetBillableTimeAccount(Object):
    Key = UUID("9f3c0a1a-dd0b-4b5c-ba50-3e4939a0e90c")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetCapitalAccountsAccount(Object):
    Key = UUID("054dfae1-c34a-475e-abde-49e0385ffc9a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetCashAtBankAccount(Object):
    Key = UUID("6d4af96a-0959-4bb2-9160-fa825ec67c43")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetEmployeeClearingAccount(Object):
    Key = UUID("650a36fe-801f-4031-8d5b-ab422d061fca")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetExpenseClaimsAccount(Object):
    Key = UUID("f728124f-c6b6-4dad-82c5-22fc0d8d0571")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetFixedAssetsAccumulatedDepreciationAccount(Object):
    Key = UUID("f813a6c8-1ead-46bd-8911-f12714be193c")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetFixedAssetsAtCostAccount(Object):
    Key = UUID("4a0e8917-fee2-4033-9161-48dd513fdb73")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetGroup(Object):
    Guid: ClassVar[UUID] = "c03d1921-7a45-4eda-8742-a2d9082dcf4f"
    Name: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount(Object):
    Key = UUID("aa12d048-bfbd-47dc-a5b8-03e35c417996")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetIntangibleAssetsAtCostAccount(Object):
    Key = UUID("31d369e3-32c7-4bd2-bb83-9c1c58010c1a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetInterdivisionalLoan(Object):
    Key = UUID("ac4ab22b-0fbd-485f-8434-d25745b9be22")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetInventoryOnHandAccount(Object):
    Key = UUID("0fb45a62-fc42-43a8-a776-782e8b5ffc96")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetInvestmentsAccount(Object):
    Key = UUID("352897d1-e7fe-462e-9965-458ed9e27b82")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatementInvestingActivityGroup: Optional[model.CashFlowStatementInvestingActivityGroup]
    Position: Optional[int]


class BalanceSheetProductionInProgressAccount(Object):
    Key = UUID("30a1b83c-68a8-4f2c-ae70-25b0acc2d12a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetRetainedEarningsAccount(Object):
    Key = UUID("74dfd025-d68e-4a99-9c78-5d43e17c0e09")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetSpecialAccountsAccount(Object):
    Key = UUID("ef49facb-203b-4b45-aebd-99af4645700b")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatement: Optional[model.CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[model.CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[model.CashFlowStatementInvestingActivityGroup]
    Position: Optional[int]


class BalanceSheetSuspenseAccount(Object):
    Key = UUID("11211c9e-0988-4d16-8bf2-fa39487123aa")


class BalanceSheetTaxPayableAccount(Object):
    Key = UUID("30c697fa-4196-438a-ab5a-1957478034b1")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetWithholdingTaxAccount(Object):
    Key = UUID("8f75a810-abd0-4d89-a6a2-66c9003a60e2")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetWithholdingTaxPayableAccount(Object):
    Key = UUID("a4dffac2-35d1-47e1-a4bd-b6de15975fdb")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BalanceSheetWithholdingTaxReceivableAccount(Object):
    Key = UUID("c66de1bf-6f63-4bc8-9452-0b019e41c47f")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]


class BankAccountSummary(Object):
    Guid: ClassVar[UUID] = "77afd97c-51d7-484b-8192-b7eb006daadb"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
    BankAccount: Optional[model.BankOrCashAccount]
    Periods: Optional[List[Period]]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class BankOrCashAccount(Object):
    Guid: ClassVar[UUID] = "1408c33b-6284-4f50-9e31-48cbea21f3cf"
    Name: Optional[str]
    Code: Optional[str]
    Currency: Optional[model.ForeignCurrency]
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForBankAccounts]
    StartingBalance: Optional[model.Decimal]
    HasInternationalBankAccountNumber: Optional[bool]
    InternationalBankAccountNumber: Optional[str]
    CanHavePendingTransactions: Optional[bool]
    HasCreditLimit: Optional[bool]
    CreditLimit: Optional[model.Decimal]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    IsBankAccount: Optional[bool]


class BankReconciliation(Object):
    Guid: ClassVar[UUID] = "a3b1d610-b5e8-4f17-8e97-e53e69b78bb5"
    Date: Optional[model.date]
    BankAccount: Optional[model.BankOrCashAccount]
    StatementBalance: Optional[model.Decimal]


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
    Date: Optional[model.date]
    Customer: Optional[model.Customer]
    Description: Optional[str]
    HourlyRate: Optional[model.Decimal]
    TimeSpent: Optional[int]
    TimeSpentMinutes: Optional[int]
    Division: Optional[model.Division]
    Status: Optional[model.BillableTimeStatus]
    SalesInvoice: Optional[model.SalesInvoice]
    WrittenOffDate: Optional[model.date]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class BillableTimeSummary(Object):
    Guid: ClassVar[UUID] = "5516d6e5-d1fe-4271-8625-f7f0acc7f961"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class BusinessDetails(Object):
    Key = UUID("38cf4712-6e95-4ce1-b53a-bff03edad273")
    Name: Optional[str]
    Address: Optional[str]
    Country: Optional[str]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


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
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForCapitalAccounts]
    StartingBalance: Optional[model.StartingBalanceType]
    StartingBalanceAmount: Optional[model.Decimal]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    Inactive: Optional[bool]


class CapitalAccountsSummary(Object):
    Guid: ClassVar[UUID] = "19f661de-d63c-4d25-bd00-3e05578018b1"
    Title: Optional[str]
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Rounding: Optional[model.Rounding]
    ReverseSigns: Optional[bool]
    ExcludeZeroBalances: Optional[bool]
    Footer: Optional[str]


class CashFlowStatement(Object):
    Guid: ClassVar[UUID] = "2a9a4b8e-8b06-4819-adee-4b766a55119c"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Method: Optional[model.CashFlowStatementMethod]
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
    Placement: Optional[List[model.CustomFieldsAttribute]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]


class Column(Object):
    pass


class ControlAccountForBankAccounts(Object):
    Guid: ClassVar[UUID] = "c97264e3-eed6-4afd-8d2c-e1c1a00b4dc1"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForCapitalAccounts(Object):
    Guid: ClassVar[UUID] = "95b9d17d-f5f8-4722-a89d-456fa0906e13"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForCustomers(Object):
    Guid: ClassVar[UUID] = "7a57978e-583d-4997-86c7-c557de0e7fdd"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForEmployees(Object):
    Guid: ClassVar[UUID] = "fb804fba-df12-4628-ae54-df7a67d67f1b"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForFixedAssets(Object):
    Guid: ClassVar[UUID] = "014742b2-fc31-4ded-90b5-2e0d437a1589"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForFixedAssetsAccumulatedDepreciation(Object):
    Guid: ClassVar[UUID] = "c2e88cf8-4d05-4bec-8c42-fdef424faf1a"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForIntangibleAssets(Object):
    Guid: ClassVar[UUID] = "8ed99282-8ec3-4505-8846-0507bd0d0f70"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForIntangibleAssetsAccumulatedAmortization(Object):
    Guid: ClassVar[UUID] = "47995ee3-b2c9-4799-ace3-768f7514c644"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForInventoryItems(Object):
    Guid: ClassVar[UUID] = "acc019f7-9bb9-4d8e-ba66-0956916b4247"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForInvestments(Object):
    Guid: ClassVar[UUID] = "fb2c120e-6b30-47cb-a61e-14f0189bec06"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForSpecialAccounts(Object):
    Guid: ClassVar[UUID] = "6af7e809-1de3-4a09-923f-27ad786ed837"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatement: Optional[model.CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[model.CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[model.CashFlowStatementInvestingActivityGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForSuppliers(Object):
    Guid: ClassVar[UUID] = "78e7aefb-9dff-4ae5-981e-4165b14fd963"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.BalanceSheetAbstractGroup]
    CashFlowStatementGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]
    Inactive: Optional[bool]


class CreditNote(Object):
    Guid: ClassVar[UUID] = "245e5943-0092-409d-96ae-e2ee10eac75b"
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        Account: Optional[model.ISalesInvoiceAccount]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        SalesUnitPrice: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    IssueDate: Optional[model.date]
    Reference: Optional[str]
    Customer: Optional[model.Customer]
    SalesInvoice: Optional[model.SalesInvoice]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    SalesInventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsIncludeTax: Optional[bool]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxAmount: Optional[model.Decimal]
    WithholdingTaxRate: Optional[model.Decimal]
    HasCreditNoteCustomTheme: Optional[bool]
    CreditNoteCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasCreditNoteFooters: Optional[bool]
    CreditNoteFooters: Optional[List[model.CreditNoteFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    Type: Optional[model.CreditNoteType]


class CreditNoteFooter(Object):
    Guid: ClassVar[UUID] = "90f7ba80-5666-49a2-af1b-908cf9a651cd"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class CustomField(Object):
    Guid: ClassVar[UUID] = "dcb382dc-a4e0-4354-a845-b7d647f610f7"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[model.CustomFieldsAttribute]]
    Type: Optional[model.CustomFieldStyle]
    OptionsForDropdownList: Optional[str]
    Size: Optional[model.CustomFieldSize]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class CustomFields(Object):
    Strings: Optional[Dict[model.ICustomField, str]]
    Decimals: Optional[Dict[model.ICustomField, model.Decimal]]
    Dates: Optional[Dict[model.ICustomField, model.date]]
    Booleans: Optional[Dict[model.ICustomField, bool]]
    StringArrays: Optional[Dict[model.ICustomField, List[str]]]


class CustomReport(Object):
    Guid: ClassVar[UUID] = "7df43b64-9aea-4b19-a60a-a56f2e390df4"
    class SelectElement(ManagerBaseModel):
        SelectPrimaryField: Optional[model.MemberInfo]
        SelectSecondaryField: Optional[model.MemberInfo]
        SelectCustomField: Optional[model.CustomField]
        DisplayName: Optional[str]
    class OrderByElement(ManagerBaseModel):
        OrderByPrimaryField: Optional[model.MemberInfo]
        OrderBySecondaryField: Optional[model.MemberInfo]
        OrderByCustomField: Optional[model.CustomField]
        SortOrder: Optional[model.SortOrder]
    class GroupByElement(ManagerBaseModel):
        GroupByPrimaryField: Optional[model.MemberInfo]
        GroupBySecondaryField: Optional[model.MemberInfo]
        GroupByCustomField: Optional[model.CustomField]
    class WhereElement(ManagerBaseModel):
        WherePrimaryField: Optional[model.MemberInfo]
        WhereSecondaryField: Optional[model.MemberInfo]
        WhereCustomField: Optional[model.CustomField]
        StringOperator: Optional[model.StringOperator]
        String: Optional[str]
        DecimalOperator: Optional[model.DecimalOperator]
        Decimal: Optional[model.Decimal]
        BooleanOperator: Optional[model.BooleanOperator]
        ObjectOperator: Optional[model.ObjectOperator]
        Object: Optional[model.Object]
        DateOperator: Optional[model.DateOperator]
        StartDate: Optional[model.date]
        EndDate: Optional[model.date]
    Name: Optional[str]
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]
    Select: Optional[List[SelectElement]]
    HasWhere: Optional[bool]
    Where: Optional[List[WhereElement]]
    HasOrderBy: Optional[bool]
    OrderBy: Optional[List[OrderByElement]]
    HasGroupBy: Optional[bool]
    GroupBy: Optional[List[GroupByElement]]
    GroupsToCollapse: Optional[bool]


class Customer(Object):
    Guid: ClassVar[UUID] = "ec37c11e-2b67-49c6-8a58-6eccb7dd75ee"
    Name: Optional[str]
    Code: Optional[str]
    CreditLimit: Optional[model.Decimal]
    Currency: Optional[model.ForeignCurrency]
    BillingAddress: Optional[str]
    DeliveryAddress: Optional[str]
    Email: Optional[str]
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForCustomers]
    StartingBalance: Optional[model.Decimal]
    HasDefaultDueDateDays: Optional[bool]
    DefaultDueDateDays: Optional[int]
    HasDefaultHourlyRate: Optional[bool]
    DefaultHourlyRate: Optional[model.Decimal]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    HasDefaultBillingAddress: Optional[bool]


class CustomerPortal(Object):
    Guid: ClassVar[UUID] = "18048748-7c70-49e6-bed4-b9d310736956"
    Customer: Optional[model.Customer]
    SalesQuotes: Optional[bool]
    SalesOrders: Optional[bool]
    SalesInvoices: Optional[bool]
    CreditNotes: Optional[bool]
    DeliveryNotes: Optional[bool]


class CustomerStatementsTransactions(Object):
    Guid: ClassVar[UUID] = "c81ede5f-141e-4eb3-a586-1b0ab079cae6"
    FromDate: Optional[model.date]
    ToDate: Optional[model.DateType]
    ToCustomDate: Optional[model.date]
    Theme: Optional[model.Theme]


class CustomerStatementsUnpaidInvoices(Object):
    Guid: ClassVar[UUID] = "b9b3d678-a743-46e1-aaf5-fd1b27b5e20b"
    Date: Optional[model.DateType]
    CustomDate: Optional[model.date]
    Theme: Optional[model.Theme]


class CustomerSummary(Object):
    Guid: ClassVar[UUID] = "b8583039-fa11-441a-a727-40aa2311e74c"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Division: Optional[model.Division]


class DateAndNumberFormat(Object):
    Key = UUID("a56e89d1-7bee-4509-8b84-c9ebc3808b0c")
    class NumberFormatParts(ManagerBaseModel):
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
    Placement: Optional[List[model.CustomFieldsAttribute]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]


class DebitNote(Object):
    Guid: ClassVar[UUID] = "274fc6d0-2eac-43d0-8286-79c856e644aa"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        Account: Optional[model.IPurchaseInvoiceAccount]
        BillableExpenseCustomer: Optional[model.Customer]
        BillableExpenseSalesInvoice: Optional[model.SalesInvoice]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        Employee: Optional[model.Employee]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        PurchaseUnitPrice: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    IssueDate: Optional[model.date]
    Reference: Optional[str]
    Supplier: Optional[model.Supplier]
    PurchaseInvoice: Optional[model.PurchaseInvoice]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    PurchaseInventoryLocation: Optional[model.InventoryLocation]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    HasDebitNoteCustomTheme: Optional[bool]
    DebitNoteCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasDebitNoteFooters: Optional[bool]
    DebitNoteFooters: Optional[List[model.DebitNoteFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class DebitNoteFooter(Object):
    Guid: ClassVar[UUID] = "ae399a2e-95c0-4ef5-a32d-5cd8217d885a"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class DeliveryNote(Object):
    Guid: ClassVar[UUID] = "a0f6a539-f6a4-4a38-a69a-546a608a1f6d"
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
    DeliveryDate: Optional[model.date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    InvoiceNumber: Optional[str]
    InventoryLocation: Optional[model.InventoryLocation]
    Customer: Optional[model.Customer]
    SalesOrder: Optional[model.SalesOrder]
    SalesInvoice: Optional[model.SalesInvoice]
    DeliveryAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    HasLineNumber: Optional[bool]
    CustomTitle: Optional[bool]
    DeliveryNoteCustomTitle: Optional[str]
    HasDeliveryNoteCustomTheme: Optional[bool]
    DeliveryNoteCustomTheme: Optional[model.Theme]
    HasDeliveryNoteFooters: Optional[bool]
    DeliveryNoteFooters: Optional[List[model.DeliveryNoteFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    AutomaticReference: Optional[bool]


class DeliveryNoteColumns(Object):
    Guid: ClassVar[UUID] = "8e82c77b-b894-4df8-939d-9c6983eb58d4"
    class Column(ManagerBaseModel):
        Name: Optional[enums.DeliveryNoteColumns]
        CustomField: Optional[model.ICustomField]
        ClassicCustomField: Optional[model.CustomField]
    CustomColumns: Optional[bool]
    Columns: Optional[List[Column]]


class DeliveryNoteFooter(Object):
    Guid: ClassVar[UUID] = "fd737085-d270-4749-9274-7b458a2ec740"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class DepreciationCalculationWorksheet(Object):
    Guid: ClassVar[UUID] = "105604f5-5bc1-4bfa-a101-3c339c22989a"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class DepreciationEntry(Object):
    Guid: ClassVar[UUID] = "75cdc055-6dec-4381-bc40-b670366e6abc"
    class Line(ManagerBaseModel):
        FixedAsset: Optional[model.FixedAsset]
        Division: Optional[model.Division]
        Amount: Optional[model.Decimal]
    Date: Optional[model.date]
    Reference: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    AutomaticReference: Optional[bool]


class Division(Object):
    Guid: ClassVar[UUID] = "cc7fc110-e3e4-4b3b-823d-86c4a4cdabbc"
    Name: Optional[str]
    Inactive: Optional[bool]


class DivisionExceptionReport(Object):
    Guid: ClassVar[UUID] = "0e7711f8-1db1-4bcd-ac91-020d74a06dab"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class EinvoiceMe(Object):
    Guid: ClassVar[UUID] = "12e0885e-65c0-4a5c-85d6-98b4b3865518"
    Enabled: Optional[bool]
    Authorization: Optional[str]
    LastSync: Optional[int]


class EmailSettings(Object):
    Key = UUID("a4ddb0e3-b207-4fee-aa01-f104b6c09932")
    SmtpServer: Optional[str]
    Port: Optional[model.SmtpPort]
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
    Currency: Optional[model.ForeignCurrency]
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForEmployees]
    StartingBalance: Optional[model.StartingBalanceType]
    StartingBalanceAmount: Optional[model.Decimal]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    Inactive: Optional[bool]


class EmployeeEmailField(Object):
    Key = UUID("f66ab672-c1c6-4280-9439-bdb0a72b7619")


class EmployeeNameField(Object):
    Key = UUID("db71c44c-ec5a-4701-aa54-67ada72aff1a")


class EmployeeSummary(Object):
    Guid: ClassVar[UUID] = "e7b3a4f4-35d7-4f92-a8fc-e9eadbc140a8"
    Employee: Optional[model.Employee]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    ExcludeZeroBalances: Optional[bool]


class Equity(Object):
    Key = UUID("9275ff4c-4cff-41d0-b7b5-f31c783f03d8")
    Name: Optional[str]


class ExchangeRate(Object):
    Guid: ClassVar[UUID] = "14240c19-3d08-4fe6-94bb-6dd17c4bcda6"
    Date: Optional[model.date]
    Currency: Optional[model.ForeignCurrency]
    Type: Optional[model.ExchangeRateType]
    BaseRate: Optional[model.Decimal]
    CounterRate: Optional[model.Decimal]


class ExpenseClaim(Object):
    Guid: ClassVar[UUID] = "02572e0c-0167-4dbd-a392-08d8f67f3fe4"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        Account: Optional[model.IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[model.Customer]
        AccountsReceivableSalesInvoice: Optional[model.SalesInvoice]
        BillableExpenseCustomer: Optional[model.Customer]
        BillableExpenseSalesInvoice: Optional[model.SalesInvoice]
        AccountsPayableSupplier: Optional[model.Supplier]
        PurchaseInvoice: Optional[model.PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[model.Supplier]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        Employee: Optional[model.Employee]
        InventoryItem: Optional[model.InventoryItem]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        LineDescription: Optional[str]
        Qty: Optional[model.Decimal]
        PurchaseUnitPrice: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    Date: Optional[model.date]
    Reference: Optional[str]
    PaidBy: Optional[model.IExpenseClaimPayer]
    Payee: Optional[str]
    Currency: Optional[model.ForeignCurrency]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[model.InventoryLocation]
    AmountsIncludeTax: Optional[bool]
    HasLineDescription: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class ExpenseClaimsPayer(Object):
    Guid: ClassVar[UUID] = "563d7f9e-d64c-49ec-a938-e5531e72f4d8"
    Name: Optional[str]
    StartingBalance: Optional[model.StartingBalanceType]
    StartingBalanceAmount: Optional[model.Decimal]
    Division: Optional[model.Division]
    Inactive: Optional[bool]


class ExpenseClaimsSummary(Object):
    Guid: ClassVar[UUID] = "faa1756c-5aaf-4646-9f33-555e45e37efb"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class Extension(Object):
    Guid: ClassVar[UUID] = "9a8fc328-7553-469f-88ed-dc533f2160b2"
    Name: Optional[str]
    Script: Optional[str]
    Location: Optional[model.LocationType]
    CustomLocation: Optional[str]
    Inactive: Optional[bool]


class FixedAsset(Object):
    Guid: ClassVar[UUID] = "00082353-9fca-4ab4-91ae-20505479cbda"
    ItemCode: Optional[str]
    ItemName: Optional[str]
    DepreciationRate: Optional[model.Decimal]
    Description: Optional[str]
    Division: Optional[model.Division]
    ControlAccountForFixedAssets: Optional[model.ControlAccountForFixedAssets]
    ControlAccountForFixedAssetsAccumulatedDepreciation: Optional[model.ControlAccountForFixedAssetsAccumulatedDepreciation]
    StartingBalance: Optional[model.Decimal]
    StartingBalanceAccumulatedDepreciation: Optional[model.Decimal]
    CustomDepreciationExpenseAccount: Optional[bool]
    CustomDepreciationExpenseAccountSelection: Optional[model.ProfitAndLossStatementAccount]
    DisposedFixedAsset: Optional[bool]
    DisposalDate: Optional[model.date]
    CustomExpenseAccountForDisposal: Optional[model.ProfitAndLossStatementAccount]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class FixedAssetSummary(Object):
    Guid: ClassVar[UUID] = "0dbf7789-7a6f-4182-b641-6b8e561b4a9c"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class Folder(Object):
    Guid: ClassVar[UUID] = "5d6fae1e-ff34-4870-80e9-8a755842d46e"
    Description: Optional[str]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class Forecast(Object):
    Guid: ClassVar[UUID] = "821030a6-9820-4cba-8879-eda07853b9a6"
    class Line(ManagerBaseModel):
        Account: Optional[model.IJournalEntryAccount]
        Amount: Optional[model.Decimal]
    Date: Optional[model.date]
    Repeat: Optional[model.Repeat]
    Growth: Optional[model.Decimal]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    Inactive: Optional[bool]


class ForecastProfitAndLossStatement(Object):
    Guid: ClassVar[UUID] = "a513a0b4-24f2-49ac-a820-d116ab9d198a"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
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
    StartingExchangeRate: Optional[model.Decimal]
    Inactive: Optional[bool]


class FreightInItem(Object):
    Key = UUID("3458c24f-2a5f-4dcf-9de7-7340b1463d9c")


class GeneralLedgerSummary(Object):
    Guid: ClassVar[UUID] = "6c1d3132-7978-45c8-a6e2-2387c7de46b0"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class GeneralLedgerTransactions(Object):
    Guid: ClassVar[UUID] = "a3283b79-76be-44b6-9639-fa22d9b63246"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Account: Optional[model.IGeneralLedgerAccount]


class GoodsReceipt(Object):
    Guid: ClassVar[UUID] = "866217a4-f841-47de-a4e6-87152405c88d"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
    Date: Optional[model.date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    InvoiceNumber: Optional[str]
    Supplier: Optional[model.Supplier]
    PurchaseOrder: Optional[model.PurchaseOrder]
    PurchaseInvoice: Optional[model.PurchaseInvoice]
    InventoryLocation: Optional[model.InventoryLocation]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    HasLineNumber: Optional[bool]
    HasGoodsReceiptCustomTheme: Optional[bool]
    GoodsReceiptCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    HasGoodsReceiptFooters: Optional[bool]
    GoodsReceiptFooters: Optional[List[model.GoodsReceiptFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


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
    AmortizationRate: Optional[model.Decimal]
    Description: Optional[str]
    Division: Optional[model.Division]
    ControlAccountForIntangibleAssets: Optional[model.ControlAccountForIntangibleAssets]
    ControlAccountForIntangibleAssetsAccumulatedAmortization: Optional[model.ControlAccountForIntangibleAssetsAccumulatedAmortization]
    StartingBalance: Optional[model.Decimal]
    StartingBalanceAccumulatedAmortization: Optional[model.Decimal]
    CustomAmortizationExpenseAccount: Optional[bool]
    CustomAmortizationExpenseAccountSelection: Optional[model.ProfitAndLossStatementAccount]
    DisposedIntangibleAsset: Optional[bool]
    DisposalDate: Optional[model.date]
    CustomExpenseAccountForDisposal: Optional[model.ProfitAndLossStatementAccount]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class IntangibleAssetSummary(Object):
    Guid: ClassVar[UUID] = "d76b3a1a-bb37-4767-9f65-f0389ec9d5df"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Description: Optional[str]


class InterAccountTransfer(Object):
    Guid: ClassVar[UUID] = "dea4f923-c498-4504-b3ef-30be3c33175e"
    Date: Optional[model.date]
    Reference: Optional[str]
    description: Optional[str]
    paidFrom: Optional[model.IBankOrCashAccount]
    CreditAmount: Optional[model.Decimal]
    CreditClearStatus: Optional[model.BankAccountClearStatus]
    CreditClearDate: Optional[model.date]
    receivedIn: Optional[model.IBankOrCashAccount]
    DebitAmount: Optional[model.Decimal]
    DebitClearStatus: Optional[model.BankAccountClearStatus]
    DebitClearDate: Optional[model.date]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    HasInterAccountTransferFooters: Optional[bool]
    InterAccountTransferFooters: Optional[List[model.InterAccountTransferFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class InterAccountTransferFooter(Object):
    Guid: ClassVar[UUID] = "12479269-1209-4684-8d6a-ccc7a447fd62"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class InternalPdfGenerator(Object):
    Key = UUID("7e9fe6d7-d3a4-4456-981f-8112184b5517")
    Enabled: Optional[bool]
    PageSize: Optional[model.PageSize]


class InventoryItem(Object):
    Guid: ClassVar[UUID] = "0dbdbf8a-d80c-48e6-b453-bb7862445b7c"
    class StartingBalanceQuantity(ManagerBaseModel):
        Qty: Optional[model.Decimal]
        InventoryLocation: Optional[model.InventoryLocation]
    ItemCode: Optional[str]
    ItemName: Optional[str]
    UnitName: Optional[str]
    ProductionStage: Optional[int]
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForInventoryItems]
    StartingBalance: Optional[List[StartingBalanceQuantity]]
    StartingBalanceAverageCost: Optional[model.Decimal]
    TrackQuantityToReceive: Optional[bool]
    TrackQuantityToDeliver: Optional[bool]
    CustomIncomeAccount: Optional[bool]
    IncomeAccount: Optional[model.ProfitAndLossStatementAccount]
    CustomExpenseAccount: Optional[bool]
    ExpenseAccount: Optional[model.ProfitAndLossStatementAccount]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[model.Decimal]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[model.Decimal]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[model.Division]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    HasDefaultQty: Optional[bool]


class InventoryKit(Object):
    Guid: ClassVar[UUID] = "efc4f2cc-acf0-4815-a9a8-13bae00c6167"
    class Item(ManagerBaseModel):
        InventoryItem: Optional[model.InventoryItem]
        Qty: Optional[model.Decimal]
    ItemCode: Optional[str]
    ItemName: Optional[str]
    UnitName: Optional[str]
    BillOfMaterials: Optional[List[Item]]
    Division: Optional[model.Division]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[model.Decimal]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[model.Division]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    CustomIncomeAccount: Optional[bool]
    IncomeAccount: Optional[model.ProfitAndLossStatementAccount]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class InventoryLocation(Object):
    Guid: ClassVar[UUID] = "fae8151d-252e-45e3-b1f4-e048075b8983"
    Name: Optional[str]
    Inactive: Optional[bool]


class InventoryPriceList(Object):
    Guid: ClassVar[UUID] = "14da35e1-9b94-4403-8575-9d64ade4d7b4"
    Name: Optional[str]
    FilterByCustomField: Optional[bool]
    CustomField: Optional[model.CustomField]
    Filter: Optional[str]


class InventoryProfitMargin(Object):
    Guid: ClassVar[UUID] = "796da7cf-3551-4ff4-afad-942d4fc750cc"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]


class InventoryQuantityByLocation(Object):
    Guid: ClassVar[UUID] = "0e50586b-d1d0-40a3-81eb-8b6602e3050b"
    Date: Optional[model.date]
    Description: Optional[str]
    CustomInventoryLocations: Optional[bool]
    InventoryLocations: Optional[List[model.InventoryLocation]]


class InventoryQuantityMovement(Object):
    Guid: ClassVar[UUID] = "bd9e1f26-91e4-4c7b-b410-a62cb966bcfc"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    ExcludeItemsWithNoMovement: Optional[bool]


class InventoryTransfer(Object):
    Guid: ClassVar[UUID] = "7eaafddc-54c9-4235-98d2-e8a1ee438150"
    class Line(ManagerBaseModel):
        Item: Optional[model.InventoryItem]
        LineDescription: Optional[str]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
    Date: Optional[model.date]
    Reference: Optional[str]
    InventoryLocation: Optional[model.InventoryLocation]
    ToInventoryLocation: Optional[model.InventoryLocation]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    CustomFields: Optional[Dict[model.CustomField, str]]
    AutomaticReference: Optional[bool]
    CustomFields2: Optional[model.CustomFields]


class InventoryValueSummary(Object):
    Guid: ClassVar[UUID] = "7e9405f2-ed99-4891-8757-5c4c23cabdb2"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    ExcludeItemsWithNoMovement: Optional[bool]


class InventoryWriteOff(Object):
    Guid: ClassVar[UUID] = "d7ff6694-f1ef-419f-8ae2-55527a02e95f"
    class Item(ManagerBaseModel):
        InventoryItem: Optional[model.InventoryItem]
        Qty: Optional[model.Decimal]
    Date: Optional[model.date]
    Reference: Optional[str]
    Description: Optional[str]
    InventoryLocation: Optional[model.InventoryLocation]
    Items: Optional[List[Item]]
    Allocation: Optional[model.IInventoryWriteOffAccount]
    FixedAsset: Optional[model.FixedAsset]
    TaxCode: Optional[model.TaxCode]
    Project: Optional[model.Project]
    Division: Optional[model.Division]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class Investment(Object):
    Guid: ClassVar[UUID] = "a8f95068-fc73-43f7-aabb-fd868e506b51"
    Code: Optional[str]
    Name: Optional[str]
    ControlAccount: Optional[model.ControlAccountForInvestments]
    MarketPrice: Optional[model.Decimal]
    StartingBalance: Optional[model.Decimal]
    StartingBalanceTotalCost: Optional[model.Decimal]
    Inactive: Optional[bool]


class JournalEntry(Object):
    Guid: ClassVar[UUID] = "5ea52bc4-90ae-4e4a-aec4-ef1224b279ad"
    class Line(ManagerBaseModel):
        Account: Optional[model.IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[model.Customer]
        AccountsReceivableSalesInvoice: Optional[model.SalesInvoice]
        BillableExpenseCustomer: Optional[model.Customer]
        BillableExpenseSalesInvoice: Optional[model.SalesInvoice]
        AccountsPayableSupplier: Optional[model.Supplier]
        PurchaseInvoice: Optional[model.PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[model.Supplier]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        Employee: Optional[model.Employee]
        InventoryItem: Optional[model.InventoryItem]
        InventoryLocation: Optional[model.InventoryLocation]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        ExpenseClaimPayer: Optional[model.ExpenseClaimsPayer]
        Investment: Optional[model.Investment]
        LineDescription: Optional[str]
        Qty: Optional[model.Decimal]
        Debit: Optional[model.Decimal]
        Credit: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    Date: Optional[model.date]
    Reference: Optional[str]
    Currency: Optional[model.ForeignCurrency]
    Narration: Optional[str]
    Lines: Optional[List[Line]]
    ForTaxPurposesThisIs: Optional[model.TaxTransactionType]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    HasJournalEntryFooters: Optional[bool]
    JournalEntryFooters: Optional[List[model.JournalEntryFooter]]
    CashTransactionForCashFlowStatementPurposes: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    AutomaticReference: Optional[bool]


class JournalEntryFooter(Object):
    Guid: ClassVar[UUID] = "5be035ca-d96b-4e8d-b963-53340cf7f4f8"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class LatePaymentFee(Object):
    Guid: ClassVar[UUID] = "4dada073-022f-464e-bdb3-ff38c83e577f"
    Date: Optional[model.date]
    Customer: Optional[model.Customer]
    SalesInvoice: Optional[model.SalesInvoice]
    Amount: Optional[model.Decimal]


class Liabilities(Object):
    Key = UUID("ed5a19f6-12c5-45cc-b4b7-4e79f7ef50bc")


class LockDate(Object):
    Key = UUID("4c5dac8f-2d5e-4634-a51b-0bbdd021a499")
    LockAccountingPeriods: Optional[bool]
    Date: Optional[model.date]


class MemberInfo(Object):
    Key: Optional[str]


class MultipleValueCustomField(Object):
    Guid: ClassVar[UUID] = "f32774a9-f740-4c2b-8353-b321576f6166"
    class Option(ManagerBaseModel):
        Value: Optional[str]
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[model.CustomFieldsAttribute]]
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
    WhenSold: Optional[model.INonInventoryItemAccount]
    WhenPurchased: Optional[model.INonInventoryItemAccount]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[model.Decimal]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[model.Decimal]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[model.Division]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    HasDefaultQty: Optional[bool]


class NumberCustomField(Object):
    Guid: ClassVar[UUID] = "68e09438-7aa1-4d63-b7d3-ce2dcd052e88"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[model.CustomFieldsAttribute]]
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
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        Account: Optional[model.IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[model.Customer]
        AccountsReceivableSalesInvoice: Optional[model.SalesInvoice]
        BillableExpenseCustomer: Optional[model.Customer]
        BillableExpenseSalesInvoice: Optional[model.SalesInvoice]
        AccountsPayableSupplier: Optional[model.Supplier]
        PurchaseInvoice: Optional[model.PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[model.Supplier]
        Employee: Optional[model.Employee]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        ExpenseClaimsPayer: Optional[model.ExpenseClaimsPayer]
        Investment: Optional[model.Investment]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        PurchaseUnitPrice: Optional[model.Decimal]
        Amount: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    Date: Optional[model.date]
    Reference: Optional[str]
    PaidFrom: Optional[model.IBankOrCashAccount]
    Cleared: Optional[model.BankAccountClearStatus]
    BankClearDate: Optional[model.date]
    Payee: Optional[model.PayerPayeeType]
    Customer: Optional[model.Customer]
    Supplier: Optional[model.Supplier]
    Contact: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    FixedTotal: Optional[bool]
    FixedTotalAmount: Optional[model.Decimal]
    CustomTheme: Optional[bool]
    PaymentCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    PaymentCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPaymentFooters: Optional[bool]
    PaymentFooters: Optional[List[model.PaymentFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PaymentFooter(Object):
    Guid: ClassVar[UUID] = "6fbe0380-de89-4351-b5ac-eda06b5e7a80"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PaymentRule(Object):
    Guid: ClassVar[UUID] = "71ac4a94-6a53-4c0a-990c-e8174ab398d1"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        Account: Optional[model.IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[model.Customer]
        BillableExpenseCustomer: Optional[model.Customer]
        AccountsPayableSupplier: Optional[model.Supplier]
        WithholdingTaxPayableSupplier: Optional[model.Supplier]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        Employee: Optional[model.Employee]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        ExpenseClaimsPayer: Optional[model.ExpenseClaimsPayer]
        Investment: Optional[model.Investment]
        Description: Optional[str]
        Qty: Optional[model.Decimal]
        Amount: Optional[model.DiscountType]
        ExactAmount: Optional[model.Decimal]
        Percentage: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Division: Optional[model.Division]
    class Condition(ManagerBaseModel):
        AndDescriptionContains: Optional[str]
    IfBankAccountIs: Optional[model.BankOrCashAccount]
    AndAmountIs: Optional[model.AmountType]
    AndAmountIsAmount: Optional[model.Decimal]
    Conditions: Optional[List[Condition]]
    Payee: Optional[model.PayerPayeeType]
    Customer: Optional[model.Customer]
    Supplier: Optional[model.Supplier]
    OtherContact: Optional[str]
    Lines: Optional[List[Line]]
    DescriptionColumn: Optional[bool]
    QuantityColumn: Optional[bool]


class Payslip(Object):
    Guid: ClassVar[UUID] = "1d103fa7-6fc1-4951-811e-972968b842cc"
    class Earned(ManagerBaseModel):
        Item: Optional[model.PayslipEarningsItem]
        Description: Optional[str]
        Units: Optional[model.Decimal]
        UnitPrice: Optional[model.Decimal]
        Division: Optional[model.Division]
    class Deduction(ManagerBaseModel):
        Item: Optional[model.PayslipDeductionItem]
        Description: Optional[str]
        DeductionAmount: Optional[model.Decimal]
        Division: Optional[model.Division]
    class Contribution(ManagerBaseModel):
        Item: Optional[model.PayslipContributionItem]
        Description: Optional[str]
        ContributionAmount: Optional[model.Decimal]
        Division: Optional[model.Division]
    Date: Optional[model.date]
    Reference: Optional[str]
    description: Optional[str]
    employee: Optional[model.Employee]
    Earnings: Optional[List[Earned]]
    Deductions: Optional[List[Deduction]]
    Contributions: Optional[List[Contribution]]
    ShowTotalsForThePeriod: Optional[bool]
    TotalsPeriodStart: Optional[model.date]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    HasPayslipFooters: Optional[bool]
    PayslipFooters: Optional[List[model.PayslipFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PayslipContributionItem(Object):
    Guid: ClassVar[UUID] = "73af4c68-c347-4088-8846-758f1e7bc5bb"
    Name: Optional[str]
    ExpenseAccount: Optional[model.ProfitAndLossStatementAccount]
    LiabilityAccount: Optional[model.BalanceSheetAccount]
    ReportingCategory: Optional[model.PayslipContributionItemReportingCategory]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PayslipContributionItemReportingCategory(Object):
    Guid: ClassVar[UUID] = "ad4c002b-f4ea-4bf5-85cc-f65dd4398794"
    Name: Optional[str]
    Inactive: Optional[bool]


class PayslipDeductionItem(Object):
    Guid: ClassVar[UUID] = "0444eb18-6fc5-4d1f-be8b-c114da01832c"
    Name: Optional[str]
    Account: Optional[model.ICustomGeneralLedgerAccount]
    ReportingCategory: Optional[model.PayslipDeductionItemReportingCategory]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PayslipDeductionItemReportingCategory(Object):
    Guid: ClassVar[UUID] = "1ccb2c74-e9ed-4642-9687-bdf9f3403f3b"
    Name: Optional[str]
    Inactive: Optional[bool]


class PayslipEarningsItem(Object):
    Guid: ClassVar[UUID] = "ab02f6ab-c91c-4fc2-b979-66a6682c200e"
    Name: Optional[str]
    ExpenseAccount: Optional[model.ProfitAndLossStatementAccount]
    ReportingCategory: Optional[model.PayslipEarningsItemReportingCategory]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


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
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]


class PayslipTotalsPerItemAndEmployee(Object):
    Guid: ClassVar[UUID] = "13de6e5f-cacf-46a1-adb9-2250f76d77dd"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class ProductionOrder(Object):
    Guid: ClassVar[UUID] = "da996523-e77e-493c-b134-31c6c6ccae4a"
    class Item(ManagerBaseModel):
        BillOfMaterials: Optional[model.InventoryItem]
        Qty: Optional[model.Decimal]
    class ExpenseItem(ManagerBaseModel):
        Account: Optional[model.ICustomGeneralLedgerAccount]
        Amount: Optional[model.Decimal]
        Division: Optional[model.Division]
    Date: Optional[model.date]
    Reference: Optional[str]
    Description: Optional[str]
    FinishedInventoryItem: Optional[model.InventoryItem]
    Qty: Optional[model.Decimal]
    BillOfMaterials: Optional[List[Item]]
    InventoryLocation: Optional[model.InventoryLocation]
    AddNonInventoryCostIntoProduction: Optional[bool]
    ExpenseItems: Optional[List[ExpenseItem]]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    AutomaticReference: Optional[bool]


class ProfitAndLossStatement(Object):
    Guid: ClassVar[UUID] = "165c0392-9aad-4067-b855-a2393ead5df4"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        Division: Optional[model.Division]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    AccountingMethod: Optional[model.AccountingBasis]
    Rounding: Optional[model.Rounding]
    GroupsToCollapse: Optional[List[model.ProfitAndLossStatementGroup]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class ProfitAndLossStatementAccount(Object):
    Guid: ClassVar[UUID] = "26b9e4a5-ce10-4f30-94c7-23a1ca4428f9"
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    CashFlowStatement: Optional[model.CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    CashFlowStatementFinancingActivityGroup: Optional[model.CashFlowStatementFinancingActivityGroup]
    CashFlowStatementInvestingActivityGroup: Optional[model.CashFlowStatementInvestingActivityGroup]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    Position: Optional[int]
    Inactive: Optional[bool]


class ProfitAndLossStatementAccountBillableExpensesCost(Object):
    Key = UUID("234d263d-cf0e-4e3e-85ca-ef899016e58a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableExpensesInvoiced(Object):
    Key = UUID("1ae41f36-c83a-428c-be23-a99714110807")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableTimeInvoiced(Object):
    Key = UUID("8d86390b-b90f-4cf6-862b-9b4050449b91")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableTimeMovement(Object):
    Key = UUID("03d41bd1-8dd4-4ce3-9b82-5ce17a40171a")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountCurrencyGainsLosses(Object):
    Key = UUID("635ddd64-1176-4d35-b1c2-2d7d3bb12bb6")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    CashFlowStatementGroup: Optional[model.CashFlowStatementOperatingActivityGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountFixedAssetDepreciation(Object):
    Key = UUID("fb6fdbfd-b39f-4674-8928-10c2bdd87e58")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountFixedAssetLossOnDisposal(Object):
    Key = UUID("428ea9ba-4679-4568-b05b-7fcf62504893")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountIntangibleAssetsAmortization(Object):
    Key = UUID("83d56444-fed8-4de8-8e58-e325a370ae44")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal(Object):
    Key = UUID("43e14984-202e-4e9e-b843-d417dddcd3d2")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountInventoryPurchases(Object):
    Key = UUID("aa80b662-3642-4c08-b328-2fccf132ceb1")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountInventorySales(Object):
    Key = UUID("ea44f579-9548-4954-baf0-48538aceff1e")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[model.TaxCode]
    Position: Optional[int]


class ProfitAndLossStatementAccountLatePaymentFees(Object):
    Key = UUID("841b2acb-8bb5-4742-864e-4226fa421f44")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementAccountRoundingExpense(Object):
    Key = UUID("2aa99eac-faca-4017-a157-edbbbcb160ac")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementActualVsBudget(Object):
    Guid: ClassVar[UUID] = "25c7aa0e-536c-42be-a75c-1b5ac71e955a"
    class BudgetItem(ManagerBaseModel):
        Account: Optional[model.IProfitAndLossAccount]
        Amount: Optional[model.Decimal]
    Title: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]
    Division: Optional[model.Division]
    Lines: Optional[List[BudgetItem]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    RoundDecimals: Optional[bool]


class ProfitAndLossStatementCapitalGainsOnInvestments(Object):
    Key = UUID("de8d014f-e862-4ab5-88cc-335d464315a6")
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class ProfitAndLossStatementGroup(Object):
    Guid: ClassVar[UUID] = "5770616c-0e01-46ca-a172-f7042275da6c"
    Name: Optional[str]
    Type: Optional[model.ProfitAndLossStatementGroupType]
    ParentGroup: Optional[model.ProfitAndLossStatementGroup]
    Position: Optional[int]


class Project(Object):
    Guid: ClassVar[UUID] = "5170f738-cfba-42e3-bb8e-a7d5c5ab66f2"
    Name: Optional[str]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PurchaseInvoice(Object):
    Guid: ClassVar[UUID] = "58b9eb90-f6b8-4abc-8ea1-12fd77b8336e"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        Account: Optional[model.IPurchaseInvoiceAccount]
        BillableExpenseCustomer: Optional[model.Customer]
        BillableExpenseSalesInvoice: Optional[model.SalesInvoice]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        Employee: Optional[model.Employee]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        PurchaseUnitPrice: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    IssueDate: Optional[model.date]
    DueDate: Optional[model.DueDateType]
    DueDateDays: Optional[int]
    DueDateDate: Optional[model.date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    Supplier: Optional[model.Supplier]
    PurchaseQuote: Optional[model.PurchaseQuote]
    PurchaseOrder: Optional[model.PurchaseOrder]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    PurchaseInventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsIncludeTax: Optional[bool]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    HasPurchaseInvoiceCustomTheme: Optional[bool]
    PurchaseInvoiceCustomTheme: Optional[model.Theme]
    HideBalanceDue: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseInvoiceFooters: Optional[bool]
    PurchaseInvoiceFooters: Optional[List[model.PurchaseInvoiceFooter]]
    ClosedInvoice: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PurchaseInvoiceFooter(Object):
    Guid: ClassVar[UUID] = "06205221-f856-402f-8df9-104942cf579a"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PurchaseOrder(Object):
    Guid: ClassVar[UUID] = "a26bbea1-57aa-4fd9-b7c9-e26b83114385"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        PurchaseUnitPrice: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
    Date: Optional[model.date]
    Reference: Optional[str]
    Supplier: Optional[model.Supplier]
    PurchaseQuote: Optional[model.PurchaseQuote]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    TrackQuantityToReceive: Optional[bool]
    HasPurchaseOrderCustomTheme: Optional[bool]
    PurchaseOrderCustomTheme: Optional[model.Theme]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseOrderFooters: Optional[bool]
    PurchaseOrderFooters: Optional[List[model.PurchaseOrderFooter]]
    Cancelled: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    AutomaticReference: Optional[bool]


class PurchaseOrderFooter(Object):
    Guid: ClassVar[UUID] = "38104c9e-7805-47de-935e-f6b660a470de"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PurchaseQuote(Object):
    Guid: ClassVar[UUID] = "38d606f7-6358-4ace-9d1d-f6c0b9ea9d68"
    class Line(ManagerBaseModel):
        Item: Optional[model.IPurchaseItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        PurchaseUnitPrice: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
    Date: Optional[model.date]
    Reference: Optional[str]
    Supplier: Optional[model.Supplier]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    RequestForQuotation: Optional[bool]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    HasPurchaseQuoteCustomTheme: Optional[bool]
    PurchaseQuoteCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    Cancelled: Optional[bool]
    CustomTitle: Optional[bool]
    PurchaseQuoteCustomTitle: Optional[str]
    RequestForQuotationCustomTitleOption: Optional[bool]
    RequestForQuotationCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseQuoteFooters: Optional[bool]
    PurchaseQuoteFooters: Optional[List[model.PurchaseQuoteFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class PurchaseQuoteFooter(Object):
    Guid: ClassVar[UUID] = "072dd522-a137-4e91-8966-93f56f987cda"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Receipt(Object):
    Guid: ClassVar[UUID] = "7662b887-c8d8-486e-98fd-f9dbcd41c6dc"
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        Account: Optional[model.IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[model.Customer]
        AccountsReceivableSalesInvoice: Optional[model.SalesInvoice]
        BillableExpenseCustomer: Optional[model.Customer]
        BillableExpenseSalesInvoice: Optional[model.SalesInvoice]
        AccountsPayableSupplier: Optional[model.Supplier]
        PurchaseInvoice: Optional[model.PurchaseInvoice]
        WithholdingTaxPayableSupplier: Optional[model.Supplier]
        Employee: Optional[model.Employee]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        ExpenseClaimsPayer: Optional[model.ExpenseClaimsPayer]
        Investment: Optional[model.Investment]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        SalesUnitPrice: Optional[model.Decimal]
        Amount: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    Date: Optional[model.date]
    Reference: Optional[str]
    PaidBy: Optional[model.PayerPayeeType]
    Customer: Optional[model.Customer]
    Supplier: Optional[model.Supplier]
    Contact: Optional[str]
    ReceivedIn: Optional[model.IBankOrCashAccount]
    Cleared: Optional[model.BankAccountClearStatus]
    BankClearDate: Optional[model.date]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    FixedTotal: Optional[bool]
    FixedTotalAmount: Optional[model.Decimal]
    CustomTheme: Optional[bool]
    ReceiptCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    ReceiptCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasReceiptFooters: Optional[bool]
    ReceiptFooters: Optional[List[model.ReceiptFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class ReceiptColumns(Object):
    Guid: ClassVar[UUID] = "ab9df426-967c-4851-92e8-d45e3188fc9c"
    Columns: Optional[List[model.Column]]


class ReceiptFooter(Object):
    Guid: ClassVar[UUID] = "b4053b7c-b07a-45ba-aa14-1e3a624f8565"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class ReceiptRule(Object):
    Guid: ClassVar[UUID] = "72ed576f-e78b-41eb-8188-73285f32c2d2"
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        Account: Optional[model.IJournalEntryAccount]
        AccountsReceivableCustomer: Optional[model.Customer]
        BillableExpenseCustomer: Optional[model.Customer]
        AccountsPayableSupplier: Optional[model.Supplier]
        WithholdingTaxPayableSupplier: Optional[model.Supplier]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        Employee: Optional[model.Employee]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        ExpenseClaimsPayer: Optional[model.ExpenseClaimsPayer]
        Investment: Optional[model.Investment]
        Description: Optional[str]
        Qty: Optional[model.Decimal]
        Amount: Optional[model.DiscountType]
        ExactAmount: Optional[model.Decimal]
        Percentage: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Division: Optional[model.Division]
    class Condition(ManagerBaseModel):
        AndDescriptionContains: Optional[str]
    IfBankAccountIs: Optional[model.BankOrCashAccount]
    AndAmountIs: Optional[model.AmountType]
    AndAmountIsAmount: Optional[model.Decimal]
    Conditions: Optional[List[Condition]]
    PaidBy: Optional[model.PayerPayeeType]
    Customer: Optional[model.Customer]
    Supplier: Optional[model.Supplier]
    OtherContact: Optional[str]
    Lines: Optional[List[Line]]
    DescriptionColumn: Optional[bool]
    QuantityColumn: Optional[bool]


class ReceiptsAndPaymentsSummary(Object):
    Guid: ClassVar[UUID] = "fa775461-39a2-46a2-b022-adcad6c9b830"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    AccountCodes: Optional[bool]


class RecurringInterAccountTransfer(Object):
    Guid: ClassVar[UUID] = "10ac4ab8-df74-4faf-b7fc-eb343556fb1b"
    nextIssueDate: Optional[model.date]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    description: Optional[str]
    paidFrom: Optional[model.IBankOrCashAccount]
    CreditAmount: Optional[model.Decimal]
    CreditClearStatus: Optional[model.BankAccountClearStatus]
    CreditClearDate: Optional[model.date]
    receivedIn: Optional[model.IBankOrCashAccount]
    DebitAmount: Optional[model.Decimal]
    DebitClearStatus: Optional[model.BankAccountClearStatus]
    DebitClearDate: Optional[model.date]
    AutomaticReference: Optional[bool]
    HasInterAccountTransferFooters: Optional[bool]
    InterAccountTransferFooters: Optional[List[model.InterAccountTransferFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringJournalEntry(Object):
    Guid: ClassVar[UUID] = "b4c1b390-351e-4579-b43b-412b920cddaf"
    NextIssueDate: Optional[model.date]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    Currency: Optional[model.ForeignCurrency]
    Narration: Optional[str]
    Lines: Optional[List[model.JournalEntry.Line]]
    InventoryLocation: Optional[model.InventoryLocation]
    ForTaxPurposesThisIs: Optional[model.TaxTransactionType]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    HasJournalEntryFooters: Optional[bool]
    JournalEntryFooters: Optional[List[model.JournalEntryFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringPayment(Object):
    Guid: ClassVar[UUID] = "789d22dc-bc42-4952-a591-60123b344726"
    NextIssueDate: Optional[model.date]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    PaidFrom: Optional[model.IBankOrCashAccount]
    Cleared: Optional[model.BankAccountClearStatus]
    Payee: Optional[model.PayerPayeeType]
    Customer: Optional[model.Customer]
    Supplier: Optional[model.Supplier]
    Contact: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[model.Payment.Line]]
    InventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    PaymentCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPaymentFooters: Optional[bool]
    PaymentFooters: Optional[List[model.PaymentFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringPayslip(Object):
    Guid: ClassVar[UUID] = "ae6e14e3-1d3d-4996-b466-ba41732a8dbe"
    nextIssueDate: Optional[model.date]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    employee: Optional[model.Employee]
    description: Optional[str]
    Earnings: Optional[List[model.Payslip.Earned]]
    Deductions: Optional[List[model.Payslip.Deduction]]
    Contributions: Optional[List[model.Payslip.Contribution]]
    ShowTotalsForThePeriod: Optional[bool]
    TotalsPeriodStart: Optional[model.date]
    CustomTheme: Optional[bool]
    Theme: Optional[model.Theme]
    HasPayslipFooters: Optional[bool]
    PayslipFooters: Optional[List[model.PayslipFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    NextIssueDate: Optional[model.date]


class RecurringPurchaseInvoice(Object):
    Guid: ClassVar[UUID] = "11de04ac-c448-4665-b206-8aa631e63532"
    NextIssueDate: Optional[model.date]
    DueDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    Supplier: Optional[model.Supplier]
    PurchaseOrder: Optional[model.PurchaseOrder]
    Description: Optional[str]
    Lines: Optional[List[model.PurchaseInvoice.Line]]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    AmountsIncludeTax: Optional[bool]
    AutomaticReference: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    HasPurchaseInvoiceCustomTheme: Optional[bool]
    PurchaseInvoiceCustomTheme: Optional[model.Theme]
    HasPurchaseInvoiceFooters: Optional[bool]
    PurchaseInvoiceFooters: Optional[List[model.PurchaseInvoiceFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringPurchaseOrder(Object):
    Guid: ClassVar[UUID] = "3be38758-7bf2-46f1-84a5-34e8748cade0"
    NextIssueDate: Optional[model.date]
    DueDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    Supplier: Optional[model.Supplier]
    Description: Optional[str]
    Lines: Optional[List[model.PurchaseOrder.Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    TrackQuantityToReceive: Optional[bool]
    HasPurchaseOrderCustomTheme: Optional[bool]
    PurchaseOrderCustomTheme: Optional[model.Theme]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseOrderFooters: Optional[bool]
    PurchaseOrderFooters: Optional[List[model.PurchaseOrderFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringReceipt(Object):
    Guid: ClassVar[UUID] = "1c7ecd01-eb32-47b1-8ccd-e85f77969b03"
    NextIssueDate: Optional[model.date]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    PaidBy: Optional[model.PayerPayeeType]
    Customer: Optional[model.Customer]
    Supplier: Optional[model.Supplier]
    Contact: Optional[str]
    ReceivedIn: Optional[model.IBankOrCashAccount]
    Cleared: Optional[model.BankAccountClearStatus]
    Description: Optional[str]
    Lines: Optional[List[model.Receipt.Line]]
    InventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    ReceiptCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasReceiptFooters: Optional[bool]
    ReceiptFooters: Optional[List[model.ReceiptFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringSalesInvoice(Object):
    Guid: ClassVar[UUID] = "81385989-81e5-48c7-a819-c344324c1c01"
    NextIssueDate: Optional[model.date]
    DueDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    Customer: Optional[model.Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[model.SalesInvoice.Line]]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[model.RoundingMethod]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxRate: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    HasSalesInvoiceCustomTheme: Optional[bool]
    SalesInvoiceCustomTheme: Optional[model.Theme]
    EarlyPaymentDiscount: Optional[bool]
    EarlyPaymentDiscountType: Optional[model.DiscountType]
    EarlyPaymentDiscountRate: Optional[model.Decimal]
    EarlyPaymentDiscountAmount: Optional[model.Decimal]
    EarlyPaymentDiscountDays: Optional[int]
    LatePaymentFees: Optional[bool]
    LatePaymentFeesPercentage: Optional[model.Decimal]
    CustomTitle: Optional[bool]
    SalesInvoiceCustomTitle: Optional[str]
    TotalAmountInWords: Optional[bool]
    HideDueDate: Optional[bool]
    HasSalesInvoiceFooters: Optional[bool]
    SalesInvoiceFooters: Optional[List[model.SalesInvoiceFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringSalesOrder(Object):
    Guid: ClassVar[UUID] = "dd7d5b17-c4be-4369-b0f5-79361525f3c2"
    NextIssueDate: Optional[model.date]
    ExpiryDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    Customer: Optional[model.Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[model.SalesOrder.Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    TrackQuantityToDeliver: Optional[bool]
    HasSalesOrderCustomTheme: Optional[bool]
    SalesOrderCustomTheme: Optional[model.Theme]
    ShowTaxAmountColumn: Optional[bool]
    CustomTitle: Optional[bool]
    SalesOrderCustomTitle: Optional[str]
    HasSalesOrderFooters: Optional[bool]
    SalesOrderFooters: Optional[List[model.SalesOrderFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class RecurringSalesQuote(Object):
    Guid: ClassVar[UUID] = "1ca6ee3a-3583-41d8-83b1-74ac9129e1c1"
    NextIssueDate: Optional[model.date]
    ExpiryDate: Optional[int]
    Interval: Optional[int]
    PeriodType: Optional[model.Period]
    ExpirationType: Optional[model.ExpirationType]
    UntilDate: Optional[model.date]
    Customer: Optional[model.Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[model.SalesQuote.Line]]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[model.RoundingMethod]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    HideTotalAmount: Optional[bool]
    HasSalesQuoteCustomTheme: Optional[bool]
    SalesQuoteCustomTheme: Optional[model.Theme]
    CustomTitle: Optional[bool]
    SalesQuoteCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesQuoteFooters: Optional[bool]
    SalesQuoteFooters: Optional[List[model.SalesQuoteFooter]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class ReportTranformationFromDate(Object):
    Key = UUID("cef33379-d1b3-4172-b090-0fc24cf978da")


class ReportTranformationToDate(Object):
    Key = UUID("8ba7e5e7-8f74-443a-b7ee-d8539b12e7e2")


class ReportTransformation2(Object):
    Guid: ClassVar[UUID] = "02c3fbc6-4473-436f-b58d-fd51937f4e77"
    class Item(ManagerBaseModel):
        Name: Optional[str]
        Column1: Optional[List[model.IReportingCategory]]
        Column2: Optional[List[model.IReportingCategory]]
        Column3: Optional[List[model.IReportingCategory]]
        Column4: Optional[List[model.IReportingCategory]]
        Column5: Optional[List[model.IReportingCategory]]
    class InstructionStep(ManagerBaseModel):
        Text: Optional[str]
    Name: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Employee: Optional[model.Employee]
    Columns: Optional[model.ColumnCount]
    Items2: Optional[List[Item]]
    AccountingMethod: Optional[bool]
    AccountingMethodOption: Optional[model.AccountingBasis]
    Suppliers: Optional[bool]
    SupplierCustomField: Optional[model.CustomField]
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
    ReportTransformation: Optional[model.ReportTransformation2]
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]
    Employee: Optional[model.Employee]


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
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        Account: Optional[model.ISalesInvoiceAccount]
        CapitalAccount: Optional[model.CapitalAccount]
        SubAccount: Optional[model.SubAccount]
        SpecialAccount: Optional[model.SpecialAccount]
        FixedAsset: Optional[model.FixedAsset]
        IntangibleAsset: Optional[model.IntangibleAsset]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        SalesUnitPrice: Optional[model.Decimal]
        CurrencyAmount: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
        Project: Optional[model.Project]
        Division: Optional[model.Division]
    IssueDate: Optional[model.date]
    DueDate: Optional[model.DueDateType]
    DueDateDays: Optional[int]
    DueDateDate: Optional[model.date]
    Reference: Optional[str]
    QuoteNumber: Optional[str]
    OrderNumber: Optional[str]
    Customer: Optional[model.Customer]
    SalesQuote: Optional[model.SalesQuote]
    SalesOrder: Optional[model.SalesOrder]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    SalesInventoryLocation: Optional[model.InventoryLocation]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[model.RoundingMethod]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    EarlyPaymentDiscount: Optional[bool]
    EarlyPaymentDiscountType: Optional[model.DiscountType]
    EarlyPaymentDiscountRate: Optional[model.Decimal]
    EarlyPaymentDiscountAmount: Optional[model.Decimal]
    EarlyPaymentDiscountDays: Optional[int]
    LatePaymentFees: Optional[bool]
    LatePaymentFeesPercentage: Optional[model.Decimal]
    TotalAmountInWords: Optional[bool]
    TotalAmountInBaseCurrency: Optional[bool]
    Bilingual: Optional[bool]
    CustomTitle: Optional[bool]
    SalesInvoiceCustomTitle: Optional[str]
    HasSalesInvoiceCustomTheme: Optional[bool]
    SalesInvoiceCustomTheme: Optional[model.Theme]
    AutomaticReference: Optional[bool]
    HideDueDate: Optional[bool]
    HideBalanceDue: Optional[bool]
    ClosedInvoice: Optional[bool]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesInvoiceFooters: Optional[bool]
    SalesInvoiceFooters: Optional[List[model.SalesInvoiceFooter]]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class SalesInvoiceFooter(Object):
    Guid: ClassVar[UUID] = "eaaee0ba-9c58-4f7b-a800-2857f0a675af"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class SalesInvoiceTotalsByCustomField(Object):
    Guid: ClassVar[UUID] = "8ea7ac48-0071-4e58-8647-c1f9b17f1dc6"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Name: Optional[str]
    CustomField: Optional[model.CustomField]
    Periods: Optional[List[Period]]


class SalesInvoiceTotalsByCustomer(Object):
    Guid: ClassVar[UUID] = "997f3bd6-37ee-4b36-b066-2bb0a402ebab"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class SalesInvoiceTotalsByItem(Object):
    Guid: ClassVar[UUID] = "c70ca645-2d2b-4536-8f81-aead1b7eba99"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class SalesOrder(Object):
    Guid: ClassVar[UUID] = "2dac5598-128d-4954-b2e4-21515047b3a7"
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        SalesUnitPrice: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
    Date: Optional[model.date]
    Reference: Optional[str]
    Customer: Optional[model.Customer]
    SalesQuote: Optional[model.SalesQuote]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    TrackQuantityToDeliver: Optional[bool]
    HasSalesOrderCustomTheme: Optional[bool]
    SalesOrderCustomTheme: Optional[model.Theme]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    CustomTitle: Optional[bool]
    SalesOrderCustomTitle: Optional[str]
    HasSalesOrderFooters: Optional[bool]
    SalesOrderFooters: Optional[List[model.SalesOrderFooter]]
    Cancelled: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class SalesOrderFooter(Object):
    Guid: ClassVar[UUID] = "38bf923a-9ab8-4d86-a12a-9d2581d13fa8"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class SalesQuote(Object):
    Guid: ClassVar[UUID] = "ba89de75-cb87-4bde-b20f-314f01b31037"
    class Line(ManagerBaseModel):
        Item: Optional[model.ISaleItem]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[model.CustomField, str]]
        CustomFields2: Optional[model.CustomFields]
        Qty: Optional[model.Decimal]
        SalesUnitPrice: Optional[model.Decimal]
        DiscountPercentage: Optional[model.Decimal]
        DiscountAmount: Optional[model.Decimal]
        TaxCode: Optional[model.TaxCode]
    IssueDate: Optional[model.date]
    ExpiryDate: Optional[int]
    Reference: Optional[str]
    Customer: Optional[model.Customer]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    AmountsIncludeTax: Optional[bool]
    Rounding: Optional[bool]
    RoundingMethod: Optional[model.RoundingMethod]
    HasLineNumber: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[model.DiscountType]
    WithholdingTax: Optional[bool]
    WithholdingTaxType: Optional[model.WithholdingTaxType]
    WithholdingTaxPercentage: Optional[model.Decimal]
    WithholdingTaxAmount: Optional[model.Decimal]
    HideTotalAmount: Optional[bool]
    HasSalesQuoteCustomTheme: Optional[bool]
    SalesQuoteCustomTheme: Optional[model.Theme]
    CustomTitle: Optional[bool]
    SalesQuoteCustomTitle: Optional[str]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesQuoteFooters: Optional[bool]
    SalesQuoteFooters: Optional[List[model.SalesQuoteFooter]]
    Cancelled: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class SalesQuoteFooter(Object):
    Guid: ClassVar[UUID] = "d95df676-e2cb-4be6-a9b3-86dcd79ac3bc"
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Schema(Object):
    Guid: ClassVar[UUID] = "a9a71e47-82b3-49db-8aec-898adb460a80"
    Version: Optional[int]


class Session(Object):
    Key: Optional[model.UUID]
    Timestamp: Optional[model.date]
    UserAgent: Optional[str]
    Location: Optional[str]


class SetZeroIfNegativeReportingCategory(Object):
    Key = UUID("1a94b65c-4869-4138-acc1-49d16bbfeed6")


class SpecialAccount(Object):
    Guid: ClassVar[UUID] = "e495f4e8-5fad-48ac-8a66-f35049ac4ef3"
    Name: Optional[str]
    Code: Optional[str]
    Currency: Optional[model.ForeignCurrency]
    TaxCode: Optional[model.TaxCode]
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForSpecialAccounts]
    StartingBalance: Optional[model.Decimal]
    StartingBalanceType: Optional[model.DebitCredit]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


class StatementOfChangesInEquity(Object):
    Guid: ClassVar[UUID] = "06d97eb4-27de-41ee-80ef-47b8115b5b36"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    AccountingMethod: Optional[model.AccountingBasis]
    Rounding: Optional[model.Rounding]
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
    FromDate: Optional[model.date]
    ToDate: Optional[model.DateType]
    ToDateValue: Optional[model.date]
    ShowBalancesOnCashBasis: Optional[bool]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]
    HasGroupsToCollapse: Optional[bool]
    GroupsToCollapse: Optional[List[model.ChartOfAccountsGroup]]


class Supplier(Object):
    Guid: ClassVar[UUID] = "6d2dc48d-2053-4e45-8330-285ebd431242"
    Name: Optional[str]
    Code: Optional[str]
    CreditLimit: Optional[model.Decimal]
    Currency: Optional[model.ForeignCurrency]
    Address: Optional[str]
    Email: Optional[str]
    Division: Optional[model.Division]
    ControlAccount: Optional[model.ControlAccountForSuppliers]
    StartingBalance: Optional[model.Decimal]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]
    Inactive: Optional[bool]


class SupplierNameField(Object):
    Key = UUID("22ec22e1-8ed2-4cba-a5b9-533a1e451977")


class SupplierStatementsTransactions(Object):
    Guid: ClassVar[UUID] = "401d5f3c-92ef-47da-942a-3cd6cf64aa9c"
    FromDate: Optional[model.date]
    ToDate: Optional[model.DateType]
    ToCustomDate: Optional[model.date]
    Theme: Optional[model.Theme]


class SupplierStatementsUnpaidInvoices(Object):
    Guid: ClassVar[UUID] = "119e71a0-3ea5-4c6f-a8f2-76384b86831a"
    Date: Optional[model.DateType]
    CustomDate: Optional[model.date]
    Theme: Optional[model.Theme]


class SupplierSummary(Object):
    Guid: ClassVar[UUID] = "80d4616c-d083-4f8a-9ea9-b9dd5f04360f"
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    Division: Optional[model.Division]


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
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]


class TaxCode(Object):
    Guid: ClassVar[UUID] = "7f368d97-8b7f-4b39-b156-dc66afd9496a"
    class Component(ManagerBaseModel):
        Name: Optional[str]
        ComponentRate: Optional[model.Decimal]
        ComponentAccount: Optional[model.BalanceSheetAccount]
        ComponentTaxAmountReportingCategory: Optional[model.TaxAmountReportingCategory]
        ComponentTaxAmountReversedReportingCategory: Optional[model.TaxAmountReversedReportingCategory]
        TaxCode: Optional[model.TaxCode]
    Name: Optional[str]
    Label: Optional[str]
    ReportingCategory: Optional[model.TaxCodeReportingCategory]
    ReportingCategoryReversed: Optional[model.TaxCodeReversedReportingCategory]
    TaxRate: Optional[model.TaxRate]
    Type: Optional[model.TaxRateType]
    Rate: Optional[model.Decimal]
    Account: Optional[model.BalanceSheetAccount]
    TaxAmountReportingCategory: Optional[model.TaxAmountReportingCategory]
    TaxAmountReversedReportingCategory: Optional[model.TaxAmountReversedReportingCategory]
    Components: Optional[List[Component]]
    ReverseCharged: Optional[bool]
    CustomSalesInvoiceTitle: Optional[bool]
    SalesInvoiceTitle: Optional[str]
    CustomCreditNoteTitle: Optional[bool]
    CreditNoteTitle: Optional[str]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


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
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
    Description: Optional[str]
    AccountingMethod: Optional[model.AccountingBasis]
    Periods: Optional[List[Period]]


class TaxSummary(Object):
    Guid: ClassVar[UUID] = "68e0d57b-4a59-453e-b8d4-6166f097eacd"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]
    Division: Optional[model.Division]


class TaxTransactions(Object):
    Guid: ClassVar[UUID] = "9a441483-1a09-46d3-aecd-477c91c13ae1"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]


class TaxablePurchasesPerSupplier(Object):
    Guid: ClassVar[UUID] = "1f957bf2-d198-4a9a-bb51-8d7d26b2fc5c"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]


class TaxableSalesPerCustomer(Object):
    Guid: ClassVar[UUID] = "2623ae0a-3c13-45e7-83b7-e4c9b2b9404d"
    Description: Optional[str]
    FromDate: Optional[model.date]
    ToDate: Optional[model.date]
    AccountingMethod: Optional[model.AccountingBasis]


class TextCustomField(Object):
    Guid: ClassVar[UUID] = "411f5975-0376-4ba9-b7ff-5bb2baa6f69f"
    Name: Optional[str]
    Position: Optional[int]
    Placement: Optional[List[model.CustomFieldsAttribute]]
    Type: Optional[model.TextCustomFieldType]
    OptionsForDropdownList: Optional[str]
    Size: Optional[model.CustomFieldSize]
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


class TrialBalance(Object):
    Guid: ClassVar[UUID] = "e5dc98ef-4662-4a68-8a9d-b3e2d12b55d6"
    class Period(ManagerBaseModel):
        FromDate: Optional[model.date]
        ToDate: Optional[model.date]
        Division: Optional[model.Division]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    AccountingMethod: Optional[model.AccountingBasis]
    Periods: Optional[List[Period]]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class User(Object):
    Guid: ClassVar[UUID] = "8112e1a9-fe00-47c4-9d7a-2d034f8a1f34"
    Name: Optional[str]
    Username: Optional[str]
    Password: Optional[str]
    Type: Optional[model.UserType]
    Businesses: Optional[List[str]]
    Sessions: Optional[List[model.Session]]


class UserPermissions(Object):
    Guid: ClassVar[UUID] = "c6a5d19f-6f47-4716-841d-ba06ca9fc311"
    Username: Optional[str]
    BankAndCashAccounts: Optional[List[model.IBankOrCashAccount]]
    AccessType: Optional[model.UserPermissionsAccessType]
    Namespaces: Optional[Dict[str, bool]]
    Namespaces2: Optional[Dict[str, model.PermittedActions]]
    FullAccess: Optional[bool]


class WithholdingTaxReceipt(Object):
    Guid: ClassVar[UUID] = "8f7510d9-a92d-4b4c-9421-fd745e198b3c"
    Date: Optional[model.date]
    Customer: Optional[model.Customer]
    Amount: Optional[model.Decimal]
    Description: Optional[str]
    CustomFields: Optional[Dict[model.CustomField, str]]
    CustomFields2: Optional[model.CustomFields]


__all__ = [
    "AgedPayables",
    "AgedReceivables",
    "AmortizationCalculationWorksheet",
    "AmortizationEntry",
    "Assets",
    "Attachment",
    "BalanceSheet",
    "BalanceSheetAbstractGroup",
    "BalanceSheetAccount",
    "BalanceSheetAccountsPayableAccount",
    "BalanceSheetAccountsReceivableAccount",
    "BalanceSheetBillableExpensesAccount",
    "BalanceSheetBillableTimeAccount",
    "BalanceSheetCapitalAccountsAccount",
    "BalanceSheetCashAtBankAccount",
    "BalanceSheetEmployeeClearingAccount",
    "BalanceSheetExpenseClaimsAccount",
    "BalanceSheetFixedAssetsAccumulatedDepreciationAccount",
    "BalanceSheetFixedAssetsAtCostAccount",
    "BalanceSheetGroup",
    "BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount",
    "BalanceSheetIntangibleAssetsAtCostAccount",
    "BalanceSheetInterdivisionalLoan",
    "BalanceSheetInventoryOnHandAccount",
    "BalanceSheetInvestmentsAccount",
    "BalanceSheetProductionInProgressAccount",
    "BalanceSheetRetainedEarningsAccount",
    "BalanceSheetSpecialAccountsAccount",
    "BalanceSheetSuspenseAccount",
    "BalanceSheetTaxPayableAccount",
    "BalanceSheetWithholdingTaxAccount",
    "BalanceSheetWithholdingTaxPayableAccount",
    "BalanceSheetWithholdingTaxReceivableAccount",
    "BankAccountSummary",
    "BankOrCashAccount",
    "BankReconciliation",
    "BaseCurrency",
    "BillableExpenses",
    "BillableTime",
    "BillableTimeSummary",
    "BusinessDetails",
    "BusinessDetailsNameField",
    "BusinessLogo",
    "CapitalAccount",
    "CapitalAccountsSummary",
    "CashFlowStatement",
    "CashFlowStatementFinancingActivityGroup",
    "CashFlowStatementInvestingActivityGroup",
    "CashFlowStatementOperatingActivityGroup",
    "ChartOfAccountsGroup",
    "CheckboxCustomField",
    "Column",
    "ControlAccountForBankAccounts",
    "ControlAccountForCapitalAccounts",
    "ControlAccountForCustomers",
    "ControlAccountForEmployees",
    "ControlAccountForFixedAssets",
    "ControlAccountForFixedAssetsAccumulatedDepreciation",
    "ControlAccountForIntangibleAssets",
    "ControlAccountForIntangibleAssetsAccumulatedAmortization",
    "ControlAccountForInventoryItems",
    "ControlAccountForInvestments",
    "ControlAccountForSpecialAccounts",
    "ControlAccountForSuppliers",
    "CreditNote",
    "CreditNoteFooter",
    "CustomField",
    "CustomFields",
    "CustomReport",
    "Customer",
    "CustomerPortal",
    "CustomerStatementsTransactions",
    "CustomerStatementsUnpaidInvoices",
    "CustomerSummary",
    "DateAndNumberFormat",
    "DateCustomField",
    "DebitNote",
    "DebitNoteFooter",
    "DeliveryNote",
    "DeliveryNoteColumns",
    "DeliveryNoteFooter",
    "DepreciationCalculationWorksheet",
    "DepreciationEntry",
    "Division",
    "DivisionExceptionReport",
    "EinvoiceMe",
    "EmailSettings",
    "EmailTemplateForCreditNote",
    "EmailTemplateForCustomerStatement",
    "EmailTemplateForDebitNote",
    "EmailTemplateForDeliveryNote",
    "EmailTemplateForPayment",
    "EmailTemplateForPayslip",
    "EmailTemplateForPurchaseInvoice",
    "EmailTemplateForPurchaseOrder",
    "EmailTemplateForPurchaseQuote",
    "EmailTemplateForReceipt",
    "EmailTemplateForSalesInvoice",
    "EmailTemplateForSalesOrder",
    "EmailTemplateForSalesQuote",
    "Employee",
    "EmployeeEmailField",
    "EmployeeNameField",
    "EmployeeSummary",
    "Equity",
    "ExchangeRate",
    "ExpenseClaim",
    "ExpenseClaimsPayer",
    "ExpenseClaimsSummary",
    "Extension",
    "FixedAsset",
    "FixedAssetSummary",
    "Folder",
    "Forecast",
    "ForecastProfitAndLossStatement",
    "ForeignCurrency",
    "FreightInItem",
    "GeneralLedgerSummary",
    "GeneralLedgerTransactions",
    "GoodsReceipt",
    "GoodsReceiptFooter",
    "HideIfEmptyReportingCategory",
    "IntangibleAsset",
    "IntangibleAssetSummary",
    "InterAccountTransfer",
    "InterAccountTransferFooter",
    "InternalPdfGenerator",
    "InventoryItem",
    "InventoryKit",
    "InventoryLocation",
    "InventoryPriceList",
    "InventoryProfitMargin",
    "InventoryQuantityByLocation",
    "InventoryQuantityMovement",
    "InventoryTransfer",
    "InventoryValueSummary",
    "InventoryWriteOff",
    "Investment",
    "JournalEntry",
    "JournalEntryFooter",
    "LatePaymentFee",
    "Liabilities",
    "LockDate",
    "MemberInfo",
    "MultipleValueCustomField",
    "NamedObject",
    "NonInventoryItem",
    "NumberCustomField",
    "Object",
    "Payment",
    "PaymentFooter",
    "PaymentRule",
    "Payslip",
    "PayslipContributionItem",
    "PayslipContributionItemReportingCategory",
    "PayslipDeductionItem",
    "PayslipDeductionItemReportingCategory",
    "PayslipEarningsItem",
    "PayslipEarningsItemReportingCategory",
    "PayslipFooter",
    "PayslipSummary",
    "PayslipTotalsPerItemAndEmployee",
    "ProductionOrder",
    "ProfitAndLossStatement",
    "ProfitAndLossStatementAccount",
    "ProfitAndLossStatementAccountBillableExpensesCost",
    "ProfitAndLossStatementAccountBillableExpensesInvoiced",
    "ProfitAndLossStatementAccountBillableTimeInvoiced",
    "ProfitAndLossStatementAccountBillableTimeMovement",
    "ProfitAndLossStatementAccountCurrencyGainsLosses",
    "ProfitAndLossStatementAccountFixedAssetDepreciation",
    "ProfitAndLossStatementAccountFixedAssetLossOnDisposal",
    "ProfitAndLossStatementAccountIntangibleAssetsAmortization",
    "ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal",
    "ProfitAndLossStatementAccountInventoryPurchases",
    "ProfitAndLossStatementAccountInventorySales",
    "ProfitAndLossStatementAccountLatePaymentFees",
    "ProfitAndLossStatementAccountRoundingExpense",
    "ProfitAndLossStatementActualVsBudget",
    "ProfitAndLossStatementCapitalGainsOnInvestments",
    "ProfitAndLossStatementGroup",
    "Project",
    "PurchaseInvoice",
    "PurchaseInvoiceFooter",
    "PurchaseOrder",
    "PurchaseOrderFooter",
    "PurchaseQuote",
    "PurchaseQuoteFooter",
    "Receipt",
    "ReceiptColumns",
    "ReceiptFooter",
    "ReceiptRule",
    "ReceiptsAndPaymentsSummary",
    "RecurringInterAccountTransfer",
    "RecurringJournalEntry",
    "RecurringPayment",
    "RecurringPayslip",
    "RecurringPurchaseInvoice",
    "RecurringPurchaseOrder",
    "RecurringReceipt",
    "RecurringSalesInvoice",
    "RecurringSalesOrder",
    "RecurringSalesQuote",
    "ReportTranformationFromDate",
    "ReportTranformationToDate",
    "ReportTransformation2",
    "ReportTransformationFromDateLastJuly",
    "ReportTransformationLabel",
    "ReportTransformationNetAmounts",
    "ReportTransformationReport",
    "ReportTransformationTaxAmounts",
    "ReportTransformationTaxPurchases",
    "ReportTransformationTaxSales",
    "ReverseSignReportingCategory",
    "RoundDownReportingCategory",
    "SalesInvoice",
    "SalesInvoiceFooter",
    "SalesInvoiceTotalsByCustomField",
    "SalesInvoiceTotalsByCustomer",
    "SalesInvoiceTotalsByItem",
    "SalesOrder",
    "SalesOrderFooter",
    "SalesQuote",
    "SalesQuoteFooter",
    "Schema",
    "Session",
    "SetZeroIfNegativeReportingCategory",
    "SpecialAccount",
    "StatementOfChangesInEquity",
    "SubAccount",
    "Subtotal",
    "Summary",
    "Supplier",
    "SupplierNameField",
    "SupplierStatementsTransactions",
    "SupplierStatementsUnpaidInvoices",
    "SupplierSummary",
    "Tabs",
    "TaxAmountReportingCategory",
    "TaxAmountReversedReportingCategory",
    "TaxAudit",
    "TaxCode",
    "TaxCodeReportingCategory",
    "TaxCodeReversedReportingCategory",
    "TaxReconciliation",
    "TaxSummary",
    "TaxTransactions",
    "TaxablePurchasesPerSupplier",
    "TaxableSalesPerCustomer",
    "TextCustomField",
    "Theme",
    "TrialBalance",
    "User",
    "UserPermissions",
    "WithholdingTaxReceipt",
]
