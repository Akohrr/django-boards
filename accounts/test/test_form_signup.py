from django.test import TestCase
from  ..forms import SignUpForm


class SignUpFormTest(TestCase):
    def test_form_had_finds(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)