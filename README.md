# API Response Size Checker

Bu Python projesi, belirli bir API'ye (random.dog) 100 istek göndererek her bir istekten dönen görsellerin boyutlarını kontrol eder. Görsellerin boyutlarını karşılaştırarak, 1.050.000 byte (1 MB) sınırını aşan görsellerin sayısını ve bu sınırın altında kalan görsellerin sayısını hesaplar. Ayrıca, görsel boyutlarının dağılımını histogram şeklinde görselleştirir.

## Proje Amacı

Bu proje, API yanıtlarının boyutlarını kontrol etmek ve analiz etmek için basit bir araçtır. Özellikle, görsel boyutları gibi belirli parametrelerin sınırlarını aşan verilerin izlenmesini sağlar.

## Özellikler

- 100 istek gönderir.
- Her istek için dönen görselin boyutunu kontrol eder.
- Boyutlar 1.050.000 byte sınırına göre iki gruba ayrılır (büyük / küçük).
- Sonuçları terminalde yazdırır.
- Boyutların dağılımını bir histogram grafiği ile görselleştirir.

## Kullanım

### Gereksinimler

Bu projeyi çalıştırabilmek için Python 3 ve aşağıdaki kütüphaneler gereklidir:

- `requests`
- `matplotlib`

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install requests matplotlib
