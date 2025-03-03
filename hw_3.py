import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.outliers_influence import OLSInfluence
import statsmodels.stats.api as sms


# Equations for linear model


def quant_lin_reg(df):
    X = df["flow_packets_per_s"]
    y = df["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    y_pred = model.predict(X)

    plt.figure()
    plt.scatter(df["flow_packets_per_s"], df["data_compromised"], color="darkorange", alpha=0.5)
    plt.plot(df["flow_packets_per_s"], y_pred)
    plt.xlabel("Response Time (min)", fontsize=15)
    plt.ylabel("Data Compromised", fontsize=15)
    plt.title("Response Time and Amount of Data Compromised", fontsize=20)

    print(model.summary())


def qual_lin_reg(df):
    pred = ["attack_success", "attack_type"]
    df_dumb = pd.get_dummies(df, columns=pred, drop_first=True, dtype=int)
    df_dumb.rename(columns={
        "attack_type_SQL Injection": "attack_type_SQL_Injection",
        "attack_type_Man-in-the-Middle": "attack_type_Man_in_the_Middle"
    }, inplace=True)

    new_cat = ["attack_success_Yes", "attack_type_Malware", "attack_type_Man_in_the_Middle",
               "attack_type_Phishing", "attack_type_Ransomware",
               "attack_type_SQL_Injection"]

    X = df_dumb[new_cat]
    y = df["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    print(model.summary())


# Extending the linear models


def quant_ext(df):
    y = df["data_compromised"]
    df["response_time_min_squared"] = df["response_time_min"] ** 2
    X = df[["response_time_min", "response_time_min_squared"]]

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())


def qual_ext(df):
    pred = ["attack_success", "attack_type"]
    df_dumb = pd.get_dummies(df, columns=pred, drop_first=True, dtype=int)
    df_dumb.rename(columns={
        "attack_type_SQL Injection": "attack_type_SQL_Injection",
        "attack_type_Man-in-the-Middle": "attack_type_Man_in_the_Middle"
    }, inplace=True)

    new_cat = ["attack_success_Yes", "attack_type_Malware", "attack_type_Man_in_the_Middle",
               "attack_type_Phishing", "attack_type_Ransomware",
               "attack_type_SQL_Injection"]





def main():
    df = pd.read_csv("cybersecurity_incidents.csv")
    quant_lin_reg(df)
    #qual_lin_reg(df)

    #quant_ext(df)
    #qual_ext(df)
    plt.show()


if __name__ == '__main__':
    main()


# - Marketing/Research plan (or
# research plan) as described in section
# 3.4. Be sure to formulate your
# questions, not just your answers!
"""
Q1. Is there a correlation between the amount of data compromised and the amount
of minutes it took for the cyber attack to be responded to?

A1: No, there is not a strong correlation between the amount of data compromised
and the amount of minutes it took for the attack to be responded to. The
response time of an attack is not a good predictor for how much data will be



"""


# - Concept, coding, question sections





