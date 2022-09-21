Link aplikasi Heroku: https://tugas-2-pbp-glan.herokuapp.com/katalog/ 

**1. Bagan _request client_ ke web aplikasi Django** 
![Gambar Bagan Tugas 2](https://user-images.githubusercontent.com/112403421/189969418-930c7d5d-5a91-4bc9-b96d-d2abfe239fe2.JPG)

Pertama, saat membuka web menggunakan link atau URL yang tersedia, terkirim request untuk mengisi konten dari halaman web yang sudah dibuat ke internet atau ke launchernya (Heroku). Setelah itu request dilanjutkan ke host atau database yang sudah di buat, dalam kasus tugas 2 ini ke settings.py. Setelah request diterima, URLS.py yang utama (di dalam folder project_django) akan mengakses views.py. Views.py berguna untuk menghubungkan models.py dengan file html-nya. Models.py berisi pelengkap atau data yang nanti akan di gabungkan di html. Setelah itu, file html akan diterima launcher menjadi Web dengan tampilan sesuai dengan kode yang ada di file html dan lalu akan ditampilkan di device user yang membuka web.

**2._Virtual Enviroment_**
Kita masih dapat membuat aplikasi web tanpa menggunakan _virtual enviroment_, tetapi terdapat kekurangannya juga, seperti saat kita ingin membuat proyek aplikasi menggunakan django 1.1. Aplikasi dapat berjalan dengan sempurna dengan menggunakan modul versi 1.1. Lalu, misalkan terdapat versi baru daru django 2.0 dan kita upgrade modul django kita. Aplikasi yang sudah kita buat tidak bisa berjalan dengan modul versi baru ini, karena banyak perubahan fungsi dan lain-lain sesuai updatenya. Aplikasi kita hanya dapat berjalan lancar dengan menggunakan django versi 1.1. Oleh karena itu, kita membutuhkan _virtual enviroment_ agar masing-masing aplikasi memiliki modulnya sendiri.

**3.Implementasi Poin-Poin**
Untuk poin pertama, saya membuat views.py dengan kode dari tutorial 1 dan sedikit penyesuaian. Setelah isi konten web sesuai dengan yang saya inginkan (models.py, views.py, html file), saya menyesuaikan isi urls.py dalam folder katalog untuk routing ke views.py. Saya juga menambahkan _path_ menuju folder katalog di urls.py yang ada di dalam folder project_django. Setelah itu, saya push ke github saya dan melakukan deployment dari git ke heroku. 
