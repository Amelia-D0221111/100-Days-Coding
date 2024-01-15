import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class HalamanTiga extends StatelessWidget {
  const HalamanTiga({
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
        height: double.infinity,
        width: double.infinity,
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

              final data = snapshot.data!
                  .where((element) => element["favorite"])
                  .toList();

              return data.isEmpty // isEmpty == ApakahKosong
                  ? Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.heart_broken,
                            size: 100,
                          ),
                          const Text(
                            "Tidak ada Favorit",
                            style: TextStyle(fontWeight: FontWeight.w600),
                          ),
                        ],
                      ),
                    )
                  : GridView.count(
                      padding: const EdgeInsets.all(15.0),
                      crossAxisCount: 2,
                      children: List.generate(
                        data.length,
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
                                    data[index]["url"],
                                  ),
                                  fit: BoxFit.cover),
                            ),
                            child: Align(
                              alignment: Alignment.bottomRight,
                              child: IconButton(
                                onPressed: () async {
                                  await addToFavorite(
                                    data[index]["key"],
                                    data[index]["favorite"],
                                  );
                                },
                                icon: Icon(
                                  data[index]["favorite"]
                                      ? Icons.favorite
                                      : Icons.favorite_outline,
                                  color: data[index]["favorite"]
                                      ? Colors.pink
                                      : Colors.grey,
                                ),
                              ),
                            ),
                          );
                        },
                      ),
                    );
            },
          ),
        ),
      ),
    );
  }
}
