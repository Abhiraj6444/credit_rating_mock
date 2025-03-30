import unittest
from credit_rating import CreditRating


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        ''' SetUp class will run at the beginning (i.e. before) of the all test method'''
        self.json = {
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }

    @classmethod
    def tearDownClass(self):
        ''' tearDownClass class will run at the end (i.e. after) of the all test method'''
        pass
        # print('teardownclass')

    def test_ltv_ratio(self):
        result = CreditRating().loan_to_value_ratio(self.json)
        self.assertEqual(result, 0)

    def test_dti_ratio(self):
        result = CreditRating().debt_to_income_ratio(self.json)
        self.assertEqual(result, 0)

    def test_credit_score(self):
        result = CreditRating().credit_score(self.json)
        self.assertEqual(result, -1)

    def test_mortgage_loan(self):
        result = CreditRating().mortgage_loan_type(self.json)
        self.assertEqual(result, -1)

    def test_property_type(self):
        result = CreditRating().property_type(self.json)
        self.assertEqual(result, 0)

    def test_average_credit_score(self):
        result = CreditRating().average_credit_score(750)
        self.assertEqual(result, -1)

    def test_get_credit_rating(self):
        final_risk_score = -3
        result = CreditRating().get_credit_rating(final_risk_score)
        self.assertEqual(result, 'AAA')

    # >>> >>> >>> EDGE CASE TESTS >>> >>> >>> #
    def test_missing_property_type(self):
        test_data = self.json.copy()

        del test_data["property_type"]
        with self.assertRaises(ValueError) as context:
            CreditRating().property_type(test_data)
        self.assertEqual(str(context.exception), "Property Type is missing")

    def test_invalid_property_type(self):
        test_data = self.json.copy()

        test_data["property_type"] = "UNKNOWN"
        with self.assertRaises(ValueError) as context:
            CreditRating().property_type(test_data)
        self.assertEqual(str(context.exception), "Property Type is Invalid")

    def test_missing_credit_score(self):
        test_score = self.json.copy()
        del test_score["credit_score"]
        with self.assertRaises(ValueError) as context:
            CreditRating().credit_score(test_score)
        self.assertEqual(
            str(context.exception),
            "Credit Score is missing"
        )

    def test_invalid_credit_score(self):
        test_data = self.json.copy()

        test_data["credit_score"] = 300
        with self.assertRaises(ValueError) as context:
            CreditRating().credit_score(test_data)
        self.assertEqual(
            str(context.exception),
            "Credit score is out of valid range (350-850)"
        )

    def test_invalid_int_credit_score(self):
        test_data = self.json.copy()

        test_data["credit_score"] = "300"
        with self.assertRaises(ValueError) as context:
            CreditRating().credit_score(test_data)
        self.assertEqual(
            str(context.exception),
            "Credit score must be a whole number"
        )


if __name__ == '__main__':
    unittest.main()
