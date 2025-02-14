import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../../core/common/widgets/loader.dart';
import '../../../../core/utils/snack_bar.dart';
import '../bloc/book_bloc.dart';
import '../widgets/book_collections.dart';
import '../widgets/categries_list.dart';
import '../widgets/custom_app_bar.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  @override
  void initState() {
    context.read<BookBloc>().add(FetchBooks());
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.black,
        onPressed: () {},
        child: const Icon(
          CupertinoIcons.conversation_bubble,
          color: Colors.white,
        ),
      ),
      // AppBar(
      //   actions: [
      //     IconButton(
      //       icon: Icon(CupertinoIcons.shopping_cart),
      //       onPressed: () {},
      //     ),
      //   ],
      // ),
      body: BlocConsumer<BookBloc, BookState>(
        listener: (context, state) {
          if (state is FetchBooksfailure) {
            return showSnackBar(context, state.errMessage);
          }
        },
        builder: (context, state) {
          if (state is BookLoading) {
            return Loader();
          } else if (state is FetchBooksSuccess) {
            return SafeArea(
              child: Padding(
                padding: const EdgeInsets.symmetric(
                  horizontal: 16.0,
                  vertical: 8.0,
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    CustomAppBar(),
                    SizedBox(height: 10),
                    const Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Welcome ibaa ',
                          style: TextStyle(
                            fontWeight: FontWeight.w700,
                            fontSize: 25,
                          ),
                        ),
                        Text('books way to learn and read '),
                        SizedBox(height: 10),
                      ],
                    ),

                    CategoriesList(selectedTopics: []),
                    Expanded(
                      child: ListView(
                        children: [
                          const SizedBox(height: 6),
                          BookCollections(
                            collectionName: 'Recommended',
                            books: state.books,
                          ),

                          const SizedBox(height: 6),
                          BookCollections(
                            collectionName: 'Favourites',
                            books: state.books,
                          ),

                          const SizedBox(height: 6),
                          BookCollections(
                            collectionName: 'Others',
                            books: state.books,
                          ),
                          // Add more sections here if needed
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            );
          }
          return Center(child: Text('Something went wrong'));
        },
      ),
    );
  }
}
