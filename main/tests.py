from django.test import TestCase, Client
from django.test import LiveServerTestCase, TestCase, tag
from django.urls import reverse
from selenium import webdriver

#Create your tests here.
class MainTestCase(TestCase):
    def test_eksistensi_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # You can also use path names instead of explicit paths.
        response = self.client.get(reverse('main:main'))
        self.assertEqual(response.status_code, 200)

    def test_eksistensi_template(self):
        response = Client().get('/')
        html_response = response.content.decode('utf8')
        self.assertIn("Cita-cita", html_response)
        self.assertIn("Kesibukan yang saat ini saya jalani", html_response)
        self.assertIn("Pengalaman saya selama ini", html_response)
        self.assertIn("Fun fact tentang saya", html_response)

    def test_eksistensi_tombol(self):
        response = Client().get('/')
        html_response = response.content.decode('utf8')
        self.assertIn("+", html_response)
        self.assertIn("-", html_response)

    def test_slide(self):
        response = Client().get('/')
        html_response = response.content.decode('utf8')
        self.assertIn("Hai namaku James.", html_response)
        self.assertIn("Kotak yang ada di sebelah kiri bisa kalian naik turunkan posisinya sesuka hati kalian.", html_response)
        self.assertIn("Kalian bisa mendapatkan beberapa fakta menarik tentang saya disini.", html_response)