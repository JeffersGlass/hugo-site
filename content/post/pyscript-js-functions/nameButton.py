from faker import Faker

fake = Faker()

def add_a_name(*args, **kwargs):
    new_name = fake.name()
    console.log(f"Adding {new_name} to names")
    names.append(new_name)

Element("add-name").element.addEventListener("click", create_proxy(add_a_name))