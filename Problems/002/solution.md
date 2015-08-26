## Çözüm 1:

### Problemin analizi:
* Satılan eşya sayısı 20'ye eşit ya da 20'den daha az.
* Tekrar eden sayı yok.
* 1. ve 2. maddeden dolayı inputta en fazla 20 tane integer verilebilir.
* Verilen sayılar sıralı olmayabilir.

### İzleyeceğimiz yol.
* 20 boyutunda bir integer array'i yaratıp içine inputtan aldığımız integerları koyacağız.
* 1'den 20'ye kadar her sayı için array'i arayıp, array'de bulunmayan sayıları bastıracağız.

~~~~{.c}
#include <stdio.h>

int main()
{
    int n, i, j;
    int flag;
    /*satilmis esyalarin numaralarini koymak icin boyutu 20 olan bir integer array'i alalim.*/
    int satilmis_esyalar[20];

    /*kac tane esyanin satilgini n'e atiyoruz.*/
    scanf("%d", &n);

    /*tekrar eden esya numarasi olmadigi icin ve n tane
    esya satildigi icin verilen inputta n tane sayi olacak.*/
    /*bu n tane sayiyi arrayimize kaydediyoruz.*/
    for(i=0;i<n;i++)
    {
        scanf("%d", &satilmis_esyalar[i]);
    }

    /*1'den 20'ye kadar olan butun sayilari dolasiyoruz.*/
    for(i=1;i<=20;i++)
    {

        flag=0;

        /*Ikinci for dongusunde i numarali esya
        satilmis esyalarin arasinda var mi diye kontrol ediyoruz.*/
        for(j=0;j<n;j++)
        {
            /*Eger i numarali esyaya satilmis_esyalar arrayinde rastlarsak
            o eşya numarasini bastirmayacagimizi bi ustteki for dongusune bildirmek
            icin flag adli degiskenin degerini 1 yapiyoruz*/
            if(i==satilmis_esyalar[j])
            {
                flag=1;
            }
        }

        /*ikinci for dongusunde flagin degeri 1 yapilmis mi diye kontrol ediyoruz.
        Eger flag'in degeri 1 ise demek ki i numarali esya satilmis esyalarin arasinda.
        Eger flag'in degeri 1 ise bu esya satilmamis demektir. Bu nedenle bu esyanin
        numarasi olan i degiskenini bastiriyoruz.*/
        if(flag!=1)
        {
            printf("%d ", i);
        }
    }

    printf("\n");

    return 0;
}
~~~~

## Çözüm 2:

### Problemin Analizi:
* Verilecek sayilar 1'den 20'ye kadar olan tam sayılar.
* Üstteki maddeden dolayı verilecek olan herhangi bir sayı 20'den küçük.

### İzleyeceğimiz yol:
* 21 tane integer alabilecek bir array alacağız.(programlaması daha kolay olacağı için 21)
* Bu array'in bütün indexlerini 0'a eşitleyeceğiz.(aldığımız local değişkenlerin değeri ilk başta 0 olmayabiliyor.)
* Hepsini en başta 0'a eşitlememizin sebebi, bu indexlerde inputta o sayıdan kaç kere girildiğini tutacak olmamız. (Sonraki maddeleri okursanız bu maddede anlatılmak isteneni daha iyi anlayabilirsiniz.)
* Input'u alırken her yani sayi geldiğinde, örneğin X, arrayimizin X. index'ini 1 arttıracağız.(arr[X]++;)
* Bu şekilde inputların hepsini alacağız.
* Inputları aldıktan sonra bütün arrayi 1. index'ten başlayarak 20. index'e kadar dolaşıp değeri 0 (yani hiç arttırılmamış) olan indexleri bastıracağız.

### Bu çözümün mantığı:
Elimizde bütün değerleri 0 olan 20 boyutunda index'i 1 den baslayan bi array olduğunu farz edelim.

| Array(int) |
| ------ | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| index: | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| değer: | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |

Input'umuz da şöyle olsun:
>5 7 15 12

Inputtaki ilk değeri index olarak kullanıp arrayimizdeki o lokasyonu 1 arttıralım. Bu arttırmadan sonra arrayimiz şu hale geliyor: (arr[5]++;)

| Array(int) |
| ------ | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| index: | 1 | 2 | 3 | 4 | **5** | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| değer: | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |

Diğer inputları aldıktan sonra tablomuzun en son hali şu şekilde:

| Array(int) |
| ------ | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| index: | 1 | 2 | 3 | 4 | **5** | 6 | **7** | 8 | 9 | 10 | 11 | **12** | 13 | 14 | **15** | 16 | 17 | 18 | 19 | 20 |
| değer: | 0 | 0 | 0 | 0 | **1** | 0 | **0** | 0 | 0 | 0  | 0  | **0**  | 0  | 0  | **0**  | 0  | 0  | 0  | 0  | 0  |

Farkedeceğiniz gibi eğer tablomuzun herhangi bir indexinin değeri 0 ise bu index inputlarımızın arasında yok demektir. Biz de bu özelliği kullanarak tabloyu en başından gezerek değeri 0 olan indexleri (yani inputta verilmemiş indexleri) bastırıyoruz.

~~~~{.c}
#include <stdio.h>

int main()
{
    int i, n;
    int temp;

    /*Inputta verilen esyalarin numaralarinin bulundugu indexi
    1 arttiracagimiz arrayi yaratiyoruz.*/
    int esya_numaralari[21];

    /*Local degiskenler yaratildiginda degeleri 0'a esit olmayabilir
    Bu yuzden hepsini 0'a esitliyoruz.*/
    for(i=0;i<21;i++)
    {
        esya_numaralari[i]=0;
    }

    scanf("%d", &n);

    for(i=0;i<n;i++)
    {
        /*Inputtaki her bir integer'i temp adli degiskene kaydediyoruz.*/
        scanf("%d", &temp);

        /*arrayimizin temp'inci index ini 1 arttiriyoruz.*/
        esya_numaralari[temp]++;
    }

    for(i=1;i<=20;i++)
    {
        /*Bir onceki for dongusunde aldigimiz input'un arraydeki indexini 1 arttirdik.
        Eger arraydeki o index'in hala 0 ise inputlarin arasinda gecmemis demektir.
        Bu yuzden degeri 0 olan indexler satilmis esyalarin arasinda DEGILDIR.*/
        if(esya_numaralari[i]==0)
        {
            printf("%d ", i);
        }
    }

    printf("\n");

    return 0;
}
~~~~
