import requests

base_url = "https://cdn.poketwo.net/images/"
total_images = 10238 
start_index = 1 # i changed it to 10001 coz i wanted to start from there
number_in_url = [base_url + str(i) + ".png" for i in range(start_index, total_images+1)]

for index, url in enumerate(number_in_url):
    response = requests.get(url)
# added some error handling
    if response.status_code == 200:
        with open(f"pokemon_{index + start_index}.png", "wb") as f:
            f.write(response.content)
        print(f"Downloaded {url} as pokemon_{index + start_index}.png")
    else:
        print(f"Failed to download {url}")

print("DONE BOI 👍")
