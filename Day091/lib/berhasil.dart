import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class BerhasilScreen extends StatelessWidget {
  const BerhasilScreen({super.key, required this.skor});
  final String skor;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: const Text(
          "Color Master",
          style: TextStyle(fontFamily: "MotleyForces", fontSize: 35),
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
      ),
      body: Center(
        child: Container(
          height: MediaQuery.of(context).size.height,
          width: MediaQuery.of(context).size.width,
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [
                Color(0xFFFF7D7D),
                Colors.white,
                Colors.white,
                Color(0xFFFF7D7D),
              ],
            ),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Text(
                'Skor: $skor',
                style: const TextStyle(
                  fontFamily: "MotleyForces",
                  fontSize: 40,
                  color: Color(0xFFFF7D7D),
                ),
              ),
              FutureBuilder(
                future: SharedPreferences.getInstance(),
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const SizedBox(
                      height: 24,
                      width: 24,
                      child: CircularProgressIndicator(
                        color: Color(0xFFFF7D7D),
                      ),
                    );
                  }

                  final data = snapshot.data!;

                  return Text(
                    'Skor Tertinggi: ${data.getInt('skor-tertinggi') ?? 0}',
                    style: const TextStyle(
                      fontFamily: "MotleyForces",
                      fontSize: 24,
                      color: Color(0xFFFF7D7D),
                    ),
                  );
                },
              ),
              const SizedBox(
                height: 40.0,
              ),
              ElevatedButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                style: ElevatedButton.styleFrom(
                  textStyle: const TextStyle(
                    fontFamily: "MotleyForces",
                    fontSize: 40,
                  ),
                  backgroundColor: const Color(0xFFFF7D7D),
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                ),
                child: const Text(
                  "Back",
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
