import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.linear_model import LinearRegression


# 1. Non-linearity of the X-Y relationships

def lin_reg(df):
    X = df["response_time_min"]
    y = df["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)

    # residuals = model.resid
    # print(residuals)

    # when the response time minutes increases, the amount of data compromised decreases
    # double check this regression

    fig, ax = plt.subplots()

    ax.scatter(df["response_time_min"], df["data_compromised"], color="darkorange", alpha=0.5)

    ax.plot(df["response_time_min"], y_pred)

    ax.set_xlabel("Response Time (min)", fontsize=15)
    ax.set_ylabel("Data Compromised", fontsize=15)
    ax.set_title("Response Time and Amount of Data Compromised", fontsize=20)

    # print(model.summary())


# intercept: 257.8809 <-- expected amount of data compromised
# slope: -0.0117 <--

# 257.8809 + -0.0117*(mins)


def lin_reg2(df):
    df_dumb = pd.get_dummies(df, columns=["attack_success"], drop_first=True, dtype=int)

    # print(df_dumb.columns)

    X = df_dumb["attack_success_Yes"]
    y = df_dumb["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    # y_pred = model.predict(X)
    # print(y_pred)

    print(model.summary())


# 2. Correlation of error terms


def error_terms(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df_sorted = df.sort_values(by="timestamp")

    cat_vals = ["attack_type", "severity_level"]
    num_vals = ["response_time_min", "flow_bytes_per_s", "flow_packets_per_s"]

    df_dumb = pd.get_dummies(df, columns=cat_vals, drop_first=True)


# Create plot with time data and residuals




# 3. Non-constant variance of error terms


# 4. Outliers


# 5. High-leverage points


# 6. Collinearity


def main():
    df = pd.read_csv("cybersecurity_incidents.csv")
    # lin_reg(df)
    # lin_reg2(df)
    error_terms(df)
    plt.show()


if __name__ == '__main__':
    main()
