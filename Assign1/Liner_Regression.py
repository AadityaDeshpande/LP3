from sklearn import linear_model
import matplotlib.pyplot as plt


hrs=[[10],[9],[2],[15],[10],[16],[11],[16]]

score=[95,80,10,50,45,98,38,93]


print("hours score")

for row in zip(hrs, score):
    print(row[0][0],"->",row[1])



plt.scatter(hrs,score,color='black')
plt.xlabel('hrs')
plt.ylabel('score')
#plt.show();


reg=linear_model.LinearRegression()
reg.fit(hrs,score)


m=reg.coef_[0]
b=reg.intercept_
print("slope=",m, "intercept=",b)

print("Required Equation of line is: y=",m,"X +",b);

#plt.plot(height, predicted_values, 'b')
plt.scatter(hrs,score,color='black')

predicted_values = [reg.coef_ * i + reg.intercept_ for i in hrs]

plt.plot(hrs, predicted_values, 'b')
plt.xlabel("hrs")
plt.ylabel("score")
plt.show()
#print("run till here")


'''
(base) ubuntu@OS-lab:~/Aaditya$ python3 Liner_Regression.py 
hours score
10 -> 95
9 -> 80
2 -> 10
15 -> 50
10 -> 45
16 -> 98
11 -> 38
16 -> 93
slope= 4.587898609975469 intercept= 12.584627964022907
Required Equation of line is: y= 4.587898609975469 X + 12.584627964022907
(base) ubuntu@OS-lab:~/Aaditya$ 

'''
