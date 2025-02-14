import 'package:dio/dio.dart';
import 'package:get_it/get_it.dart';

import 'core/common/cubits/app_user/app_user_cubit.dart';
import 'features/auth/data/datasources/auth_remote_data_source.dart';
import 'features/auth/data/repository/auth_repository_implementation.dart';
import 'features/auth/domain/repository/auth_repository.dart';
import 'features/auth/domain/usecases/user_sign_in.dart';
import 'features/auth/domain/usecases/user_sign_up.dart';
import 'features/auth/presentation/bloc/auth_bloc.dart';
import 'features/home/data/datasource/books_remote_data_source.dart';
import 'features/home/data/repository/books_repository_implementation.dart';
import 'features/home/domain/repository/books_repository.dart';
import 'features/home/domain/usecase/fetch_books.dart';
import 'features/home/presentation/bloc/book_bloc.dart';

final serviceLocator = GetIt.instance;
Future<void> initDependencies() async {
  serviceLocator.registerLazySingleton(() => Dio());
  _initAuth();
  _initBooks();
}

void _initAuth() {
  serviceLocator
    ..registerFactory<AuthRemoteDataSource>(
      () => AuthRemoteDataSourceImplementation(dio: serviceLocator<Dio>()),
    )
    ..registerFactory<AuthRepository>(
      () => AuthRepositoryImplementation(serviceLocator<AuthRemoteDataSource>()),
    )
    ..registerFactory(() => UserSignUp(serviceLocator<AuthRepository>()))
    ..registerFactory(() => UserSignIn(serviceLocator<AuthRepository>()))
    ..registerFactory(() => AppUserCubit())
    // ..registerFactory(() => CurrentUser(serviceLocator()))
    ..registerLazySingleton(
      () => AuthBloc(
        userSignUp: serviceLocator<UserSignUp>(),
        userSignIn: serviceLocator<UserSignIn>(),
        appUserCubit: serviceLocator<AppUserCubit>(),
      ),
    );
}

void _initBooks() {
  serviceLocator
    ..registerFactory<BooksRemoteDataSource>(
      () => BooksRemoteDataSourceImplementation(
         serviceLocator<Dio>(),
      ),
    )
    ..registerFactory<BooksRepository>(
      () => BooksRepositoryImplementation(
        serviceLocator<BooksRemoteDataSource>(),
      ),
    )
    ..registerFactory(
      () => FetchBooksUseCase(serviceLocator<BooksRepository>()),
    )
    ..registerLazySingleton<BookBloc>(
      () => BookBloc(fetchBooks: serviceLocator<FetchBooksUseCase>()),
    );
}
