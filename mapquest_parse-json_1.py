import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "NRLPKMJTVAcKWAJ09be2HRfatstrDNbF"

# convert miles
def convert(miles, newUnit):
    if (newUnit == "Kilometers"):
        return miles * 1.61
    if (newUnit == "Miles"):
        return miles

while True:
    orig = input("Starting location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    units = input("Preferred Units [Kilometers/Miles]: ")
    if units == "quit" or units == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()
    print("URL: " (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["status code"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from: " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format(convert(each["distance"], units)) + " " + units.lower() + ")"))
        print("=============================================\n")
    
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")

    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")

    else:
        print("**********************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("**********************************************\n")
