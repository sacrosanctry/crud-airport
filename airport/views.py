from django.shortcuts import render, redirect
from airport.models import Passenger, Flight, Registration, Luggage, Interpol
from airport.forms import PassengerForm, FlightForm, RegistrationForm, LuggageForm, InterpolForm
# Create your views here.


def main(request):
    return render(request, "main.html")


# class Passenger
def passenger(request):
    passengers = Passenger.objects.all()
    return render(request, "passenger.html", {'passengers': passengers})


def add_passenger(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('passenger')
            except:
                pass
    else:
        form = PassengerForm()
    return render(request, "add_passenger.html", {'form': form})

# def add_passenger(request):
#     form = PassengerForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('passenger')
#     return render(request, "add_passenger.html", {'form': form})


def edit_passenger(request, id):
    passenger = Passenger.objects.get(id=id)
    return render(request, 'edit_passenger.html', {'passenger': passenger})


def update_passenger(request, id):
    passenger = Passenger.objects.get(id=id)
    form = PassengerForm(request.POST, instance=passenger)
    if form.is_valid():
        form.save()
        return redirect("passenger")
    context = {'passenger': passenger,
               'form': form}
    return render(request, 'edit_passenger.html', context)


def delete_passenger(request, id):
    passenger = Passenger.objects.get(id=id)
    passenger.delete()
    return redirect("passenger")


# class Flight
def flight(request):
    flights = Flight.objects.all()
    return render(request, "flight.html", {'flights': flights})


def add_flight(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('flight')
            except:
                pass
    else:
        form = FlightForm()
    return render(request, "add_flight.html", {'form': form})


def edit_flight(request, id):
    flight = Flight.objects.get(id=id)
    return render(request, 'edit_flight.html', {'flight': flight})


def update_flight(request, id):
    flight = Flight.objects.get(id=id)
    form = FlightForm(request.POST, instance=flight)
    if form.is_valid():
        form.save()
        return redirect("flight")
    return render(request, 'edit_flight.html', {'flight': flight})


def delete_flight(request, id):
    flight = Flight.objects.get(id=id)
    flight.delete()
    return redirect("flight")


# class Registration
def registration(request):
    registrations = Registration.objects.all()
    return render(request, "registration.html", {'registrations': registrations})


def add_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('registration')
            except:
                pass
    else:
        form = RegistrationForm()
    return render(request, "add_registration.html", {'form': form})


# def edit_registration(request, id):
#     registration = Registration.objects.get(id=id)
#     return render(request, 'add_registration.html', {'registration': registration})


# def update_registration(request, id):
#     registration = Registration.objects.get(id=id)
#     form = RegistrationForm(request.POST, instance=registration)
#     if form.is_valid():
#         form.save()
#         return redirect("registration")
#     return render(request, 'edit_registration.html', {'registration': registration})


# TODO registration_form.html is new edit_registration.html
# TODO we dont need edit_registration.html, edit_registration/<int:id>', views.edit_registration
def update_registration(request, id):
    registration = Registration.objects.get(id=id)
    form = RegistrationForm(instance=registration)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect("registration")
    context = {'form': form,
               'registration': registration}
    return render(request, 'registration_form.html', context)


def delete_registration(request, id):
    registration = Registration.objects.get(id=id)
    registration.delete()
    return redirect("registration")


# class Luggage
def luggage(request):
    luggages = Luggage.objects.all()
    return render(request, "luggage.html", {'luggages': luggages})


def add_luggage(request):
    if request.method == "POST":
        form = LuggageForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('luggage')
            except:
                pass
    else:
        form = LuggageForm()
    return render(request, "add_luggage.html", {'form': form})


# def edit_luggage(request, id):
#     luggage = Luggage.objects.get(id=id)
#     return render(request, 'edit_luggage.html', {'luggage': luggage})


# def update_luggage(request, id):
#     luggage = Luggage.objects.get(id=id)
#     form = LuggageForm(request.POST, instance=luggage)
#     if form.is_valid():
#         form.save()
#         return redirect("luggage")
#     return render(request, 'edit_luggage.html', {'luggage': luggage})


# TODO edit_luggage.html has better format than passenger and flight (old)
def update_luggage(request, id):
    luggage = Luggage.objects.get(id=id)
    form = LuggageForm(instance=luggage)
    if request.method == 'POST':
        form = LuggageForm(request.POST, instance=luggage)
        if form.is_valid():
            form.save()
            return redirect("luggage")
    context = {'form': form,
               'luggage': luggage}
    return render(request, 'edit_luggage.html', context)


def delete_luggage(request, id):
    luggage = Luggage.objects.get(id=id)
    luggage.delete()
    return redirect("luggage")


# class Interpol
def interpol(request):
    interpols = Interpol.objects.all()
    return render(request, "interpol.html", {'interpols': interpols})


def add_interpol(request):
    if request.method == "POST":
        form = InterpolForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('interpol')
            except:
                pass
    else:
        form = InterpolForm()
    return render(request, "add_interpol.html", {'form': form})


# def edit_interpol(request, id):
#     interpol = Interpol.objects.get(id=id)
#     return render(request, 'edit_interpol.html', {'interpol': interpol})


# def update_interpol(request, id):
#     interpol = Interpol.objects.get(id=id)
#     form = InterpolForm(request.POST, instance=interpol)
#     if form.is_valid():
#         form.save()
#         return redirect("interpol")
#     return render(request, 'edit_interpol.html', {'interpol': interpol})


# TODO new
def update_interpol(request, id):
    interpol = Interpol.objects.get(id=id)
    form = InterpolForm(instance=interpol)
    if request.method == 'POST':
        form = InterpolForm(request.POST, instance=interpol)
        if form.is_valid():
            form.save()
            return redirect("interpol")
    context = {'form': form,
               'interpol': interpol}
    return render(request, 'edit_interpol.html', context)


def delete_interpol(request, id):
    interpol = Interpol.objects.get(id=id)
    interpol.delete()
    return redirect("interpol")