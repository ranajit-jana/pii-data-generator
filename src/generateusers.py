import csv
import os
from faker import Faker
import hashlib

# Create an instance of the Faker class
faker = Faker()

# Generate synthetic data for each field
def generate_user():
    user_id = faker.uuid4()
    username = faker.user_name()
    email = faker.email()
    # Generate a random password hash (not a real hash, for demonstration purposes only)
    password_hash = hashlib.sha256(faker.password().encode()).hexdigest()
    profile_picture_url = faker.image_url()
    bio = faker.text()
    location = faker.address()
    registration_timestamp = faker.date_time_between(start_date="-1y", end_date="now").strftime('%Y-%m-%d %H:%M:%S')
    phone = faker.phone_number()
    driver_license = faker.random_number(digits=10)
    aadhar_number = faker.random_number(digits=12)

    return [
        user_id,
        username,
        email,
        password_hash,
        profile_picture_url,
        bio,
        location,
        registration_timestamp,
        phone,
        driver_license,
        aadhar_number
    ]

# Generate user data and write to CSV file
num_users = 10
csv_file = "users.csv"

# Check if the file exists
file_exists = os.path.exists(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:  # Write mode, add header row
        writer.writerow([
            "user_id",
            "username",
            "email",
            "password_hash",
            "profile_picture_url",
            "bio",
            "location",
            "registration_timestamp",
            "phone",
            "driver_license",
            "aadhar_number"
        ])

    # Append user data
    for _ in range(num_users):
        user_data = generate_user()
        writer.writerow(user_data)

if not file_exists:
    print(f"Generated user data has been written to '{csv_file}' with a header row.")
else:
    print(f"Generated user data has been appended to '{csv_file}'.")
