### Problemin analizi:
Bu sorunun çözümünden önce artık yıl koşulumuzun ne olduğunu daha iyi anlayalım.

* Öncelikle bir yıl 100'e tam bölünmüyorsa 4'e tam bölünmesi yeterlidir deniyor. Örneğin, 2016 yılı artık bir yıldır. Çünkü 2016 iki tane özelliği sağlıyor.
1- 100'e tam bölünmüyor
2- 4'e tam bölünüyor.

* Tam bu noktada 1900'ün artık yıl olmaması genelde kafa karıştırıyor. Ama eğer problemi daha dikkatli incelersek 1900 yılı 100'e tam bölündüğü için, bu yıla 4'e bölünme kuralını uygulayamıyoruz. Ve ikinci kuralımız geliyor.

* Eğer bir yıl 100'e tam bölünüyorsa, artık yıl olması için 400'e tam bölünmesi lazımdır. Bu yüzden 1900 yılına uygulamamız gereken kural 400'e bölünebilme kuralı ve 1900 bu testten kalıyor.

Daha iyi anlatmak gerekirse, bir sayının (N) artık yıl olup olmadığını anlamak için ilk test olarak 100'e tam bölünüp bölünemediğini kontrol edeceğiz. Bu testtin sonucu olarak ikincil testlerden hangisini uygulamamız gerektiğini öğreneceğiz.

Aşağıdaki karar ağacı daha iyi anlamanız için yardımcı olabilir:

![Artık yıl karar ağacı](/static/resources/003/artik_yil.png)

### İzleyeceğimiz yol:
Üstteki karar ağacını kodlarken iç içe if kullanacağız.
* Aldığımız sayının 100'e tam bölünüp bölünmediğini kontrol edeceğiz. Bu kontrolün sonucunda iki olasılık var:

1- Eğer sayı 100'e tam bölünüyor ise 4'e tam bölünüp bölünmediğini kontrol edeceğiz. Eğer 4'e tam bölünüyor ise "EVET", aksi takdirde "HAYIR" yazdıracağız.

2- Eğer sayı 100'e tam bölünmüyor ise 400'e tam bölünüp bölünmediğini kontrol edeceğiz. Eğer 400'e tam bölünüyor ise "EVET", aksi takdirde "HAYIR" yazdıracağız.

> **Hatırlatma :** A sayısının B sayısına tam bölünüp bölünemediğini bulmak için modüler aritmetik operatörünü kullanabilirsiniz.
>Örneğin: A%B==0 ifadesi B, A'yı tam bölüyorsa 0 harici bir değer (yani True), tam bölmüyosa 0 (yani False) döner.

~~~~{.c}
#include <stdio.h>

int main()
{
    int yil;

    scanf("%d", &yil);

    /*Sayinin 100'e tam bolunup bolunmediginin testi*/
    if(yil%100!=0)
    {
     /*Eger sayi 100'e tam BOLUNMUYORSA yapilacak test*/
        if(yil%4==0)/*4'e tam BOLUNUYORSA*/
        {
            printf("EVET\n");
        }
        else/*4'e tam BOLUNMUYORSA*/
        {
            printf("HAYIR\n");
        }

    }
    else
    {
        /*Eger sayi 100'e tam BOLUNUYORSA yapilacak test*/
        if(yil%400==0)/*400'e tam BOLUNUYORSA*/
        {
            printf("EVET\n");
        }
        else/*400'e tam BOLUNMUYORSA*/
        {
            printf("HAYIR\n");
        }

    }

    return 0;
}
~~~~
