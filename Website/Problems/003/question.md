Bazı yıllar Şubat ayı 29 gün olur. Bu yıllara artık yıl denir. Herhangi bir yılın artık yıl olup olmadığını anlamak için şu işlemleri uygularız:
* Eğer bir yıl 100'e bölünüyorsa artık yıl olması için 400'e de bölünmesi gerekir.
* Aksi takdirde 4'e bölünmesi onun artık yıl olması için yeterlidir.
Örneğin;
* 2016 bir artık yıldır. Çünkü 100'e bölünmediği için 4'e bölünmesi yeterlidir.
* 2015 bir artık yıl değildir. Çünkü 4'e bölünmüyor.
* 1900 bir artık yıl değildir. Çünkü 100'e bölündüğü halde 400'e tam bölünmüyor.
* 1600 bir artık yıldır. Çünkü 100'e tam bölünmeyi sağlayıp aynı zamanda 400'e de tam bölünüyür.

Sayıların artık yıl olup olmadığını hesaplayan bir program yaz.


### Özet:
	Yukarıdaki özellikleri sağlayan bir yıl verildiyse "EVET", değilse "HAYIR" yazdır.

### Input biçimi:
	Tek bir satırda bir tam sayı, N.
	0<N<10^9

### Output biçimi:
	Eğer girilen yıl artık yıl ise "EVET", değil ise "HAYIR".
	Output'un sonuna endline ("\n") koyabilirsiniz.

| Örnek Input 1 : |
| --------------- |
| 2016            |

| Örnek Output 1 : |
| ---------------- |
| EVET             |

>Örnek 1'de sayı 100'e bölünmediği için 4'e bölünmeyi sağlaması yeterlidir. Bu yüzden 2016 bir artık yıldır.


| Örnek Input 2 : |
| --------------- |
| 2017            |

| Örnek Output 2 : |
| ---------------- |
| HAYIR            |

>Örnek 2'deki yıl (2017) 4'e bölünmediği için artık yıl değildir.


| Örnek Input 3 : |
| --------------- |
| 1900            |

| Örnek Output 3 : |
| ---------------- |
| HAYIR            |

>Örnek 3'de 1900, 4'e tam bölünmesine rağmen bir artık yıl değildir. Bunun nedeni 1900'ün 100'e tam bölünürken 400'e tam bölünmemesidir.
