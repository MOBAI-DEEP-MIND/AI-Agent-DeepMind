import 'dart:convert';
import 'dart:developer';

import 'package:dio/dio.dart';

import '../../../../core/common/entities/user.dart';
import '../../../../core/error/exception.dart';
import '../models/user_model.dart';

abstract interface class AuthRemoteDataSource {
  Future<User> signUpWithEmailAndPassword({
    required String name,
    required String email,
    required String password,
  });
  Future<User> signInWithEmailAndPassword({
    required String email,
    required String password,
  });
  // Future<UserModel?> getCurrentUserData();
}

class AuthRemoteDataSourceImplementation implements AuthRemoteDataSource {
  final Dio dio;
  AuthRemoteDataSourceImplementation({required this.dio});
  @override
  @override
  Future<User> signInWithEmailAndPassword({
    required String email,
    required String password,
  }) async {
    try {
      log('email: $email, password: $password');
      final response = await dio.post(
        'http://localhost:8000/app/v1/sign_in',
        queryParameters: {'email': email, 'password': password},
      );

      return UserModel.fromJson(response.data);
    } catch (e) {
      throw ServerException(e.toString());
    }
  }

  @override
  Future<User> signUpWithEmailAndPassword({
    required String name,
    required String email,
    required String password,
  }) async {
    try {
      log('name: $name, email: $email, password: $password');
      final response = await dio.post(
        'http://localhost:8000/app/v1/sign_up',
        queryParameters: {'name': name, 'email': email, 'password': password},
      );

      return UserModel.fromJson(response.data);
    } catch (e) {
      throw ServerException(e.toString());
    }
  }
}
