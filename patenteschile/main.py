import rstr


class Patente:
    BLOCKED_CHARS = {'A', 'E', 'I', 'M', 'N', 'Ñ', 'O', 'Q', 'U'}

    def calculate_patente(self):
        while True:
            letters = rstr.xeger(r"[B-Z]{4}")
            if not any(c in self.BLOCKED_CHARS for c in letters):
                number = rstr.xeger(r"[1-9][0-9]")
                return f"{letters}-{number}"

    def generate(self, num: int):
        return [self.calculate_patente() for _ in range(num)]
