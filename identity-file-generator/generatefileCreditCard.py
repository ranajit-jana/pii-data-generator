import os
from faker import Faker
import random
import hashlib
import uuid


country_codes = [
    "en_IN",
    "en_AU",
    "en_CA",
    "en_GB",
    "en_NZ",
    "en_US",
    "es_ES",
    "es_MX",
    "dk_DK",
]
fake = Faker()


def luhn_algorithm(card_number):
    digits = [int(d) for d in str(card_number)]
    checksum = 0

    # Reverse the card number and process every second digit
    digits.reverse()
    for i in range(len(digits)):
        if i % 2 == 1:
            digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
        checksum += digits[i]

    # The card number is valid if the checksum is a multiple of 10
    return checksum % 10 == 0


def generate_credit_card():
    while True:
        credit_card_number = fake.credit_card_number(card_type=None)
        if luhn_algorithm(credit_card_number):
            return credit_card_number
        else:
            print(
                f" Did not receive correct credit card number {credit_card_number} - Thus retrying"
            )


def generate_personal_info(country_codes):

    person = fake.name()
    phone_number = fake.phone_number()
    email = fake.email()
    address = fake.address().replace("\n", ", ")
    credit_card_number = fake.credit_card_number()
    credit_card_cvv = fake.credit_card_security_code()
    credit_card_expiry = fake.credit_card_expire()
    dob = fake.date_of_birth().strftime("%d/%m/%Y")
    mothers_maiden_name = fake.last_name()

    return (
        person,
        phone_number,
        email,
        address,
        credit_card_number,
        credit_card_cvv,
        credit_card_expiry,
        dob,
        mothers_maiden_name,
    )


def generate_unique_filename(folder):
    unique_id = uuid.uuid4().hex
    filename = hashlib.md5(unique_id.encode()).hexdigest()
    return os.path.join(folder, f"{filename}.txt")


def generate_text_files(folder, num_files, country_codes):
    os.makedirs(folder, exist_ok=True)
    for i in range(1, num_files + 1):
        filename = generate_unique_filename(folder)
        with open(filename, "w") as file:
            (
                person,
                phone_number,
                email,
                address,
                credit_card_number,
                credit_card_cvv,
                credit_card_expiry,
                dob,
                mothers_maiden_name,
            ) = generate_personal_info(country_codes)

            # Write each piece of information to the file
            file.write(f"Name: {person}\n")
            file.write(f"Phone/Mobile: {phone_number}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Residential Address: {address}\n")
            file.write(f"Credit Card Issued: {credit_card_number}\n")
            file.write(f"Generated CVV: {credit_card_cvv}\n")
            file.write(f"Expiry date as on Credit Card: {credit_card_expiry}\n")
            file.write(f"Date Of Birth: {dob}\n")
            file.write(f"MOTHERS_MAIDEN_NAME: {mothers_maiden_name}\n\n\n")
            file.write(
                "I have received the Credit Card as per the above information. \n\n"
            )
            file.write("Data Entered in the system is true as per my knowledge. \n\n")
            file.write("\nSignature of Applicant\n")
            file.write("Date\n")
            file.write("Place\n")

        print(f"Generated {filename}")


# Main entry point
if __name__ == "__main__":
    # Specify the folder where files will be saved
    output_folder = "credit_card_processing"
    for country_code in country_codes:
        # Generate 5 text files in the specified folder
        num_files = 5
        generate_text_files(output_folder, num_files, country_codes)
        print(f"Generated {num_files} files in '{output_folder}'.")
