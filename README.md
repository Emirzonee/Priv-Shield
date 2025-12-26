# Priv-Shield: Data Anonymization Tool 

Kurumsal log dosyalarında bulunan hassas verileri (Email, IP adresi, Kredi Kartı, T.C. Kimlik) tespit edip maskeleyen (anonymize) siber güvenlik aracı.

KVKK ve GDPR (General Data Protection Regulation) uyumluluğu süreçlerinde, verilerin üçüncü taraflarla paylaşılmadan önce temizlenmesi için geliştirilmiştir.

## Özellikler
- **Regex Tabanlı Tespit:** Düzenli ifadeler kullanarak hassas veri kalıplarını yakalar.
- **Otomatik Maskeleme:** Tespit edilen verileri `<VERI_GIZLENDI>` etiketiyle değiştirir.
- **Log Analizi:** İşlem sonunda kaç verinin maskelendiğini raporlar.

## Nasıl Kullanılır?
Python 3 ile çalışır. Ek kütüphane gerektirmez.

```bash
python main.py