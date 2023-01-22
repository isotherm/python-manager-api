#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Do not edit. Automatically generated from Manager v23.1.11.592.

from datetime import date
from decimal import Decimal
from typing import ClassVar, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field

from . import enums
from .enums import *


class ManagerBaseModel(BaseModel):
    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)


class AgedPayables(ManagerBaseModel):
    Key: ClassVar[UUID] = '6abe86ec-a6c9-46a8-a9c9-7104056a2730'
    Singleton: ClassVar[bool] = False
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Division: Optional[Optional[UUID]]
    SortBy: Optional[SortBy]
    Description: Optional[str]
    ShowInvoices: Optional[bool]


class AgedReceivables(ManagerBaseModel):
    Key: ClassVar[UUID] = '39f00628-27a7-4924-9030-5bc655ee234f'
    Singleton: ClassVar[bool] = False
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Division: Optional[Optional[UUID]]
    SortBy: Optional[SortBy]
    Description: Optional[str]
    ShowInvoices: Optional[bool]


class AmortizationCalculationWorksheet(ManagerBaseModel):
    Key: ClassVar[UUID] = '011cf167-ff32-49e7-b0f3-ac12a3fe43ed'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class CustomFields(ManagerBaseModel):
    Strings: Optional[Dict[UUID, str]]
    Decimals: Optional[Dict[UUID, Optional[Decimal]]]
    Dates: Optional[Dict[UUID, Optional[date]]]
    Booleans: Optional[Dict[UUID, bool]]
    StringArrays: Optional[Dict[UUID, List[str]]]


class AmortizationEntry(ManagerBaseModel):
    Key: ClassVar[UUID] = 'd33519a3-e8e0-4556-9833-b744a58dd2f7'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        IntangibleAsset: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
        Amount: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class Amount(ManagerBaseModel):
    class Component(ManagerBaseModel):
        Qty: Optional[Optional[Decimal]]
        UnitPrice: Optional[Decimal]
    Currency: Optional[Optional[UUID]]
    Components: Optional[List[Component]]


class Assets(ManagerBaseModel):
    Key: ClassVar[UUID] = '4c05c221-ca57-4c7c-be62-115669302ed4'
    Singleton: ClassVar[bool] = True


class Attachment(ManagerBaseModel):
    Key: ClassVar[UUID] = '2e541a82-94d7-42fc-a388-26bdc0803455'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Name: Optional[str]
    ContentType: Optional[str]
    Size: Optional[int]
    Object: Optional[Optional[UUID]]


