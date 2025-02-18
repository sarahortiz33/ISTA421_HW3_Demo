import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np


# 1. Non-linearity of the X-Y relationships

def lin_reg(df):
    X = df["response_time_min"]
    y = df["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)

    fig, ax = plt.subplots()

    ax.scatter(df["response_time_min"], df["data_compromised"], color="darkorange", alpha=0.5)

    ax.plot(df["response_time_min"], y_pred)

    ax.set_xlabel("Response Time (min)", fontsize=15)
    ax.set_ylabel("Data Compromised", fontsize=15)
    ax.set_title("Response Time and Amount of Data Compromised", fontsize=20)

    print(model.summary())




# 2. Correlation of error terms


# 3. Non-constant variance of error terms


# 4. Outliers


# 5. High-leverage points


# 6. Collinearity


def main():
    df = pd.read_csv("cybersecurity_incidents.csv")
    lin_reg(df)

    plt.show()


if __name__ == '__main__':
    main()

