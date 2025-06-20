Basics of HTTP/HTTPS
1. HTTP və HTTPS arasındakı fərqlər
HTTP (Hypertext Transfer Protocol) və HTTPS (HTTP Secure) internetdə məlumat
mübadiləsi üçün istifadə olunan protokollardır. Əsas fərq onların təhlükəsizlik səviyyəsindədir:

HTTP şifrələnməmiş məlumat ötürür, yəni ötürülən məlumatı üçüncü şəxslər asanlıqla
ələ keçirə bilər. Bu səbəbdən şəxsi və maliyyə məlumatları üçün təhlükəsiz deyil.

HTTPS isə SSL/TLS şifrələmə protokolu vasitəsilə məlumatları şifrələyir.
Bu, məlumatların təhlükəsiz ötürülməsini təmin edir və məlumatların ələ keçirilməsinin qarşısını alır.

HTTPS həmçinin serverin autentifikasiyasını təmin edir, yəni istifadəçi
həmin serverin etibarlı olduğunu təsdiq edə bilir.

HTTPS protokolu xüsusilə bank, e-poçt və onlayn alış-veriş
saytlarında geniş istifadə olunur.

Wireshark kimi paket analizi alətlərindən istifadə edərək HTTP trafiki
açıq mətn kimi görünür, HTTPS trafiki isə şifrələnmiş olduğu üçün anlaşılmazdır.

2. HTTP sorğu və cavab strukturu
Veb səhifəyə daxil olduqda, brauzer serverə HTTP sorğusu göndərir və
server sorğuya HTTP cavabı ilə cavab verir. Bu prosesdə əsas elementlər aşağıdakılardır:

HTTP Sorğusu (Request):
Metod: Sorğunun növünü göstərir (məsələn, GET, POST).

URL/Path: Serverdə istənilən resursun ünvanı.

Başlıqlar (Headers): Sorğu haqqında əlavə məlumatlar (məsələn, istifadəçi agenti, qəbul edilən format).

Bədən (Body): Bəzi metodlarda (POST, PUT) məlumat göndərmək üçün istifadə olunur.

HTTP Cavabı (Response):
Status kodu: Sorğunun nəticəsini bildirir (məsələn, 200 OK, 404 Not Found).

Başlıqlar (Headers): Cavab haqqında əlavə məlumatlar (məsələn, server növü, tarix).

Bədən (Body): Serverdən gələn məlumat (məsələn, HTML, JSON).

Brauzerin “Inspect” → “Network” bölməsində bu məlumatları rahatlıqla müşahidə etmək mümkündür.

3. HTTP metodları və status kodları
Ümumi HTTP metodları
Metod	Təsviri	İstifadə halı
GET	Resursu əldə etmək üçün istifadə olunur	Veb səhifəni yükləmək və ya məlumat sorğulamaq
POST	Serverə yeni məlumat göndərmək üçün istifadə olunur	Form məlumatlarını göndərmək
PUT	Mövcud resursu yeniləmək üçün istifadə olunur	İstifadəçi məlumatını dəyişmək
DELETE	Resursu silmək üçün istifadə olunur	Hesabı və ya faylı serverdən silmək

Ümumi HTTP status kodları
Kod	Təsviri	İstifadə halı
200	OK — Sorğu uğurla tamamlandı	Veb səhifə və ya məlumat uğurla yükləndi
301	Moved Permanently — Resurs daimi olaraq başqa ünvana köçürüldü	Köhnə URL yeni ünvana yönləndirildi
404	Not Found — Soruşulan resurs tapılmadı	Yanlış URL daxil edildikdə və ya səhifə silindikdə
403	Forbidden — İcazəsiz giriş cəhdi	Məsələn, məhdudlaşdırılmış səhifəyə giriş zamanı
500	Internal Server Error — Serverdə daxili xəta baş verdi	Serverdə proqram səhvi və ya konfiqurasiya problemi zamanı

Nəticə
HTTP və HTTPS internetdə məlumatların mübadiləsi üçün əsas protokollardır. HTTPS, HTTP-dən fərqli olaraq, əlavə şifrələmə
və autentifikasiya təmin edir ki, bu da məlumatların təhlükəsizliyini və gizliliyini artırır. HTTP sorğu və cavabları metod,
URL, status kodları və başlıqlardan ibarətdir. Ən çox istifadə olunan HTTP metodları GET, POST, PUT və DELETE-dir.
Status kodları isə sorğunun nəticəsini göstərir və ən çox rast gəlinən kodlar 200, 301, 404, 403 və 500-dür.