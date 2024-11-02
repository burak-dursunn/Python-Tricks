import faker
from faker.providers import internet
import requests

fake = faker.Faker()
fake.add_provider(internet)
print("Fake:", fake.ipv4_private())
site = requests.get("http://checkip.amazonaws.com/")
print("Real:", site.text)
