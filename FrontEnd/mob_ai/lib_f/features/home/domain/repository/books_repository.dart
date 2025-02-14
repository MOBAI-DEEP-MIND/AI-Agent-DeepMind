import 'package:fpdart/fpdart.dart';

import '../../../../core/error/failure.dart';
import '../entities/book.dart';

abstract interface  class BooksRepository {
  Future<Either<Failure, List<Book>>> fetchBooks();
}