# You should write unit tests for the five inputs from the stock visualizer challenge that enforce the following constraints.
    # symbol: capitalized, 1-7 alpha characters
    # chart type: 1 numeric character, 1 or 2
    # time series: 1 numeric character, 1 - 4
    # start date: date type YYYY-MM-DD
    # end date: date type YYYY-MM-DD

import unittest
from datetime import datetime

class testVisualizer(unittest.TestCase):
    # symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        symbols = ["Apple", "", "ABCDEFGHIJ", "E!NT*", "IBM"]
        for symbol in symbols:
            with self.subTest(symbol=symbol):
                self.assertTrue(symbol.isupper(), msg="Value is not capitalized.")
                self.assertGreaterEqual(len(symbol), 1, msg="Value does not have ≥ 1 characters.")
                self.assertLessEqual(len(symbol), 7, msg="Value does not have ≤ 7 characters.")
                self.assertTrue(symbol.isalpha(), msg="Value is not alpha characters.")
    
    # chart type: 1 numeric character, 1 or 2
    def test_chartType(self):
        chartTypes = ["one", "30", "7", "2"]
        for chartType in chartTypes:
            with self.subTest(chartType=chartType):
                self.assertTrue(chartType.isdigit(), msg="Value is not a numeric character.")
                self.assertEqual(len(chartType), 1, msg="Value is not 1 character long.")
                self.assertIn(int(chartType), [1, 2], msg="Value is not 1 or 2.")
    
    # time series: 1 numeric character, 1 - 4
    def test_timeSeries(self):
        timeSeries_list = ["one", "30", "7", "4"]
        for timeSeries in timeSeries_list:
            with self.subTest(timeSeries=timeSeries):
                self.assertTrue(timeSeries.isdigit(), msg="Value is not a numeric character.")
                self.assertEqual(len(timeSeries), 1, msg="Value is not 1 character long.")
                self.assertIn(int(timeSeries), [1, 2, 3, 4], msg="Value is not 1, 2, 3, or 4.")
    
    # start date: date type YYYY-MM-DD
    # end date: date type YYYY-MM-DD
    def test_date(self):
        dates = ["23-01-01", "2023/02/28", "2023-13-31", "2023-04-31", "2023-02-29", "2023-01-01"]
        for date in dates:
            with self.subTest(date=date):
                    datetime.strptime(date, "%Y-%m-%d")

if __name__ == "__main__":
    # Create a TestSuite object
    suite = unittest.TestSuite()

    # Add test methods to the suite
    suite.addTest(testVisualizer('test_symbol'))
    suite.addTest(testVisualizer('test_chartType'))
    suite.addTest(testVisualizer('test_timeSeries'))
    suite.addTest(testVisualizer('test_date'))

    # Create a TestRunner object
    runner = unittest.TextTestRunner()

    # Run the tests in the suite
    runner.run(suite)
    
    # unittest.main()