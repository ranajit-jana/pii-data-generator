import json
from faker import Faker
import glob
import os

# Initialize Faker
fake = Faker()

# Define labels for named entities
labels = ["PERSON", "ADDRESS", "PHONE", "EMAIL", "UID"]

def generate_fake_data(passeddata):
    # Generate fake data
    name = fake.name()
    address = str(fake.address())
    phone_number_gen = fake.phone_number()
    phone_number = str(phone_number_gen)
    email_gen = fake.email()
    email = str(email_gen)
    aadhar_gen = fake.random_number(digits=12)
    # Decode the bytes back to a string using UTF-8 decoding
    aadhar = str(aadhar_gen)

    gentext = passeddata.format(name=name, phone_number=phone_number, address=address, email=email, aadhar=aadhar)
    text = str(gentext)
    # Create entities with spans
    entities = []
    start_idx = 0
    for label in labels:
        if label == "PERSON" and name in text:
            start_idx = text.find(name, start_idx)
            print(start_idx , label, name, type(name), text)
            if start_idx != -1:
                entities.append([start_idx, start_idx + len(name), label])
        elif label == "ADDRESS" and address in text:
            start_idx = text.find(address, start_idx)
            print(start_idx , label, address , type(address),text)
            if start_idx != -1:
                entities.append([start_idx, start_idx + len(address), label])
        elif label == "PHONE" and phone_number in text:
            start_idx = text.find(phone_number, start_idx)
            print(start_idx  , label, phone_number, type(phone_number), text)
            if start_idx != -1:
                entities.append([start_idx, start_idx + len(str(phone_number)), label])
        elif label == "EMAIL" and email in text:
            start_idx = text.find(email, start_idx)
            print(start_idx  , label, email,  type(email),text)
            if start_idx != -1:
                entities.append([start_idx, start_idx + len(email), label])
        elif label == "UID" and str(aadhar) in text:
            start_idx = text.find(str(aadhar).strip(), start_idx)
            print(start_idx , label , aadhar, type(aadhar), text)
            if start_idx != -1:
                entities.append([start_idx, start_idx + len(str(aadhar)), label])

    record = [text, {"entities": entities}]

    return record

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    num_records = 10  # Specify the number of records to generate
    data = {"annotations": []}
    file_path = "output.json"  # Specify the file path

    template_dir = 'templates'

    # Get a list of template files matching the pattern 'template*.txt'
    template_files = glob.glob(os.path.join(template_dir, 'template*.txt'))

    # Iterate over each template file
    for template_file in template_files:
        # Read template lines from file
        with open(template_file, 'r', encoding='utf-8') as file:
            for template in file:
        # Generate Aadhar template
               json_data = generate_fake_data(str(template).strip())
               data["annotations"].append(json_data)





    # text = "Name: {name}. Address: {address}. Phone: {phone_number}. Email: {email}. UID: {aadhar}"
    # for _ in range(num_records):
    #     # Generate JSON data
    #     json_data = generate_fake_data(text)
            
    # Write JSON data to file
    write_json_to_file(data, file_path)
    print(f"JSON data with entity spans written to file: {file_path}")

if __name__ == "__main__":
    main()