class BalanceSheet(ManagerBaseModel):
    Key: ClassVar[UUID] = '7b4f463a-470d-44c4-9e75-fafc630b5851'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        Date: Optional[date]
        Division: Optional[Optional[UUID]]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    AccountingMethod: Optional[AccountingBasis]
    Rounding: Optional[Rounding]
    Layout: Optional[BalanceSheetLayout]
    GroupsToCollapse: Optional[List[UUID]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class BalanceSheetAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '6ef13e42-ad89-4d42-9480-546e0c04a411'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementFinancingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementInvestingActivityGroup: Optional[Optional[UUID]]
    Division: Optional[Optional[UUID]]
    Position: Optional[int]
    StartingBalance: Optional[Decimal]
    StartingBalanceType: Optional[DebitCredit]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    Inactive: Optional[bool]


class BalanceSheetAccountsPayableAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'dac7ba37-0ccd-45e5-906e-548e6c50df37'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatementGroup: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetAccountsReceivableAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'd1489e95-bb28-4f5d-b42e-67d3291b3893'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatementGroup: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetBillableExpensesAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '059dbfb9-1c80-4043-887f-0fc441099fe0'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetBillableTimeAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '9f3c0a1a-dd0b-4b5c-ba50-3e4939a0e90c'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetCapitalAccountsAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '054dfae1-c34a-475e-abde-49e0385ffc9a'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetCashAtBankAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '6d4af96a-0959-4bb2-9160-fa825ec67c43'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetEmployeeClearingAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '650a36fe-801f-4031-8d5b-ab422d061fca'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetExpenseClaimsAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'f728124f-c6b6-4dad-82c5-22fc0d8d0571'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetFixedAssetsAccumulatedDepreciationAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'f813a6c8-1ead-46bd-8911-f12714be193c'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetFixedAssetsAtCostAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '4a0e8917-fee2-4033-9161-48dd513fdb73'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetGroup(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c03d1921-7a45-4eda-8742-a2d9082dcf4f'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetIntangibleAssetsAccumulatedAmortizationAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'aa12d048-bfbd-47dc-a5b8-03e35c417996'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetIntangibleAssetsAtCostAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '31d369e3-32c7-4bd2-bb83-9c1c58010c1a'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetInterdivisionalLoan(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ac4ab22b-0fbd-485f-8434-d25745b9be22'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetInventoryOnHandAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '0fb45a62-fc42-43a8-a776-782e8b5ffc96'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetInvestmentsAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '352897d1-e7fe-462e-9965-458ed9e27b82'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatementInvestingActivityGroup: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetProductionInProgressAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '30a1b83c-68a8-4f2c-ae70-25b0acc2d12a'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetRetainedEarningsAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '74dfd025-d68e-4a99-9c78-5d43e17c0e09'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetSpecialAccountsAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ef49facb-203b-4b45-aebd-99af4645700b'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementFinancingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementInvestingActivityGroup: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetSuspenseAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '11211c9e-0988-4d16-8bf2-fa39487123aa'
    Singleton: ClassVar[bool] = True


class BalanceSheetTaxPayableAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '30c697fa-4196-438a-ab5a-1957478034b1'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetWithholdingTaxAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '8f75a810-abd0-4d89-a6a2-66c9003a60e2'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetWithholdingTaxPayableAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a4dffac2-35d1-47e1-a4bd-b6de15975fdb'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BalanceSheetWithholdingTaxReceivableAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c66de1bf-6f63-4bc8-9452-0b019e41c47f'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class BankAccountSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '77afd97c-51d7-484b-8192-b7eb006daadb'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
    BankAccount: Optional[Optional[UUID]]
    Periods: Optional[List[Period]]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class BankOrCashAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '1408c33b-6284-4f50-9e31-48cbea21f3cf'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Currency: Optional[Optional[UUID]]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[Decimal]
    HasInternationalBankAccountNumber: Optional[bool]
    InternationalBankAccountNumber: Optional[str]
    CanHavePendingTransactions: Optional[bool]
    HasCreditLimit: Optional[bool]
    CreditLimit: Optional[Decimal]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    IsBankAccount: Optional[bool]
    IsCashAccount: Optional[bool]


class BankReconciliation(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a3b1d610-b5e8-4f17-8e97-e53e69b78bb5'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    BankAccount: Optional[Optional[UUID]]
    StatementBalance: Optional[Decimal]


class BaseCurrency(ManagerBaseModel):
    Key: ClassVar[UUID] = '39dde4fc-7af8-44cc-8572-3b1ff4cfb918'
    Singleton: ClassVar[bool] = True
    Code: Optional[str]
    Name: Optional[str]
    Symbol: Optional[str]
    DecimalPlaces: Optional[Optional[int]]


class BillableExpenses(ManagerBaseModel):
    Key: ClassVar[UUID] = 'e3ea8ce1-4fa4-43df-aec6-38ef5b574b1b'
    Singleton: ClassVar[bool] = False
    Enabled: Optional[bool]


class BillableTime(ManagerBaseModel):
    Key: ClassVar[UUID] = '6bfb652c-11cb-46fa-9e5a-c5950ccbae15'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Customer: Optional[Optional[UUID]]
    Description: Optional[str]
    HourlyRate: Optional[Decimal]
    TimeSpent: Optional[Optional[int]]
    TimeSpentMinutes: Optional[Optional[int]]
    Division: Optional[Optional[UUID]]
    Status: Optional[BillableTimeStatus]
    SalesInvoice: Optional[Optional[UUID]]
    WrittenOffDate: Optional[Optional[date]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class BillableTimeSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '5516d6e5-d1fe-4271-8625-f7f0acc7f961'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class BusinessDetails(ManagerBaseModel):
    Key: ClassVar[UUID] = '38cf4712-6e95-4ce1-b53a-bff03edad273'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Address: Optional[str]
    Country: Optional[str]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class BusinessDetailsNameField(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ce6302f8-0b02-42d8-b6b7-850063e4bbe0'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class BusinessLogo(ManagerBaseModel):
    Key: ClassVar[UUID] = '096d0af9-df72-425d-aae8-d59c0497f119'
    Singleton: ClassVar[bool] = True
    ContentType: Optional[str]
    Content: Optional[bytes]


class CapitalAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'b9c4cd62-7569-44f0-bc62-9df3007a6a5c'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[StartingBalanceType]
    StartingBalanceAmount: Optional[Decimal]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    Inactive: Optional[bool]


class CashFlowStatement(ManagerBaseModel):
    Key: ClassVar[UUID] = '2a9a4b8e-8b06-4819-adee-4b766a55119c'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Method: Optional[CashFlowStatementMethod]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    RoundDecimals: Optional[bool]


class CashFlowStatementFinancingActivityGroup(ManagerBaseModel):
    Key: ClassVar[UUID] = 'da08116a-6fe3-47c2-805c-d5a81a03931a'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]


class CashFlowStatementInvestingActivityGroup(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a9cf8675-afb3-42d6-9440-f5efedef55b8'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]


class CashFlowStatementOperatingActivityGroup(ManagerBaseModel):
    Key: ClassVar[UUID] = '25299eaa-3460-4a62-bd5d-8bc65b24375d'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]


class CheckboxCustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ccad5339-206e-4145-aa3d-3bd8d785b2fb'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Position: Optional[Optional[int]]
    Placement: Optional[List[UUID]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class Column(ManagerBaseModel):
    Name: Optional[str]
    ClassicCustomField: Optional[Optional[UUID]]
    CustomField: Optional[Optional[UUID]]


class ControlAccountForBankAccounts(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c97264e3-eed6-4afd-8d2c-e1c1a00b4dc1'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForCapitalAccounts(ManagerBaseModel):
    Key: ClassVar[UUID] = '95b9d17d-f5f8-4722-a89d-456fa0906e13'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForCustomers(ManagerBaseModel):
    Key: ClassVar[UUID] = '7a57978e-583d-4997-86c7-c557de0e7fdd'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatementGroup: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForEmployees(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fb804fba-df12-4628-ae54-df7a67d67f1b'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForFixedAssets(ManagerBaseModel):
    Key: ClassVar[UUID] = '014742b2-fc31-4ded-90b5-2e0d437a1589'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForFixedAssetsAccumulatedDepreciation(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c2e88cf8-4d05-4bec-8c42-fdef424faf1a'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForIntangibleAssets(ManagerBaseModel):
    Key: ClassVar[UUID] = '8ed99282-8ec3-4505-8846-0507bd0d0f70'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForIntangibleAssetsAccumulatedAmortization(ManagerBaseModel):
    Key: ClassVar[UUID] = '47995ee3-b2c9-4799-ace3-768f7514c644'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForInventoryItems(ManagerBaseModel):
    Key: ClassVar[UUID] = 'acc019f7-9bb9-4d8e-ba66-0956916b4247'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForInvestments(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fb2c120e-6b30-47cb-a61e-14f0189bec06'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForSpecialAccounts(ManagerBaseModel):
    Key: ClassVar[UUID] = '6af7e809-1de3-4a09-923f-27ad786ed837'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementFinancingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementInvestingActivityGroup: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ControlAccountForSuppliers(ManagerBaseModel):
    Key: ClassVar[UUID] = '78e7aefb-9dff-4ae5-981e-4165b14fd963'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatementGroup: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class CreditNote(ManagerBaseModel):
    Key: ClassVar[UUID] = '245e5943-0092-409d-96ae-e2ee10eac75b'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        SalesUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    IssueDate: Optional[date]
    Reference: Optional[str]
    Customer: Optional[Optional[UUID]]
    SalesInvoice: Optional[Optional[UUID]]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    SalesInventoryLocation: Optional[Optional[UUID]]
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
    CreditNoteCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasCreditNoteFooters: Optional[bool]
    CreditNoteFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    Type: Optional[CreditNoteType]


class CreditNoteFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '90f7ba80-5666-49a2-af1b-908cf9a651cd'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Customer(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ec37c11e-2b67-49c6-8a58-6eccb7dd75ee'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    CreditLimit: Optional[Decimal]
    Currency: Optional[Optional[UUID]]
    BillingAddress: Optional[str]
    DeliveryAddress: Optional[str]
    Email: Optional[str]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[Decimal]
    HasDefaultDueDateDays: Optional[bool]
    DefaultDueDateDays: Optional[Optional[int]]
    HasDefaultHourlyRate: Optional[bool]
    DefaultHourlyRate: Optional[Decimal]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultBillingAddress: Optional[bool]
    DefaultBillingAddress: Optional[str]
    HasDefaultDeliveryAddress: Optional[bool]
    DefaultDeliveryAddress: Optional[str]


class CustomerPortal(ManagerBaseModel):
    Key: ClassVar[UUID] = '18048748-7c70-49e6-bed4-b9d310736956'
    Singleton: ClassVar[bool] = False
    Customer: Optional[Optional[UUID]]
    SalesQuotes: Optional[bool]
    SalesOrders: Optional[bool]
    SalesInvoices: Optional[bool]
    CreditNotes: Optional[bool]
    DeliveryNotes: Optional[bool]


class CustomerStatementsTransactions(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c81ede5f-141e-4eb3-a586-1b0ab079cae6'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[DateType]
    ToCustomDate: Optional[date]
    Theme: Optional[Optional[UUID]]


class CustomerStatementsUnpaidInvoices(ManagerBaseModel):
    Key: ClassVar[UUID] = 'b9b3d678-a743-46e1-aaf5-fd1b27b5e20b'
    Singleton: ClassVar[bool] = False
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Theme: Optional[Optional[UUID]]


class CustomerSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = 'b8583039-fa11-441a-a727-40aa2311e74c'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Division: Optional[Optional[UUID]]


class CustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = 'dcb382dc-a4e0-4354-a845-b7d647f610f7'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Position: Optional[Optional[int]]
    Placement: Optional[List[UUID]]
    Type: Optional[CustomFieldStyle]
    OptionsForDropdownList: Optional[str]
    Size: Optional[CustomFieldSize]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class MemberInfo(ManagerBaseModel):
    Key: Optional[str]
    DeclaringType: Optional[str]
    IsCustomFields: Optional[bool]


class CustomReport(ManagerBaseModel):
    Key: ClassVar[UUID] = '7df43b64-9aea-4b19-a60a-a56f2e390df4'
    Singleton: ClassVar[bool] = False
    class SelectElement(ManagerBaseModel):
        SelectPrimaryField: Optional[MemberInfo]
        SelectSecondaryField: Optional[MemberInfo]
        SelectCustomField: Optional[Optional[UUID]]
        DisplayName: Optional[str]
        SelectCustomFieldFilter: Optional[object]
    class OrderByElement(ManagerBaseModel):
        OrderByPrimaryField: Optional[MemberInfo]
        OrderBySecondaryField: Optional[MemberInfo]
        OrderByCustomField: Optional[Optional[UUID]]
        SortOrder: Optional[SortOrder]
        OrderByCustomFieldFilter: Optional[object]
    class GroupByElement(ManagerBaseModel):
        GroupByPrimaryField: Optional[MemberInfo]
        GroupBySecondaryField: Optional[MemberInfo]
        GroupByCustomField: Optional[Optional[UUID]]
        GroupByCustomFieldFilter: Optional[object]
    class WhereElement(ManagerBaseModel):
        WherePrimaryField: Optional[MemberInfo]
        WhereSecondaryField: Optional[MemberInfo]
        WhereCustomField: Optional[Optional[UUID]]
        WhereCustomFieldFilter: Optional[object]
        ObjectType: Optional[object]
        ObjectKey: Optional[object]
        StringOperator: Optional[StringOperator]
        String: Optional[str]
        DecimalOperator: Optional[DecimalOperator]
        Decimal: Optional[Optional[Decimal]]
        BooleanOperator: Optional[BooleanOperator]
        ObjectOperator: Optional[ObjectOperator]
        Object: Optional[Optional[UUID]]
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


class DateAndNumberFormat(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a56e89d1-7bee-4509-8b84-c9ebc3808b0c'
    Singleton: ClassVar[bool] = True
    class NumberFormatParts(ManagerBaseModel):
        DecimalSeparator: Optional[str]
        GroupSeparator: Optional[str]
        GroupSizes: Optional[List[int]]
    DateFormat: Optional[str]
    TimeFormat: Optional[str]
    FirstDayOfWeek: Optional[enums.FirstDayOfWeek]
    NumberFormat: Optional[str]


class DateCustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = '6c564f4c-380c-432e-af3b-2d6514c1891c'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Position: Optional[Optional[int]]
    Placement: Optional[List[UUID]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class DebitNote(ManagerBaseModel):
    Key: ClassVar[UUID] = '274fc6d0-2eac-43d0-8286-79c856e644aa'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        BillableExpenseSalesInvoice: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        PurchaseUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    IssueDate: Optional[date]
    Reference: Optional[str]
    Supplier: Optional[Optional[UUID]]
    PurchaseInvoice: Optional[Optional[UUID]]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    PurchaseInventoryLocation: Optional[Optional[UUID]]
    AmountsIncludeTax: Optional[bool]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    HasDebitNoteCustomTheme: Optional[bool]
    DebitNoteCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasDebitNoteFooters: Optional[bool]
    DebitNoteFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class DebitNoteFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ae399a2e-95c0-4ef5-a32d-5cd8217d885a'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class DeliveryNote(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a0f6a539-f6a4-4a38-a69a-546a608a1f6d'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
    DeliveryDate: Optional[date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    InvoiceNumber: Optional[str]
    InventoryLocation: Optional[Optional[UUID]]
    Customer: Optional[Optional[UUID]]
    SalesOrder: Optional[Optional[UUID]]
    SalesInvoice: Optional[Optional[UUID]]
    DeliveryAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    HasLineNumber: Optional[bool]
    CustomTitle: Optional[bool]
    DeliveryNoteCustomTitle: Optional[str]
    HasDeliveryNoteCustomTheme: Optional[bool]
    DeliveryNoteCustomTheme: Optional[Optional[UUID]]
    HasDeliveryNoteFooters: Optional[bool]
    DeliveryNoteFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class DeliveryNoteColumns(ManagerBaseModel):
    Key: ClassVar[UUID] = '8e82c77b-b894-4df8-939d-9c6983eb58d4'
    Singleton: ClassVar[bool] = False
    class Column(ManagerBaseModel):
        Name: Optional[enums.DeliveryNoteColumns]
        CustomField: Optional[Optional[UUID]]
        ClassicCustomField: Optional[Optional[UUID]]
    CustomColumns: Optional[bool]
    Columns: Optional[List[Column]]


class DeliveryNoteFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fd737085-d270-4749-9274-7b458a2ec740'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class DepreciationCalculationWorksheet(ManagerBaseModel):
    Key: ClassVar[UUID] = '105604f5-5bc1-4bfa-a101-3c339c22989a'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class DepreciationEntry(ManagerBaseModel):
    Key: ClassVar[UUID] = '75cdc055-6dec-4381-bc40-b670366e6abc'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        FixedAsset: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
        Amount: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class Division(ManagerBaseModel):
    Key: ClassVar[UUID] = 'cc7fc110-e3e4-4b3b-823d-86c4a4cdabbc'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]


class DivisionExceptionReport(ManagerBaseModel):
    Key: ClassVar[UUID] = '0e7711f8-1db1-4bcd-ac91-020d74a06dab'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class EinvoiceMe(ManagerBaseModel):
    Key: ClassVar[UUID] = '12e0885e-65c0-4a5c-85d6-98b4b3865518'
    Singleton: ClassVar[bool] = False
    Enabled: Optional[bool]
    Authorization: Optional[str]
    LastSync: Optional[Optional[int]]


class EmailSettings(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a4ddb0e3-b207-4fee-aa01-f104b6c09932'
    Singleton: ClassVar[bool] = True
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


class EmailTemplateForCreditNote(ManagerBaseModel):
    Key: ClassVar[UUID] = '85bf4dd0-fd18-4d03-b106-460839d2e3f7'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForCustomerStatement(ManagerBaseModel):
    Key: ClassVar[UUID] = 'aacecb53-f501-4db7-9879-f03d3304e08a'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForDebitNote(ManagerBaseModel):
    Key: ClassVar[UUID] = '252d164a-90fc-45a3-bd35-b84f6d08d3e2'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForDeliveryNote(ManagerBaseModel):
    Key: ClassVar[UUID] = '4768f2b1-4388-4cc3-ac50-c00284434dd6'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPayment(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fe8baa5b-5737-4852-b520-cb9a590f3a94'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPayslip(ManagerBaseModel):
    Key: ClassVar[UUID] = '61648ae7-4613-459a-aca6-9913928f776f'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPurchaseInvoice(ManagerBaseModel):
    Key: ClassVar[UUID] = '21129fc9-26db-4cab-a70b-b42802f7017d'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPurchaseOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a45a2ffe-2c07-4564-8a98-431032a3387f'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForPurchaseQuote(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ff22d093-a191-47eb-acad-4ed0b439dc43'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForReceipt(ManagerBaseModel):
    Key: ClassVar[UUID] = 'b5d1faec-e726-4700-8666-8197b8681984'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForSalesInvoice(ManagerBaseModel):
    Key: ClassVar[UUID] = '48279506-e1bc-4011-bb47-97c0336401a0'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForSalesOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = '3087728d-7fd5-42a4-b92c-8c0a4c87ab0c'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class EmailTemplateForSalesQuote(ManagerBaseModel):
    Key: ClassVar[UUID] = 'cc707d1f-5a8d-43f1-84a4-22732fb0ccd6'
    Singleton: ClassVar[bool] = True
    Subject: Optional[str]
    MessageBody: Optional[str]


class Employee(ManagerBaseModel):
    Key: ClassVar[UUID] = 'dadb7f95-a5dd-45c0-945d-6ad4ee28776e'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Address: Optional[str]
    Email: Optional[str]
    Currency: Optional[Optional[UUID]]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[StartingBalanceType]
    StartingBalanceAmount: Optional[Decimal]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    Inactive: Optional[bool]


class EmployeeEmailField(ManagerBaseModel):
    Key: ClassVar[UUID] = 'f66ab672-c1c6-4280-9439-bdb0a72b7619'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class EmployeeNameField(ManagerBaseModel):
    Key: ClassVar[UUID] = 'db71c44c-ec5a-4701-aa54-67ada72aff1a'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class EmployeeSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = 'e7b3a4f4-35d7-4f92-a8fc-e9eadbc140a8'
    Singleton: ClassVar[bool] = False
    Employee: Optional[Optional[UUID]]
    FromDate: Optional[date]
    ToDate: Optional[date]
    ExcludeZeroBalances: Optional[bool]


class Equity(ManagerBaseModel):
    Key: ClassVar[UUID] = '9275ff4c-4cff-41d0-b7b5-f31c783f03d8'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]


class ExchangeRate(ManagerBaseModel):
    Key: ClassVar[UUID] = '14240c19-3d08-4fe6-94bb-6dd17c4bcda6'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Currency: Optional[Optional[UUID]]
    Type: Optional[ExchangeRateType]
    BaseRate: Optional[Decimal]
    CounterRate: Optional[Decimal]


class ExpenseClaim(ManagerBaseModel):
    Key: ClassVar[UUID] = '02572e0c-0167-4dbd-a392-08d8f67f3fe4'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        AccountsReceivableCustomer: Optional[Optional[UUID]]
        AccountsReceivableSalesInvoice: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        BillableExpenseSalesInvoice: Optional[Optional[UUID]]
        AccountsPayableSupplier: Optional[Optional[UUID]]
        PurchaseInvoice: Optional[Optional[UUID]]
        WithholdingTaxPayableSupplier: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        InventoryItem: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        Qty: Optional[Optional[Decimal]]
        PurchaseUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    PaidBy: Optional[Optional[UUID]]
    Payee: Optional[str]
    Currency: Optional[Optional[UUID]]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[Optional[UUID]]
    AmountsIncludeTax: Optional[bool]
    HasLineDescription: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class ExpenseClaimsPayer(ManagerBaseModel):
    Key: ClassVar[UUID] = '563d7f9e-d64c-49ec-a938-e5531e72f4d8'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    StartingBalance: Optional[StartingBalanceType]
    StartingBalanceAmount: Optional[Decimal]
    Division: Optional[Optional[UUID]]
    Inactive: Optional[bool]


class ExpenseClaimsSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = 'faa1756c-5aaf-4646-9f33-555e45e37efb'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class Extension(ManagerBaseModel):
    Key: ClassVar[UUID] = '9a8fc328-7553-469f-88ed-dc533f2160b2'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Script: Optional[str]
    Location: Optional[LocationType]
    CustomLocation: Optional[str]
    Inactive: Optional[bool]


class FixedAsset(ManagerBaseModel):
    Key: ClassVar[UUID] = '00082353-9fca-4ab4-91ae-20505479cbda'
    Singleton: ClassVar[bool] = False
    ItemCode: Optional[str]
    ItemName: Optional[str]
    DepreciationRate: Optional[Decimal]
    Description: Optional[str]
    Division: Optional[Optional[UUID]]
    ControlAccountForFixedAssets: Optional[Optional[UUID]]
    ControlAccountForFixedAssetsAccumulatedDepreciation: Optional[Optional[UUID]]
    StartingBalance: Optional[Decimal]
    StartingBalanceAccumulatedDepreciation: Optional[Decimal]
    CustomDepreciationExpenseAccount: Optional[bool]
    CustomDepreciationExpenseAccountSelection: Optional[Optional[UUID]]
    DisposedFixedAsset: Optional[bool]
    DisposalDate: Optional[Optional[date]]
    CustomExpenseAccountForDisposal: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class FixedAssetSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '0dbf7789-7a6f-4182-b641-6b8e561b4a9c'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class Folder(ManagerBaseModel):
    Key: ClassVar[UUID] = '5d6fae1e-ff34-4870-80e9-8a755842d46e'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class Forecast(ManagerBaseModel):
    Key: ClassVar[UUID] = '821030a6-9820-4cba-8879-eda07853b9a6'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Account: Optional[Optional[UUID]]
        Amount: Optional[Decimal]
    class ForecastTransaction(ManagerBaseModel):
        Key: Optional[UUID]
        Date: Optional[date]
        Account: Optional[UUID]
        Description: Optional[str]
        Amount: Optional[Decimal]
    Date: Optional[date]
    Repeat: Optional[Repeat]
    Growth: Optional[Decimal]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    Inactive: Optional[bool]


class ForecastProfitAndLossStatement(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a513a0b4-24f2-49ac-a820-d116ab9d198a'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class ForeignCurrency(ManagerBaseModel):
    Key: ClassVar[UUID] = '6116531b-cb3d-4f85-b239-745972943a6b'
    Singleton: ClassVar[bool] = False
    Code: Optional[str]
    Name: Optional[str]
    Symbol: Optional[str]
    DecimalPlaces: Optional[Optional[int]]
    StartingExchangeRate: Optional[Decimal]
    Inactive: Optional[bool]


class FreightInItem(ManagerBaseModel):
    Key: ClassVar[UUID] = '3458c24f-2a5f-4dcf-9de7-7340b1463d9c'
    Singleton: ClassVar[bool] = True
    PurchasePrice: Optional[Decimal]
    PurchaseItemAccount: Optional[Optional[UUID]]
    PurchaseItemTaxCode: Optional[Optional[UUID]]
    PurchaseItemTrackingCode: Optional[Optional[UUID]]
    HasDefaultQty: Optional[bool]
    DefaultQty: Optional[Optional[Decimal]]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[Decimal]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]


class GeneralLedgerSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '6c1d3132-7978-45c8-a6e2-2387c7de46b0'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class GeneralLedgerTransactions(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a3283b79-76be-44b6-9639-fa22d9b63246'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    Account: Optional[Optional[UUID]]


class GoodsReceipt(ManagerBaseModel):
    Key: ClassVar[UUID] = '866217a4-f841-47de-a4e6-87152405c88d'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
    Date: Optional[date]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    InvoiceNumber: Optional[str]
    Supplier: Optional[Optional[UUID]]
    PurchaseOrder: Optional[Optional[UUID]]
    PurchaseInvoice: Optional[Optional[UUID]]
    InventoryLocation: Optional[Optional[UUID]]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    HasLineNumber: Optional[bool]
    HasGoodsReceiptCustomTheme: Optional[bool]
    GoodsReceiptCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    HasGoodsReceiptFooters: Optional[bool]
    GoodsReceiptFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class GoodsReceiptFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '6db45d4f-ef92-4cb8-916f-a7c8645384be'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class HideIfEmptyReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c9d0844e-7628-4bf4-899c-155be1577983'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class IntangibleAsset(ManagerBaseModel):
    Key: ClassVar[UUID] = '94d5307e-4332-4545-ab1e-1528c9032b7d'
    Singleton: ClassVar[bool] = False
    ItemCode: Optional[str]
    ItemName: Optional[str]
    AmortizationRate: Optional[Decimal]
    Description: Optional[str]
    Division: Optional[Optional[UUID]]
    ControlAccountForIntangibleAssets: Optional[Optional[UUID]]
    ControlAccountForIntangibleAssetsAccumulatedAmortization: Optional[Optional[UUID]]
    StartingBalance: Optional[Decimal]
    StartingBalanceAccumulatedAmortization: Optional[Decimal]
    CustomAmortizationExpenseAccount: Optional[bool]
    CustomAmortizationExpenseAccountSelection: Optional[Optional[UUID]]
    DisposedIntangibleAsset: Optional[bool]
    DisposalDate: Optional[Optional[date]]
    CustomExpenseAccountForDisposal: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class IntangibleAssetSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = 'd76b3a1a-bb37-4767-9f65-f0389ec9d5df'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Description: Optional[str]


class JournalEntry(ManagerBaseModel):
    Key: ClassVar[UUID] = '5ea52bc4-90ae-4e4a-aec4-ef1224b279ad'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Account: Optional[Optional[UUID]]
        AccountsReceivableCustomer: Optional[Optional[UUID]]
        AccountsReceivableSalesInvoice: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        BillableExpenseSalesInvoice: Optional[Optional[UUID]]
        AccountsPayableSupplier: Optional[Optional[UUID]]
        PurchaseInvoice: Optional[Optional[UUID]]
        WithholdingTaxPayableSupplier: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        InventoryItem: Optional[Optional[UUID]]
        InventoryLocation: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        ExpenseClaimPayer: Optional[Optional[UUID]]
        Investment: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        Qty: Optional[Decimal]
        Debit: Optional[Decimal]
        Credit: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    Currency: Optional[Optional[UUID]]
    Narration: Optional[str]
    Lines: Optional[List[Line]]
    OutOfBalance: Optional[object]
    ForTaxPurposesThisIs: Optional[TaxTransactionType]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    HasJournalEntryFooters: Optional[bool]
    JournalEntryFooters: Optional[List[UUID]]
    CashTransactionForCashFlowStatementPurposes: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class InterAccountTransfer(ManagerBaseModel):
    Key: ClassVar[UUID] = 'dea4f923-c498-4504-b3ef-30be3c33175e'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Reference: Optional[str]
    description: Optional[str]
    paidFrom: Optional[Optional[UUID]]
    CreditAmount: Optional[Decimal]
    CreditClearStatus: Optional[BankAccountClearStatus]
    CreditClearDate: Optional[Optional[date]]
    receivedIn: Optional[Optional[UUID]]
    DebitAmount: Optional[Decimal]
    DebitClearStatus: Optional[BankAccountClearStatus]
    DebitClearDate: Optional[Optional[date]]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    HasInterAccountTransferFooters: Optional[bool]
    InterAccountTransferFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class InterAccountTransferFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '12479269-1209-4684-8d6a-ccc7a447fd62'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class InternalPdfGenerator(ManagerBaseModel):
    Key: ClassVar[UUID] = '7e9fe6d7-d3a4-4456-981f-8112184b5517'
    Singleton: ClassVar[bool] = True
    Enabled: Optional[bool]
    PageSize: Optional[PageSize]


class InventoryItem(ManagerBaseModel):
    Key: ClassVar[UUID] = '0dbdbf8a-d80c-48e6-b453-bb7862445b7c'
    Singleton: ClassVar[bool] = False
    class StartingBalanceQuantity(ManagerBaseModel):
        Qty: Optional[Decimal]
        InventoryLocation: Optional[Optional[UUID]]
    ItemCode: Optional[str]
    ItemName: Optional[str]
    UnitName: Optional[str]
    ProductionStage: Optional[Optional[int]]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[List[StartingBalanceQuantity]]
    StartingBalanceAverageCost: Optional[Decimal]
    TrackQuantityToReceive: Optional[bool]
    TrackQuantityToDeliver: Optional[bool]
    CustomIncomeAccount: Optional[bool]
    IncomeAccount: Optional[Optional[UUID]]
    CustomExpenseAccount: Optional[bool]
    ExpenseAccount: Optional[Optional[UUID]]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[Decimal]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[Decimal]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[Optional[UUID]]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultQty: Optional[bool]
    DefaultQty: Optional[Optional[Decimal]]
    PurchaseItemAccount: Optional[Optional[UUID]]
    PurchaseItemTaxCode: Optional[Optional[UUID]]
    PurchaseItemTrackingCode: Optional[Optional[UUID]]
    SaleItemAccount: Optional[Optional[UUID]]
    SaleItemTaxCode: Optional[Optional[UUID]]
    SaleItemTrackingCode: Optional[Optional[UUID]]


class InventoryKit(ManagerBaseModel):
    Key: ClassVar[UUID] = 'efc4f2cc-acf0-4815-a9a8-13bae00c6167'
    Singleton: ClassVar[bool] = False
    class Item(ManagerBaseModel):
        InventoryItem: Optional[Optional[UUID]]
        Qty: Optional[Decimal]
    ItemCode: Optional[str]
    ItemName: Optional[str]
    UnitName: Optional[str]
    BillOfMaterials: Optional[List[Item]]
    Division: Optional[Optional[UUID]]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[Decimal]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[Optional[UUID]]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    CustomIncomeAccount: Optional[bool]
    IncomeAccount: Optional[Optional[UUID]]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultQty: Optional[bool]
    DefaultQty: Optional[Optional[Decimal]]
    SaleItemAccount: Optional[Optional[UUID]]


class InventoryLocation(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fae8151d-252e-45e3-b1f4-e048075b8983'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]


class InventoryPriceList(ManagerBaseModel):
    Key: ClassVar[UUID] = '14da35e1-9b94-4403-8575-9d64ade4d7b4'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    FilterByCustomField: Optional[bool]
    CustomField: Optional[Optional[UUID]]
    Filter: Optional[str]


class InventoryProfitMargin(ManagerBaseModel):
    Key: ClassVar[UUID] = '796da7cf-3551-4ff4-afad-942d4fc750cc'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]


class InventoryQuantityByLocation(ManagerBaseModel):
    Key: ClassVar[UUID] = '0e50586b-d1d0-40a3-81eb-8b6602e3050b'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Description: Optional[str]
    CustomInventoryLocations: Optional[bool]
    InventoryLocations: Optional[List[UUID]]


class InventoryQuantityMovement(ManagerBaseModel):
    Key: ClassVar[UUID] = 'bd9e1f26-91e4-4c7b-b410-a62cb966bcfc'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    ExcludeItemsWithNoMovement: Optional[bool]


class InventoryTransfer(ManagerBaseModel):
    Key: ClassVar[UUID] = '7eaafddc-54c9-4235-98d2-e8a1ee438150'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
    Date: Optional[date]
    Reference: Optional[str]
    InventoryLocation: Optional[Optional[UUID]]
    ToInventoryLocation: Optional[Optional[UUID]]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    AutomaticReference: Optional[bool]
    CustomFields2: Optional[CustomFields]


class InventoryValueSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '7e9405f2-ed99-4891-8757-5c4c23cabdb2'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    ExcludeItemsWithNoMovement: Optional[bool]


class InventoryWriteOff(ManagerBaseModel):
    Key: ClassVar[UUID] = 'd7ff6694-f1ef-419f-8ae2-55527a02e95f'
    Singleton: ClassVar[bool] = False
    class Item(ManagerBaseModel):
        InventoryItem: Optional[Optional[UUID]]
        Qty: Optional[Decimal]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    InventoryLocation: Optional[Optional[UUID]]
    Items: Optional[List[Item]]
    Allocation: Optional[Optional[UUID]]
    FixedAsset: Optional[Optional[UUID]]
    TaxCode: Optional[Optional[UUID]]
    Project: Optional[Optional[UUID]]
    Division: Optional[Optional[UUID]]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class Investment(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a8f95068-fc73-43f7-aabb-fd868e506b51'
    Singleton: ClassVar[bool] = False
    Code: Optional[str]
    Name: Optional[str]
    ControlAccount: Optional[Optional[UUID]]
    MarketPrice: Optional[Decimal]
    StartingBalance: Optional[Decimal]
    StartingBalanceTotalCost: Optional[Decimal]
    Inactive: Optional[bool]


class JournalEntryFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '5be035ca-d96b-4e8d-b963-53340cf7f4f8'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class LatePaymentFee(ManagerBaseModel):
    Key: ClassVar[UUID] = '4dada073-022f-464e-bdb3-ff38c83e577f'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Customer: Optional[Optional[UUID]]
    SalesInvoice: Optional[Optional[UUID]]
    Amount: Optional[Decimal]


class Liabilities(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ed5a19f6-12c5-45cc-b4b7-4e79f7ef50bc'
    Singleton: ClassVar[bool] = True


class LockDate(ManagerBaseModel):
    Key: ClassVar[UUID] = '4c5dac8f-2d5e-4634-a51b-0bbdd021a499'
    Singleton: ClassVar[bool] = True
    LockAccountingPeriods: Optional[bool]
    Date: Optional[Optional[date]]


class MultipleValueCustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = 'f32774a9-f740-4c2b-8353-b321576f6166'
    Singleton: ClassVar[bool] = False
    class Option(ManagerBaseModel):
        Value: Optional[str]
    Name: Optional[str]
    Position: Optional[Optional[int]]
    Placement: Optional[List[UUID]]
    Options: Optional[List[Option]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class NonInventoryItem(ManagerBaseModel):
    Key: ClassVar[UUID] = '7affe9ee-731f-4936-8acf-15cae7bcacee'
    Singleton: ClassVar[bool] = False
    Code: Optional[str]
    Name: Optional[str]
    UnitName: Optional[str]
    WhenSold: Optional[Optional[UUID]]
    WhenPurchased: Optional[Optional[UUID]]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultSalesUnitPrice: Optional[bool]
    DefaultSalesUnitPrice: Optional[Decimal]
    HasDefaultPurchaseUnitPrice: Optional[bool]
    DefaultPurchaseUnitPrice: Optional[Decimal]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    HasDefaultDivision: Optional[bool]
    DefaultDivision: Optional[Optional[UUID]]
    HideItemNameOnPrintedDocuments: Optional[bool]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    HasDefaultQty: Optional[bool]
    DefaultQty: Optional[Optional[Decimal]]
    PurchaseItemAccount: Optional[Optional[UUID]]
    SaleItemAccount: Optional[Optional[UUID]]


class NumberCustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = '68e09438-7aa1-4d63-b7d3-ce2dcd052e88'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Position: Optional[Optional[int]]
    Placement: Optional[List[UUID]]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    HideTotalAmount: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class Payment(ManagerBaseModel):
    Key: ClassVar[UUID] = '79f99d26-e43a-4ecb-a9c9-0774601a9b2e'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        AccountsReceivableCustomer: Optional[Optional[UUID]]
        AccountsReceivableSalesInvoice: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        BillableExpenseSalesInvoice: Optional[Optional[UUID]]
        AccountsPayableSupplier: Optional[Optional[UUID]]
        PurchaseInvoice: Optional[Optional[UUID]]
        WithholdingTaxPayableSupplier: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        ExpenseClaimsPayer: Optional[Optional[UUID]]
        Investment: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        PurchaseUnitPrice: Optional[Decimal]
        AutoUnitPrice: Optional[object]
        Amount: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    PaidFrom: Optional[Optional[UUID]]
    Cleared: Optional[BankAccountClearStatus]
    BankClearDate: Optional[Optional[date]]
    Payee: Optional[PayerPayeeType]
    Customer: Optional[Optional[UUID]]
    Supplier: Optional[Optional[UUID]]
    Contact: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[Optional[UUID]]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    FixedTotal: Optional[bool]
    FixedTotalAmount: Optional[Decimal]
    BalancingAmount: Optional[object]
    CustomTheme: Optional[bool]
    PaymentCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    PaymentCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPaymentFooters: Optional[bool]
    PaymentFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PaymentFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '6fbe0380-de89-4351-b5ac-eda06b5e7a80'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PaymentRule(ManagerBaseModel):
    Key: ClassVar[UUID] = '71ac4a94-6a53-4c0a-990c-e8174ab398d1'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        AccountsReceivableCustomer: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        AccountsPayableSupplier: Optional[Optional[UUID]]
        WithholdingTaxPayableSupplier: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        ExpenseClaimsPayer: Optional[Optional[UUID]]
        Investment: Optional[Optional[UUID]]
        Description: Optional[str]
        Qty: Optional[Optional[Decimal]]
        Amount: Optional[DiscountType]
        ExactAmount: Optional[Decimal]
        Percentage: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    class Condition(ManagerBaseModel):
        AndDescriptionContains: Optional[str]
    IfBankAccountIs: Optional[Optional[UUID]]
    AndAmountIs: Optional[AmountType]
    AndAmountIsAmount: Optional[Decimal]
    Conditions: Optional[List[Condition]]
    Payee: Optional[PayerPayeeType]
    Customer: Optional[Optional[UUID]]
    Supplier: Optional[Optional[UUID]]
    OtherContact: Optional[str]
    Lines: Optional[List[Line]]
    DescriptionColumn: Optional[bool]
    QuantityColumn: Optional[bool]


class Payslip(ManagerBaseModel):
    Key: ClassVar[UUID] = '1d103fa7-6fc1-4951-811e-972968b842cc'
    Singleton: ClassVar[bool] = False
    class Earned(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Description: Optional[str]
        Units: Optional[Optional[Decimal]]
        UnitPrice: Optional[Decimal]
        Division: Optional[Optional[UUID]]
    class Deduction(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Description: Optional[str]
        DeductionAmount: Optional[Decimal]
        Division: Optional[Optional[UUID]]
    class Contribution(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Description: Optional[str]
        ContributionAmount: Optional[Decimal]
        Division: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    description: Optional[str]
    employee: Optional[Optional[UUID]]
    Earnings: Optional[List[Earned]]
    Deductions: Optional[List[Deduction]]
    Contributions: Optional[List[Contribution]]
    ShowTotalsForThePeriod: Optional[bool]
    TotalsPeriodStart: Optional[Optional[date]]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    HasPayslipFooters: Optional[bool]
    PayslipFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PayslipContributionItem(ManagerBaseModel):
    Key: ClassVar[UUID] = '73af4c68-c347-4088-8846-758f1e7bc5bb'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    ExpenseAccount: Optional[Optional[UUID]]
    LiabilityAccount: Optional[Optional[UUID]]
    ReportingCategory: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PayslipContributionItemReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ad4c002b-f4ea-4bf5-85cc-f65dd4398794'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class PayslipDeductionItem(ManagerBaseModel):
    Key: ClassVar[UUID] = '0444eb18-6fc5-4d1f-be8b-c114da01832c'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Account: Optional[Optional[UUID]]
    ReportingCategory: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PayslipDeductionItemReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '1ccb2c74-e9ed-4642-9687-bdf9f3403f3b'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class PayslipEarningsItem(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ab02f6ab-c91c-4fc2-b979-66a6682c200e'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    ExpenseAccount: Optional[Optional[UUID]]
    ReportingCategory: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PayslipEarningsItemReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '3de1fae6-48ea-4901-8e1b-507483bfc4f3'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class PayslipFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '9c4197b6-212a-4c22-9338-6eaa659cfe49'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PayslipSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '3278903e-bf63-4f6f-b04d-a9e5ebd5a055'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]


class PayslipTotalsPerItemAndEmployee(ManagerBaseModel):
    Key: ClassVar[UUID] = '13de6e5f-cacf-46a1-adb9-2250f76d77dd'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class ProductionOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = 'da996523-e77e-493c-b134-31c6c6ccae4a'
    Singleton: ClassVar[bool] = False
    class Item(ManagerBaseModel):
        BillOfMaterials: Optional[Optional[UUID]]
        Qty: Optional[Decimal]
    class ExpenseItem(ManagerBaseModel):
        Account: Optional[Optional[UUID]]
        Amount: Optional[Decimal]
        Division: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    Description: Optional[str]
    FinishedInventoryItem: Optional[Optional[UUID]]
    Qty: Optional[Decimal]
    BillOfMaterials: Optional[List[Item]]
    InventoryLocation: Optional[Optional[UUID]]
    AddNonInventoryCostIntoProduction: Optional[bool]
    ExpenseItems: Optional[List[ExpenseItem]]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class ProfitAndLossStatement(ManagerBaseModel):
    Key: ClassVar[UUID] = '165c0392-9aad-4067-b855-a2393ead5df4'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        Division: Optional[Optional[UUID]]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    AccountingMethod: Optional[AccountingBasis]
    Rounding: Optional[Rounding]
    GroupsToCollapse: Optional[List[UUID]]
    Footer: Optional[str]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class ProfitAndLossStatementAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = '26b9e4a5-ce10-4f30-94c7-23a1ca4428f9'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatement: Optional[CashFlowStatementCategory]
    CashFlowStatementOperatingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementFinancingActivityGroup: Optional[Optional[UUID]]
    CashFlowStatementInvestingActivityGroup: Optional[Optional[UUID]]
    HasDefaultLineDescription: Optional[bool]
    DefaultLineDescription: Optional[str]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    Position: Optional[int]
    Inactive: Optional[bool]


class ProfitAndLossStatementAccountBillableExpensesCost(ManagerBaseModel):
    Key: ClassVar[UUID] = '234d263d-cf0e-4e3e-85ca-ef899016e58a'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableExpensesInvoiced(ManagerBaseModel):
    Key: ClassVar[UUID] = '1ae41f36-c83a-428c-be23-a99714110807'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableTimeInvoiced(ManagerBaseModel):
    Key: ClassVar[UUID] = '8d86390b-b90f-4cf6-862b-9b4050449b91'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountBillableTimeMovement(ManagerBaseModel):
    Key: ClassVar[UUID] = '03d41bd1-8dd4-4ce3-9b82-5ce17a40171a'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountCurrencyGainsLosses(ManagerBaseModel):
    Key: ClassVar[UUID] = '635ddd64-1176-4d35-b1c2-2d7d3bb12bb6'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    CashFlowStatementGroup: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountFixedAssetDepreciation(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fb6fdbfd-b39f-4674-8928-10c2bdd87e58'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountFixedAssetLossOnDisposal(ManagerBaseModel):
    Key: ClassVar[UUID] = '428ea9ba-4679-4568-b05b-7fcf62504893'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountIntangibleAssetsGainsLossOnDisposal(ManagerBaseModel):
    Key: ClassVar[UUID] = '43e14984-202e-4e9e-b843-d417dddcd3d2'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountIntangibleAssetsAmortization(ManagerBaseModel):
    Key: ClassVar[UUID] = '83d56444-fed8-4de8-8e58-e325a370ae44'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountInventoryPurchases(ManagerBaseModel):
    Key: ClassVar[UUID] = 'aa80b662-3642-4c08-b328-2fccf132ceb1'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountInventorySales(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ea44f579-9548-4954-baf0-48538aceff1e'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    HasDefaultTaxCode: Optional[bool]
    DefaultTaxCode: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountLatePaymentFees(ManagerBaseModel):
    Key: ClassVar[UUID] = '841b2acb-8bb5-4742-864e-4226fa421f44'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementAccountRoundingExpense(ManagerBaseModel):
    Key: ClassVar[UUID] = '2aa99eac-faca-4017-a157-edbbbcb160ac'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementActualVsBudget(ManagerBaseModel):
    Key: ClassVar[UUID] = '25c7aa0e-536c-42be-a75c-1b5ac71e955a'
    Singleton: ClassVar[bool] = False
    class BudgetItem(ManagerBaseModel):
        Account: Optional[Optional[UUID]]
        Amount: Optional[Decimal]
    Title: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Division: Optional[Optional[UUID]]
    Lines: Optional[List[BudgetItem]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    RoundDecimals: Optional[bool]


class ProfitAndLossStatementCapitalGainsOnInvestments(ManagerBaseModel):
    Key: ClassVar[UUID] = 'de8d014f-e862-4ab5-88cc-335d464315a6'
    Singleton: ClassVar[bool] = True
    Name: Optional[str]
    Code: Optional[str]
    Group: Optional[Optional[UUID]]
    Position: Optional[int]


class ProfitAndLossStatementGroup(ManagerBaseModel):
    Key: ClassVar[UUID] = '5770616c-0e01-46ca-a172-f7042275da6c'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Type: Optional[ProfitAndLossStatementGroupType]
    ParentGroup: Optional[Optional[UUID]]
    Position: Optional[int]


class Project(ManagerBaseModel):
    Key: ClassVar[UUID] = '5170f738-cfba-42e3-bb8e-a7d5c5ab66f2'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PurchaseInvoice(ManagerBaseModel):
    Key: ClassVar[UUID] = '58b9eb90-f6b8-4abc-8ea1-12fd77b8336e'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        BillableExpenseSalesInvoice: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        PurchaseUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    IssueDate: Optional[date]
    DueDate: Optional[DueDateType]
    DueDateDays: Optional[Optional[int]]
    DueDateDate: Optional[Optional[date]]
    Reference: Optional[str]
    OrderNumber: Optional[str]
    Supplier: Optional[Optional[UUID]]
    PurchaseQuote: Optional[Optional[UUID]]
    PurchaseOrder: Optional[Optional[UUID]]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    PurchaseInventoryLocation: Optional[Optional[UUID]]
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
    PurchaseInvoiceCustomTheme: Optional[Optional[UUID]]
    HideBalanceDue: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseInvoiceFooters: Optional[bool]
    PurchaseInvoiceFooters: Optional[List[UUID]]
    ClosedInvoice: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PurchaseInvoiceFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '06205221-f856-402f-8df9-104942cf579a'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PurchaseOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a26bbea1-57aa-4fd9-b7c9-e26b83114385'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        PurchaseUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    Supplier: Optional[Optional[UUID]]
    PurchaseQuote: Optional[Optional[UUID]]
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
    PurchaseOrderCustomTheme: Optional[Optional[UUID]]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseOrderFooters: Optional[bool]
    PurchaseOrderFooters: Optional[List[UUID]]
    Cancelled: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    AutomaticReference: Optional[bool]


class PurchaseOrderFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '38104c9e-7805-47de-935e-f6b660a470de'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class PurchaseQuote(ManagerBaseModel):
    Key: ClassVar[UUID] = '38d606f7-6358-4ace-9d1d-f6c0b9ea9d68'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        PurchaseUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    Supplier: Optional[Optional[UUID]]
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
    PurchaseQuoteCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    Cancelled: Optional[bool]
    CustomTitle: Optional[bool]
    PurchaseQuoteCustomTitle: Optional[str]
    RequestForQuotationCustomTitleOption: Optional[bool]
    RequestForQuotationCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseQuoteFooters: Optional[bool]
    PurchaseQuoteFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class PurchaseQuoteFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '072dd522-a137-4e91-8966-93f56f987cda'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Receipt(ManagerBaseModel):
    Key: ClassVar[UUID] = '7662b887-c8d8-486e-98fd-f9dbcd41c6dc'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        AccountsReceivableCustomer: Optional[Optional[UUID]]
        AccountsReceivableSalesInvoice: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        BillableExpenseSalesInvoice: Optional[Optional[UUID]]
        AccountsPayableSupplier: Optional[Optional[UUID]]
        PurchaseInvoice: Optional[Optional[UUID]]
        WithholdingTaxPayableSupplier: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        ExpenseClaimsPayer: Optional[Optional[UUID]]
        Investment: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        SalesUnitPrice: Optional[Decimal]
        AutoUnitPrice: Optional[object]
        Amount: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    PaidBy: Optional[PayerPayeeType]
    Customer: Optional[Optional[UUID]]
    Supplier: Optional[Optional[UUID]]
    Contact: Optional[str]
    ReceivedIn: Optional[Optional[UUID]]
    Cleared: Optional[BankAccountClearStatus]
    BankClearDate: Optional[Optional[date]]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    InventoryLocation: Optional[Optional[UUID]]
    HasLineNumber: Optional[bool]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    UnitPriceColumn: Optional[bool]
    Discount: Optional[bool]
    DiscountType: Optional[DiscountType]
    AmountsAreTaxExclusive: Optional[bool]
    FixedTotal: Optional[bool]
    FixedTotalAmount: Optional[Decimal]
    BalancingAmount: Optional[object]
    CustomTheme: Optional[bool]
    ReceiptCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    CustomTitle: Optional[bool]
    ReceiptCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasReceiptFooters: Optional[bool]
    ReceiptFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class ReceiptColumns(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ab9df426-967c-4851-92e8-d45e3188fc9c'
    Singleton: ClassVar[bool] = False
    Columns: Optional[List[Column]]


class ReceiptFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = 'b4053b7c-b07a-45ba-aa14-1e3a624f8565'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class ReceiptRule(ManagerBaseModel):
    Key: ClassVar[UUID] = '72ed576f-e78b-41eb-8188-73285f32c2d2'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        AccountsReceivableCustomer: Optional[Optional[UUID]]
        BillableExpenseCustomer: Optional[Optional[UUID]]
        AccountsPayableSupplier: Optional[Optional[UUID]]
        WithholdingTaxPayableSupplier: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        Employee: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        ExpenseClaimsPayer: Optional[Optional[UUID]]
        Investment: Optional[Optional[UUID]]
        Description: Optional[str]
        Qty: Optional[Optional[Decimal]]
        Amount: Optional[DiscountType]
        ExactAmount: Optional[Decimal]
        Percentage: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    class Condition(ManagerBaseModel):
        AndDescriptionContains: Optional[str]
    IfBankAccountIs: Optional[Optional[UUID]]
    AndAmountIs: Optional[AmountType]
    AndAmountIsAmount: Optional[Decimal]
    Conditions: Optional[List[Condition]]
    PaidBy: Optional[PayerPayeeType]
    Customer: Optional[Optional[UUID]]
    Supplier: Optional[Optional[UUID]]
    OtherContact: Optional[str]
    Lines: Optional[List[Line]]
    DescriptionColumn: Optional[bool]
    QuantityColumn: Optional[bool]


class ReceiptsAndPaymentsSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = 'fa775461-39a2-46a2-b022-adcad6c9b830'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]
    Footer: Optional[str]
    ExcludeZeroBalances: Optional[bool]
    AccountCodes: Optional[bool]


class RecurringInterAccountTransfer(ManagerBaseModel):
    Key: ClassVar[UUID] = '10ac4ab8-df74-4faf-b7fc-eb343556fb1b'
    Singleton: ClassVar[bool] = False
    nextIssueDate: Optional[Optional[date]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    description: Optional[str]
    paidFrom: Optional[Optional[UUID]]
    CreditAmount: Optional[Decimal]
    CreditClearStatus: Optional[BankAccountClearStatus]
    CreditClearDate: Optional[Optional[date]]
    receivedIn: Optional[Optional[UUID]]
    DebitAmount: Optional[Decimal]
    DebitClearStatus: Optional[BankAccountClearStatus]
    DebitClearDate: Optional[Optional[date]]
    AutomaticReference: Optional[bool]
    HasInterAccountTransferFooters: Optional[bool]
    InterAccountTransferFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    NextIssueDate: Optional[Optional[date]]
    PaidFrom: Optional[Optional[UUID]]
    ReceivedIn: Optional[Optional[UUID]]
    Description: Optional[str]


class RecurringJournalEntry(ManagerBaseModel):
    Key: ClassVar[UUID] = 'b4c1b390-351e-4579-b43b-412b920cddaf'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    Currency: Optional[Optional[UUID]]
    Narration: Optional[str]
    Lines: Optional[List[JournalEntry.Line]]
    InventoryLocation: Optional[Optional[UUID]]
    ForTaxPurposesThisIs: Optional[TaxTransactionType]
    HasLineDescription: Optional[bool]
    QuantityColumn: Optional[bool]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    HasJournalEntryFooters: Optional[bool]
    JournalEntryFooters: Optional[List[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringPayment(ManagerBaseModel):
    Key: ClassVar[UUID] = '789d22dc-bc42-4952-a591-60123b344726'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    PaidFrom: Optional[Optional[UUID]]
    Cleared: Optional[BankAccountClearStatus]
    Payee: Optional[PayerPayeeType]
    Customer: Optional[Optional[UUID]]
    Supplier: Optional[Optional[UUID]]
    Contact: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Payment.Line]]
    InventoryLocation: Optional[Optional[UUID]]
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
    PaymentFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringPayslip(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ae6e14e3-1d3d-4996-b466-ba41732a8dbe'
    Singleton: ClassVar[bool] = False
    nextIssueDate: Optional[Optional[date]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    employee: Optional[Optional[UUID]]
    description: Optional[str]
    Earnings: Optional[List[Payslip.Earned]]
    Deductions: Optional[List[Payslip.Deduction]]
    Contributions: Optional[List[Payslip.Contribution]]
    ShowTotalsForThePeriod: Optional[bool]
    TotalsPeriodStart: Optional[Optional[date]]
    CustomTheme: Optional[bool]
    Theme: Optional[Optional[UUID]]
    HasPayslipFooters: Optional[bool]
    PayslipFooters: Optional[List[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    NextIssueDate: Optional[Optional[date]]
    Employee: Optional[Optional[UUID]]
    Description: Optional[str]


class RecurringPurchaseInvoice(ManagerBaseModel):
    Key: ClassVar[UUID] = '11de04ac-c448-4665-b206-8aa631e63532'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    DueDate: Optional[Optional[int]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    Supplier: Optional[Optional[UUID]]
    PurchaseOrder: Optional[Optional[UUID]]
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
    PurchaseInvoiceCustomTheme: Optional[Optional[UUID]]
    HasPurchaseInvoiceFooters: Optional[bool]
    PurchaseInvoiceFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringPurchaseOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = '3be38758-7bf2-46f1-84a5-34e8748cade0'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    DueDate: Optional[Optional[int]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    Supplier: Optional[Optional[UUID]]
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
    PurchaseOrderCustomTheme: Optional[Optional[UUID]]
    ShowTaxAmountColumn: Optional[bool]
    HasPurchaseOrderFooters: Optional[bool]
    PurchaseOrderFooters: Optional[List[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringReceipt(ManagerBaseModel):
    Key: ClassVar[UUID] = '1c7ecd01-eb32-47b1-8ccd-e85f77969b03'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    PaidBy: Optional[PayerPayeeType]
    Customer: Optional[Optional[UUID]]
    Supplier: Optional[Optional[UUID]]
    Contact: Optional[str]
    ReceivedIn: Optional[Optional[UUID]]
    Cleared: Optional[BankAccountClearStatus]
    Description: Optional[str]
    Lines: Optional[List[Receipt.Line]]
    InventoryLocation: Optional[Optional[UUID]]
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
    ReceiptFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class SalesInvoice(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ad12b60b-23bf-4421-94df-8be79cef533e'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        Account: Optional[Optional[UUID]]
        CapitalAccount: Optional[Optional[UUID]]
        SubAccount: Optional[Optional[UUID]]
        SpecialAccount: Optional[Optional[UUID]]
        FixedAsset: Optional[Optional[UUID]]
        IntangibleAsset: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        SalesUnitPrice: Optional[Decimal]
        CurrencyAmount: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
        Project: Optional[Optional[UUID]]
        Division: Optional[Optional[UUID]]
    IssueDate: Optional[date]
    DueDate: Optional[DueDateType]
    DueDateDays: Optional[Optional[int]]
    DueDateDate: Optional[Optional[date]]
    Reference: Optional[str]
    QuoteNumber: Optional[str]
    OrderNumber: Optional[str]
    Customer: Optional[Optional[UUID]]
    SalesQuote: Optional[Optional[UUID]]
    SalesOrder: Optional[Optional[UUID]]
    BillingAddress: Optional[str]
    Description: Optional[str]
    Lines: Optional[List[Line]]
    SalesInventoryLocation: Optional[Optional[UUID]]
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
    EarlyPaymentDiscountDays: Optional[Optional[int]]
    LatePaymentFees: Optional[bool]
    LatePaymentFeesPercentage: Optional[Decimal]
    TotalAmountInWords: Optional[bool]
    TotalAmountInBaseCurrency: Optional[bool]
    Bilingual: Optional[bool]
    CustomTitle: Optional[bool]
    SalesInvoiceCustomTitle: Optional[str]
    HasSalesInvoiceCustomTheme: Optional[bool]
    SalesInvoiceCustomTheme: Optional[Optional[UUID]]
    AutomaticReference: Optional[bool]
    HideDueDate: Optional[bool]
    HideBalanceDue: Optional[bool]
    ClosedInvoice: Optional[bool]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesInvoiceFooters: Optional[bool]
    SalesInvoiceFooters: Optional[List[UUID]]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringSalesInvoice(ManagerBaseModel):
    Key: ClassVar[UUID] = '81385989-81e5-48c7-a819-c344324c1c01'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    DueDate: Optional[Optional[int]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    Customer: Optional[Optional[UUID]]
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
    SalesInvoiceCustomTheme: Optional[Optional[UUID]]
    EarlyPaymentDiscount: Optional[bool]
    EarlyPaymentDiscountType: Optional[DiscountType]
    EarlyPaymentDiscountRate: Optional[Decimal]
    EarlyPaymentDiscountAmount: Optional[Decimal]
    EarlyPaymentDiscountDays: Optional[Optional[int]]
    LatePaymentFees: Optional[bool]
    LatePaymentFeesPercentage: Optional[Decimal]
    CustomTitle: Optional[bool]
    SalesInvoiceCustomTitle: Optional[str]
    TotalAmountInWords: Optional[bool]
    HideDueDate: Optional[bool]
    HasSalesInvoiceFooters: Optional[bool]
    SalesInvoiceFooters: Optional[List[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class SalesOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = '2dac5598-128d-4954-b2e4-21515047b3a7'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        SalesUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
    Date: Optional[date]
    Reference: Optional[str]
    Customer: Optional[Optional[UUID]]
    SalesQuote: Optional[Optional[UUID]]
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
    SalesOrderCustomTheme: Optional[Optional[UUID]]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    CustomTitle: Optional[bool]
    SalesOrderCustomTitle: Optional[str]
    HasSalesOrderFooters: Optional[bool]
    SalesOrderFooters: Optional[List[UUID]]
    Cancelled: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringSalesOrder(ManagerBaseModel):
    Key: ClassVar[UUID] = 'dd7d5b17-c4be-4369-b0f5-79361525f3c2'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    ExpiryDate: Optional[Optional[int]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    Customer: Optional[Optional[UUID]]
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
    SalesOrderCustomTheme: Optional[Optional[UUID]]
    ShowTaxAmountColumn: Optional[bool]
    CustomTitle: Optional[bool]
    SalesOrderCustomTitle: Optional[str]
    HasSalesOrderFooters: Optional[bool]
    SalesOrderFooters: Optional[List[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class SalesQuote(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ba89de75-cb87-4bde-b20f-314f01b31037'
    Singleton: ClassVar[bool] = False
    class Line(ManagerBaseModel):
        Item: Optional[Optional[UUID]]
        LineDescription: Optional[str]
        CustomFields: Optional[Dict[UUID, str]]
        CustomFields2: Optional[CustomFields]
        Qty: Optional[Optional[Decimal]]
        SalesUnitPrice: Optional[Decimal]
        DiscountPercentage: Optional[Decimal]
        DiscountAmount: Optional[Decimal]
        TaxCode: Optional[Optional[UUID]]
    IssueDate: Optional[date]
    ExpiryDate: Optional[Optional[int]]
    Reference: Optional[str]
    Customer: Optional[Optional[UUID]]
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
    SalesQuoteCustomTheme: Optional[Optional[UUID]]
    CustomTitle: Optional[bool]
    SalesQuoteCustomTitle: Optional[str]
    ShowItemImages: Optional[bool]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesQuoteFooters: Optional[bool]
    SalesQuoteFooters: Optional[List[UUID]]
    Cancelled: Optional[bool]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class RecurringSalesQuote(ManagerBaseModel):
    Key: ClassVar[UUID] = '1ca6ee3a-3583-41d8-83b1-74ac9129e1c1'
    Singleton: ClassVar[bool] = False
    NextIssueDate: Optional[Optional[date]]
    ExpiryDate: Optional[Optional[int]]
    Interval: Optional[Optional[int]]
    PeriodType: Optional[Period]
    ExpirationType: Optional[ExpirationType]
    UntilDate: Optional[Optional[date]]
    Customer: Optional[Optional[UUID]]
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
    SalesQuoteCustomTheme: Optional[Optional[UUID]]
    CustomTitle: Optional[bool]
    SalesQuoteCustomTitle: Optional[str]
    ShowTaxAmountColumn: Optional[bool]
    HasSalesQuoteFooters: Optional[bool]
    SalesQuoteFooters: Optional[List[UUID]]
    AutomaticReference: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class ReportTranformationFromDate(ManagerBaseModel):
    Key: ClassVar[UUID] = 'cef33379-d1b3-4172-b090-0fc24cf978da'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTranformationToDate(ManagerBaseModel):
    Key: ClassVar[UUID] = '8ba7e5e7-8f74-443a-b7ee-d8539b12e7e2'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTransformation2(ManagerBaseModel):
    Key: ClassVar[UUID] = '02c3fbc6-4473-436f-b58d-fd51937f4e77'
    Singleton: ClassVar[bool] = False
    class Item(ManagerBaseModel):
        Name: Optional[str]
        Column1: Optional[List[UUID]]
        Column2: Optional[List[UUID]]
        Column3: Optional[List[UUID]]
        Column4: Optional[List[UUID]]
        Column5: Optional[List[UUID]]
    class InstructionStep(ManagerBaseModel):
        Text: Optional[str]
    Name: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    Employee: Optional[Optional[UUID]]
    Columns: Optional[ColumnCount]
    Items2: Optional[List[Item]]
    AccountingMethod: Optional[bool]
    AccountingMethodOption: Optional[AccountingBasis]
    Suppliers: Optional[bool]
    SupplierCustomField: Optional[Optional[UUID]]
    SupplierCustomFieldValue: Optional[str]
    ForEachSupplier: Optional[List[Item]]
    Employees: Optional[bool]
    ForEachEmployee: Optional[List[Item]]
    Script: Optional[bool]
    CustomScript: Optional[str]
    Instructions: Optional[bool]
    InstructionLines: Optional[List[InstructionStep]]
    Published: Optional[bool]
    HasAccountingMethod: Optional[bool]


class ReportTransformationFromDateLastJuly(ManagerBaseModel):
    Key: ClassVar[UUID] = '7d3ddc8b-49f1-4064-997a-430367e54055'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTransformationLabel(ManagerBaseModel):
    Key: ClassVar[UUID] = '849c558a-5f58-4779-939b-dc9d2f5ac89f'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTransformationNetAmounts(ManagerBaseModel):
    Key: ClassVar[UUID] = '928f0950-d042-46fd-9ea8-b73c947a23b7'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTransformationReport(ManagerBaseModel):
    Key: ClassVar[UUID] = 'bbe8c088-729b-4b56-a7d7-26555270eced'
    Singleton: ClassVar[bool] = False
    ReportTransformation: Optional[Optional[UUID]]
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Employee: Optional[Optional[UUID]]


class ReportTransformationTaxAmounts(ManagerBaseModel):
    Key: ClassVar[UUID] = '094377dd-1f71-40cf-bb48-58daf961aa71'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTransformationTaxPurchases(ManagerBaseModel):
    Key: ClassVar[UUID] = '89c4e9b6-f555-4243-8432-680a1cc97a61'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReportTransformationTaxSales(ManagerBaseModel):
    Key: ClassVar[UUID] = '211bb6c2-9ca7-4cda-a099-99bcde19a173'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class ReverseSignReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '0b3fe333-755b-42c0-b921-2835e39e50f0'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class RoundDownReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '0846abcd-dc2a-4914-9c9b-9d7130ac99d6'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class SalesInvoiceFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = 'eaaee0ba-9c58-4f7b-a800-2857f0a675af'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class SalesInvoiceTotalsByCustomer(ManagerBaseModel):
    Key: ClassVar[UUID] = '997f3bd6-37ee-4b36-b066-2bb0a402ebab'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class SalesInvoiceTotalsByCustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = '8ea7ac48-0071-4e58-8647-c1f9b17f1dc6'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Name: Optional[str]
    CustomField: Optional[Optional[UUID]]
    Periods: Optional[List[Period]]


class SalesInvoiceTotalsByItem(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c70ca645-2d2b-4536-8f81-aead1b7eba99'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        ColumnName: Optional[str]
    Description: Optional[str]
    Periods: Optional[List[Period]]


class SalesOrderFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = '38bf923a-9ab8-4d86-a12a-9d2581d13fa8'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class SalesQuoteFooter(ManagerBaseModel):
    Key: ClassVar[UUID] = 'd95df676-e2cb-4be6-a9b3-86dcd79ac3bc'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Content: Optional[str]
    Inactive: Optional[bool]


class Schema(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a9a71e47-82b3-49db-8aec-898adb460a80'
    Singleton: ClassVar[bool] = False
    Version: Optional[int]


class SetZeroIfNegativeReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '1a94b65c-4869-4138-acc1-49d16bbfeed6'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class SpecialAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'e495f4e8-5fad-48ac-8a66-f35049ac4ef3'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    Currency: Optional[Optional[UUID]]
    TaxCode: Optional[Optional[UUID]]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[Decimal]
    StartingBalanceType: Optional[DebitCredit]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class CapitalAccountsSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '19f661de-d63c-4d25-bd00-3e05578018b1'
    Singleton: ClassVar[bool] = False
    Title: Optional[str]
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    Rounding: Optional[Rounding]
    ReverseSigns: Optional[bool]
    ExcludeZeroBalances: Optional[bool]
    Footer: Optional[str]


class StatementOfChangesInEquity(ManagerBaseModel):
    Key: ClassVar[UUID] = '06d97eb4-27de-41ee-80ef-47b8115b5b36'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
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


class SubAccount(ManagerBaseModel):
    Key: ClassVar[UUID] = 'f361339b-932a-4436-b56e-a337c1587c72'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]


class Subtotal(ManagerBaseModel):
    Key: ClassVar[UUID] = '9601ce49-6058-4dac-9405-82f35005ea90'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Position: Optional[int]


class Summary(ManagerBaseModel):
    Key: ClassVar[UUID] = '2631d044-861d-4710-a871-d7a11461b4ba'
    Singleton: ClassVar[bool] = False
    ShowBalancesForSpecifiedPeriod: Optional[bool]
    FromDate: Optional[date]
    ToDate: Optional[DateType]
    ToDateValue: Optional[date]
    ShowBalancesOnCashBasis: Optional[bool]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]
    HasGroupsToCollapse: Optional[bool]
    GroupsToCollapse: Optional[List[UUID]]


class Supplier(ManagerBaseModel):
    Key: ClassVar[UUID] = '6d2dc48d-2053-4e45-8330-285ebd431242'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Code: Optional[str]
    CreditLimit: Optional[Decimal]
    Currency: Optional[Optional[UUID]]
    Address: Optional[str]
    Email: Optional[str]
    Division: Optional[Optional[UUID]]
    ControlAccount: Optional[Optional[UUID]]
    StartingBalance: Optional[Decimal]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
    Inactive: Optional[bool]


class SupplierNameField(ManagerBaseModel):
    Key: ClassVar[UUID] = '22ec22e1-8ed2-4cba-a5b9-533a1e451977'
    Singleton: ClassVar[bool] = True
    ContainsGeneralLedgerTransactions: Optional[bool]


class SupplierStatementsTransactions(ManagerBaseModel):
    Key: ClassVar[UUID] = '401d5f3c-92ef-47da-942a-3cd6cf64aa9c'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[DateType]
    ToCustomDate: Optional[date]
    Theme: Optional[Optional[UUID]]


class SupplierStatementsUnpaidInvoices(ManagerBaseModel):
    Key: ClassVar[UUID] = '119e71a0-3ea5-4c6f-a8f2-76384b86831a'
    Singleton: ClassVar[bool] = False
    Date: Optional[DateType]
    CustomDate: Optional[date]
    Theme: Optional[Optional[UUID]]


class SupplierSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '80d4616c-d083-4f8a-9ea9-b9dd5f04360f'
    Singleton: ClassVar[bool] = False
    FromDate: Optional[date]
    ToDate: Optional[date]
    Division: Optional[Optional[UUID]]


class Tabs(ManagerBaseModel):
    Key: ClassVar[UUID] = 'ac789d1f-034f-4964-a8b5-ebfffc3511f2'
    Singleton: ClassVar[bool] = True
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


class TaxablePurchasesPerSupplier(ManagerBaseModel):
    Key: ClassVar[UUID] = '1f957bf2-d198-4a9a-bb51-8d7d26b2fc5c'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TaxableSalesPerCustomer(ManagerBaseModel):
    Key: ClassVar[UUID] = '2623ae0a-3c13-45e7-83b7-e4c9b2b9404d'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TaxAmountReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = 'f58e8724-7e63-422c-8649-a12cf77c2208'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class TaxAmountReversedReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '52a10ec1-0808-4641-91b8-45eb33626ae3'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class TaxAudit(ManagerBaseModel):
    Key: ClassVar[UUID] = 'a43c996d-707a-48cb-91c8-191feab4411f'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TaxCode(ManagerBaseModel):
    Key: ClassVar[UUID] = '7f368d97-8b7f-4b39-b156-dc66afd9496a'
    Singleton: ClassVar[bool] = False
    class Component(ManagerBaseModel):
        Name: Optional[str]
        ComponentRate: Optional[Decimal]
        ComponentAccount: Optional[Optional[UUID]]
        ComponentTaxAmountReportingCategory: Optional[Optional[UUID]]
        ComponentTaxAmountReversedReportingCategory: Optional[Optional[UUID]]
    class TaxAmount(ManagerBaseModel):
        TaxCode: Optional[UUID]
        Code: Optional[str]
        Amount: Optional[Decimal]
        Account: Optional[Optional[UUID]]
        TaxReportingCategory: Optional[Optional[UUID]]
        TaxReportingCategoryReversed: Optional[Optional[UUID]]
        NegativeRate: Optional[bool]
    Name: Optional[str]
    Label: Optional[str]
    ReportingCategory: Optional[Optional[UUID]]
    ReportingCategoryReversed: Optional[Optional[UUID]]
    TaxRate: Optional[TaxRate]
    Type: Optional[TaxRateType]
    Rate: Optional[Decimal]
    Account: Optional[Optional[UUID]]
    TaxAmountReportingCategory: Optional[Optional[UUID]]
    TaxAmountReversedReportingCategory: Optional[Optional[UUID]]
    Components: Optional[List[Component]]
    ReverseCharged: Optional[bool]
    CustomSalesInvoiceTitle: Optional[bool]
    SalesInvoiceTitle: Optional[str]
    CustomCreditNoteTitle: Optional[bool]
    CreditNoteTitle: Optional[str]
    Inactive: Optional[bool]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]


class TaxCodeReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '0cb739c7-6767-4949-88a7-6415c5ec083d'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class TaxCodeReversedReportingCategory(ManagerBaseModel):
    Key: ClassVar[UUID] = '6027ab88-f804-4827-beff-26b76bb94587'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class TaxReconciliation(ManagerBaseModel):
    Key: ClassVar[UUID] = '82fb1232-ba69-4310-b443-22df87ef18fa'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
    Description: Optional[str]
    AccountingMethod: Optional[AccountingBasis]
    Periods: Optional[List[Period]]


class TaxSummary(ManagerBaseModel):
    Key: ClassVar[UUID] = '68e0d57b-4a59-453e-b8d4-6166f097eacd'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]
    Division: Optional[Optional[UUID]]


class TaxTransactions(ManagerBaseModel):
    Key: ClassVar[UUID] = '9a441483-1a09-46d3-aecd-477c91c13ae1'
    Singleton: ClassVar[bool] = False
    Description: Optional[str]
    FromDate: Optional[date]
    ToDate: Optional[date]
    AccountingMethod: Optional[AccountingBasis]


class TextCustomField(ManagerBaseModel):
    Key: ClassVar[UUID] = '411f5975-0376-4ba9-b7ff-5bb2baa6f69f'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Position: Optional[Optional[int]]
    Placement: Optional[List[UUID]]
    Type: Optional[TextCustomFieldType]
    OptionsForDropdownList: Optional[str]
    Size: Optional[CustomFieldSize]
    Description: Optional[str]
    DisplayOnList: Optional[bool]
    DisplayOnView: Optional[bool]
    ShowAtTheTop: Optional[bool]
    Inactive: Optional[bool]
    ContainsGeneralLedgerTransactions: Optional[bool]


class Theme(ManagerBaseModel):
    Key: ClassVar[UUID] = '01e1bcb2-74c1-467d-aedc-5e8f738fe776'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Template: Optional[str]
    Inactive: Optional[bool]


class TrialBalance(ManagerBaseModel):
    Key: ClassVar[UUID] = 'e5dc98ef-4662-4a68-8a9d-b3e2d12b55d6'
    Singleton: ClassVar[bool] = False
    class Period(ManagerBaseModel):
        FromDate: Optional[date]
        ToDate: Optional[date]
        Division: Optional[Optional[UUID]]
        ColumnName: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    AccountingMethod: Optional[AccountingBasis]
    Periods: Optional[List[Period]]
    AccountCodes: Optional[bool]
    ExcludeZeroBalances: Optional[bool]


class Session(ManagerBaseModel):
    Key: Optional[UUID]
    Timestamp: Optional[date]
    UserAgent: Optional[str]
    Location: Optional[str]


class User(ManagerBaseModel):
    Key: ClassVar[UUID] = '8112e1a9-fe00-47c4-9d7a-2d034f8a1f34'
    Singleton: ClassVar[bool] = False
    Name: Optional[str]
    Username: Optional[str]
    Password: Optional[str]
    Type: Optional[UserType]
    Businesses: Optional[List[str]]
    Sessions: Optional[List[Session]]


class UserPermissions(ManagerBaseModel):
    Key: ClassVar[UUID] = 'c6a5d19f-6f47-4716-841d-ba06ca9fc311'
    Singleton: ClassVar[bool] = False
    Username: Optional[str]
    BankAndCashAccounts: Optional[List[UUID]]
    AccessType: Optional[UserPermissionsAccessType]
    Namespaces: Optional[Dict[str, bool]]
    Namespaces2: Optional[Dict[str, Optional[PermittedActions]]]
    FullAccess: Optional[bool]


class WithholdingTaxReceipt(ManagerBaseModel):
    Key: ClassVar[UUID] = '8f7510d9-a92d-4b4c-9421-fd745e198b3c'
    Singleton: ClassVar[bool] = False
    Date: Optional[date]
    Customer: Optional[Optional[UUID]]
    Amount: Optional[Decimal]
    Description: Optional[str]
    CustomFields: Optional[Dict[UUID, str]]
    CustomFields2: Optional[CustomFields]
