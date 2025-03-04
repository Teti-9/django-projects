import re

# MONGODB
def individual_serial(template) -> dict:
    return {
        "id": str(template["_id"]),
        "nome": template['nome'],
        "musculo": template["musculo"],
        "musculo_residual": template["musculo_residual"],
        "series": template["series"],
        "carga": template["carga"],
        "carga_anterior": template["carga_anterior"],
        "repeticoes": template["repeticoes"],
        "repeticoes_anterior": template["repeticoes_anterior"],
        "infos": template["infos"],
        "data": template["data"],
        "data_anterior": template["data_anterior"],
        "user_id": template["user_id"],
    }

def list_serial(templates) -> list:
    return [individual_serial(template) for template in templates]

def regex_pattern(string):
    return re.compile(string, re.IGNORECASE)