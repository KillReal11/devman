import file_operations
from faker import Faker
import random
import ast
import os


def main():

    with open("skills.txt", "r", encoding="utf-8") as my_file:
        skills = my_file.read()
        skills = skills.split("\n")
    with open("letters_mapping.txt", "r", encoding="utf-8") as my_file:
        alphabet = my_file.read()
        alphabet = ast.literal_eval(alphabet)
        
    os.makedirs("cards", exist_ok=True)

    for i in range(1, 11):
        
        fake = Faker("ru_RU")
        characteristics_min = 3
        characteristics_max = 18
        skills_3 = random.sample(skills, 3)
        runic_skills = list()

        for skill in skills_3:
            temp_skill = skill
            for letter, upd_letter in alphabet.items():
                temp_skill = temp_skill.replace(letter, upd_letter)
            runic_skills.append(temp_skill)

        context = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(characteristics_min, characteristics_max),
            "agility": random.randint(characteristics_min, characteristics_max),
            "endurance": random.randint(characteristics_min, characteristics_max),
            "intelligence": random.randint(characteristics_min, characteristics_max),
            "luck": random.randint(characteristics_min, characteristics_max),
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2],
        }

        template_path = "charsheet.svg"
        output_path = f"cards/result_charsheet_{i}.svg"
        file_operations.render_template(template_path, output_path,context)

if __name__ == "__main__":
    main()
