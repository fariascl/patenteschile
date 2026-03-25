import re
import rstr


class Patente:
    CURRENT_CONSONANTS = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'P', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}
    CURRENT_BLOCKED = {'A', 'E', 'I', 'M', 'N', 'Ñ', 'O', 'Q', 'U'}
    OLD_LETTERS = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    OLD_BLOCKED = {'Ñ', 'Q'}

    FORMATS = {
        "auto": {
            "current": {
                "pattern": r"^([B-Z]{4})-([1-9][0-9])$",
                "letters": 4,
                "numbers": 2,
                "blocked": CURRENT_BLOCKED
            },
            "old": {
                "pattern": r"^([A-Z]{2})-(\d{4})$",
                "letters": 2,
                "numbers": 4,
                "blocked": OLD_BLOCKED
            }
        },
        "moto": {
            "current": {
                "pattern": r"^([B-Z]{2})-(\d{3})$",
                "letters": 2,
                "numbers": 3,
                "blocked": CURRENT_BLOCKED
            },
            "old": {
                "pattern": r"^([B-Z]{2})-(\d{3})$",
                "letters": 2,
                "numbers": 3,
                "blocked": CURRENT_BLOCKED
            }
        },
        "remolque_liviano": {
            "old": {
                "pattern": r"^([A-Z]{2})-(\d{4})$",
                "letters": 2,
                "numbers": 4,
                "blocked": OLD_BLOCKED
            }
        },
        "remolque_pesado": {
            "old": {
                "pattern": r"^([A-Z]{2})-(\d{4})$",
                "letters": 2,
                "numbers": 4,
                "blocked": OLD_BLOCKED
            }
        }
    }

    def generate_current(self, vehicle_type="auto"):
        while True:
            if vehicle_type == "auto":
                letters = rstr.xeger(r"[B-Z]{4}")
                if not any(c not in self.CURRENT_CONSONANTS for c in letters):
                    number = rstr.xeger(r"[1-9][0-9]")
                    return f"{letters}-{number}"
            elif vehicle_type == "moto":
                letters = rstr.xeger(r"[B-Z]{2}")
                if not any(c not in self.CURRENT_CONSONANTS for c in letters):
                    number = rstr.xeger(r"[1-9]\d{2}")
                    return f"{letters}-{number}"

    def generate_old(self, vehicle_type="auto"):
        while True:
            if vehicle_type == "auto":
                letters = rstr.xeger(r"[A-Z]{2}")
                if not any(c in self.OLD_BLOCKED for c in letters):
                    number = rstr.xeger(r"\d{4}")
                    return f"{letters}-{number}"
            elif vehicle_type == "moto":
                letters = rstr.xeger(r"[B-Z]{2}")
                if not any(c not in self.CURRENT_CONSONANTS for c in letters):
                    number = rstr.xeger(r"[1-9]\d{2}")
                    return f"{letters}-{number}"
            elif vehicle_type == "remolque_liviano":
                letters = rstr.xeger(r"[A-Z]{2}")
                if not any(c in self.OLD_BLOCKED for c in letters):
                    number = rstr.xeger(r"\d{4}")
                    return f"{letters}-{number}"
            elif vehicle_type == "remolque_pesado":
                letters = rstr.xeger(r"[A-Z]{2}")
                if not any(c in self.OLD_BLOCKED for c in letters):
                    number = rstr.xeger(r"\d{4}")
                    return f"{letters}-{number}"

    def generate(self, num: int, system="current", vehicle_type="auto"):
        if system == "current":
            return [self.generate_current(vehicle_type) for _ in range(num)]
        elif system == "old":
            return [self.generate_old(vehicle_type) for _ in range(num)]

    def validate(self, patente: str):
        patente = patente.upper().strip()
        
        for system_key, system_data in self.FORMATS.items():
            for format_key, format_info in system_data.items():
                pattern = format_info["pattern"]
                match = re.match(pattern, patente)
                if match:
                    letters = match.group(1)
                    blocked = format_info["blocked"]
                    if not any(c in blocked for c in letters):
                        return True
        return False
