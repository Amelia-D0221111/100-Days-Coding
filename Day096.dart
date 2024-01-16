import 'dart:io';

void main() {
  String nama = getInputNama();
  print("Nama saya adalah $nama");
}

String getInputNama() {
  stdout.write("Masukkan Nama : ");
  return stdin.readLineSync()!;
}
