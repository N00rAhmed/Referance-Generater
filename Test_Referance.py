import unittest
from unittest.mock import patch
from Referance import main
from datetime import date

class TestReferenceProgram(unittest.TestCase):

    @patch('builtins.input', side_effect=['Sample Header', '2022', 'https://www.forbes.com/sites/christinemoorman/2018/01/12/why-apple-is-still-a-great-marketer-and-what-you-can-learn/?sh=3f9c8c8315bd', 'pull'])
    @patch('builtins.print')
    def test_main_function(self, mock_print, mock_input):
        main()
        # Gets current date
        today = date.today()

        # Formats current date as a string in the "day/month/year" format
        access_date = today.strftime("%d/%m/%Y")

        expected_reference = 'Sample Header (2022) Why Apple Is Still A Great Marketer And What You Can Learn [online] Address: https://www.forbes.com/sites/christinemoorman/2018/01/12/why-apple-is-still-a-great-marketer-and-what-you-can-learn/?sh=3f9c8c8315bd' + f' [accessed: {access_date}] '

        # Collect the printed content by joining the first arguments of all calls made to the mock_print object
        # Each call represents a print statement, and call[0][0] corresponds to the printed content
        printed_content = ''.join([call[0][0] for call in mock_print.call_args_list])
        self.assertIn(expected_reference, printed_content)

if __name__ == '__main__':
    unittest.main()
