import matplotlib.pyplot as plt
import pandas as pd

x=[1,2,3,4,5]
y = [1,2,9,16,25]

plt.plot(x,y)

# x axis label
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#show method will display the data
plt.show()

#simple data
subjects =["Maths","Science","English","History","Computer"]
marks =[85,78,92,74,88]

#creates the line graph
plt.plot(subjects,marks)
plt.title("Student Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()

#matplotlib with pandas integration
data={
    "Months":["Jan","Feb","Mar","Apr","May"],
    "Sales":[100,150,130,170,160]
}
df =pd.DataFrame(data)
plt.plot(df["Months"],df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()




