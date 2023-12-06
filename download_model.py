import requests
import zipfile

URL = "https://drive.drivem.workers.dev/download.aspx?file=EL%2B76Ci2PEBxuALH2lWtqVk91W0AC7lHP8WKeECR2PjsbWI90DjxgEAhk6iM1UEe&expiry=2IZQUm5HC%2Fxa36yeh0TBvw%3D%3D&mac=6cde01f98d1556a311a09cd694a686448f9a51e82451b5b2068e3189d86fd4e2"


def download_file(URL):
    content = requests.get(URL).content
    with open("tire_quality_model.zip", "wb") as f:
        f.write(content)
    with zipfile.ZipFile("tire_quality_model.zip", "r") as zip_ref:
        zip_ref.extractall("tire_quality_model")
    return "Model downloaded!"
