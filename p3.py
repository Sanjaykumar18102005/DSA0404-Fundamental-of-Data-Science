import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(r"C:\python\FDS\email_spam.csv")

print("Dataset:")
print(df)

X = df[['Num_Links', 'Num_Caps_Words', 'Email_Length']]
y = df['Spam']

model = LogisticRegression()
model.fit(X, y)

links = int(input("Enter Number of Links: "))
caps = int(input("Enter Number of Capitalized Words: "))
length = int(input("Enter Email Length: "))

prediction = model.predict([[links, caps, length]])

if prediction[0] == 1:
    print("Prediction: Spam Email")
else:
    print("Prediction: Not Spam")