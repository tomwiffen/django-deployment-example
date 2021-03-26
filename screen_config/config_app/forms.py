from django import forms
from django.core import validators
from config_app.models import LedPanel, Screen

class NewPanelForm(forms.ModelForm):
    class Meta():
        model = LedPanel
        fields = ("panel_name", "panel_width", "panel_height", "panel_pixel_width", "panel_pixel_height", "panel_curent_draw")


class NewScreenForm(forms.ModelForm):
    class Meta():
        model = Screen
        fields = ("screen_name","panel","panels_wide","panels_high","refresh_rate")
