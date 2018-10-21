var fs = require('fs');
var parsed_json = require('./converted_volunteer_default_shifts.json');

var details = parsed_json.map((row) => {
  var dingo = {}
  dingo.pk = parseInt(row.id)
  dingo.model = "scheduling.VolunteerDefaultShift"
  dingo.fields = {}
  let keys = Object.keys(row)

  // drop id
  keys.filter(key => key !== 'id')
    .map((key) => {
      dingo.fields[key] = row[key]
    })

  return dingo
})
console.log(details)

const str = JSON.stringify(details)
fs.writeFile('volunteer_default_shifts.json', str, 'utf8', ()=> {});

// 1. convert csv to json then
  // csvtojson volunteer_default_shifts.csv > converted_volunteer_default_shifts.json
// 2. use custom js script to take parsed json grab correct fields and change shape
  // node convert_json_to_fixture_volunteer_default_shifts.js
// 3. beautify json in editor to verify json shape
// 4.
  // mv converted_volunteer_default_shifts.json ~/code/freegeek/free-geek/scheduling/fixtures/
//




// TODO: get extender cable back for laptop
