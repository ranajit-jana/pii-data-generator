import csv
import os
from faker import Faker
import hashlib
import random

# Create an instance of the Faker class
faker = Faker()

template_sentences = [
    "Hi, my name is {name}, you can reach me at {phone_number}, and I live at {address}.",
    "I'm {name}, my phone number is {phone_number}, and my address is {address}.",
    "You can contact me at {phone_number}. My name is {name} and I live at {address}.",
    "Give me a call anytime at {phone_number}",
    "Drop me a note at {email}",
    "I will be staying at {address} during vacation"
]

# Function to check if the file is empty
def is_empty_file(file_path):
    return os.stat(file_path).st_size == 0

# Function to get the last used IDs from the existing CSV file
def get_last_ids(csv_file):
    last_comment_id = 0
    last_post_id = 0

    if os.path.exists(csv_file):
        with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            for row in reader:
                comment_id = int(row[0])
                post_id = int(row[2])
                last_comment_id = max(last_comment_id, comment_id)
                last_post_id = max(last_post_id, post_id)

    return last_comment_id, last_post_id

# Function to generate synthetic data for each field
def generate_comment(user_id):
    user_id = random.randint(1, 100)  # Random user_id between 1 and 100
    global comment_id_counter
    global post_id_counter

    comment_id, post_id = get_last_ids(csv_file)
    comment_id += 1
    post_id += 1
    template_sentence = random.choice(template_sentences)
    name = faker.name()
    phone_number = faker.phone_number()
    email = faker.email()
    address = faker.address()
    comment_content = template_sentence.format(name=name, phone_number=phone_number, address=address, email=email)
    print(comment_content)
    timestamp = faker.date_time_between(start_date="-1y", end_date="now").strftime('%Y-%m-%d %H:%M:%S')

    return [
        comment_id,
        user_id,
        post_id,
        comment_content,
        timestamp
    ]

# Generate comments and write to CSV file
num_comments = 20
csv_file = "comments.csv"

# Check if the file exists
file_exists = os.path.exists(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists or is_empty_file(csv_file):  # Check if the file is empty
        writer.writerow([
            "comment_id",
            "user_id",
            "post_id",
            "content",
            "timestamp"
        ])

    # Append comment data
    for _ in range(num_comments):
        user_id = faker.uuid4()
        comment_data = generate_comment(user_id)
        writer.writerow(comment_data)

if not file_exists:
    print(f"Generated comment data has been written to '{csv_file}' with a header row.")
else:
    print(f"Generated comment data has been appended to '{csv_file}'.")
