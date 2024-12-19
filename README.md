# API Response Size Checker

Bu Python projesi, random.dog API'sine 100 istek gönderir ve her bir istekten dönen görsellerin boyutlarını kontrol eder. İsteklerin yanıtlarında dönen görsellerin boyutları, 1.050.000 byte (yaklaşık 1 MB) sınırına göre değerlendirilir. Sonuç olarak, büyük ve küçük boyutlu görsellerin sayıları hesaplanır ve görsel boyutlarının dağılımı histogram ile görselleştirilir.

## Proje Amacı

Bu proje, API yanıtlarından elde edilen görsellerin boyutlarını analiz etmek amacıyla geliştirilmiştir. Belirli bir boyut sınırına (1.050.000 byte) göre görsellerin boyutlarını karşılaştırmak ve bu bilgiyi görsel bir şekilde sunmak amacıyla kullanılır.

## Özellikler

- 100 API isteği gönderilir.
- API yanıtından dönen görselin boyutu alınır.
- Boyutlar, 1.050.000 byte (1 MB) limitine göre iki gruba ayrılır: büyük ve küçük.
- Sonuçlar terminalde yazdırılır.
- Boyutların dağılımı histogram grafiğiyle görselleştirilir.

## Kullanım

### Gereksinimler

Bu projeyi çalıştırabilmek için Python 3 ve aşağıdaki kütüphanelerin yüklü olması gereklidir:

- `requests`: API'ye istek göndermek için.
- `matplotlib`: Görselleştirme (grafik) oluşturmak için.


