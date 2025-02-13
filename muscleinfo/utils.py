import re

# MONGODB
def individual_serial(template) -> dict:
    return {
        "id": str(template["_id"]),
        "nome": template['nome'],
        "musculo": template["musculo"],
        "musculo_residual": template["musculo_residual"],
        "series": template["series"],
        "infos": template["infos"],
        "user_id": template["user_id"],
    }

def list_serial(templates) -> list:
    return [individual_serial(template) for template in templates]

def regex_pattern(string):
    return re.compile(string, re.IGNORECASE)