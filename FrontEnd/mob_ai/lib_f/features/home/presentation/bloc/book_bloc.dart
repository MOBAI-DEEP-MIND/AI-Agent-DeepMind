import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../../../core/usecase/use_case.dart';
import '../../domain/entities/book.dart';
import '../../domain/usecase/fetch_books.dart';

part 'book_event.dart';
part 'book_state.dart';

class BookBloc extends Bloc<BookEvent, BookState> {
  final FetchBooksUseCase _fetchBooks;
  BookBloc({required FetchBooksUseCase fetchBooks})
    : _fetchBooks = fetchBooks,
      super(BookInitial()) {
    on<BookEvent>((event, emit) {
      emit(BookLoading());
    });
    on<FetchBooks>((event, emit) async {
      final response = await _fetchBooks(NoParams());
      response.fold(
        (failure) {
          emit(FetchBooksfailure(errMessage: failure.errMessage));
        },
        (books) {
          emit(FetchBooksSuccess(books: books));
        },
      );
    });
  }
}
