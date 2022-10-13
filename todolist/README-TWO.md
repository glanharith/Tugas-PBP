Link: https://tugas-2-pbp-glan.herokuapp.com/todolist

Tugas 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

Asynchronous programming merupakan pendekatan pemrograman yang tidak terikat pada input atau ouput. Jadi, program tidak melakukan perkerjaannya dengan mengeksekusi baris program satu persatu secara hirarki.
Synchronous programming merupakan pendekatan pemrogram secara sequential. Jadi, program dieksekusi berdasarkan antrian yang duluan.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Event-Driven Programming adalah sebuah paradigma saat objek, kode, atau lainnya berkomunikasi secara tidak langsung seperti memberi pesan dari satu ke lainnya. Salah satu contoh pada tugas ini adalah penerapan tombol add menggunakan JS. Saat tombol tersebut ditekan, html akan memberi signal ke JS untuk melakukan tugas atau functionnya

3. Jelaskan penerapan asynchronous programming pada AJAX
Penulisan kode untuk AJAX berupa function-function. Sama seperti di bahasa lainnya jika kita membuat sebuah function lalu kita call function tersebut, maka kode akan mengarah ke function tersebut bukan melanjutkan kode di baris setelahnya.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Pertama, saya membuat views baru bernama show_json untuk implementasi AJAX get. Lalu, saya import JS dan AJAX. Setelah itu, saya membuat function GET menggunakan AJAX untuk mengambil data yang nanti akan diinput user. Lalu, saya mengedit kode html saya, seperti menghilangkan pengambilan data dari views dan menambahkan fitur modal menggunakan bootstrap. Di dalam modal saya menambahkan fitur form untuk data yang didapatkan bisa digunakan saat melakukan POST. Setelah itu, saya membuat function POS.Sebelumnya saya menambahkan views bernama post_json untuk menyambungkan json ke htmlnya. Fungsi POST ini memanggil function GET untuk menyimpan atau menerima data yang sudah diinpu user. Setelah itu saya mengerjakan soal Bonus, yaitu menambahkan fitur delete menggunakan AJAX. Saya mengedit delete_task yang pada tugas sebelumnya sudah dibuat tanpa implementasi AJAX. Setelah itu, saya membuat function DELETE. Implementasinya adalah saat GET dijalankan saya membuat id berdasarkan pk dari json untuk setiap card. Jadi, saat DELETE dilakukan saya tinggal mengakses id cardnya lalu menggunakan method remove pada JS.
