import pandas as pd

df_1 = pd.read_csv(r"C:\Users\MrMagoo\Desktop\Data Science\Final Project - easyMoney\data\sociodemographic_df.csv")
df_2 = pd.read_csv(r"C:\Users\MrMagoo\Desktop\Data Science\Final Project - easyMoney\data\products_df.csv")
df_3 = pd.read_csv(r"C:\Users\MrMagoo\Desktop\Data Science\Final Project - easyMoney\data\commercial_activity_df.csv")

df_1.drop(columns = ["Unnamed: 0"], inplace = True)
df_2.drop(columns = ["Unnamed: 0", "pk_cid", "pk_partition"], inplace = True)
df_3.drop(columns = ["Unnamed: 0", "pk_cid", "pk_partition"], inplace = True)

df = pd.concat([df_1, df_2, df_3], axis = 1)
df.to_csv("../data/Bobs_df.csv")