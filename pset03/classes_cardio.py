# Programmer: Estella Moody

import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def circumference(self):
        return (self.radius * 2) * math.pi

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):

        print(f"Playing {self.title} by {self.artist} ({self.duration}s)")

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration}s)"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        if len(self.songs) > 0:
            return "|".join(str(song) for song in self.songs)
        else:
            return "Playlist is empty."


def test_rectangle():
    rect = Rectangle(3, 4)
    assert rect.area() == 12
    assert rect.perimeter() == 14
    assert str(rect) == "Rectangle(3 x 4)"


def test_circle():
    circle = Circle(5)
    assert circle.area() == 25*math.pi
    assert circle.circumference() == 10*math.pi
    assert str(circle) == "Circle(radius=5)"


def test_song(capfd):
    song = Song("Night Shift", "Lucy Dacus", 391)
    assert str(song) == "Night Shift by Lucy Dacus (391s)"
    song.play()
    captured_output = capfd.readouterr()
    assert captured_output.out == (
        "Playing Night Shift by Lucy Dacus (391s)\n"
    )


def test_playlist(capfd):
    playlist = Playlist()
    song1 = Song("Night Shift", "Lucy Dacus", 391)
    song2 = Song("I Was Neon", "Julia Jacklin", 243)
    song3 = Song("Forgiveness", "Alice Glass", 191)
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    assert str(playlist) == (
        "Night Shift by Lucy Dacus (391s)|"
        "I Was Neon by Julia Jacklin (243s)|"
        "Forgiveness by Alice Glass (191s)"
    )
    playlist.play_all()
    captured_output = capfd.readouterr()
    assert captured_output.out == (
        "Playing Night Shift by Lucy Dacus (391s)\n"
        "Playing I Was Neon by Julia Jacklin (243s)\n"
        "Playing Forgiveness by Alice Glass (191s)\n"
    )
