### Шифрованные инструкции

Марсоход получает с Земли сокращённые инструкции с заданиями, например:

с — сделать снимок;
в — взять образец грунта;
ш — сделать шаг;
о — включить освещение;
и — инициировать сканирование местности.

Из-за ограничений канала связи инструкции отправляются в сжатом виде. 
Например, если марсоходу нужно сделать 10 снимков подряд, инструкция будет выглядеть как 10[с].
Число перед квадратными скобками обозначает, сколько раз надо повторить последовательность внутри скобок. 
Скобки могут быть и вложенными: 2[ш3[с]]10[с].
Таким образом, командный центр на Земле может отправить марсоходу сжатую строку инструкций, 
а марсоход получит и расшифрует её в полную последовательность команд.
Команды могут обозначаться символами латиницы или кириллицы.

**Пример:**

Команда: 2[с]3[в]ш
Расшифровка: «ссвввш».
Смысл: сделать два снимка, взять три образца грунта и сделать шаг.

**Пример 2:**

Команда: 2[в3[ш]]с
Расшифровка: «вшшшвшшшс»
Смысл: Взять образец грунта, сделать три шага; взять образец грунта, сделать три шага; сделать снимок.

Напишите программу, которая расшифровывает сжатые сообщения и возвращает строку с командами.