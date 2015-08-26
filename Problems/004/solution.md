### İzleyeceğimiz yol:
* 2 tane tam sayı tanımlayacağız, a ve b.

* Bu tamsayıların değerleri ilk başlangıçta a=F(0)=0 ve b=F(1)=1 şeklinde olacak.

* Bunları bir döngüye koyacağız ve her döngüde b'nin değeri (a+b) olacak ve a'nın değeri b'nin eski değeri olacak. Örneğin, a=2 ve b=3 iken bir döngü sonra a=3 ve b=5 olacak.

* Fark etmişsinizdir ki eğer a=F(k) ve b=F(k+1) ise bir döngü sonra a=F(k+1) ve b=F(k+2) oluyor. Bu şekilde n'inci fibonacci sayısına kadar döngüyü sürdüreceğiz.

> **Hatırlatma :** b'nin içine (a+b)'yi koyarken a'nın içine de b'nin eski değerini koyma işini şu şekilde yapabilirsiniz:
> İlk önce geçici bir değişken belirleyelim. (Bunun sebebini daha sonra anlayacaksınız.) Adı temp olsun.
> temp<-b
> b<-a+b
> a<-temp
>
> Eğer b'nin eski değerini bir geçici değişkene kaydetmeseydik b<-a+b işlemini yaptıktan sonra b'nin eski değerini kaybederdik.

~~~~{.c}
#include <stdio.h>

int main()
{
    int i, n;
    int a, b;
    int temp;

    /*a=F(0)=0 ve b=F(1)=1*/
    a=0;
    b=1;

    scanf("%d", &n);

    /*n. fibonacci sayisini istedigi icin n kere
    donguyu devam ettiriyoruz. Bu sayede n. fibonacci
    sayisina kadar a ve b yi kaydirmis oluyoruz.*/
    for(i=0;i<n;i++)
    {
        temp=b;
        b=a+b;
        a=temp;
    }

    /*n. fibonacci sayisi dongu bittikten sonra
    a'nin icinde duruyor, bu yuzden a'yi bastiriyoruz.*/
    printf("%d\n", a);

    return 0;
}

~~~~


