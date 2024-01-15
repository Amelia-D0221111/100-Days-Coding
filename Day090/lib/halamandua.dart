import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class HalamanDua extends StatelessWidget {
  const HalamanDua({super.key});

  @override
  Widget build(BuildContext context) {
    var dbRef = FirebaseFirestore.instance.collection('gambar');
    Stream<List<Map>> read() {
      final data = dbRef.snapshots();
      var result = data.map((event) {
        return event.docs.map((e) {
          Map<String, dynamic> data = e.data();
          data.addEntries({"key": e.id}.entries);
          return data;
        }).toList();
      });

      return result;
    }

    return Scaffold(
      body: Container(
        color: const Color.fromARGB(255, 212, 117, 149),
        child: Container(
          decoration: const BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.only(
              topLeft: Radius.circular(30),
              topRight: Radius.circular(30),
            ),
          ),
          child: SingleChildScrollView(
            child: StreamBuilder(
                stream: read(),
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const CircularProgressIndicator();
                  }
                  final data1 = snapshot.data!
                      .firstWhere((element) => element["category"] == "0");

                  var data2 = {};
                  try {
                    data2 = snapshot.data!
                        .firstWhere((element) => element["category"] == "1");
                  } catch (e) {}
                  return Padding(
                    padding: const EdgeInsets.all(10.0),
                    child: Column(
                      children: [
                        Container(
                          height: 140,
                          width: double.infinity,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(99),
                            image: DecorationImage(
                                image: NetworkImage(data1["url"]),
                                fit: BoxFit.cover),
                          ),
                          child: Container(
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(99),
                              color: Colors.black45,
                            ),
                            child: Center(
                              child: Text(
                                "FLOWERS",
                                style: TextStyle(
                                  fontSize: 24,
                                  fontWeight: FontWeight.w600,
                                  color: Colors.white,
                                ),
                              ),
                            ),
                          ),
                        ),
                        SizedBox(
                          height: 10.0,
                        ),
                        Container(
                          height: 140,
                          width: double.infinity,
                          decoration: BoxDecoration(
                            color: Colors.grey[300],
                            borderRadius: BorderRadius.circular(99),
                            image: data2.isEmpty
                                ? null
                                : DecorationImage(
                                    image: NetworkImage(data2["url"]),
                                    fit: BoxFit.cover),
                          ),
                          child: Container(
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(99),
                              color: Colors.black45,
                            ),
                            child: Center(
                              child: Text(
                                "ANIMALS",
                                style: TextStyle(
                                  fontSize: 24,
                                  fontWeight: FontWeight.w600,
                                  color: Colors.white,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  );
                }),
          ),
        ),
      ),
    );
  }
}
