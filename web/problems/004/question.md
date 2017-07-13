Artun fibonacci dizisini çok sevmektedir ve telefonunun şifresini fibonacci dizisini kullanarak oluşturmak istemektedir. Fibonacci dizisinin genel formülü şöyledir:
> F(n) : n'inci fibonacci sayısını veriyor olsun.
>
> F(0)=0
> F(1)=1
> olarak kabul edelim.
>
> F(n)=F(n-1)+F(n-2)

Artun şifreyi aklında tutmak için sadece kaçıncı fibonacci sayısı olduğunu hatırlıyor ve şifre gerektiği zaman o fibonacci sayısını hesaplayıp telefonunu açıyor. Ama bazen hesaplaması çok uzun sürdüğü için telefonunu açması saatler sürebiliyor. Artun'a yardım etmek için N. fibonacci sayısını hesaplayan bir program yaz.

### Özet:
	N. fibonacci sayısını hesaplayan program yaz.

### Input biçimi:
	Tek bir satırda bir tam sayı, N.
	0<=N<=45

### Output biçimi:
	N. fibonacci sayısı.
	Output'un sonuna endline ("\n") koyabilirsiniz.

| Örnek Input 1 : |
| --------------- |
| 6               |

| Örnek Output 1 : |
| ---------------- |
| 8                |

> Örnek 1'de 6. fibonacci sayısını hesaplamamız gerekiyor.  
> F(0)=0  
> F(1)=1  
> F(2)=F(0)+F(1)=0+1=1  
> F(3)=F(1)+F(2)=1+1=2  
> F(4)=F(2)+F(3)=1+2=3  
> F(5)=F(3)+F(4)=2+3=5  
> F(6)=F(4)+F(5)=3+5=8  
> Bu şekilde 6. fibonacci sayısını (F(6)=8) bulmuş oluyoruz.
