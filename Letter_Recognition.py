from sklearn import datasets
digits = datasets.load_digits()
digits.target
digits.data.shape
digits.images[0]

import matplotlib.pyplot as plt
plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.title('Visualizing an array')
# save the figure
plt.savefig('plot2.png', dpi=100, bbox_inches='tight')

import numpy as np
plt.figure(figsize=(15,4))
plt.subplots_adjust(hspace=0.8)
for index, (image, label) in enumerate(zip(digits.data[0:10], digits.target[0:10])):
    plt.subplot(2, 5, index + 1)
    plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
    plt.title('Training: %i\n' % label, fontsize =12)

# save the figure
plt.savefig('plot1.png', dpi=300, bbox_inches='tight')

digits.target.size

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.2, random_state=0)

from sklearn import svm
svc = svm.SVC(gamma=0.001, C=100.)
svc.fit(x_train, y_train)

y_pred = svc.predict(x_test)

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, x_test, y_pred):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')

# save the figure
plt.savefig('plot7.png', dpi=300, bbox_inches='tight')

score = svc.score(x_test, y_test)
print('Accuracy Score: {0}'.format(score))

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import seaborn as sns
import pandas as pd
labels=['0','1','2', '3','4','5','6','7','8','9']
f, ax = plt.subplots(figsize=(10,10))
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True,ax=ax,cmap="Dark2_r")
#labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Accuracy Score: {0} \n Confusion Matrix'.format(np.round(score,2)))
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.savefig('plot3.png', dpi=300, bbox_inches='tight')
plt.show()
f, ax = plt.subplots(figsize=(6,6))
class_report=classification_report(y_test,y_pred,target_names=labels, output_dict=True)
sns.heatmap(pd.DataFrame(class_report).iloc[:-1, :].T, annot=True,ax=ax,cmap="Dark2_r")
ax.set_title('Classification Report')
plt.savefig('plot4.png', dpi=300, bbox_inches='tight')
plt.show()

from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()

import warnings
warnings.filterwarnings("ignore")
logisticRegr.fit(x_train, y_train)

y_pred=logisticRegr.predict(x_test)

score = logisticRegr.score(x_test, y_test)
print('Accuracy Score: {0}'.format(score))

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import seaborn as sns
import pandas as pd
labels=['0','1','2', '3','4','5','6','7','8','9']
f, ax = plt.subplots(figsize=(10,10))
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True,ax=ax,cmap="Dark2_r")
#labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Accuracy Score: {0} \n Confusion Matrix'.format(np.round(score,2)))
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.savefig('plot5.png', dpi=300, bbox_inches='tight')
plt.show()
f, ax = plt.subplots(figsize=(6,6))
class_report=classification_report(y_test,y_pred,target_names=labels, output_dict=True)
sns.heatmap(pd.DataFrame(class_report).iloc[:-1, :].T, annot=True,ax=ax,cmap="Dark2_r")
ax.set_title('Classification Report')
plt.savefig('plot6.png', dpi=300, bbox_inches='tight')
plt.show()

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(criterion = 'gini')

dt.fit(x_train, y_train)

y_pred=dt.predict(x_test)

score = dt.score(x_test, y_test)
print('Accuracy Score: {0}'.format(score))

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import seaborn as sns
import pandas as pd
labels=['0','1','2', '3','4','5','6','7','8','9']
f, ax = plt.subplots(figsize=(10,10))
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True,ax=ax,cmap="Dark2_r")
#labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Accuracy Score: {0} \n Confusion Matrix'.format(np.round(score,2)))
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.savefig('plot7.png', dpi=300, bbox_inches='tight')
plt.show()
f, ax = plt.subplots(figsize=(6,6))
class_report=classification_report(y_test,y_pred,target_names=labels, output_dict=True)
sns.heatmap(pd.DataFrame(class_report).iloc[:-1, :].T, annot=True,ax=ax,cmap="Dark2_r")
ax.set_title('Classification Report')
plt.savefig('plot8.png', dpi=300, bbox_inches='tight')
plt.show()

from sklearn.ensemble import RandomForestClassifier
rc = RandomForestClassifier(n_estimators = 150)

rc.fit(x_train, y_train)

y_pred=rc.predict(x_test)

score = rc.score(x_test, y_test)
print('Accuracy Score: {0}'.format(score))

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import seaborn as sns
import pandas as pd
labels=['0','1','2', '3','4','5','6','7','8','9']
f, ax = plt.subplots(figsize=(10,10))
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm, annot=True,ax=ax,cmap="Dark2_r")
#labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Accuracy Score: {0} \n Confusion Matrix'.format(np.round(score,2)))
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.savefig('plot9.png', dpi=300, bbox_inches='tight')
plt.show()
f, ax = plt.subplots(figsize=(6,6))
class_report=classification_report(y_test,y_pred,target_names=labels, output_dict=True)
sns.heatmap(pd.DataFrame(class_report).iloc[:-1, :].T, annot=True,ax=ax,cmap="Dark2_r")
ax.set_title('Classification Report')
plt.savefig('plot10.png', dpi=300, bbox_inches='tight')
plt.show()

"""This dataset predicts the digit accurately 95% of the times."""

