#! /usr/bin/env python3
import bs4, requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
} #Error 503 from amazon that is possibly because amazon only blocks IPs that it recognizes are from cloud platforms and that are systematically scraping their site., you need to insert headers



res=requests.get('https://www.amazon.com.mx/TANNYS-KITCHEN-almacenamiento-JUEGO-RECIPIENTES/dp/B0BYTSBC55?ref_=Oct_DLandingS_D_e834e6a4_0&th=1', headers=headers)
assert res.status_code == 200

res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'html.parser')
print(soup.text)

elems=soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole') #select method selects the css selectors
print(elems)