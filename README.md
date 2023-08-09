# SMS

Send SMS from the command line using the Africa's Talking API. The motivation is not to store phone numbers in more databases.

## Usage
You need to have the following:
- Clone the repo
  ```
  git clone https://github.com/bmwasaru/sms.git
  ```
- Create virtual environment in the folder
  ```
  cd sms
  virtualenv venv
  pip install -r requirements.txt
  ```
- Add the env variables in the `venv/bin/activate` file
  ```
  export at_username="africas_talking_username"
  export at_sender_id="africas_talking_sender_id"
  export at_api_key="africas_talking_api_key"
  ```
- Activate the virtualenv with the new variables based on your O.S version
  ```
  . venv/bin/activate
  ```
- Africa's Talking API Key, username, sender ID
- A csv file with `phone_number` that has the phone number in the right format `+254XXXXXXXXX`
- Run the command script pass the parameters are shown below
  ```
  python send_sms.py phone_numbers.csv "Your message goes here"
  ```
