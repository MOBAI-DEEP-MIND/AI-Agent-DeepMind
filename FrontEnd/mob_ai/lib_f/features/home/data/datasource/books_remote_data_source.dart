import 'package:dio/dio.dart';

import '../../../../core/error/exception.dart';
import '../../domain/entities/book.dart';
import '../models/book_model.dart';

abstract interface class BooksRemoteDataSource {
  Future<List<Book>> fetchBooks();
}
class BooksRemoteDataSourceImplementation implements BooksRemoteDataSource {
  final Dio dio;

  BooksRemoteDataSourceImplementation(this.dio);
  @override
  Future<List<Book>> fetchBooks() {
    try{
      return Future.value([
        BookModel(id: 1, title: 'Book 1', author: 'Author 1',url: '', description: ''),
        BookModel(id: 2, title: 'Book 2', author: 'Author 2', url: '', description: ''),
        BookModel(id: 3, title: 'Book 3', author: 'Author 3',url:'', description: ''),
      ]);
    }catch (e){
      throw ServerException('Failed to fetch books');
    }
  }
}