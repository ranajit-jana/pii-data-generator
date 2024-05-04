import random
from faker import Faker
import glob
import os

def generate_aadhar_number():
    # Generate a random 12-digit Aadhar number
    aadhar_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    return aadhar_number

def generate_aadhar_template(template):
    # Create a Faker instance
    fake = Faker()

    # Generate random values for name, phone_number, address, and email
    name = fake.name()
    phone_number = fake.phone_number()
    address = fake.address()
    email = fake.email()

    # Generate Aadhar number
    aadhar = generate_aadhar_number()

    # Fill in the template with generated values
    filled_template = template.format(name=name, phone_number=phone_number, address=address, email=email, aadhar=aadhar)
    return filled_template

def main():
    # Get the directory path containing the template files
    template_dir = 'templates'

    # Get a list of template files matching the pattern 'template*.txt'
    template_files = glob.glob(os.path.join(template_dir, 'template*.txt'))

    # Create the 'testdata' directory if it doesn't exist
    output_dir = 'testdata'
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each template file
    for template_file in template_files:
        # Read template lines from file
        with open(template_file, 'r') as file:
            template = file.read()

        # Generate Aadhar template
        aadhar_template = generate_aadhar_template(template)

        # Write the generated template to a file in the 'testdata' directory
        output_file = os.path.join(output_dir, os.path.basename(template_file))
        with open(output_file, 'w') as outfile:
            outfile.write(aadhar_template)
            print("Generated Aadhar Template written to:", output_file)

if __name__ == "__main__":
    main()
