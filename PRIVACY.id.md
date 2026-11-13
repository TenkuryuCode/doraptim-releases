# Kebijakan Privasi

Terakhir diperbarui: 14 November 2026

Engine, extension browser, aplikasi desktop, dan installer DoRaptim berjalan sepenuhnya di komputer pengguna sendiri. Komponen tersebut tidak mengirim telemetri atau analitik kepada Tenkuryu Code dan tidak memiliki layanan akun maupun proxy unduhan terpusat. Website publik DoRaptim dapat memakai Google Analytics untuk mengukur penggunaan website secara agregat.

Halaman ini mencakup engine, extension browser, aplikasi desktop, dan installer.

## Website publik

Website publik DoRaptim memuat Google Analytics 4 pada build produksi. Google Analytics dapat memakai cookie atau penyimpanan browser serupa serta mengumpulkan kunjungan halaman, interaksi, perkiraan informasi geografis, informasi perangkat dan browser, dan informasi perujuk. Data tersebut dikirim kepada Google dan digunakan untuk memahami penggunaan website. Data tersebut tidak dipakai untuk mengidentifikasi atau menggabungkan pengunjung website dengan unduhan yang dilakukan melalui engine atau extension browser. Jangan memasukkan kredensial atau URL unduhan sensitif pada website.

## Apa yang ditangani oleh extension

Extension mengambil alih unduhan yang dimulai oleh browser apabila unduhan tersebut menggunakan protokol HTTP atau HTTPS, tidak berasal dari jendela penyamaran (incognito/private) maupun dari extension lain, serta berukuran minimal 1 MiB atau berukuran belum diketahui; batas ukuran minimum ini dapat diubah di pengaturan. Untuk unduhan semacam itu, extension meneruskan informasi berikut ke engine melalui Chrome native messaging, yaitu saluran komunikasi lokal ke program di komputer yang sama:

- alamat URL unduhan beserta hasil pengalihannya (redirect);
- nama berkas yang disarankan;
- alamat perujuk (referrer) dan teks user-agent browser.

Extension tidak membaca atau mengirimkan kata sandi, riwayat penjelajahan umum, atau isi halaman di luar kebutuhan unduhan, dan tidak meminta izin akses situs (host permission) saat pertama kali dipasang. Pengaturannya (apakah pengambilalihan otomatis aktif, ukuran berkas minimum, apakah berkas dinamai mengikuti judul halaman, notifikasi, dan apakah pencarian video otomatis diaktifkan) disimpan di penyimpanan lokal extension Chrome pada perangkat Anda.

Fitur penamaan berkas berdasarkan judul halaman nonaktif secara bawaan. Ketika pengguna mengaktifkannya, Chrome meminta izin `tabs`, yang memungkinkan extension membaca judul dan alamat tab yang terbuka. Extension menggunakannya hanya ketika unduhan yang ditangkap memiliki nama berkas yang tidak bermakna, semata-mata untuk membaca judul halaman asal unduhan dan menyarankan nama yang lebih jelas di jendela pratinjau. Judul tersebut hanya disimpan di memori browser hingga jendela pratinjau ditutup; hanya nama berkas yang dikonfirmasi oleh pengguna yang diteruskan ke engine. Menonaktifkan pengaturan ini akan mengembalikan izin tersebut.

