# Simulated DynamoDB table (for demo purpose)

donors_table = []

def add_donor(donor):
    donors_table.append(donor)
    return {
        "message": "Donor added successfully",
        "donor": donor
    }

def get_donors():
    return donors_table