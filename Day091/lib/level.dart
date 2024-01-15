import 'package:flutter/material.dart';
import 'package:game/berhasil.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LevelScreen extends StatefulWidget {
  const LevelScreen({super.key});

  @override
  State<LevelScreen> createState() => _LevelScreenState();
}

class _LevelScreenState extends State<LevelScreen> {
  var indexSekarng = 0;
  var skor = 0;
  int salah = 0;
  final List<Map<String, dynamic>> level = [
    {
      "jumlah_bola": 6,
      "pembagi": 3,
      "index_benar": 2,
      "warna": const Color(0xFFCE0067),
      "warna_benar": const Color(0xFFCC6566),
    },
    {
      "jumlah_bola": 6,
      "pembagi": 3,
      "index_benar": 3,
      "warna": const Color(0xFF009900),
      "warna_benar": const Color(0xFF669934),
    },
    {
      "jumlah_bola": 9,
      "pembagi": 3,
      "index_benar": 3,
      "warna": const Color(0xFFC18319),
      "warna_benar": const Color(0xFF97CC2D),
    },
    {
      "jumlah_bola": 9,
      "pembagi": 3,
      "index_benar": 2,
      "warna": const Color(0xFF41A67C),
      "warna_benar": const Color(0xFF3D9563),
    },
    {
      "jumlah_bola": 9,
      "pembagi": 3,
      "index_benar": 7,
      "warna": const Color(0xFFC29C91),
      "warna_benar": const Color(0xFF3D9563),
    },
    {
      "jumlah_bola": 9,
      "pembagi": 3,
      "index_benar": 2,
      "warna": Color.fromARGB(255, 202, 89, 177),
      "warna_benar": const Color(0xFF3D9563),
    },
    {
      "jumlah_bola": 9,
      "pembagi": 3,
      "index_benar": 7,
      "warna": Color.fromARGB(255, 200, 172, 49),
      "warna_benar": const Color(0xFF3D9563),
    },
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: const Text(
          "Color Master",
          style: TextStyle(
            fontFamily: "MotleyForces",
            fontSize: 35,
          ),
        ),
        backgroundColor: const Color(0xFFFF7D7D),
        foregroundColor: Colors.white,
        toolbarHeight: 80,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
            bottomLeft: Radius.circular(20),
            bottomRight: Radius.circular(20),
          ),
        ),
        actions: [
          Row(
            children: [
              Icon(
                Icons.favorite,
                size: 28,
                color: salah >= 3
                    ? Colors.white
                    : Colors.red.withBlue(0).withGreen(0),
              ),
              Icon(
                Icons.favorite,
                size: 28,
                color: salah >= 2
                    ? Colors.white
                    : Colors.red.withBlue(0).withGreen(0),
              ),
              Icon(
                Icons.favorite,
                size: 28,
                color: salah >= 1
                    ? Colors.white
                    : Colors.red.withBlue(0).withGreen(0),
              ),
              const SizedBox(
                width: 15.0,
              )
            ],
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          children: [
            Row(
              children: [
                Text(
                  "Level ${indexSekarng + 1}",
                  style: const TextStyle(
                    fontFamily: "MotleyForces",
                    fontSize: 24,
                    color: Color(0xFFFF7D7D),
                  ),
                ),
                const Spacer(),
                Text(
                  "Score: $skor",
                  style: const TextStyle(
                    fontFamily: "MotleyForces",
                    fontSize: 24,
                    color: Color(0xFFFF7D7D),
                  ),
                ),
              ],
            ),
            const SizedBox(
              height: 60.0,
            ),
            Expanded(
              child: SizedBox(
                width: double.infinity,
                child: GridView.count(
                  shrinkWrap: true,
                  crossAxisCount: level[indexSekarng]["pembagi"],
                  mainAxisSpacing: 10.0,
                  crossAxisSpacing: 10.0,
                  children: List.generate(
                    level[indexSekarng]["jumlah_bola"] as int,
                    (index) {
                      final warna = level[indexSekarng]["warna"] as Color;
                      return InkWell(
                        borderRadius: BorderRadius.circular(
                          99,
                        ),
                        onTap: index == level[indexSekarng]["index_benar"]
                            ? () async {
                                if (indexSekarng == (level.length - 1)) {
                                  final prefs =
                                      await SharedPreferences.getInstance();

                                  int skorTertinggi =
                                      prefs.getInt('skor-tertinggi') ?? 0;

                                  if ((skor + 10) > skorTertinggi) {
                                    await prefs.setInt(
                                      'skor-tertinggi',
                                      (skor + 10).toInt(),
                                    );
                                  }
                                  if (context.mounted) {
                                    Navigator.of(context).pop();
                                    Navigator.of(context).push(
                                      MaterialPageRoute(
                                        builder: (context) => BerhasilScreen(
                                          skor: (skor + 10).toString(),
                                        ),
                                      ),
                                    );
                                  }
                                } else {
                                  setState(() {
                                    indexSekarng += 1;
                                    skor += 10;
                                  });
                                }
                              }
                            : () async {
                                setState(() {
                                  salah += 1;
                                });
                                if (salah == 3) {
                                  final prefs =
                                      await SharedPreferences.getInstance();

                                  int skorTertinggi =
                                      prefs.getInt('skor-tertinggi') ?? 0;

                                  if ((skor) > skorTertinggi) {
                                    await prefs.setInt(
                                      'skor-tertinggi',
                                      (skor).toInt(),
                                    );
                                  }
                                  if (context.mounted) {
                                    Navigator.of(context).pop();
                                    Navigator.of(context).push(
                                      MaterialPageRoute(
                                        builder: (context) => BerhasilScreen(
                                          skor: (skor).toString(),
                                        ),
                                      ),
                                    );
                                  }
                                } else {
                                  if ((skor - 5) <= 0) {
                                    setState(() {
                                      skor = 0;
                                    });
                                  } else {
                                    setState(
                                      () {
                                        skor -= 5;
                                      },
                                    );
                                  }
                                }
                              },
                        child: Container(
                          height: 30,
                          width: 30,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: index == level[indexSekarng]["index_benar"]
                                ? warna.withOpacity(
                                    (indexSekarng + 1) / (level.length + 1))
                                : warna,
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
