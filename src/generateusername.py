import csv
import os
from faker import Faker
import hashlib

    # ar_AA (Arabic)
    # az_AZ (Azerbaijani)
    # bg_BG (Bulgarian)
    # bs_BA (Bosnian)
    # cs_CZ (Czech)
    # de_DE (German)
    # dk_DK (Danish)
    # el_GR (Greek)
    # en_AU (English - Australia)
    # en_CA (English - Canada)
    # en_GB (English - Great Britain)
    # en_IN (English - India)
    # en_NZ (English - New Zealand)
    # en_US (English - United States)
    # es_ES (Spanish - Spain)
    # es_MX (Spanish - Mexico)
    # et_EE (Estonian)
    # fa_IR (Farsi)
    # fi_FI (Finnish)
    # fr_FR (French)
    # hi_IN (Hindi)
    # hr_HR (Croatian)
    # hu_HU (Hungarian)
    # hy_AM (Armenian)
    # id_ID (Indonesian)
    # it_IT (Italian)
    # ja_JP (Japanese)
    # ka_GE (Georgian)
    # kk_KZ (Kazakh)
    # ko_KR (Korean)
    # lt_LT (Lithuanian)
    # lv_LV (Latvian)
    # ne_NP (Nepali)
    # nl_NL (Dutch)
    # no_NO (Norwegian)
    # pl_PL (Polish)
    # pt_BR (Portuguese - Brazil)
    # pt_PT (Portuguese - Portugal)
    # ro_RO (Romanian)
    # ru_RU (Russian)
    # sk_SK (Slovakian)
    # sl_SI (Slovenian)
    # sr_RS (Serbian)
    # sv_SE (Swedish)
    # tr_TR (Turkish)
    # uk_UA (Ukrainian)
    # zh_CN (Chinese - China)
    # zh_TW (Chinese - Taiwan)
# Create an instance of the Faker class
faker = Faker('hu_HU')

# Generate synthetic data for each field
def generate_username():
    first_name = faker.first_name()
    last_name = faker.last_name()

    return [
        first_name,
        last_name,

    ]

# Generate user data and write to CSV file
num_users = 5
csv_file = "username.csv"

# Check if the file exists
file_exists = os.path.exists(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:  # Write mode, add header row
        writer.writerow([
            "first_name",
            "last_name",
        ])

    # Append user data
    for _ in range(num_users):
        user_data = generate_username()
        writer.writerow(user_data)

if not file_exists:
    print(f"Generated user data has been written to '{csv_file}' with a header row.")
else:
    print(f"Generated user data has been appended to '{csv_file}'.")
