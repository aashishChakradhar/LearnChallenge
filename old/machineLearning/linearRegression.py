import numpy as np
import matplotlib
import matplotlib.pyplot as plt
print(f"Learning about linear regression")

def model_function(x,w,b):
    # model function
    y_predict = w*x +b
    return(y_predict)

def model_function_array(x_train,w,b):
    # produce prediction for y
    m = len(x_train)
    y_predict = np.zeros(m) # produces array of m numbers with 0 as its elements
    for i in range(m):
        y_predict[i]=model_function(w,x_train[i],b)
    return y_predict #  returns array

def cost_function(x_train,y_train,w,b):
    m = len(x_train)
    y_predict = model_function_array(x_train,w,b)
    error = 0
    for i in range(0,m):
        error += (y_predict[i]-y_train[i])**2
    error = ( 1/(2*m))*error
    return error



# training data set
x_train =  np.array([1,2,3])
y_train = np.array([300,500,700])
m = len(x_train)
print(f"x_train: {x_train}\ny_train: {y_train}\nthe number of training data set(m): {m}")

#labeling of the graph
plt.title("housing price")
plt.ylabel('price in 1000')
plt.xlabel('size in 1000sqft')

# to plot the training data set
w= 200
b = 100
plt.scatter(x_train,y_train,marker = 'x', c='y',label="Actual values")
# scatter gives the points only

#to test model function that we created
y_predict = model_function_array(x_train,w,b)
plt.plot(x_train,y_predict,marker='x', c='b',label = "Predicted values")
#plot gives the solid line joining the points

# to make prediction
x = float(input("Enter square feet: "))
y1 = model_function(x,w,b)
plt.scatter(x,y1,marker='o',c='g',label='Specified Price')
print(f"the cost of the house is: {y1}")
error = cost_function(x_train,y_train,w,b)
print(f"Error is: {error}")
plt.scatter(x,error,marker='o',c='r',label='Error')
plt.legend()
plt.show()
