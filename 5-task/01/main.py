# Здесь пиши программу
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
how_long_song = float(0)
long_song = int(input('Сколько песен выбрать? '))
for i in range(long_song):
    song_name = input('Введите название песни: ')
    how_long_song = violator_songs[song_name] + how_long_song
print(how_long_song)