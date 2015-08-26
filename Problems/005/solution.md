### Problemin analizi:
Problemde ilk dikkat etmemiz gereken nokta input olarak alacağımız sayının sınırının 10^100 olmasının. Bunun önemli olmasının nedeni

~~~~{.c}
int number;
~~~~

üstteki şekilde tanımlayacağımız bir değişkenin tutabileceği sayının limiti 2,147,483,647'dir. Bu da 2*10^9 civarında bir sayıdır ve 10^100 gibi bir sayıyı tutamaz. Bu yüzden sayısı bir **integer** olarak değil de bir **string**'miş gibi alacağız. C dilinde string olmadığı için bu yapıya en uygun olan **char array**'ini kullanabiliriz.

### İzleyeceğimiz yol:
* Sayımızı tutacağımız bir **char array**'i tanımlayacağız. Sayımız 10^100'den küçük olacağı için en fazla 99 basamaklı olabilir. Bu yüzden 100 boyutunda bir array yaratmamız yeterli olacaktır.
~~~~{.c}
char number[100];
~~~~

* Sayımızı bir char array'inde tuttuğumuza göre sayıyı bir string alıyormuş gibi alabiliriz. Bunun için scanf fonksiyonun format string'inde "%s" opsiyonunu kullanacağız.
~~~~{.c}
scanf("%s", number);
~~~~

* Sayımızı aldığımıza göre geriye sayımızın palindrom olup olmadığını test etmek kaldı. Bunun için uygulayacağımız strateji aşağıdaki gibi olacak. Aldığımız sayı farz edelim 123321.

| Array(char) |
| ------ |  -  |  -  |  -  |  -  |  -  |  -  |  -   |  -  |  -  |  -  |  -  |
| index: |  0  |  1  |  2  |  3  |  4  |  5  |  6   |  7  |  8  |  9  | ... |
| değer: | '1' | '2' | '3' | '3' | '2' | '1' | '\0' | ... | ... | ... | ... |

* İlk önce sayımızın kaç basamaklı olduğunu öğreneceğiz. Bunun için **string.h** kütüphanesindeki **strlen()** fonksiyonunu kullanmamız işimizi görecektir. Bu sayıyı daha sonra kullanabilmek için bir **integer değişkenine** atayalım.
~~~~{.c}
n = strlen(number);
~~~~

* Bir tane değişken belirleyelim. Bu değişkenin başlangıç değeri 1 olsun. Bu değikenin değerinin 1 olması sayımızın palindrome olduğunu, 0 olması ise palindrome olmadığını belirtsin. Yani bir **flag** yaratalım. (Şu an flag'in ne olduğunu anlamadıysanız çözümü okumaya devam edebilirsiniz, ileride daha anlaşılır olacak.)

* Bir baştan bir de sondan char arrayimizdeki iki karakteri alalım.  

| Array(char) |
| ------ |  -  |  -  |  -  |  -  |  -  |  -  |  -   |  -  |  -  |  -  |  -  |
| index: |  **0**  |  1  |  2  |  3  |  4  |  **5**  |  6   |  7  |  8  |  9  | ... |
| değer: | **'1'** | '2' | '3' | '3' | '2' | **'1'** | '\0' | ... | ... | ... | ... |

* Ve bu değerler eşit mi diye kontrol edelim. Eğer eşit ise hiçbir şey yapmayalım ama farklı ise **flag**'in değerini 0 yapalım. Böylelikle bütün sayıyı taramamız boyunca, palindrom kuralını ihlal eden herhangi bir şey olup olmadığını döngü bittikten sonra flag'in değerine bakarak anlayabileceğiz.

~~~~{.c}
for(i=0;i<n/2;i++)
{
	if(number[i]!=number[(n-1)-i])
		flag=0;
}
~~~~


* Üstteki örnekte 123321 sayısı palindrom olduğundan böyle bir ihlal gerçekleşmeyecek ve flag'in değeri döngü bittikten sonra da 1 kalacak.

* En son ise flag in değerine bakarak sayımızın palindrom olup olmadığını anlayıp cevabı yazdırmak kaldı.

~~~~{.c}
if(flag==1)
	printf("EVET\n");
else
	printf("HAYIR\n");
~~~~

> Küçük bir ayrıntı daha var. Eğer sayımızın basamak sayısı tek olsaydı bu kod hala düzgün sonuç verecek miydi? Bunu görebilmenin en kolay yolu denemektir. Farz edelim girilen sayı 12321 olsun. Bu sayının palindrom olduğunu biliyoruz. Peki programımız nasıl çalışacak?

| Array(char) |
| ------ |  -  |  -  |  -  |  -  |  -  |  -   |  -  |  -  |  -  |  -  |  -  |
| index: |  0  |  1  |  2  |  3  |  4  |  5   |  6  |  7  |  8  |  9  | ... |
| değer: | '1' | '2' | '3' | '2' | '1' | '\0' | ... | ... | ... | ... | ... |

> Sayımızın basamak sayısı, n, 5. for döngüsünde n/2 bize (integer divison olacağı için) 2 değerini dönecek. Yani i değişkenimiz sadece 0 ve 1 değerlerini alacak ki bu da tam bizim istediğimiz şey çünkü '3'(number[2]) tam ortada olacağı için onu herhangi bir sayıyla kontrol etmemize gerek yok. Bu yüzden programımız basamak sayısı tek olan sayılar için de çalışıyor.

~~~~{.c}

#include <stdio.h>
#include <string.h>

int main()
{
	int i, n;
	char number[100];
	int flag;
	
	/*sayimizi char array'imize string'mis gibi aliyoruz*/
	scanf("%s", number);
	
	/*sayimizin kac basamakli oldugunu n adli degiskene atiyoruz.*/
	n = strlen(number);	
	
	flag=1;
	
	for(i=0;i<n;i++)
	{
		/*Bir bastan bir sondan karsilastirma yaparken 
		esit olmayan iki karakter var ise flag'in degerini
		0 yapiyoruz*/
		if(number[i]!=number[(n-1)-i])
		{
			flag=0;
		}
	}
	
	/*Eger flag'in degeri hala 1 ise sayimiz palindrom'dur.
	flag'in degeri 0 olmus ise demek ki bir bastan bir sondan
	alis islemimizde birbirine esit olmayan iki karaktere
	raslanmis demektir ve sayi palinrom degildir.*/
	if(flag==1)
		printf("EVET\n");
	else
		printf("HAYIR\n");
	
	return 0;
}

~~~~



