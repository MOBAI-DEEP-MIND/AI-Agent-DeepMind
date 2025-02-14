part of 'book_bloc.dart';

@immutable
sealed class BookState {}

final class BookInitial extends BookState {}

final class BookLoading extends BookState {}

final class FetchBooksSuccess extends BookState {
  final List<Book> books;
  FetchBooksSuccess({required this.books});
}

final class FetchBooksfailure extends BookState {
  final String errMessage;
  FetchBooksfailure({required this.errMessage});
}

