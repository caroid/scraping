# -*- coding : utf-8 -*-
from selenium import webdriver
import json
from time import sleep

driver = webdriver.Firefox()
KEY_WORDS = (
    'empresas', 'transporte', 'acarreo', 'construccion', 'flete', 'ferreteria',
    'aluminio', 'acero', 'vidrio', 'pvc', 'ladrillo', 'carga', 'materiales',
    'floristerias', 'comida+rapida', 'supermercado', 'respuestos', 'autopartes',
    'ingenieria', 'mensajeria', 'arena', 'plasticos', 'empaques', 'neveras',
    'muebles', 'maderas', 'automotores', 'electricos', 'electrodomesticos',
    'papeles', 'bebidas', 'libros', 'restaurantes', 'alimentos', 'colegios',
    'universidades', 'eventos', 'hogar', 'animales', 'estructuras', 'ornamentacion',
    )

companies = {}
n = 1

for key in KEY_WORDS:
    url = 'http://www.paginasamarillas.com.co/busqueda/empresas-bogota?match={key_word}'
    driver.get(url.format(key_word=key))

    while True:
        try:
            next_btn = driver.find_element_by_css_selector('.arrow-results.aw-rtl02.pager-link')
        except:
            break

        links = driver.find_elements_by_css_selector('.send.show-contact-window')

        if not links:
            break

        for link in links:
            try:
                email = link.get_attribute('data-email')
                company = link.get_attribute('data-namecmp')
            except:
                continue

            if email not in companies:
                companies[email] = company
                print email, company

        next_btn.click()
        sleep(5)
        n += 1
    n = 1

with open('db.json', 'wb') as fp:
    json.dump(companies, fp)

driver.quit()