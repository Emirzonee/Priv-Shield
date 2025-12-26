import re
import os
import time

def anonymize_log(filepath):
    print(f"\n[*] PRIV-SHIELD: Veri Gizliliği Aracı Başlatılıyor...")
    print(f"[*] Hedef Dosya: {filepath}")
    
    # 1. Regex Desenleri (Hassas Veri Tanımları)
    patterns = {
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b': '<EMAIL_GIZLENDI>', # Email
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b': '<IP_GIZLENDI>',          # IP Adresi
        r'\b\d{11}\b': '<TC_NO_GIZLENDI>',                        # 11 Haneli TC/ID
        r'\b(50|51|4\d)\d{2}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b': '<KREDI_KARTI_GIZLENDI>' # Kredi Kartı
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            original_len = len(content)

        # 2. Maskeleme İşlemi
        masked_content = content
        count = 0
        for pattern, mask in patterns.items():
            matches = len(re.findall(pattern, masked_content))
            if matches > 0:
                masked_content = re.sub(pattern, mask, masked_content)
                count += matches

        # 3. Yeni Dosyayı Kaydet
        new_filename = "masked_output.txt"
        with open(new_filename, 'w', encoding='utf-8') as f:
            f.write(masked_content)

        print("-" * 50)
        print(f"[+] İŞLEM BAŞARILI!")
        print(f"[+] Toplam Maskelenen Veri: {count}")
        print(f"[+] Orijinal Boyut: {original_len} karakter")
        print(f"[+] Oluşturulan Güvenli Dosya: {new_filename}")
        print("-" * 50)

    except FileNotFoundError:
        print("[!] Hata: Dosya bulunamadı.")
    except Exception as e:
        print(f"[!] Beklenmedik Hata: {e}")

if __name__ == "__main__":
    # Test için örnek veri oluştur
    sample_text = """
    [INFO] User login: ahmet.yilmaz@sirket.com
    [DEBUG] Connection from: 192.168.1.14
    [WARN] Payment attempt CC: 4543-1234-5678-9010
    """
    with open("sample.log", "w") as f:
        f.write(sample_text)
    
    print("Test için 'sample.log' dosyası oluşturuldu.")
    anonymize_log("sample.log")