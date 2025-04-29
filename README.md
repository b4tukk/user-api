# 👤 User API with Python, Flask & GitHub Actions

Bu proje, Python ile yazılmış basit bir REST API örneğidir. Kullanıcı ekleme ve listeleme işlemlerini gerçekleştirir. Ayrıca yazılım test sürecine DevOps yaklaşımlarını entegre eden bir Continuous Integration (CI) pipeline'ı içerir.

## 🚀 Özellikler

- Flask ile REST API
- Basit kullanıcı veri işlemleri
- Pytest ile birim testler
- GitHub Actions ile CI otomasyonu
- Gereksinim dosyası (`requirements.txt`) ile kolay kurulum

## 🧱 Proje Yapısı

user_api/
├── app.py # Flask uygulaması
├── users.py # Kullanıcı işlemleri
├── test_users.py # Pytest testleri
├── requirements.txt # Gerekli Python paketleri
└── .github/workflows/
    └── python-app.yml # CI pipeline (GitHub Actions)

## ⚙️ Kurulum ve Çalıştırma

### 1. Ortamı Hazırla

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Uygulamayı Başlat

```bash
python app.py
```

### 3. API Kullanımı

POST /users – Yeni kullanıcı ekler

```bash
{
  "name": "Ali"
}
```

GET /users – Tüm kullanıcıları listeler

🧪 Testler
Testleri çalıştırmak için:

```bash
pytest
```

🔄 DevOps & GitHub Actions
Her push veya pull request sonrası, GitHub Actions aşağıdaki adımları otomatik olarak çalıştırır:

Bağımlılıkları yükler (pip install)

Testleri çalıştırır (pytest)

Başarısız test varsa uyarı verir, başarılıysa CI başarılı olur ✅

CI dosyası yolu: .github/workflows/python-app.yml

📸 Ekran Görüntüsü

👨‍💻 Geliştirici
Batuhan Korkmaz

Samsun Üniversitesi

GitHub: [github.com/b4tukk]
