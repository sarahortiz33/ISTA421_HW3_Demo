import pandas as pd
import statsmodels.api as sm


# Equations for linear models


def response_dcomp(df):
    X = df["response_time_min"]
    y = df["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())


def byte_packet_response(df):
    X = df[["flow_bytes_per_s", "flow_packets_per_s"]]
    y = df["response_time_min"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())


def attacks_dcomp(df):
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


def packets_level(df):
    pred = ["severity_level"]
    df_dumb = pd.get_dummies(df, columns=pred, drop_first=True, dtype=int)

    new_cat = ["severity_level_Low", "severity_level_Medium",
               "severity_level_High"]

    X = df_dumb[new_cat]
    y = df["flow_packets_per_s"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    print(model.summary())


# Extending the linear models


def byte_packet_ext(df):
    y = df["data_compromised"]
    df["response_time_min_squared"] = df["response_time_min"] ** 2
    X = df[["response_time_min", "response_time_min_squared"]]

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())


def attack_dcomp_ext(df):
    pred = ["attack_success", "attack_type"]
    df_dumb = pd.get_dummies(df, columns=pred, drop_first=True, dtype=int)
    df_dumb.rename(columns={
        "attack_type_SQL Injection": "attack_type_SQL_Injection",
        "attack_type_Man-in-the-Middle": "attack_type_Man_in_the_Middle"
    }, inplace=True)

    df_dumb["s_malware"] = df_dumb["attack_success_Yes"] * df_dumb["attack_type_Malware"]
    df_dumb["s_ransom"] = df_dumb["attack_success_Yes"] * df_dumb["attack_type_Ransomware"]
    df_dumb["s_phish"] = df_dumb["attack_success_Yes"] * df_dumb["attack_type_Phishing"]
    df_dumb["s_sql"] = df_dumb["attack_success_Yes"] * df_dumb["attack_type_SQL_Injection"]
    df_dumb["s_middle"] = df_dumb["attack_success_Yes"] * df_dumb["attack_type_Man_in_the_Middle"]

    new_cat = ["attack_success_Yes", "attack_type_Malware", "attack_type_Man_in_the_Middle",
               "attack_type_Phishing", "attack_type_Ransomware",
               "attack_type_SQL_Injection", "s_malware", "s_ransom", "s_phish",
               "s_sql", "s_middle"]

    X = df_dumb[new_cat]
    y = df["data_compromised"]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())



def main():
    df = pd.read_csv("cybersecurity_incidents.csv")
    response_dcomp(df)
    byte_packet_response(df)
    attacks_dcomp(df)
    packets_level(df)
    byte_packet_ext(df)
    attack_dcomp_ext(df)


if __name__ == '__main__':
    main()


# Marketing/Research plan
"""
Q1. Is there a correlation between the amount of data compromised and the amount
of minutes it took for the cyber attack to be responded to?

A1: No, there is not a strong correlation between the amount of data compromised
and the amount of minutes it took for the attack to be responded to. The
response time of an attack is not a good predictor for how much data will be
compromised in an attack, as the R-squared value is 0.001, the F-statistic is
0.2755, and the p-value for the response time is 0.302.


Q2. Does whether or not the attack was successful and the type of attack
significantly affect the amount of data compromised?

A2: No, the attack success was not statistically significant and does not have
a strong correlation with the amount of data compromised. The same is true for
the attack type, as none of the p-values for all the different types of attacks
were less than 0.5. However, malware did have a p-value of 0.061, which was the
lowest of all the others. While not statistically significant, it suggests that
it has the largest effect on data compromised out of all the other attack types.


Q3. Is response time affected by any other numerical variables in the dataset?

A3: When response time was checked alongside the flow bytes per second and flow
packets per second, the model did not indicate that there was a strong
correlation between the two predictors and the response variable. The R-squared
value was low, at 0.001, and both the F-statistics and p-values were high, and
not indicate any statistical significance. 


Q4. Does the extension of the linear models reveal any key insights?

A4: The extension of the flow bytes and packets per second slightly fits the
data better than the linear regression model. Instead of the R-squared value
being 0.001, it increases to 0.002. While not a large improvement, it could
suggest that a more flexible model may be more useful. In the extension with
the qualitative model with attack success and type as the predictors and data
compromised as the response, the R-squared is also low, at 0.011, and is only
a slight improvement from the linear model. Because of this, it does not seem
to reveal anything new about the data.


Q5: How accurately can the amount of compromised data be predicted?

A5: Based on the linear models, none of the variables had significantly strong
relationships that would have been able to accurately predict the amount of
compromised data. Using another type of model might be beneficial since this
was the case.


Q6: Is there a relationship between high severity levels and amount of flow
packets per second?

A6: There seems to be an association with low severity levels and the number of
flow packets per second as its p-value is 0.050. When the severity level is low,
the predicted value of flow packets decreases by about 519 packets per second.
Because the rest of results from the model is not statistically significant, it
is not the strongest relationship, but it is important to note this association.


"""

