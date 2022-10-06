Link: https://tugas-2-pbp-glan.herokuapp.com/todolist
Tugas 4 PBP:

1. Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

Kegunaan csrf_token adalah sebagai authenticator. Jadi saat kita login, csrf berkerja dengan memberikan dua token untuk user dan request. Kedua token tersebut akan masukan ke web, lalu akan dibandingkan. Jika tidak sesuai, maka request untuk ke web tersebut ditolak.Apabila tidak ada csrf_token tidak ada maka web kita mudah untuk diserang (cyber attack) dengan teknik Cross Site Request Forgery yaitu mengeksekusi perintah yang seharusnya tidak diizinkan, tetapi output yang dihasilkan sesuai dengan yang seharusnya.

2. Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.

Ya, kita bisa membuat elemen form secara manual. Kita dapat menggunakan POST pada elemen form. Kita perlu menggunakan POST terlebih dahulu untuk menginisiasi elemen form. Lalu, kita dapat membuat table dan mengisi table dengan request.POST.get({nama id input})


3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Data yang telah dimasukan oleh user akan dikirimkan ke database dan dapat kita akses menggunakan request.POST.get({nama id input}). Data yang sudah diinput dan tersimpan akan disesuaikan dengan models.py. Data yang sudah masuk tadi disimpan juga ke databse Django dan dapat diakses menggunakan {nama models}.Objects.filter(user=request.user) untuk dipakai dan difilter berdasarkan user yang masuk kedalam context di views.py dan akan di tampilkan ke html. Akhirnya akan ditampilkan kontennya di web.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama, saya membuat file dengan nama todolist sesuai yang diarahkan. Lalu saya menyesuaikan isi folder tersebut dengan views.py, urls.py, dan models.py. Setelah saya membuat file tersebut, saya membuat folder template untuk tempat saya menyimpan file-file html yang nanti akan ditampilkan. Lalu, saya membuat fungsi di views.py untuk login, logout, register, menambahkan perkerjaan, dan menampilkannya. Setelah itu, saya membuat routing agar dapat menerima request di urls.py. Tidak lupa, untuk membuat atau mempersiapkan models.py untuk mengisi html saat di request. Agar web yang dibuat terjaga, saat sebelum masuk ke web, user diminta untuk login. Untuk menghandle ini, saya menggunakan @login_required(login_url='/login/'). Lalu yang terakhir, saya mengedit web saya sesuai dengan keinginan saya di file htmlnya dengan bantuan css(style). git, add, commit, dan mendeploy ke heroku

Tugas 5 PBP:
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline adalah kode yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, lalu akan ditulis inlinenya di style tersebut.
Kelebihan: Sangat membantu ketika ingin menguji atau meilhat progres, mudah di debug, proses permintaan HTTP yang lebih kecil dan load website akan lebih cepat.
Kekurangan: Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

Internal adalah kode yang ditulis didalam tag<style> dan dalam kode HTML dituliskan di bagian header file HTML.
Kelebihan: Perubahan pada Internal CSS hanya berlaku pada satu halaman saja, Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file, Class dan ID bisa digunakan oleh internal stylesheet.
Kekurangan: Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file,Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.

Eksternal adalah kode yang ditulis terpisah dengan kode HTML. Jadi, kode CSS akan ditulis di sebuah file khusus yang berekstensi CSS. File eksternal CSS ini biasanya diletakan setelah bagian head pada halaman HTML.
Kelebihan:Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
Kekurangan:Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

2. Jelaskan tag HTML5 yang kamu ketahui
<div> = Merepresentasikan container/section.
<a> = Mendefinisikan hyperlink.
<head> = Mendefinisikan head dari dokumen HTML, biasanya berisi title.
<h1> to <h6> = Mendefinisikan ukuran heading HTML.
<title> = Mendefinsikan title dari dokumen HTML.
<body> = Mendefinisikan body dari dokumen HTML.
<link> = Mendefinisikan hubungan antara dokumen HTML dengan dokumen external.
<meta> = Menyediakan metadata terstruktur mengenai konten dokumen.

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui
Selektor Tag: Selektor ini akan memilih elemen berdasarkan nama tag
Selektor Class: Selektor yang memilih elemen berdasarkan nama class yang diberikan
Selektor Id: Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja
Selektor Atribut: Selektor yang memilik elemen berdasarkan atribut
Selektor Universal: Selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu
Selektor Pseudo: Selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Pertama saya me-import framework bootstrap ke kode HTML yang sudah dibuat (login.html,register.html, todolist.html, addtodolist.html) untuk memudahkan dalam mengubah atau styling HTML saya. Lalu, saya melakukan styling dengan cara internal (tidak membuat file baru). Saya mengubah warna background, padding, font dan lain-lainnya. Saya melakukan GSGS(Google Search) untuk mengetahui syntax dan kode yang dibutuhkan. Setelah, itu saya membuat card sesuai yang disuruh soal, dengan menggunakan kode bootstrap. setelah itu saya add, push, dan commut ke gitu lalu deploy.

