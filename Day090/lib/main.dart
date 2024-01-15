import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:pix_wallpaper/firebase_options.dart';
import 'package:pix_wallpaper/halamandua.dart';
import 'package:pix_wallpaper/halamansatu.dart';
import 'package:pix_wallpaper/halamantiga.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Pix Wallpaper',
      theme: ThemeData(
        useMaterial3: true,
      ),
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int indexTerpilih = 0;
  final listHalaman = [
    const HalamanSatu(),
    const HalamanDua(),
    const HalamanTiga()
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color.fromARGB(255, 212, 117, 149),
        foregroundColor: Colors.white,
        title: const Text(
          'Pix Wallpaper',
          style: TextStyle(fontWeight: FontWeight.w600),
        ),
        actions: [
          IconButton(onPressed: () {}, icon: const Icon(Icons.search)),
          IconButton(onPressed: () {}, icon: const Icon(Icons.more_vert))
        ],
      ),
      body: listHalaman[indexTerpilih],
      bottomNavigationBar: ClipRRect(
        borderRadius: const BorderRadius.only(
          topLeft: Radius.circular(30),
          topRight: Radius.circular(30),
        ),
        child: NavigationBar(
          indicatorColor: const Color.fromARGB(255, 179, 97, 124),
          selectedIndex: indexTerpilih,
          onDestinationSelected: (index) {
            setState(() {
              indexTerpilih = index;
            });
          },
          backgroundColor: const Color.fromARGB(255, 212, 117, 149),
          destinations: const [
            NavigationDestination(
              icon: Icon(Icons.wallpaper_outlined),
              selectedIcon: Icon(Icons.wallpaper),
              label: 'Wallpaper',
            ),
            NavigationDestination(
              icon: Icon(Icons.folder_outlined),
              selectedIcon: Icon(Icons.folder),
              label: 'Collections',
            ),
            NavigationDestination(
              icon: Icon(Icons.favorite_outline),
              selectedIcon: Icon(Icons.favorite),
              label: 'Favorites',
            ),
          ],
        ),
      ),
    );
  }
}
