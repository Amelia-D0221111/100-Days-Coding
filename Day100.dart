void main() {
  Map<String, dynamic> map1 = {'a': 1, 'b': 2, 'c': 3};
  Map<String, dynamic> map2 = {'d': 4, 'e': 5, 'f': 6};

  Map<String, dynamic> hasilGabungan = {...map1, ...map2};

  print('Hasil Gabungan Map: $hasilGabungan');
}
