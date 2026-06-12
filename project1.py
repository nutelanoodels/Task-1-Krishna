import pandas as pd 
data = pd.read_excel("dataset1.xlsx")

#checkhing the data
print(data.head())
print(data.shape)
print(data.columns)
print(data.info())

#finding missing values
print("Total number of missing values :")
print(data.isnull().sum())
print("persentage of missing values :")
missingvalpercentage = (data.isnull().sum()/len(data))*100
print(missingvalpercentage)

#handeling the missing values
data["CouponCode"] = data["CouponCode"].fillna("no coupons")
print(data.isnull().sum())

#checking duplicate rows
duplicates = data.duplicated().sum()
print("duplicated rows :", duplicates)
data.drop_duplicates()

#checking duplicate orders
duplicateorders = data["OrderID"].duplicated().sum()
print("duplicate orders : ", duplicateorders)
print(data[data["OrderID"].duplicated()])
data.drop_duplicates(subset="OrderID")

#verify date formatw 
data["Date"] = pd.to_datetime(data["Date"])
print([data["Date"].head()])
data["Date"] = data["Date"].dt.strftime("%Y-%m-%d")
print([data["Date"].head()])

#removeing extraspaces
text_column = [
    "CustomerID",
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "CouponCode",
    "ReferralSource"
]
for col in text_column:
    data[col] = data[col].astype(str).str.strip()
    
#validating the numeric columns
numeric_cols = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors="coerce")
print(data[numeric_cols].dtypes)

#checking if the data is clean 
print("report")
print("Rows : ",len(data))
print("Columns : ",len(data.columns))
print("missing values : ")
print(data.isnull().sum())
print("duplicate rows : ",data.duplicated().sum())
print("duplicated orderid's : ",data["OrderID"].duplicated().sum())

#creating a clean dataset
data.to_excel("Cleaned_dataset.xlsx", index=False)
print("file saved succesfully")