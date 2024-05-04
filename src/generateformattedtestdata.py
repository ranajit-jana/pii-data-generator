import json
from faker import Faker

# Initialize Faker
fake = Faker()

# Define labels for named entities
labels = ["PERSON", "ADDRESS", "PHONE", "EMAIL", "UID"]

def generate_fake_data(num_records):
    data = {"annotations": []}
    for _ in range(num_records):
        # Generate fake data
        name = fake.name()
        address = fake.address()
        phone_number = fake.phone_number()
        email = fake.email()
        aadhar = fake.random_number(digits=12)

        # Generate fake text
        text = f"Name: {name}. Address: {address}. Phone: {phone_number}. Email: {email}. UID: {aadhar}"

        # Create entities with spans
        entities = []
        start_idx = 0
        for label in labels:
            if label == "PERSON" and name in text:
                start_idx = text.find(name, start_idx)
                entities.append([start_idx, start_idx + len(name), label])
            elif label == "ADDRESS" and address in text:
                start_idx = text.find(address, start_idx)
                entities.append([start_idx, start_idx + len(address), label])
            elif label == "PHONE" and phone_number in text:
                start_idx = text.find(phone_number, start_idx)
                entities.append([start_idx, start_idx + len(phone_number), label])
            elif label == "EMAIL" and email in text:
                start_idx = text.find(email, start_idx)
                entities.append([start_idx, start_idx + len(email), label])
            elif label == "UID" and str(aadhar) in text:
                start_idx = text.find(str(aadhar), start_idx)
                entities.append([start_idx, start_idx + len(str(aadhar)), label])

        record = [text, {"entities": entities}]
        data["annotations"].append(record)
    return data

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    num_records = 10  # Specify the number of records to generate
    file_path = "output.json"  # Specify the file path

    # Generate JSON data
    json_data = generate_fake_data(num_records)

    # Write JSON data to file
    write_json_to_file(json_data, file_path)
    print(f"JSON data with entity spans written to file: {file_path}")

if __name__ == "__main__":
    main()