Pencarian video bekerja dalam dua cara. **Find videos** (dan **Find images**) di dalam popup memeriksa halaman yang sedang dibuka pengguna hanya ketika tombol tersebut diklik, termasuk bingkai pemutar video tertanam (embedded player frame) yang dapat dibaca oleh extension. **Find videos automatically** (pencarian video otomatis), yang nonaktif secara bawaan, melakukan hal serupa pada setiap halaman—termasuk halaman yang sudah terbuka saat fitur diaktifkan—agar tombol unduh dapat muncul langsung di atas video; mengaktifkannya akan meminta izin akses ke seluruh situs pada Chrome, dan menonaktifkannya akan mencabut izin tersebut kembali. Dalam kedua cara tersebut, extension membaca di dalam halaman: alamat video dan audio, tautan ke berkas media, berkas takarir (subtitle) beserta label dan bahasanya, serta alamat berkas yang dimuat oleh pemutar halaman (untuk pemutar yang mengambil jalur video dan audio secara terpisah, alamat berkas utuhnya dihitung dari informasi tersebut). Ketika pengguna membuka menu tombol video untuk sebuah stream atau pemutar dengan video dan audio terpisah, alamat berkas-berkasnya dikirimkan ke engine lokal, yang kemudian menanyakan ukuran masing-masing berkas ke server asalnya (dan untuk berkas video, membaca 256 KiB pertama guna mengetahui resolusi gambar) sehingga menu dapat menampilkan daftar kualitas yang tersedia; tidak ada data yang disimpan pada tahap ini. Tombol di dalam bingkai pemutar tertanam juga menanyakan judul halaman utama kepada extension untuk ditampilkan di menu. Selain itu, tidak ada informasi yang keluar dari browser sampai pengguna memilih sebuah video: barulah alamatnya (atau alamat berkas video dan audionya), alamat beserta label dan bahasa takarirnya, alamat halaman atau bingkai pemutar sebagai perujuk (referrer), judul halaman (sebagai saran nama berkas), serta durasi dan kualitas video (yang ditampilkan di pratinjau) diteruskan ke engine atau disimpan sementara di memori browser sebagaimana unduhan lainnya. Menu klik kanan **Download with DoRaptim** menyerahkan tautan atau media yang diklik pengguna dengan cara yang sama.

## Apa yang disimpan oleh engine

Engine dapat memproses dan menyimpan informasi berikut di dalam jurnal SQLite lokal pada perangkat Anda:

- alamat URL sumber dan hasil pengalihannya (redirect);
- metadata opsional berupa perujuk (referrer) dan user-agent yang diberikan oleh klien lokal;
- metadata respons server seperti nama berkas, ukuran, jenis konten (content type), ETag, dan Last-Modified;
- status antrean, progres segmen, status percobaan ulang (retry), kategori folder tujuan, dan catatan kesalahan;
- nilai checksum SHA-256 yang diharapkan maupun yang telah dihitung;
- untuk stream atau video dengan audio terpisah: alamat dari pilihan kualitas yang tersedia, alamat berkas audionya, serta alamat takarir (subtitle) yang disertakan beserta label dan bahasanya;
- folder unduhan utama dan nama subfolder kategori yang dipilih pengguna, folder khusus yang dipilih untuk satu unduhan tertentu, serta jumlah unduhan paralel dan batas kecepatan yang diatur pengguna;
- jam unduh yang diatur pengguna (hari dan jam lokal) serta apakah pengaturan "Wi‑Fi or cable only" aktif.

Jurnal lokal dapat memuat URL yang bersifat sensitif karena sebagian situs menyertakan token sementara di dalam URL unduhan. Lindungi jurnal tersebut dengan izin akun sistem operasi Anda dan jangan membagikannya kepada pihak lain. Nilai perujuk (referrer) dan user-agent hanya digunakan selama proses pengunduhan dan tidak ditulis secara permanen ke dalam jurnal. Daemon lokal juga menyimpan berkas privat berisi token akses acak yang diganti setiap kali layanan dimulai ulang.

Ketika sebuah unduhan selesai, engine memberi berkas tersebut tanda "berasal dari internet" milik sistem operasi, seperti yang dilakukan browser: atribut `com.apple.quarantine` di macOS dan stream `Zone.Identifier` di Windows. Tanda itu hanya memuat waktu dan nama DoRaptim, atau zona internet; tanda itu tidak pernah memuat alamat maupun halaman asal berkas.

## Aktivitas jaringan

