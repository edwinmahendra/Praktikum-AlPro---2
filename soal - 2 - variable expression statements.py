#Edwin Mahendra / 71200541

#referensi: https://www.cermati.com/artikel/bunga-kredit-jenis-dan-cara-perhitungannya

#Andi ingin membeli iphone 13 dengan internal memory sebesar 256gb
#seharga 24.000.000
#namun karena ia hanya memiliki uang 11.000.000 maka ia akan melakukan pembayaran secara kredit
#pihak toko menawarkan kredit dengan bunga 18% per tahun yang bisa dicicil selama 9 bulan.
#hitunglah besar angsuran perbulan dan angsuran totalnya

#input
#harga iphone yang akan dibeli oleh Andi = 24.000.000 (int)
#uang muka yang dimiliki oleh Andi = 11.000.000 (int)
#bunga yang ditawarkan oleh pihak toko = 18% per tahun (float)
#lama cicilan yang ditawarkan oleh pihak toko = 9 bulan (int)

#proses
#bunga total = lama pinjaman * bunga * uang sisa (harga iphone - uang muka Andi)
#lama pinjaman = 9/12 
#angsuran total = bunga total + uang sisa
#angsuran_perbulan = angsuran total / lama cicilan

#output
#angsuran total dan angsuran perbulan

harga_iphone = int(input('Masukkan harga iPhone yang akan dibeli oleh Andi = '))
uang_muka = int(input('Masukkan uang muka yang dimiliki Andi = '))
bunga = float(input('Masukkan bunga yang ditawarkan oleh pihak toko = '))
lama_cicilan = int(input('Masukkan lama cicilan = '))

#rumus
lama = lama_cicilan / 12
uang_sisa = harga_iphone - uang_muka
bunga_total = lama * bunga * uang_sisa

angsuran_total = bunga_total + uang_sisa
angsuran_perbulan = angsuran_total / lama_cicilan

print('jadi angsuran perbulan yang harus dibayar oleh Andi adalah Rp%d,00 dan untuk angsuran total yang harus dibayar oleh Andi adalah Rp%d,00,'%(angsuran_perbulan,angsuran_total)) 
