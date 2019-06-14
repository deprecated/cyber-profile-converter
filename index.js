const fs = require('fs');
const args = process.argv;

let newProfiles = [];

let file = fs.readFileSync(`${__dirname}/${args[2]}`);
let oldProfiles = JSON.parse(file);

oldProfiles.forEach(profile => {
  newProfiles.push({
    name: profile['payment']['card']['name'],
    email: profile['payment']['email'],
    phone: profile['payment']['phone'],
    sizes: ['Random'],
    singleCheckout: false,
    billingDifferent: false,
    favorite: false,
    card: {
      number: profile['payment']['card']['number'],
      expiryMonth: profile['payment']['card']['exp_month'],
      expiryYear: profile['payment']['card']['exp_year'],
      cvv: profile['payment']['card']['cvv']
    },
    delivery: {
      firstName: profile['delivery']['first_name'],
      lastName: profile['delivery']['last_name'],
      address1: profile['delivery']['addr1'],
      address2: profile['delivery']['addr2'],
      zip: profile['delivery']['zip'],
      city: profile['delivery']['city'],
      country: profile['delivery']['country'],
      state: profile['delivery']['state']
    },
    billing: {
      firstName: null,
      lastName: null,
      address1: null,
      address2: null,
      zip: null,
      city: null,
      country: null,
      state: null
    }
  });
});

let data = JSON.stringify(newProfiles);
fs.writeFileSync('newProfiles.json', data);
