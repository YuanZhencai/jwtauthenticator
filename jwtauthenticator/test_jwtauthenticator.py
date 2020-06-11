from unittest import TestCase

from jose import jwt


class TestJSONWebTokenLoginHandler(TestCase):
  def test_parse_jwt(self):
    json_web_token = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ5dWFuemhlbmNhaSIsImF1dGgiOiJST0xFX1VTRVIiLCJleHAiOjE1OTAyMjk5NTJ9.PcI6wGxXew-AASYqCKneUyW4ZUVHosgfE0qkWh0Y5pB4nNr1kneSC8yt8liJ31TSjhzt2VVAgyoYnci-_R-Wfw'
    secret = 'b939fce9c8879b8d41886695da17c363a0004bf7'
    data = jwt.decode(json_web_token, secret, 'HS512', options={ 'verify_signature': False})
    self.assertIsNotNone(data)


