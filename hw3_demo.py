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

    df_dumb = pd.get_dummies(df_sorted, columns=cat_vals, drop_first=True, dtype=int)
    df_dumb.rename(columns={
        "attack_type_SQL Injection": "attack_type_SQL_Injection",
        "attack_type_Man-in-the-Middle": "attack_type_Man_in_the_Middle"
    }, inplace=True)

    new_cat = ["attack_type_Malware", "attack_type_Man_in_the_Middle",
               "attack_type_Phishing", "attack_type_Ransomware",
               "attack_type_SQL_Injection", "severity_level_High",
               "severity_level_Low", "severity_level_Medium"]

    X_num = df_dumb[num_vals]
    X_cat = df_dumb[new_cat]
    X = pd.concat([X_num, X_cat], axis=1)
    X = sm.add_constant(X)
    y = df_dumb["data_compromised"]
    model = sm.OLS(y, X).fit()

    residuals = model.resid
    plt.plot(df_dumb["timestamp"], residuals, marker='o', alpha=0.5, color='blue')
    plt.axhline(y=0, color='red', linestyle='--')
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Residuals", fontsize=15)
    plt.title("Residuals Against Time", fontsize=20)


# 3. Non-constant variance of error terms


def var_error_terms(df):
    cat_vals = ["attack_type", "severity_level"]
    num_vals = ["response_time_min", "flow_bytes_per_s", "flow_packets_per_s"]

    X_num = df_dumb[num_vals]
    X_cat = df_dumb[new_cat]
    X = pd.concat([X_num, X_cat], axis=1)
    X = sm.add_constant(X)
    y = df_dumb["data_compromised"]
    model = sm.OLS(y, X).fit()

    residuals = model.resid
    plt.plot(df_dumb["timestamp"], residuals, marker='o', alpha=0.5, color='blue')
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Residuals", fontsize=15)
    plt.title("Residuals Against Time", fontsize=20)




# 4. Outliers


# 5. High-leverage points


# 6. Collinearity


def main():
    df = pd.read_csv("cybersecurity_incidents.csv")
    # lin_reg(df)
    # lin_reg2(df)
    # error_terms(df)
    var_error_terms(df)
    plt.show()


if __name__ == '__main__':
    main()
