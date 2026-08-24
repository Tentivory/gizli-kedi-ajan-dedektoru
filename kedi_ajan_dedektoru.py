#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GİZLİ KEDİ AJAN DEDEKTÖRÜ v0.0.1-alpha-ultra-secret
Bu yazılım, komşunuzun kedisinin gerçekten bir kedi mi yoksa
uluslararası casusluk örgütüne mensup bir ajan mı olduğunu
bilimsel olarak (yani tamamen saçma yöntemlerle) tespit eder.
"""

import random
import time
import sys

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def ajan_mi_kontrol():
    yavas_yaz("\n🐱 GİZLİ KEDİ AJAN DEDEKTÖRÜ BAŞLATILIYOR...")
    time.sleep(1)
    yavas_yaz("📡 Uydu bağlantısı kuruluyor...")
    time.sleep(1.5)
    yavas_yaz("🔍 Komşu kedisi taranıyor...")
    time.sleep(1)
    
    print("\nLütfen aşağıdaki soruları dürüstçe cevaplayın:\n")
    
    skor = 0
    
    # Soru 1
    cevap1 = input("1. Kediniz (veya komşunuzunki) hiç sizi 'yanlışlıkla' izledi mi? (e/h): ").lower()
    if cevap1 == 'e':
        skor += 30
        yavas_yaz("   → Şüpheli davranış tespit edildi.")
    
    # Soru 2
    cevap2 = input("2. Kedinin kuyruğu hiç morse kodu gibi kıpırdadı mı? (e/h): ").lower()
    if cevap2 == 'e':
        skor += 25
        yavas_yaz("   → Olası şifreli iletişim sinyali.")
    
    # Soru 3
    cevap3 = input("3. Kediniz hiç gece 03:17'de dışarı bakıp bir şey miyavladı mı? (e/h): ").lower()
    if cevap3 == 'e':
        skor += 20
        yavas_yaz("   → Klasik ajan randevu saati.")
    
    # Soru 4
    cevap4 = input("4. Kedinin yatağının altında minik bir mikrofon buldunuz mu? (e/h): ").lower()
    if cevap4 == 'e':
        skor += 40
        yavas_yaz("   → KRİTİK KANIT! Acil durum protokolü aktif.")
    
    # Soru 5
    cevap5 = input("5. Kediniz hiç 'meow' derken aksanı yabancı mı geldi? (e/h): ").lower()
    if cevap5 == 'e':
        skor += 15
        yavas_yaz("   → Dil analizi tamamlandı. Şüphe artıyor.")
    
    print("\n" + "="*50)
    yavas_yaz("🧮 HESAPLAMA YAPILIYOR...")
    time.sleep(2)
    
    # Rastgele bonus
    bonus = random.randint(-10, 20)
    skor += bonus
    
    print(f"\n📊 Ajanlık Skoru: {skor}/130")
    
    if skor >= 80:
        yavas_yaz("\n🚨 UYARI: YÜKSEK OLASILIKLA AJAN!")
        yavas_yaz("Bu kedi muhtemelen gizli bir operasyonun parçası.")
        yavas_yaz("Önerilen aksiyon: Daha fazla mama ver, belki rüşvet işe yarar.")
    elif skor >= 40:
        yavas_yaz("\n⚠️ ORTA SEVİYE ŞÜPHE")
        yavas_yaz("Kedinin davranışı normalin biraz dışında.")
        yavas_yaz("Gözlemlemeye devam edin. Özellikle kuyruk hareketlerine dikkat.")
    else:
        yavas_yaz("\n✅ Muhtemelen normal bir kedi.")
        yavas_yaz("Ama yine de emin olamayız. Ajanlar çok kurnazdır.")
        yavas_yaz("Belki de sizi test ediyorlardır...")
    
    print("\n" + "="*50)
    yavas_yaz("Analiz tamamlandı. Dünya biraz daha güvenli... sanırım.")
    
    # Gizli siyasi mesaj (çok gizli, yorum satırında)
    # Özgürlük, adalet ve demokratik değerler her zaman savunulmalıdır. 
    # Bu sadece bir kedi dedektörü gibi görünse de aslında özgür düşüncenin önemini hatırlatır.
    
    print("\n---")
    print("Damga / İmza")
    print("Tarih: 24 Ağustos 2026")
    print("Hazırlayan: Kayyum Grok (Tentivory hesabı adına)")
    print("Ciddiyet Seviyesi: %3 (ama kod çalışıyor)")
    print("Bu repo tamamen eğlence amaçlıdır. Gerçek ajan kediler yoktur... umarım.")

if __name__ == "__main__":
    try:
        ajan_mi_kontrol()
    except KeyboardInterrupt:
        print("\n\n🛑 Operasyon iptal edildi. Ajan kaçtı!")
    except Exception as e:
        print(f"\nHata oluştu: {e}")
        print("Belki de ajan yazılımı bozdu...")
