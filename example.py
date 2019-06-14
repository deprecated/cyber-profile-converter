import sys
import json

filename = sys.argv[1]


def old2new(oldprofiles):
    newprofiles = []
    for key, value in oldprofiles.iteritems():
        newprofiles.append({
            "name": value['payment']['card']['name'],
            "email": value['payment']['email'],
            "phone": value['payment']['phone'],
            "sizes": ["Random"],
            "singleCheckout": False,
            "billingDifferent": False,
            "favorite": False,
            "card": {
                "number": value['payment']['card']['number'],
                "expiryMonth": value['payment']['card']['exp_month'],
                "expiryYear": value['payment']['card']['exp_year'],
                "cvv": value['payment']['card']['cvv']
            },
            "delivery": {
                "firstName": value['delivery']['first_name'],
                "lastName": value['delivery']['last_name'],
                "address1": value['delivery']['addr1'],
                "address2": value['delivery']['addr2'],
                "zip": value['delivery']['zip'],
                "city": value['delivery']['city'],
                "country": value['delivery']['country'],
                "state": value['delivery']['state']        
            },
            "billing": {
                "firstName": None,
                "lastName": None,
                "address1": None,
                "address2": None,
                "zip": None,
                "city": None,
                "country": None,
                "state": None
            }
        })

    return newprofiles


def main():
    oldprofiles = None
    with open(filename) as json_file:
        oldprofiles = json.load(json_file)

    newprofiles = old2new(oldprofiles)
    print json.dumps(newprofiles)

main()