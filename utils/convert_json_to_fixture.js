var fs = require('fs');
var parsed_json = require(process.argv[3]);

var details = parsed_json.map((row) => {
  var obj = {}
  obj.pk = parseInt(row.id)
  obj.model = process.argv[2]
  obj.fields = {}
  let keys = Object.keys(row)

  // if key ends in _id then parseInt
  // and set key to value
  keys.filter(key => key !== 'id')
    .map((key) => {
      const regex = /_id$/g;
      if(key.match(regex)) {
        obj.fields[key] = parseInt(row[key])
      } else {
        obj.fields[key] = row[key]
      }
    })
  return obj
})

const str = JSON.stringify(details)
const output = process.argv[2].split(".")[0] + '.json';
fs.writeFile(output, str, 'utf8', ()=> {});

// node convert_json_to_fixture.js "scheduling.VolunteerDefaultShift" "./data.json"
