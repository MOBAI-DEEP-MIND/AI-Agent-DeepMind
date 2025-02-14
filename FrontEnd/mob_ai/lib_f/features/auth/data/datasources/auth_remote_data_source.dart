import 'dart:convert';
import 'dart:developer';

import 'package:dio/dio.dart';

import '../../../../core/common/entities/user.dart';
import '../../../../core/error/exception.dart';
import '../../../../core/secrets/app_secrets.dart';
import '../models/user_model.dart';

abstract interface class AuthRemoteDataSource {
  Future<User> signUpWithEmailAndPassword({
    required String username,
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
        '${AppSecrets.baseUrl}/login/',
       data: {'email': email, 'password': password},
      );

      log(': ${response.data}');
      return UserModel.fromJson(response.data);
    } catch (e) {
      throw ServerException(e.toString());
    }
  }

  @override
  Future<User> signUpWithEmailAndPassword({
    required String username,
    required String email,
    required String password,
  }) async {
    try {
      log('name: $username, email: $email, password: $password');
      final response = await dio.post(
        AppSecrets.signUpEndpoint,
        data: {
          "email": email,
          "username": username,
          "password": password,
        },
      );
      return UserModel.fromJson(response.data);
    } on DioException catch (e) {
      log(e.message!);
      throw ServerException(e.message!);
    } catch (e) {
      throw ServerException(e.toString());
    }
  }
}
