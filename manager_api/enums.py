# -*- coding: utf-8 -*-
# Do not edit. Automatically generated from Manager v26.2.20.3187.

from typing import Literal


NumberOperator = Literal[
 "IsLessThan",
 "IsMoreThan",
 "IsNotZero",
 "IsZero",
]

EnumOperator = Literal[
 "Is",
 "IsNot",
]

StringOperator = Literal[
 "Contains",
 "DoesNotContain",
 "IsEmpty",
 "IsNotEmpty",
]

DecimalOperator = Literal[
 "IsLessThan",
 "IsMoreThan",
 "IsNotZero",
 "IsZero",
]

DateOperator = Literal[
 "IsExactly",
 "IsAfter",
 "IsOnOrAfter",
 "IsBefore",
 "IsBeforeOrOn",
]

BooleanOperator = Literal[
 "IsChecked",
 "IsNotChecked",
]

ObjectOperator = Literal[
 "Is",
 "IsNot",
 "IsEmpty",
 "IsNotEmpty",
]

LocationType = Literal[
 "Custom",
 "Everywhere",
]

FieldType = Literal[
 "String",
 "Decimal",
 "Boolean",
 "Date",
 "Object",
]

ColumnCount = Literal[
 "Two",
 "Three",
 "Four",
 "Five",
 "Six",
]

UserType = Literal[
 "Administrator",
 "Restricted",
]

Visibility = Literal[
 "Visible",
 "Hidden",
]

PermittedActions = Literal[
 "ViewCreateUpdateDelete",
 "ViewCreateUpdate",
 "ViewCreate",
 "View",
]

AccountingBasis = Literal[
 "AccrualBasis",
 "CashBasis",
]

AmountType = Literal[
 "AnyAmount",
 "Exactly",
 "MoreThan",
 "LessThan",
]

BalanceSheetLayout = Literal[
 "AssetsLiabilitiesEqualsEquity",
 "AssetsEqualsLiabilitiesEquity",
 "AssetsEqualsEquityLiabilities",
]

BankAccountClearStatus = Literal[
 "OnTheSameDate",
 "OnALaterDate",
]

BankClearStatus = Literal[
 "Pending",
 "Cleared",
]

BillableTimeStatus = Literal[
 "Uninvoiced",
 "Invoiced",
 "WrittenOff",
]

CashAccountType = Literal[
 "CashAtBank",
 "CashOnHand",
]

CashFlowStatementCategory = Literal[
 "OperatingActivities",
 "InvestingActivities",
 "FinancingActivities",
 "CashAndCashEquivalents",
]

CashFlowStatementMethod = Literal[
 "IndirectMethod",
 "DirectMethod",
]

ControlAccountType = Literal[
 "BankAccounts",
 "Customers",
 "Suppliers",
 "InventoryItems",
 "FixedAssets",
 "IntangibleAssets",
 "SpecialAccounts",
 "Employees",
 "CapitalAccounts",
 "FixedAssetsAccumulatedDepreciation",
 "IntangibleAssetsAccumulatedAmortization",
 "Investments",
]

CreditNoteType = Literal[
 "Custom",
 "EarlyPaymentDiscount",
]

CustomerField = Literal[
 "Name",
 "Code",
 "BillingAddress",
 "Email",
 "CustomField",
]

CustomFieldPlacement = Literal[
 "BusinessDetails",
 "BankAndCashAccounts",
 "Receipts",
 "Payments",
 "InterAccountTransfers",
 "Customers",
 "Suppliers",
 "Employees",
 "CreditNotes",
 "CreditNoteLines",
 "DebitNotes",
 "DebitNoteLines",
 "SalesInvoices",
 "SalesInvoiceLines",
 "WithholdingTaxReceipts",
 "SalesQuotes",
 "SalesQuoteLines",
 "SalesOrders",
 "SalesOrderLines",
 "BillableTime",
 "DeliveryNotes",
 "DeliveryNoteLines",
 "GoodsReceipts",
 "GoodsReceiptLines",
 "InventoryTransfers",
 "InventoryTransferLines",
 "Payslips",
 "JournalEntries",
 "InventoryItems",
 "InventoryWriteOffs",
 "FixedAssets",
 "IntangibleAssets",
 "ExpenseClaims",
 "PurchaseInvoices",
 "PurchaseQuotes",
 "PurchaseOrders",
 "ProductionOrders",
 "CapitalAccounts",
 "SpecialAccounts",
 "Folders",
 "NonInventoryItems",
 "TaxCodes",
]

CustomFieldSize = Literal[
 "Small",
 "Medium",
 "Large",
]

