import requests
import time

def get_country_name(country_code):
    
    url = f"https://restcountries.com/v2/alpha/{country_code}"

    try:
        response = requests.get(url=url, 
                                headers={'Accept': 'application/json'}
                                )
        response.raise_for_status() # if http errors occurr 

        data = response.json()

        time.sleep(1) # to not to harras API 
        
        return data["name"]

    except requests.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.RequestException as err:
        print ("OOps: Something Else",err)
    except Exception as e:
        print(f"An error occurred: {e}")
