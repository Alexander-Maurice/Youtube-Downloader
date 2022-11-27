from pytube import YouTube

# Выбираем файл
link = input('Вставьте ссылку на видео: ')

# создаем экземпляр класса
yt = YouTube(link)

# указываем разрешение файла
ys = yt.streams.get_highest_resolution()
print('Скачивание...')

# указываем место сохранения
ys.download('/Desktop/Downloads/')

print('Скачивание завершено!')



# При возникновении проблемы с сертификатом Youtube используем библиотеку certifi
# Устанавливаем библиотеку, вводим команду /Applications/Python\ 3.9/Install\ Certificates.command
# В данной команде указываем версию Python, которая используется в данный момент


