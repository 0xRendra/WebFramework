from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages

# View untuk halaman index
def index(request):
    return render(request, 'webapp/index.html')

# View untuk halaman resume
def resume(request):
    return render(request, 'webapp/resume.html')

# View untuk halaman projects
def projects(request):
    return render(request, 'webapp/projects.html')

# View untuk halaman contact
def contact(request):
    if request.method == 'POST':
        # Tangkap data dari formulir
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Validasi data (optional, tergantung kebijakan validasi tambahan)
        if not name or not email or not phone or not message:
            messages.error(request, 'Semua field harus diisi.')
            return redirect('contact')

        # Simpan data ke database menggunakan model Contact
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        # Berikan pesan sukses
        messages.success(request, 'Pesan kamu telah berhasil dikirim!')
        return redirect('contact')
    
    # Jika request GET, tampilkan halaman contact dengan formulir kosong
    return render(request, 'webapp/contact.html')
