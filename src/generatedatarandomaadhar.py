import json
from faker import Faker
import glob
import os
import random
import re

# Initialize Faker
fake = Faker()

# Define labels for named entities
labels = ["PERSON", "ADDRESS", "PHONE", "EMAIL", "UID"]

def generate_aadhar_number():
    regex = "^[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}$"
    aadhar_number = ""
    i = 0
    while i < len(regex):
        char = regex[i]
        if char.isdigit():
            aadhar_number += str(random.randint(0, 9))
        elif char == "{":
            start_index = i + 1
            end_index = regex.index("}", start_index)
            range_values = regex[start_index:end_index].split("-")
            if len(range_values) == 2:
                aadhar_number += str(random.randint(int(range_values[0]), int(range_values[1])))
            else:
                aadhar_number += range_values[0]
            i = end_index + 1
            continue
        else:
            aadhar_number += char
        i += 1
    return aadhar_number


def generate_fake_data(passeddata):
    # Generate fake data
    name = fake.name()
    address = str(fake.address())
    phone_number_gen = fake.phone_number()
    phone_number = str(phone_number_gen)
    email_gen = fake.email()
    email = str(email_gen)
    aadhar_gen = generate_aadhar_number()
    # Decode the bytes back to a string using UTF-8 decoding
    aadhar = str(aadhar_gen)

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
        elif label == "PHONE_NUMBER" and phone_number in text:
            start_idx = 0          
            start_idx = text.find(str(phone_number).strip(), start_idx)
            #print(start_idx  , label, type(phone_number), text)
            entities.append([start_idx, start_idx + len(str(phone_number)), label])
        elif label == "EMAIL_ADDRESS" and email in text:
            start_idx = 0
            start_idx = text.find(email, start_idx)
            #print(start_idx  , label, type(email),text)
            entities.append([start_idx, start_idx + len(email), label])
        elif label == "IN_AADHAAR" and str(aadhar) in text:
            start_idx = 0
            start_idx = text.find(str(aadhar).strip(), start_idx)
            #print(start_idx , label , type(aadhar), text)
            entities.append([start_idx, start_idx + len(str(aadhar)), label])

    record = [text, {"entities": entities}]

    return record

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    num_records = 10  # Specify the number of records to generate
    data = {"annotations": []}
    file_path = "testoutput.json"  # Specify the file path

    template_dir = 'templates'

    # Get a list of template files matching the pattern 'template*.txt'
    template_files = glob.glob(os.path.join(template_dir, 'template*.txt'))

    # Iterate over each template file
    for template_file in template_files:
        # Read template lines from file
        with open(template_file, 'r', encoding='utf-8') as file:
            for template in file:
        # Generate Aadhar template
               json_data = generate_fake_data(template.strip())
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