CustomFieldStyle = Literal[
 "SingleLineText",
 "ParagraphText",
 "DropdownList",
 "Image",
 "Date",
 "Number",
]

DateType = Literal[
 "Today",
 "Custom",
]

DebitCredit = Literal[
 "Debit",
 "Credit",
]

DeliveryNoteColumns = Literal[
 "DeliveryDate",
 "Reference",
 "SalesInvoice",
 "InventoryLocation",
 "Customer",
 "Description",
 "CustomFields2",
 "CustomFields",
 "OrderNumber",
 "InvoiceNumber",
]

DepreciationMethod = Literal[
 "Manual",
 "StraightLine",
 "DecliningBalance",
]

DisbursementStatus = Literal[
 "Uninvoiced",
 "Invoiced",
 "WrittenOff",
]

DiscountType = Literal[
 "Percentage",
 "ExactAmount",
]

DueDateType = Literal[
 "Net",
 "By",
]

DueDateType2 = Literal[
 "By",
 "Net",
]

EmailFormat = Literal[
 "Link",
 "PDF",
]

ExchangeRateType = Literal[
 "BaseRate",
 "CounterRate",
]

ExpirationType = Literal[
 "UntilFurtherNotice",
 "Custom",
]

ExtensionSource = Literal[
 "Url",
 "Inline",
]

FirstDayOfWeek = Literal[
 "Monday",
 "Sunday",
 "Saturday",
]

FixedAssetStartingBalanceType = Literal[
 "AcquisitionCost",
 "AccumulatedDepreciation",
]

IntangibleAssetStartingBalanceType = Literal[
 "AcquisitionCost",
 "AccumulatedAmortization",
]

InventoryItemStartingBalanceType = Literal[
 "QtyOnHand",
 "QtyToDeliver",
 "QtyToReceive",
]

InventoryLocationType = Literal[
 "InventoryOnHand",
 "Customer",
 "Supplier",
]

InventoryValuationMethod = Literal[
 "FirstInFirstOut",
 "WeightedAverageCost",
 "Manual",
]

InventoryValuationMethodWithoutManual = Literal[
 "FirstInFirstOut",
 "WeightedAverageCost",
]

LatePaymentFeesType = Literal[
 "DoNotCharge",
 "ChargeMonthly",
]

MonthDay = Literal[
 "OnTheSameDay",
 "OnTheLastDay",
]

PageSize = Literal[
 "A4",
 "Letter",
]

PayerPayeeType = Literal[
 "Customer",
 "Supplier",
 "Other",
]

Period = Literal[
 "Month",
 "Week",
 "Day",
]

ProfitAndLossStatementGroupType = Literal[
 "IncomeGroup",
 "ExpenseGroup",
 "SubgroupOf",
]

Protocol = Literal[
 "HTTP",
 "SMTP",
]

Repeat = Literal[
 "Never",
 "EveryDay",
 "EveryWeek",
 "EveryTwoWeeks",
 "EveryMonth",
 "EveryTwoMonths",
 "EveryThreeMonths",
 "EverySixMonths",
 "EveryYear",
]

Rounding = Literal[
 "Off",
 "On",
]

RoundingMethod = Literal[
 "None",
 "RoundToNearest",
 "RoundDown",
]

SalesInvoiceField = Literal[
 "Reference",
 "IssueDate",
 "DueDate",
 "InvoiceTotal",
 "BalanceDue",
 "TaxAmount",
 "Customer",
 "CustomField",
]

SmtpPort = Literal[
 "_25",
 "_465",
 "_587",
]

SortBy = Literal[
 "Total",
 "Name",
]

SortOrder = Literal[
 "Ascending",
 "Descending",
]

StartingBalanceAccount = Literal[
 "BankOrCashAccount",
 "Customer",
 "Supplier",
 "Employee",
 "InventoryItem",
 "Investment",
 "FixedAsset",
 "IntangibleAsset",
 "CapitalAccount",
 "SpecialAccount",
 "Other",
]

StartingBalanceType = Literal[
 "PaidInAdvance",
 "AmountToPay",
]

TaxRate = Literal[
 "ZeroRate",
 "TotalRate",
 "CustomRate",
]

TaxRateType = Literal[
 "SingleRate",
 "MultipleRates",
]

TaxTransactionType = Literal[
 "SaleOrSaleAdjustment",
 "PurchaseOrPurchaseAdjustment",
]

TextCustomFieldType = Literal[
 "SingleLineText",
 "ParagraphText",
 "DropdownList",
 "QrCode",
]

UserPermissionsAccessType = Literal[
 "CustomAccess",
 "FullAccess",
]

WithholdingTaxType = Literal[
 "Rate",
 "Amount",
]
