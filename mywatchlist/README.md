 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
        -JSON atau JavaScript Object Notation. JSON merupakan suatu format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna.
        -XML atau extensible markup language. XML digunakan untuk membuat format informasi umum serta menjadi sarana untuk membagikan format dan data yang digunakan di World Wide Web, intranet, dan di platform lain yang menggunakan teks ASCII standar.
        -HTML atau HyperText Markup Language. suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar
2.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Dalam pengembangan suatu platform kita membutuhkan pengiriman data dari suatu stack ke stack lainnya. Data yang dikirim bisa berupa HTML, XML, dan JSON. 

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
    Dalam tugas 3 ini, pertama saya menyiapkan aplikasi dengan mendaftarkan aplikasi yang saya ingin buat ke settings.py pada variable INSTALLED_APPS. Lalu, saya menyiapkan data-data yang dibutuhkan untuk melengkapi konten yang akan ditampilkan di web, entah dalam bentuk json, xml, atau html. Setelah itu saya membuat template berupa nama_aplikasi.html yang berisikan konten yang akan ditampilkan menggunakan html dan membuat file initial_namaapp_data.json untuk menampilkan konten/data menggunakan json atau xml. Lalu,saya membuat views.py pada folder mywatchlist. Setelah itu, saya merangkai views.py untuk dapat menerima request dan memberi respons, seperti xml,json, atau html. Setelah itu, saya membuat urls.py pada folder mywatchlist dan membuat urls untuk menyambungkan request dari web ke views.py. 
    
   
   
Screenshot Postman:
1. HTML
    ![image](https://user-images.githubusercontent.com/112403421/191532938-470500b1-282f-4d95-95a3-4863c2988274.png)
2. json
    ![image](https://user-images.githubusercontent.com/112403421/191533133-55201dc3-d76d-46f4-ac40-c4c976207af8.png)
3. XML
    ![image](https://user-images.githubusercontent.com/112403421/191533154-51d36d12-580f-43c8-8001-8ab1ca62b885.png)

    
