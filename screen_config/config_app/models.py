from django.db import models

# Create your models here.

class LedPanel(models.Model):
    panel_name = models.CharField(max_length=264, unique=True)
    panel_width = models.IntegerField()
    panel_height = models.IntegerField()
    panel_pixel_width = models.IntegerField()
    panel_pixel_height = models.IntegerField()
    panel_curent_draw = models.IntegerField()

    def __str__(self):
        return self.panel_name

    def panel_resolution(self):
        return self.panel_pixel_width * self.panel_pixel_height

class Screen(models.Model):
    screen_name = models.CharField(max_length=264, unique=True)
    panel = models.ForeignKey(LedPanel, on_delete = models.CASCADE)
    panels_wide = models.IntegerField()
    panels_high = models.IntegerField()
    refresh_rate = models.IntegerField()

    def __str__(self):
        return str(self.screen_name)

    @ property
    def screen_resolution(self):
        return (self.panel.panel_pixel_width * self.panels_wide, self.panel.panel_pixel_height * self.panels_high)

    @ property
    def screen_width(self):
        return str((self.panel.panel_width * self.panels_wide) / 1000) + "m"

    @ property
    def screen_height(self):
        return str((self.panel.panel_height * self.panels_high) / 1000) + "m"

    @ property
    def panels_per_string(self):
        if self.refresh_rate == 60:
            return 552960 / self.panel.panel_resolution()
        else:
            print("I'm sorry, this refresh rate is not supported by this applicaiton yet!")
