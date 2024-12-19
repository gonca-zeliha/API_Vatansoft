import requests
import matplotlib.pyplot as plt 

BYTE_LIMIT = 1050000
NUM_REQUESTS = 100
API_URL = "https://random.dog/woof.json?ref=apilist.fun"


larger_count = 0
smaller_count = 0
sizes = []  


def check_image_size():
    global larger_count, smaller_count
    
    try:
       
        response = requests.get(API_URL)
        
        if response.status_code == 200:  
            dog_image_url = response.json().get("url")
            
            image_response = requests.get(dog_image_url)
            
            if image_response.status_code == 200:
               
                response_size = len(image_response.content)
                sizes.append(response_size)  
                
                if response_size > BYTE_LIMIT:
                    larger_count += 1
                else:
                    smaller_count += 1
            else:
                print(f"Hata: Görsel URL'sine erişilemiyor: {dog_image_url}")
        else:
            print("Hata: API'ye erişilemedi!")
    
    except requests.exceptions.RequestException as e:
        print(f"Bağlantı hatası: {e}")


for i in range(NUM_REQUESTS):
    check_image_size()
    print(f"{i + 1}. istek tamamlandı")


print("\nSonuçlar:")
print(f"Boyutu 1.050.000 byte'tan büyük: {larger_count}")
print(f"Boyutu 1.050.000 byte'tan küçük: {smaller_count}")


plt.hist(sizes, bins=10, color='blue', alpha=0.7)
plt.axvline(x=BYTE_LIMIT, color='red', linestyle='--', label='1050000 byte limit')
plt.title('API Response Sizes')
plt.xlabel('Response Size (bytes)')
plt.ylabel('Frequency')
plt.legend()
plt.show()
