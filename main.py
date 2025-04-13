import pandas as pd

# The raw data
df = pd.read_csv ("sales.csv")

# read the data
print ("Data asal:")
print (df)

# Clean and transform the data
df = df[df["Amount"]>1000] # Nak amount yang lebih 1000 jer
df ["Region"] = df ["Region"].str.title() # Amount = Region

# Final outcomes
print ("\nData selepas dibersihkan:")
print (df)

# save to the new CSV file
df.to_csv ("sales_cleaned.csv", index=False)


