import requests
response = requests.get("https://thebestschools.org/rankings/best-universities-world-today/")
bolunmemis=response.content.decode('utf-8').split('<div id="toc" class="one-third first toc">')[1].split('<div class="section tbselements " id="">⁂</div>')[0]
for film in bolunmemis.split('<a')[1:]:
    if film.find('</li') > -1:
        print(film.split('</a')[0].split('>')[1])