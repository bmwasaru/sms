import os
import csv
import click
import africastalking
import phonenumbers

# Set your API credentials from Africa's Talking
username = os.environ.get('at_username')
api_key = os.environ.get("at_api_key")
sender_id = os.environ.get("at_sender_id")

# Initialize the Africa's Talking API
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Validate a phone number using phonenumbers
def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "KE")  # Assuming Kenyan numbers
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

# Send SMS to the specified phone numbers
def send_sms(phone_numbers, message):
    status_summary = {}
    for phone_number in phone_numbers:
        response = sms.send(message, [phone_number], sender_id)
        status = response['SMSMessageData']['Recipients'][0]['status']
        status_summary[phone_number] = status
        click.echo(f"SMS sent to {phone_number}: {status}")
    return status_summary

@click.command()
@click.argument('csv_file', type=click.Path(exists=True))
@click.argument('message')
def main(csv_file, message):
    """Send SMS to phone numbers from a CSV file."""
    phone_numbers = []
    with open(csv_file, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            phone_number = row.get("phone_numbers")
            if validate_phone_number(phone_number):
                phone_numbers.append(phone_number)
    
    if not phone_numbers:
        click.echo("No valid phone numbers found in the CSV file.")
        return

    summary = send_sms(phone_numbers, message)

    click.echo("\nSummary of SMS statuses:")
    for phone_number, status in summary.items():
        click.echo(f"{phone_number}: {status}")

if __name__ == "__main__":
    main()
