1. Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

Kegunaan csrf_token adalah sebagai authenticator. Jadi saat kita login, csrf berkerja dengan memberikan dua token untuk user dan request. Kedua token tersebut akan masukan ke web, lalu akan dibandingkan. Jika tidak sesuai, maka request untuk ke web tersebut ditolak.Apabila tidak ada csrf_token tidak ada maka web kita mudah untuk diserang (cyber attack) dengan teknik Cross Site Request Forgery yaitu mengeksekusi perintah yang seharusnya tidak diizinkan, tetapi output yang dihasilkan sesuai dengan yang seharusnya.

2. Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.

Ya, kita bisa membuat elemen form secara manual. Kita dapat menggunakan POST pada elemen form. Kita perlu menggunakan POST terlebih dahulu untuk menginisiasi elemen form. Lalu, kita dapat membuat table dan mengisi table dengan request.POST.get({nama id input})


3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Data yang telah dimasukan oleh user akan dikirimkan ke database dan dapat kita akses menggunakan request.POST.get({nama id input}). Data yang sudah diinput dan tersimpan akan disesuaikan dengan models.py. Data yang sudah masuk tadi disimpan juga ke databse Django dan dapat diakses menggunakan {nama models}.Objects.filter(user=request.user) untuk dipakai dan difilter berdasarkan user yang masuk kedalam context di views.py dan akan di tampilkan ke html. Akhirnya akan ditampilkan kontennya di web.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya membuat file dengan nama todolist sesuai yang diarahkan. Lalu saya menyesuaikan isi folder tersebut dengan views.py, urls.py, dan models.py. Setelah saya membuat file tersebut, saya membuat folder template untuk tempat saya menyimpan file-file html yang nanti akan ditampilkan. Lalu, saya membuat fungsi di views.py untuk login, logout, register, menambahkan perkerjaan, dan menampilkannya. Setelah itu, saya membuat routing agar dapat menerima request di urls.py. Tidak lupa, untuk membuat atau mempersiapkan models.py untuk mengisi html saat di request. Agar web yang dibuat terjaga, saat sebelum masuk ke web, user diminta untuk login. Untuk menghandle ini, saya menggunakan @login_required(login_url='/login/'). Lalu yang terakhir, saya mengedit web saya sesuai dengan keinginan saya di file htmlnya dengan bantuan css(style). git, add, commit, dan mendeploy ke heroku

