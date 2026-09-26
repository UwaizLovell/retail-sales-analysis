# Calculate revenue for each transaction
def calculate_revenue(df):
    return df["quantity"] * df["unit_price"]


# Calculate total revenue by category
def revenue_by_category(df):
    return df.groupby("category")["revenue"].sum()


# Calculate total revenue by store
def revenue_by_store(df):
    return df.groupby("store")["revenue"].sum()


# Calculate total revenue by product
def revenue_by_product(df):
    return df.groupby("product_name")["revenue"].sum()


# Calculate total revenue by month
def revenue_by_month(df):
    return df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
