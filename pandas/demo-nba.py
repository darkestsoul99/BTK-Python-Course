import pandas as pd 

df = pd.read_csv("all_seasons.csv") # conversion to data frame object 

# 1 - İlk 10 kaydı getiriniz
result = df.head(10)

# 2 - Toplam kaç kayıt vardır ? 
result = len(df.index)

# 3 - Tüm oyuncuların toplam maaş ortalaması nedir ? 
result = df["gp"].mean()

# 4 - En yüksek maaşı ne kadardır ? 
result = df["gp"].max()

print(result)

