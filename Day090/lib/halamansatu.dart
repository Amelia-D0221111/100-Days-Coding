import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class HalamanSatu extends StatelessWidget {
  const HalamanSatu({
    super.key,
  });

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

    Future addToFavorite(String id, bool value) async {
      await dbRef.doc(id).update({"favorite": !value});
    }

    return Container(
      color: const Color.fromARGB(255, 212, 117, 149),
      child: Container(
        decoration: const BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(30),
            topRight: Radius.circular(30),
          ),
        ),
        child: ClipRRect(
          borderRadius: const BorderRadius.only(
            topLeft: Radius.circular(30),
            topRight: Radius.circular(30),
          ),
          child: StreamBuilder(
              stream: read(),
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const CircularProgressIndicator();
                }
                return snapshot.data!.isEmpty
                    ? const Text("Tidak ada data")
                    : GridView.count(
                        padding: const EdgeInsets.all(15.0),
                        crossAxisCount: 2,
                        children: List.generate(
                          snapshot.data!.length,
                          (index) {
                            return Container(
                              margin: const EdgeInsets.all(8.0),
                              height: 50,
                              width: 50,
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(30.0),
                                color: Colors.grey,
                                image: DecorationImage(
                                    image: NetworkImage(
                                      snapshot.data![index]["url"],
                                    ),
                                    fit: BoxFit.cover),
                              ),
                              child: Align(
                                alignment: Alignment.bottomRight,
                                child: IconButton(
                                  onPressed: () async {
                                    await addToFavorite(
                                        snapshot.data![index]["key"],
                                        snapshot.data![index]["favorite"]);
                                  },
                                  icon: Icon(
                                    snapshot.data![index]["favorite"]
                                        ? Icons.favorite
                                        : Icons.favorite_outline,
                                    color: snapshot.data![index]["favorite"]
                                        ? Colors.pink
                                        : Colors.grey,
                                  ),
                                ),
                              ),
                            );
                          },
                        ),
                      );
              }),
        ),
      ),
    );
  }
}
