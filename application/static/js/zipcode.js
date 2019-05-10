const zipcodeInput = document.querySelector('.zipcode-input')


zipcodeInput.addEventListener('keyup', (e) => {
  const zipcode = e.target.value 
  const shouldFetch = zipcode.length === 5

  if (shouldFetch) {
    console.log('works', e.target.value)
    fetchLocationData(zipcode)
  }
})




async function fetchLocationData(zipcode) {
  const userId = '195LETSR2101'
  const requestUrl = `https://secure.shippingapis.com/shippingapi.dll?API=CityStateLookup&XML=<CityStateLookupRequest USERID="${ userId }"><ZipCode ID='0'><Zip5>${ zipcode }</Zip5></ZipCode></CityStateLookupRequest>`
  const parseXml = (xmlStr) => {
     return new window.DOMParser().parseFromString(xmlStr, "text/xml")
  }
  const response = await fetch(requestUrl)
    .then(res => res.text())

  // console.log('response: ', response)
  const parsedXml = parseXml(response)
  const locationDataJson = xmlToJson(parsedXml)
  // console.log('locationDataJson: ', locationDataJson) 
  setCityAndState(locationDataJson)
}


function setCityAndState(locationData) {
  const city = locationData.CityStateLookupResponse.ZipCode.City['#text']
  const state = locationData.CityStateLookupResponse.ZipCode.State['#text']
  console.log('city: ', city)
  console.log('state: ', state)
}




//below function from David Walsh (https://davidwalsh.name/convert-xml-json)
// Changes XML to JSON
function xmlToJson(xml) {
	
	// Create the return object
	var obj = {};

	if (xml.nodeType == 1) { // element
		// do attributes
		if (xml.attributes.length > 0) {
		obj["@attributes"] = {};
			for (var j = 0; j < xml.attributes.length; j++) {
				var attribute = xml.attributes.item(j);
				obj["@attributes"][attribute.nodeName] = attribute.nodeValue;
			}
		}
	} else if (xml.nodeType == 3) { // text
		obj = xml.nodeValue;
	}

	// do children
	if (xml.hasChildNodes()) {
		for(var i = 0; i < xml.childNodes.length; i++) {
			var item = xml.childNodes.item(i);
			var nodeName = item.nodeName;
			if (typeof(obj[nodeName]) == "undefined") {
				obj[nodeName] = xmlToJson(item);
			} else {
				if (typeof(obj[nodeName].push) == "undefined") {
					var old = obj[nodeName];
					obj[nodeName] = [];
					obj[nodeName].push(old);
				}
				obj[nodeName].push(xmlToJson(item));
			}
		}
	}
	return obj;
};
