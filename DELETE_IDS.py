import requests
import base64

# Create ads personal access token - full access
# Run with `python DELETE_IDS.py`

delete_ids = [154731,161919,161963,162154,162164,162184,162191,162195,170033,170040,170043,170045,]

def deleteId(id):
    pat = '255cmzyh6xdztpkooqapd2g6rofx4hxhzuffq76umoatzy6jm6la'  # Your personal access token (PAT) here

    authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
    
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic '+authorization
    }
    
    # Construct the URL dynamically using the current ID
    url = f"https://dev.azure.com/ADSP-Org-A03/ADS/_apis/test/plans/{id}?api-version=5.0"
    response = requests.delete(url, headers=headers)
    
    print(f"Deleted ID {id}: {response.text}")


for id in delete_ids:
    deleteId(id)


