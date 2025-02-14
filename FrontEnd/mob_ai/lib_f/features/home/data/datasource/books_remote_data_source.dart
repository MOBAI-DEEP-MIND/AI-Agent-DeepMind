import 'dart:developer';

import 'package:dio/dio.dart';

import '../../../../core/error/exception.dart';
import '../../../../core/secrets/app_secrets.dart';
import '../../domain/entities/book.dart';

abstract interface class BooksRemoteDataSource {
  Future<List<Book>> fetchBooks();
}

class BooksRemoteDataSourceImplementation implements BooksRemoteDataSource {
  final Dio dio;

  BooksRemoteDataSourceImplementation(this.dio);
  @override
  Future<List<Book>> fetchBooks() async {
    try {
      log("message");
      Response response = await dio.get(
        AppSecrets.booksEndPoint,
          data: {
            'Authorization':
                'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM5NTM2MTg0LCJpYXQiOjE3Mzk1MDYxODQsImp0aSI6IjNmMDIwNWNiM2MzYTQzY2RiMjU3ZjdmYzJiZGU2ZDMxIiwidXNlcl9pZCI6NH0.eMTlnl1OaPfh74A3zZs6uVvUvrY45DgW9D1iGGeEhXI', // Add token here
          },
        
      );
      log(response.data);
      return [];
    } catch (e) {
      throw ServerException('Failed to fetch books');
    }
  }
}