Engine hanya terhubung ke sumber unduhan yang diminta oleh pengguna atau klien lokal, termasuk pengalihan (redirect) yang diperlukan oleh sumber tersebut serta, untuk video yang dipilih pengguna, potongan segmen stream-nya, berkas audio terpisahnya, dan berkas takarir yang dicentang pengguna. Engine tidak pernah menghubungi server milik Tenkuryu Code untuk proses pengunduhan. Pemeriksaan versi engine terbaru hanya membaca berkas `latest.json` bertanda tangan kriptografi dari repositori rilis publik `doraptim-releases` (`raw.githubusercontent.com`). Permintaan tersebut hanya membawa nomor versi program pada header User-Agent dan sama sekali tidak memuat informasi tentang pengguna maupun daftar unduhannya. Perintah `doraptim update` atau tombol pemeriksa pembaruan di aplikasi desktop menjalankan pemeriksaan ini saat diminta pengguna. Pengaturan opsional yang nonaktif secara bawaan memungkinkan engine memeriksa pembaruan maksimal satu kali sehari, dan dapat dimatikan kapan saja melalui halaman Pengaturan (Settings).

Ketika pengaturan "Wi‑Fi or cable only" aktif, engine menanyakan kepada sistem operasi jenis koneksi yang sedang dipakai komputer, kira-kira setiap 30 detik: di macOS, port jaringan dari rute bawaan (misalnya Wi‑Fi, Ethernet, atau iPhone lewat USB); di Windows, apakah Windows menganggap koneksi tersebut terukur (metered). Ini hanya pertanyaan kepada komputer itu sendiri: tidak ada data yang dikirim melalui jaringan untuk keperluan ini, dan jawabannya hanya disimpan di memori engine, tidak di dalam jurnal. Jika pengaturan tersebut nonaktif, engine tidak menanyakannya sama sekali.

Ketika pengguna memasukkan alamat halaman web (bukan alamat berkas langsung), engine atau extension membuka dan memeriksa halaman tersebut langsung dari perangkat pengguna sendiri, sehingga halaman beserta medianya mengalir langsung dari situs web sumber ke perangkat Anda. Tenkuryu Code tidak mengoperasikan server perantara untuk fitur ini dan tidak pernah menerima alamat tautan, isi halaman, maupun berkas yang diunduh. Alamat dan status unduhan hanya disimpan di dalam jurnal lokal pada perangkat Anda. Jurnal tersebut tidak dienkripsi; lindungi dengan pengaturan izin akun pada sistem operasi Anda.

## Antarmuka lokal

Daemon mengikat koneksi hanya pada alamat loopback lokal (`127.0.0.1`), mewajibkan token otorisasi (bearer token), serta memeriksa informasi host dan origin pada setiap permintaan. Komunikasi native messaging menggunakan pipa proses lokal (local process pipes). Installer mendaftarkan native-messaging host hanya untuk pengguna saat ini dan khusus untuk ID extension resmi yang disertakan saat paket dibangun.

## Catatan log

Catatan log diagnostik dirancang agar tidak memuat kata sandi, nilai otorisasi, cookie, kunci rahasia, maupun URL lengkap yang mengandung kredensial.

## Kendali pengguna

Pengguna dapat menonaktifkan pengambilalihan unduhan otomatis pada extension, memilih direktori penyimpanan unduhan, menghapus riwayat antrean, dan menghapus berkas yang telah selesai diunduh. Mencopot pemasangan extension dan menjalankan `doraptim host uninstall` (atau mencopot aplikasi melalui uninstaller) akan menghapus integrasi browser. Menghapus berkas jurnal SQLite setelah daemon dihentikan akan membersihkan seluruh riwayat unduhan yang tersimpan di perangkat.

## Kontak

Pertanyaan tentang privasi: buka issue di repositori ini. Masalah keamanan: gunakan tab *Security*, *Report a vulnerability*, bukan issue publik.
