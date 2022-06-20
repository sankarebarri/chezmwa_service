import uuid

def generate_house_code():
    code = str(uuid.uuid()).replace('-','').upper()[:12]
