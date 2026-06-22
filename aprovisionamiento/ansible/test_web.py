import requests

def test_web_content():
    # El cliente usa contenedor web para ver URL.
    url = "http://web-preproduccion:8083"
    response = requests.get(url)
    # El encoding para las tildes del nombre.
    response.encoding = 'utf-8'
 # Verificamos código 200 y nombre
    assert response.status_code == 200
    assert "José Alfonso Panadero Estudillo" in response.text
