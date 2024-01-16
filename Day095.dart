import 'dart:io';

void main() {
  stdout.write("Masukkan Nama : ");
  String nama = stdin.readLineSync()!;

  print("Nama saya adalah $nama");
}
