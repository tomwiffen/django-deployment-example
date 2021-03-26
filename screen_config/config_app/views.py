from django.shortcuts import render
from config_app.forms import NewPanelForm, NewScreenForm
from config_app.models import Screen

# Create your views here.
def index(request):
    screens_list = Screen.objects.order_by('screen_name')
    screen_dict = {'screens_list': screens_list}
    return render(request,'config_app/index.html', context=screen_dict)


def new_panel(request):
    registered = False
    if request.method == "POST":
        new_panel_form = NewPanelForm(data=request.POST)

        if new_panel_form.is_valid():

            panel = new_panel_form.save()

            registered = True

        else:
            print(new_panel_form.errors)

    else:
        new_panel_form = NewPanelForm()

    return render(request,'config_app/new_panel.html',
                            {'new_panel_form':new_panel_form,
                                'registered':registered})

def new_screen(request):
    registered = False
    if request.method == "POST":
        new_screen_form = NewScreenForm(data=request.POST)

        if new_screen_form.is_valid():

            screen = new_screen_form.save()

            registered = True

        else:
            print(new_screen_form.errors)

    else:
        new_screen_form = NewScreenForm()

    return render(request,'config_app/new_screen.html',
                            {'new_screen_form':new_screen_form,
                                'registered':registered})
