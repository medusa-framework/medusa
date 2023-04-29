from datetime import datetime
import random
from faker import Faker as faker

class Generator():
    def __init__(self) -> None:
        self._value_generators = {
            "String": self.generate_string,
            "DateTime": self.generate_datetime,
            "Date": self.generate_datetime,
            "Time": self.generate_datetime,
            "Boolean": self.generate_boolean,
            "Integer": self.generate_integer
        }
        super().__init__()

    def generate_value(self, column):
        col_type = column.type.__class__.__name__
        generator = self._value_generators.get(col_type)
        if generator:
            return generator(column)
        else:
            return None

    def generate_string(self, column):
        col_name = column.name.lower().replace("_", "")
        if "email" in col_name:
            return self.generate_email()
        elif "username" in col_name:
            return self.generate_username()
        elif "phone" in col_name:
            return self.generate_phone()
        elif "firstname" in col_name:
            return self.generate_first_name()
        elif "lastname" in col_name:
            return self.generate_last_name()
        elif "displayname" in col_name:
            return self.generate_username()
        elif "password" in col_name:
            return "medusa"
        elif "address" in col_name:
            return self.generate_address()
        elif "city" in col_name or "town" in col_name:
            return self.generate_city()
        elif "zipcode" in col_name or "postcode" in col_name:
            return self.generate_zip()
        elif "title" in col_name:
            return self.generate_title()
        elif col_name in ["content", "summary", "description", "overview"]:
            return self.generate_paragraph()
        elif "message" in col_name:
            return self.generate_sentence()
        else:
            return self.generate_words(column)
    
    def generate_words(self, column):
        words = faker().words(nb=random.randint(1, 10))
        return " ".join(words)[:column.type.length]

    def generate_email(self):
        return faker().ascii_free_email()
    
    def generate_username(self):
        verb = faker().word(part_of_speech="verb").title()
        noun = faker().word(part_of_speech="noun").title()
        num = random.randint(100, 999)
        return f"{verb}_{noun}{num}"
    
    def generate_phone(self):
        r_c = random.randint(100, 999)
        a_c = random.randint(100, 999)
        digits = random.randint(1000, 9999)
        return f"({r_c}) {a_c}-{digits}"
    
    def generate_first_name(self):
        return faker().first_name()
    
    def generate_last_name(self):
        return faker().last_name()
    
    def generate_address(self):
        return faker().street_address()
    
    def generate_city(self):
        return faker().city()
    
    def generate_zip(self):
        return faker().postcode()
    
    def generate_title(self):
        return " ".join(faker().words(nb=random.randint(3, 6))).title()
    
    def generate_paragraph(self):
        return faker().paragraph(nb_sentences=5)
    
    def generate_sentence(self):
        return faker().sentence()
    
    def generate_datetime(self, column):
        return datetime.now()
    
    def generate_integer(self, column):
        return random.randint(1, 2000)
    
    def generate_boolean(self, column):
        return faker().boolean()
    