import whois
import requests
from bs4 import BeautifulSoup

def web_site_bilgisi(domain):
    # Whois sorgusu yapma
    whois_info = whois.whois(domain)
    print("Info for Domain:")
    print(whois_info)

    # Web sitesinin içeriğini çekme
    response = requests.get("http://" + domain)
    soup = BeautifulSoup(response.content, "html.parser")

    # Başlık etiketlerini (title tags) bulma
    title_tags = soup.find_all("title")
    print("\nBaşlık Etiketleri:")
    for title in title_tags:
        print(title.string)

    # Meta açıklama etiketini (meta description) bulma
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc:
        print("\nMeta Açıklama:")
        print(meta_desc.get("content"))
    else:
        print("\nMeta Açıklama bulunamadı.")

    # HTTP başlık bilgilerini alma
    print("\nHTTP Başlık Bilgileri:")
    for header in response.headers:
        print(header + ": " + response.headers[header])

    # Site haritası bağlantılarını alma
    site_map_links = soup.find_all("a", href=True)
    print("\nSite Haritası Bağlantıları:")
    for link in site_map_links:
        print(link["href"])

# Kullanıcıdan web sitesinin alan adını alınması
domain = input("Web sitesinin alan adını girin (örn. example.com): ")
web_site_bilgisi(domain)