part of 'book_bloc.dart';

@immutable
sealed class BookEvent {}

class FetchBooks extends BookEvent {}
