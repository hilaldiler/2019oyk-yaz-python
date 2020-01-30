import requests

response = requests.get('https://www.imdb.com/chart/top')
film_data = response.content.decode('utf-8').split('<tbody class="lister-list">')[1].split('</tbody>')[0]

for film in film_data.split('<tr>')[1:]:
    film_ismi = film.split('<td class="titleColumn">')[1].split('</td>')[0]
    #print(film_ismi.split('>')[1].split('<')[0])
    print(film_ismi.split('>')[1].split('<'))
    print("--"*5)