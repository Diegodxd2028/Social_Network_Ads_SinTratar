import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cargar los datos desde tu archivo Excel
data = pd.read_excel("C:\\Users\\labf603\\PycharmProjects\\Inteligencia_de_Negocios\\Social_Network_Ads_SinTratar.xlsx")

# 1. Calcular la media y la mediana de la variable Age
mean_age = data['Age'].mean()
median_age = data['Age'].median()
print("Media de Age:", mean_age)
print("Mediana de Age:", median_age)

# 2. Detectar valores atípicos en Age y EstimatedSalary
Q1_age = data['Age'].quantile(0.25)
Q3_age = data['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age

Q1_salary = data['EstimatedSalary'].quantile(0.25)
Q3_salary = data['EstimatedSalary'].quantile(0.75)
IQR_salary = Q3_salary - Q1_salary

# Identificar valores atípicos
age_outliers = data[(data['Age'] < (Q1_age - 1.5 * IQR_age)) | (data['Age'] > (Q3_age + 1.5 * IQR_age))]
salary_outliers = data[(data['EstimatedSalary'] < (Q1_salary - 1.5 * IQR_salary)) | (
            data['EstimatedSalary'] > (Q3_salary + 1.5 * IQR_salary))]

print("Valores atípicos en Age:", age_outliers)
print("Valores atípicos en EstimatedSalary:", salary_outliers)

# 3. Calcular la correlación entre Age y EstimatedSalary
correlation = data['Age'].corr(data['EstimatedSalary'])
print("Correlación entre Age y EstimatedSalary:", correlation)

# 4. Visualizar factores que determinan la compra usando gráficos
sns.boxplot(x='Purchased', y='Age', data=data)
plt.title("Distribución de Edad según Compra")
plt.show()

sns.boxplot(x='Purchased', y='EstimatedSalary', data=data)
plt.title("Distribución de Salario Estimado según Compra")
plt.show()
