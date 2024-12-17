# Конфигурационное управление

## Домашнее задание №3

**Вариант №6**

Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений.

Входной текст на учебном конфигурационном языке принимается из стандартного ввода. Выходной текст на языке yaml попадает в файл, путь к которому задан ключом командной строки.

Многострочные комментарии:
```
#|
 Это многострочный
 комментарий
|#
```

Массивы:
```
list( значение, значение, значение, ... )
```
Словари:
```
begin
 имя := значение;
 имя := значение;
 имя := значение;
 ...
end
```

Имена:
```
 [_a-zA-Z]+
```

Значения:

* Числа.
* Строки.
* Массивы.
* Словари.


Строки:
```
 'Это строка'
```

Объявление константы на этапе трансляции:
```
имя := значение
```
Вычисление константного выражения на этапе трансляции (постфиксная форма), пример:
```
{имя 1 +}
```
Результатом вычисления константного выражения является значение.

Для константных вычислений определены операции и функции:

1. Сложение.
2. Вычитание.
3. Умножение.
4. Деление.
5. max().
6. sqrt().

Все конструкции учебного конфигурационного языка (с учетом их возможной вложенности) должны быть покрыты тестами. Необходимо показать 3 примера описания конфигураций из разных предметных областей.

## Описание работы программы программы

Программа предназначен для создания Yaml файла конфигурации из обычного текстового файла с расширением .txt. В файле *config.txt* необходимо написать программу, которая будет конвертирована в файл конфигурации. ***!Внимание!** Программа должна быть написана строго по шаблонам, которые показаны в условиях задачи. При неправильном написании программы файл конфигурации создан будет только с корректными строками*.


## Требования к установке перед запуском программы

Перед запуском программы необходимо установить дополнения:
1. pyyaml

Установить дополнения можно в командной строке, находясь в данном каталоге, введя команду:
```
./install_depenseties.sh
```
После установки дополнения к python можно приступать к запуску программы.

## Запуск программы

Запуск программы осуществляется из командной строки:
```
python main.py output.yaml < config.txt
```
***!Внимание!** Если запуск осуществляется через PowerShell, то команда запуска выглядит так:*
```
Get-Content config.txt | python main.py output.yaml
```

Для запуска юнит-тестов в коммандной строке необходимо написать:
```
python -m unittest test_main.py
```

## Результат юнит-тестов программы

![2024-11-04 (4)](https://github.com/user-attachments/assets/f2c2567e-f977-4a7a-b274-d55726e8d5fd)


## Результат работы программы

**Вариант 1**

![2024-11-04 (6)](https://github.com/user-attachments/assets/a6b78620-1f18-45bb-8ae2-1fb3bcbc2e13)

![2024-11-04 (5)](https://github.com/user-attachments/assets/ca47616d-c9ff-4288-af74-7c41090cefea)

**Вариант 2**

![2024-11-12](https://github.com/user-attachments/assets/dc13c4f8-2273-4500-9c2a-3aedd03f658e)

![2024-11-12 (2)](https://github.com/user-attachments/assets/f45cf246-9a9e-43a6-98cd-94703f5adc2d)

**Вариант 3**

![2024-11-12 (1)](https://github.com/user-attachments/assets/a59a1799-00c5-4ec7-9e81-e08b98ace80b)

![2024-11-12 (3)](https://github.com/user-attachments/assets/faa12637-53cf-49a7-bd3f-3a4d0b538a59)

