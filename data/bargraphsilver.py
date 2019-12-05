import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Countries = ('Canada', 'USA', 'Russia')
y_pos = np.arange(len(Countries))
Number_Of_Silver = [203, 319, 90]

plt.bar(y_pos, Number_Of_Silver, align='center', alpha=0.5)
plt.xticks(y_pos, Countries)
plt.xlabel('Countries')
plt.ylabel('Silver Medals')
plt.title('Silver Medals Won By Canada, USA and Russia')

plt.legend(
			title="Countries",
			loc="upper right",
			bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()