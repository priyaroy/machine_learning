import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
print('HOUSING_URL = ', HOUSING_URL)
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    print(tgz_path)
    urllib.request.urlretrieve(housing_url, filename=None)[0]
    base_name=os.path.basename(housing_url)
    
    file_name, extension = os.path.splitext(base_name)
    print('file_name = ', file_name)
    
    housing_tgz = tarfile.open(housing_url)
    
    housing_tgz.extractall(file_name)
    housing_tgz.close()
    print('End of code')
    
fetch_housing_data()