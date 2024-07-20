import unittest
from unittest.mock import patch, MagicMock
from mailingmodule import sendMail

class TestSendMail(unittest.TestCase):

	@patch('mailingmodule.Client')
	@patch('mailingmodule.getBase64Content')
	@patch('mailingmodule.configparser.ConfigParser')
	def test_send_mail_success(self, mock_config, mock_get_base64_content, mock_client):
		# Setup mock responses
		mock_get_base64_content.return_value = 'base64pdfcontent'
		mock_config_instance = mock_config.return_value
		mock_config_instance.read.return_value = None
		mock_config_instance.__getitem__.side_effect = lambda x: {
			'mailjet': {'api_key': 'testkey', 'api_secret': 'testsecret'},
			'mail_options': {'sender_email': 'test@example.com', 'sender_name': 'Test Sender', 'subject': 'Test Subject'}
		}[x]
		mock_client_instance = mock_client.return_value
		mock_client_instance.send.create.return_value = MagicMock(status_code=200, json=lambda: {'success': True})

		# Call the function
		sendMail('recipient@example.com', 'Test Recipient', '/path/to/pdf')

		# Assertions
		mock_client.assert_called_once_with(auth=('testkey', 'testsecret'), version='v3.1')
		mock_client_instance.send.create.assert_called()
		# Further assertions can be added to check the structure of the data passed to send.create

	def test_send_mail_E2E(self):
		# This is an end-to-end test that sends an actual email
		# This test will only work if the configuration is set up correctly
		# modify varialbles below to match proper recipient email and name
		recipient_email = 'test@example.com'
		recipient_name = 'Test Sender'
		sendMail(recipient_email,recipient_name,'../Test/content/Test_File.pdf')

if __name__ == '__main__':
	unittest.main()