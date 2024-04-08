import csv
import os
from faker import Faker
import hashlib
import random

# Create an instance of the Faker class
faker = Faker()

template_sentences = [
    "Hi, all I got a new iphone , you can reach me at {phone_number}, {name}.",
    "I'm shifting to new place today , and my address will be {address}.",
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
    last_post_id = 0
    if os.path.exists(csv_file):
        with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            for row in reader:
                post_id = int(row[0])
                last_post_id = max(last_post_id, post_id)
    return last_post_id

# Function to generate synthetic data for each field
def generate_comment(post_id, user_id, likes_count, comments_count, shares_count):

    template_sentence = random.choice(template_sentences)
    name = faker.name()
    phone_number = faker.phone_number()
    email = faker.email()
    address = faker.address()
    comment_content = template_sentence.format(name=name, phone_number=phone_number, address=address, email=email)
    print(comment_content)
    timestamp = faker.date_time_between(start_date="-1y", end_date="now").strftime('%Y-%m-%d %H:%M:%S')

    return [
        post_id,
        user_id,
        comment_content,
        timestamp,
        likes_count,
        comments_count,
        shares_count
    ]

# Generate comments and write to CSV file
num_comments = 20
csv_file = "posts.csv"

# Check if the file exists
file_exists = os.path.exists(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists or is_empty_file(csv_file):  # Check if the file is empty
        writer.writerow([
            "post_id",
            "user_id",
            "content",
            "timestamp",
            "likes_count",
            "comments_count",
            "shares_count"
        ])

    post_id = get_last_ids(csv_file)
    user_id = random.randint(1, 100)  # Random user_id between 1 and 100
    likes_count = random.randint(100, 500)  # Random user_id between 100 and 500
    comments_count = random.randint(2, 15)  # Random user_id between 2 and 15
    shares_count = random.randint(20, 60) # Random user_id between 20 and 60
    # Append comment data
    for _ in range(num_comments):
        post_id += 1
        comment_data = generate_comment(post_id, user_id, likes_count, comments_count, shares_count)
        writer.writerow(comment_data)

if not file_exists:
    print(f"Generated comment data has been written to '{csv_file}' with a header row.")
else:
    print(f"Generated comment data has been appended to '{csv_file}'.")
