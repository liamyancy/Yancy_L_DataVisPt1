import csv
import matplotlib.pyplot as plt

canadian =[]
american = []
russian = []

catagories = [] #first row not data

with open('data/silverolympicdata.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			catagories.append(row)
			line_count += 1

		else:
			if row[4] == "CAN":
				print("Canadian medal win")
				canadian.append(row[4])
			elif row[4] == "USA":
				print("American medal win")
				american.append(row[4])
			elif row[4] == "RUS":
				print("Russian medal win")
				russian.append(row[4])

			print(line_count)
			line_count += 1

print(len(canadian))
print(len(american))
print(len(russian))

labels = ["Canadian", "American", "Russian"]
sizes = [len(canadian), len(american), len(russian)]
colors = ['red', 'blue', 'gold']

plt.pie(sizes, colors=colors, shadow=True, startangle=190)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Canada, USA and Russia - Medal Wins")
plt.xlabel("Silver Medal Counts Since 1924")
plt.show()