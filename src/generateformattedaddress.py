import json
from faker import Faker
import glob
import os

# Initialize Faker
# generated for en_IN
# en_AU
# en_CA 
# en_GB
# en_NZ
# en_US
# es_ES
# es_MX
# de_DE
# dk_DK
# el_GR
# List of country codes
country_codes = [
    "en_IN", "en_AU", "en_CA", "en_GB", "en_NZ",
    "en_US", "es_ES", "es_MX", "dk_DK"
]



# Define labels for named entities
labels = ["PERSON", "ADDRESS", "PHONE_NUMBER", "EMAIL_ADDRESS", "IN_AADHAAR"]

def generate_fake_data(passeddata, fake):
    # Generate fake data
    name = fake.name()
    phone_number_gen = fake.phone_number() 
    phone_number = str(phone_number_gen)
    email_gen = fake.email()
    email = str(email_gen)
    aadhar_gen = fake.random_number(digits=12)
    # Decode the bytes back to a string using UTF-8 decoding
    aadhar = str(aadhar_gen)


    address = str(fake.address().replace("\n", ", "))


    gentext = passeddata.format(name=name, phone_number=phone_number, address=address, email=email, aadhar=aadhar)
    text = str(gentext)
    # Create entities with spans
    entities = []
    
    for label in labels:
        if label == "PERSON" and name in text:
            start_idx = 0
            start_idx = text.find(name)
            #print(start_idx , label, type(name), text)
            entities.append([start_idx, start_idx + len(name), label])
        elif label == "ADDRESS" and address in text:
            start_idx = 0
            start_idx = text.find(address)
            #print(start_idx , label,type(address),text)
            entities.append([start_idx, start_idx + len(address), label])

    record = [text, {"entities": entities}]

    return record

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    for country_code in country_codes:

        fake = Faker(country_code)
        data = {"annotations": []}
        file_path = f"address_{country_code}_validator.json"  # Specify the file path

        template_dir = 'addresstemplate'

        # Get a list of template files matching the pattern 'template*.txt'
        template_files = glob.glob(os.path.join(template_dir, 'template3.txt'))

        # Iterate over each template file
        for template_file in template_files:
            # Read template lines from file
            with open(template_file, 'r', encoding='utf-8') as file:
                for template in file:
            # Generate Aadhar template
                  json_data = generate_fake_data(template.strip(), fake)
                  data["annotations"].append(json_data)


        # Write JSON data to file
        write_json_to_file(data, file_path)
        print(f"{file_path}")

if __name__ == "__main__":
    main()
