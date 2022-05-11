Аркадная игра Pac-man

Проект выполняется на языке программирования Python с помощью библиотеки Pygame и является всеми известной игрой Pac-man,
в которой персонаж должен набирать очки, поедая монетки, и избегать врагов. На второй стадии разработки проекта были написаны графическая состовляющая и доделаны в связи с этим классы.


Таким образом, реализованы следующие классы:  
PacMan - отвечает за действия игрока, его передвижения, жизни и очки.  
Coin - монеты, которые при съедении приносят игроку очки.  
Fruit - объекты, наследованные от Coin-ов, которые умеют еще и передвигаться.  
Special coin - особенные монеты, так же наследованные от Coin-ов, при съедении
которых игрок становится способным убивать врагов в течение некоторого времени.  
Enemy - враг, который при обычном (то есть исключающем Special coin) взаимодействии с игроком, 
убивает его.  
Level -  отвечает непосредственно за уровень и процессы в нем (проверяет монеты, делает врагов уязвимыми,
завершает уровень).  
Map - карты уровней, координаты объектов.  

UI классы (пока не ипсользуются, будут применены на следующем этапе разработки):  
Button - кнопка.  
Menu - интерфейс меню.  
Pause - интерфейс паузы.  

Подробнее поля и методы представленных класов можно изучить в UML диаграмме:
![UML Pac_Man](https://user-images.githubusercontent.com/91114932/162632612-614ee3ae-5de5-455f-bca9-e4d591bba38a.png)


На следующих этапах будет применены UI классы и доделан интерфейс игры.
В дальнешем также предусматривается введений улучшений, такие как новые уровни, различное
поведение врагов и тд.
