# 🛠️ Cron-Task-Master

Bu proje, **Açık Kaynak İşletim Sistemleri** dersi final projesi kapsamında geliştirilmiş, Linux sistemlerinde zamanlanmış görevleri ve yedekleme süreçlerini yöneten bir otomasyon aracıdır.

## 🌟 Öne Çıkan Özellikler
- **Sistem Bütünlük Kontrolü (Auto-Control):** Betik çalışmadan önce sistemdeki Cron altyapısını otomatik kontrol eder.
- **Güvenli Yedekleme:** Python `subprocess` mimarisi kullanılarak terminal komutları üzerinden güvenli sıkıştırma yapar.
- **Unix I/O Standartları:** İşlem sonuçlarını ve hataları `stdout` ve `stderr` kanalları üzerinden raporlar.
- **JSON Metadata:** Proje bilgileri ve gereksinimleri `project_info.json` dosyasında standartlaştırılmıştır.

## 📁 Klasör Yapısı
- `src/`: Ana otomasyon kodları ve mantıksal katman.
- `specs/`: Teknik gereksinimler ve proje kimlik kartı.
- `researchs/`: Yapay zeka destekli teknik araştırma raporları.
- `docs/`: Proje kullanım belgeleri ve sunum dosyaları.

## 🚀 Kullanım
Proje, Linux tabanlı sistemlerde Python 3.10 ve üzeri sürümlerde çalışacak şekilde optimize edilmiştir.

## 🛠️ Teknik Notlar 
- **I/O Yönetimi:** Betik, işlem çıktılarını `stdout` üzerinden, hataları ise `stderr` üzerinden anlık olarak raporlar.
- **Güvenlik:** `subprocess.run` kullanımı sırasında `shell=False` prensibi korunarak komut enjeksiyonu riskleri önlenmiştir.
- **Otomasyon:** Sistemde `crontab` kurulu değilse betik kullanıcıyı uyararak işlemi durdurur (Self-check).
