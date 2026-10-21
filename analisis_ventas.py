import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("Northwind.db")
cursor = conn.cursor()

cursor.execute('''
SELECT 
    o.ProductID,
    SUM(o.Quantity * p.Price) AS Ingresos
FROM OrderDetails o
INNER JOIN Products p 
    ON o.ProductID = p.ProductID
GROUP BY o.ProductID
ORDER BY Ingresos DESC
LIMIT 10;
''')

results = cursor.fetchall()

results_df = pd.DataFrame(results, columns=["ProductID", "Ingresos"])


cursor.close()
conn.close()

print(results_df)

sns.barplot(
    x="ProductID",
    y="Ingresos",
    data=results_df
)

plt.show()

conn1=sqlite3.connect("Northwind.db")
cursor1=conn1.cursor()
cursor1.execute(""" SELECT vista.EmployeeID, SUM(Quantity*price) as cantidad_de_ganancias FROM vista 
INNER JOIN Products pr ON vista.ProductID=pr.ProductID
GROUP BY vista.EmployeeID
ORDER BY cantidad_de_ganancias DESC
LIMIT 10""")
results1=cursor1.fetchall()
results1_df=pd.DataFrame(results1,columns=["EmployeeID","cantidad_de_ganancias"])
sns.barplot(x="EmployeeID",y="cantidad_de_ganancias",data=results1_df)
plt.show()
