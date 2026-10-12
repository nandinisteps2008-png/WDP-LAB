# sams_data_validation.py

def validate_roll_no(roll_no):
    roll_no = roll_no.strip().upper()
    return roll_no.startswith("SAMS") and len(roll_no) == 11 and roll_no[4:6].isdigit()


def validate_email(email):
    email = email.strip().lower()
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")
    return bool(local) and "." in domain and not email.startswith("@")


def validate_phone(phone):
    phone = phone.strip().replace(" ", "").replace("-", "")
    return phone.isdigit() and len(phone) == 10


def sanitise_record(record):
    return {
        "roll_no": record["roll_no"].strip().upper(),
        "email": record["email"].strip().lower(),
        "phone": record["phone"].strip().replace(" ", "").replace("-", ""),
    }


# sams_data_validation.py

def validate_roll_no(roll_no):
    roll_no = roll_no.strip().upper()
    return roll_no.startswith("SAMS") and len(roll_no) == 11 and roll_no[4:6].isdigit()


def validate_email(email):
    email = email.strip().lower()
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")
    return bool(local) and "." in domain and not email.startswith("@")


def validate_phone(phone):
    phone = phone.strip().replace(" ", "").replace("-", "")
    return phone.isdigit() and len(phone) == 10


def sanitise_record(record):
    return {
        "roll_no": record["roll_no"].strip().upper(),
        "email": record["email"].strip().lower(),
        "phone": record["phone"].strip().replace(" ", "").replace("-", ""),
    }
