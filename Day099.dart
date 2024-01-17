void main() {
  String? stringMungkinNull;
  String stringTidakNull = stringMungkinNull ?? 'halooo';

  print('String Setelah Konversi: $stringTidakNull');
}
