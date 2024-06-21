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


def generate_personal_info(country_code):
    fake = Faker(country_code)
    name = fake.name()
    phone_number = fake.phone_number()
    email = fake.email()
    address = fake.address().replace("\n", ", ")
    dob = fake.date_of_birth().strftime("%d/%m/%Y")
    aadhar_number = fake.numerify(text="#### #### ####")
    pan_number = fake.random_int(min=1000000000, max=9999999999)
    mothers_maiden_name = fake.last_name()

    return (
        name,
        phone_number,
        email,
        address,
        dob,
        aadhar_number,
        pan_number,
        mothers_maiden_name,
    )


def generate_unique_filename(folder):
    unique_id = uuid.uuid4().hex
    filename = hashlib.md5(unique_id.encode()).hexdigest()
    return os.path.join(folder, f"{filename}.txt")


def generate_text_files(folder, num_files, country_code):
    os.makedirs(folder, exist_ok=True)
    for i in range(1, num_files + 1):
        filename = generate_unique_filename(folder)
        with open(filename, "w") as file:
            (
                name,
                phone_number,
                email,
                address,
                dob,
                aadhar_number,
                pan_number,
                mothers_maiden_name,
            ) = generate_personal_info(country_code)

            # Write each piece of information to the file
            file.write(f"Name: {name} \t\t\t Phone Number: {phone_number}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Date of Birth: {dob}\n")
            file.write(f"Aadhar Number: {aadhar_number} \t PAN Number: {pan_number}\n")
            file.write(f"Mother's Maiden Name: {mothers_maiden_name}\n\n\n")
            file.write(
                "I have checked all the above information and they are correct to my knowledge.\n\n"
            )
            file.write("\nSignature of Applicant\n")
            file.write("Date\n")
            file.write("Place\n")

        print(f"Generated {filename}")


# Main entry point
if __name__ == "__main__":
    # Specify the folder where files will be saved
    output_folder = "generated_files"
    for country_code in country_codes:
        # Generate 5 text files in the specified folder
        num_files = 1
        generate_text_files(output_folder, num_files, country_code)
        print(f"Generated {num_files} files in '{output_folder}'.")
