print('-'*50)
total_land=80
divided_land=80/5
print("Total land = ",total_land)
print("Divided land for each crop = ",divided_land)
tomato_kg=(divided_land*0.3*10+divided_land*0.7*12)*1000
tomato_price=tomato_kg*7
potato_kg=divided_land*10*1000
potato_price=potato_kg*20
cabbage_kg=divided_land*14*1000
cabbage_price=cabbage_kg*24
sunflower_kg=divided_land*0.7*1000
sunflower_price=sunflower_kg*200
sugarcane_kg=divided_land*45
sugarcane_price=sugarcane_kg*4000

print('-'*50)
print("Revenue from tomato",tomato_price)
print("Revenue from potato",potato_price)
print("Revenue from cabbage",cabbage_price)
print("Revenue from sunflower",sunflower_price)
print("Revenue from sugarcane",sugarcane_price)

total_sales=tomato_price+potato_price+cabbage_price+sunflower_price+sugarcane_price

print("Total sales from 80 acres is ",total_sales)
print("For 11 months, only tomato, potato, cabbage, sunflower are converted to chemical free.\nSo the sales for 11 monthes are ",total_sales-sugarcane_price)

print('-'*50)