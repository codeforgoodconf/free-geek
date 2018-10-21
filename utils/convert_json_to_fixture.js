var fs = require('fs');
var parsed_json = require('./converted_volunteer_default_shifts.json');

var details = parsed_json.map((row) => {
  var dingo = {}
  dingo.pk = parseInt(row.id)
  dingo.model = "scheduling.VolunteerDefaultShift"
  dingo.fields = {}
  let keys = Object.keys(row)
  
  keys.filter(key => key !== 'id')
    .map((key) => {
      dingo.fields[key] = row[key]
    })

  return dingo
})

const str = JSON.stringify(details)
fs.writeFile('volunteer_default_shifts.json', str, 'utf8', ()=> {});
