#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import requests

host = 'https://api.weather.com'

def default_params():
  return {
    'apiKey': "09d7ff3676f24f2597ff3676f2ef2525",
    'language': 'es',
    'geocode': '-21.170401,-47.810326',
    'units': 'm',
    'format': 'json'
  }

def request_headers():
  return {
    'User-Agent': 'Request-Promise',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip'
  }

def pronostico_tiempo():
  url = "/v3/wx/forecast/daily/15day"
  
  full_url = host + url

  params = default_params()
  headers = request_headers()

  r = requests.get(full_url, params=params, headers=headers)
  
  resultado = r.json()

  pronostico = {
     'temperatureMin': resultado['temperatureMin'][14],
     'temperatureMax': resultado['temperatureMax'][14],
     'winSpeed': resultado['daypart'][0]['windSpeed'][29],
     'windDirection': resultado['daypart'][0]['windDirection'][29],
  }

  return pronostico

def evotranspiracion(crop):
    url = "/v3/wx/forecast/hourly/agriculture/15day"

    full_url = host + url

    params = default_params()
    headers = request_headers()
    params['crop'] = crop + ":50"

    r = requests.get(full_url, params=params, headers=headers)
  
    resultado = r.json()
    
    evo = {
        "evo": resultado['forecasts1Hour']['evapotranspirationCrop'][0] 
    }
    
    return evo

def main(dict):
    try:
        crop = dict["crop"]
        resultado = evotranspiracion(crop)
    except:
        resultado = pronostico_tiempo()
    return resultado
