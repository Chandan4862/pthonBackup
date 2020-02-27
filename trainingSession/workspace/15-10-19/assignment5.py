caramel={"wethers original","sugar daddy","twix","rolo","snickers","take 5","peanut bittle"}
cookie={"sugar cookie","kitkat","twix","take 5","sugar daddy","nutter butter"}
chocolate={"Kisses","rolo","twix","kitkat","take 5","snickers","peanut cup"}
nuts={"peanut cup","snickers","take 5","peanut bittle","nutter butter","sugar glazed akmound"}

#caramel but not choclate
set1= caramel.difference(chocolate)
print("caramel but not choclate",set1)

#all elements of cookie and nuts but not caramel
set2= cookie.union(nuts).difference(caramel)
print("all elements of cookie and nuts but not caramel",set2)

#common elemets of Nuts and choclate
set3= nuts.intersection(chocolate)
print("common elemets of Nuts and choclate",set3)