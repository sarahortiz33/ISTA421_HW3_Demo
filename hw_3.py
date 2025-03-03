import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.outliers_influence import OLSInfluence
import statsmodels.stats.api as sms


# Equations for linear model
# - Qualitative
# - Quantitative

def quant_lin_reg(df):
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


def qual_lin_reg(df):
    pred = ["attack_success", "attack_type"]

    df_dumb = pd.get_dummies(df[pred], drop_first=True)
    print(df_dumb.columns)

    y = df_dumb["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    y_pred = model.predict(X)

    plt.figure()
    plt.scatter(df["response_time_min"], df["data_compromised"], color="darkorange", alpha=0.5)
    plt.plot(df["response_time_min"], y_pred)
    plt.xlabel("Response Time (min)", fontsize=15)
    plt.ylabel("Data Compromised", fontsize=15)
    plt.title("Response Time and Amount of Data Compromised", fontsize=20)

    print(model.summary())


def main():
    df = pd.read_csv("cybersecurity_incidents.csv")
    qual_lin_reg(df)
    plt.show()


if __name__ == '__main__':
    main()



# How to extend your linear model







# - Apply a similar marketing plan (or
# research plan) as described in section
# 3.4. Be sure to formulate your
# questions, not just your answers!





# - Concept, coding, question sections