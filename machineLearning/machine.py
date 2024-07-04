import numpy as np
import matplotlib.pyplot as plt
print(f"Learning about linear regression")

def func(w,x,b):
# model function
    fun = w*x +b
    return(fun)

def output_model(x,w,b):
# produce prediction for y
    m = len(x)
    f_wb = np.zeros(m) # produces array of m numbers with 0 as its elements
    for i in range(m):
        f_wb[i]=func(w,x[i],b)
    return f_wb

# training data set
x_train =  np.array([1,2])
y_train = np.array([300,500])
m = len(x_train)
print(f"x_train: {x_train}\ny_train: {y_train}\nthe number of training data set(m): {m}")

#labeling of the graph
plt.title("housing price")
plt.ylabel('price in 1000')
plt.xlabel('size in 1000sqft')

# to plot the data set
w= 200
b = 100
plt.scatter(x_train,y_train,marker = 'x', c='r',label="Actual values")
# scatter gives the points only

#to test model function
temp = output_model(x_train,w,b)
plt.plot(x_train,temp, c='b',label = "Predicted values")
#plot gives the solid line joining the points

# to make prediction
x = int(input("Enter square feet: "))
cost = func(w,x,b)
plt.scatter(x,cost,marker='o',c='g',label='sold for')
print(f"the cost of the house is: {cost}")
plt.legend()
plt.show()
