Palindrom sayılar, tersten okunuşu kendisi ile aynı olan sayılara denir. Palindrome sayılara örnek olarak şunları gösterebiliriz:  
> 123321  
> 121  
> 111  
> 5  

Üstteki sayıların hepsinin tersten okunuşu kendisine eşit.

Bir sayının palindrome olup olmadığını bulan program yaz.

### Özet:
	Girilen sayının palindrome olup olmadığını kontrol et.
	
### Input biçimi:
	Tek bir satırda bir tam sayı, N.
	Sayının başında 0 yok.
	0 < N < 10^100
	
### Output biçimi:
	N bir palindrome sayı ise "EVET" yazdır.
	N bir palindrome sayı değil ise "HAYIR" yazdır.
	Output'un sonuna endline ("\n") koyabilirsiniz.


| Örnek Input 1 : |
| --------------- |
| 135531          |

| Örnek Output 1 : |
| ---------------- |
| EVET             |

> Örnek 1'de 135531'in tersten okunuşu kendisine eşit olduğu için 135531 bir palindrom sayıdır.

| Örnek Input 2 : |
| --------------- |
| 13579           |

| Örnek Output 2 : |
| ---------------- |
| HAYIR            |

> Örnek 2'de 13579 sayısının tersten okunuşu (97531) kendisine eşit olmadığı için 13579 bir palindrom sayı değildir.

| Örnek Input 3 : |
| --------------- |
| 11235853211     |

| Örnek Output 3 : |
| ---------------- |
| EVET             |

> Örnek 3'te 11235853211 sayısının tersten okunuşu kendisine eşit olduğu için 11235853211 bir palindrom sayıdır.


