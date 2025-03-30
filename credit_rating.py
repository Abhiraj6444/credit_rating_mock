import json
import pprint


class CreditRating:

    def __init__(self):
        self.risk_score = 0
        self.result = {}

    def get_data(self):
        '''Fetch the mortgages data from the below json file'''
        with open("payload.json", "r") as file:
            data = json.load(file)
        return data

    def loan_to_value_ratio(self, data):
        '''Calculate Loan-to-Value (LTV) Ratio and risk score accordingly.'''
        ltv = int(
            round((data["loan_amount"] / data["property_value"]) * 100, 0))
        if ltv > 90:
            self.risk_score += 2
            return self.risk_score
        elif 80 < ltv <= 90:
            self.risk_score += 1
            return self.risk_score
        else:
            return self.risk_score

    def debt_to_income_ratio(self, data):
        '''Calculate Debt-to-Income (DTI) Ratio and risk score accordingly.'''
        dit = int(
            round((data["debt_amount"] / data["annual_income"]) * 100, 0))
        if dit > 50:
            self.risk_score += 2
            return self.risk_score
        elif 40 < dit <= 50:
            self.risk_score += 1
            return self.risk_score
        else:
            return self.risk_score

    def credit_score(self, data):
        '''Evaluates the credit score and calculated risk score accordingly.'''
        credit_score = data.get("credit_score")

        if credit_score is None:
            raise ValueError("Credit Score is missing")

        if not isinstance(credit_score, int):
            raise ValueError("Credit score must be a whole number")

        if not (350 <= credit_score <= 850):
            raise ValueError("Credit score is out of valid range (350-850)")

        if 700 <= credit_score <= 850:
            self.risk_score -= 1
        elif 650 <= credit_score < 700:
            pass
        elif 350 >= credit_score < 650:
            self.risk_score += 1

        return self.risk_score

    def mortgage_loan_type(self, data):
        '''Checks the type of mortgage loan and calculated risk score accordingly.'''
        loan_type = data.get('loan_type')

        if loan_type is None:
            raise ValueError("mortgage Loan Type is missing")

        if loan_type == 'fixed':
            self.risk_score -= 1
            return self.risk_score
        elif loan_type == 'adjustable':
            self.risk_score += 1
            return self.risk_score
        else:
            raise ValueError('mortgage Loan Type is Invalid')

    def property_type(self, data):
        '''Checks the type of property loan and calculated risk score accordingly.'''
        loan_type = data.get('property_type')

        if loan_type is None:
            raise ValueError("Property Type is missing")

        if loan_type == 'single_family':
            return self.risk_score
        elif loan_type == 'condo':
            self.risk_score += 1
            return self.risk_score
        else:
            raise ValueError('Property Type is Invalid')

    def average_credit_score(self, avg_credit_score):
        '''Adjusted final score based on the average credit score:.'''
        if avg_credit_score >= 700:
            return -1
        elif avg_credit_score < 650:
            return
        else:
            return 0

    def get_credit_rating(self, final_risk_score):
        '''Assigns a credit rating based on the final risk score.'''
        if final_risk_score <= 2:
            return 'AAA'
        elif 3 <= final_risk_score <= 5:
            return 'BBB'
        else:
            return 'C'

    def calculate_credit_rating(self):
        '''Processing mortgage data and calculates credit ratings.'''
        json_data = self.get_data()
        TOTAL_Credit_Score = 0
        for index, item in enumerate(json_data["mortgages"], start=1):
            try:
                self.risk_score = 0
                LTV_Ratio = self.loan_to_value_ratio(item)
                DIT_Ratio = self.debt_to_income_ratio(item)
                CREDIT_Score = self.credit_score(item)
                LOAN_Type = self.mortgage_loan_type(item)
                PROPERTY_Loan = self.property_type(item)
                TOTAL_Credit_Score += item["credit_score"]
                self.result[f"Borrower {index}"] = {
                    # "LTV": LTV_Ratio,
                    # "DIT": DIT_Ratio,
                    # "CREDIT_SCORE": CREDIT_Score,
                    # "LOAN_TYPE": LOAN_Type,
                    # "PROPERTY_LOAN": PROPERTY_Loan,
                    # "TOTAL_CREDIT_SCORE" : TOTAL_Credit_Score,
                    "RISK_SCORE": self.risk_score,
                }

            except ValueError as e:
                self.result[f"Borrower {index}"] = {"ERROR": str(e)}

        avg_credit_score = TOTAL_Credit_Score / len(json_data["mortgages"])
        adjust_final_score = self.average_credit_score(avg_credit_score)

        for borrower, data in self.result.items():
            final_risk_score = data["RISK_SCORE"] + adjust_final_score
            self.result[borrower]["FINAL_RISK_SCORE"] = final_risk_score
            self.result[borrower]["RATING"] = self.get_credit_rating(
                final_risk_score)

        pprint.pprint(self.result)
        return self.result


if __name__ == '__main__':
    CreditRating().calculate_credit_rating()
