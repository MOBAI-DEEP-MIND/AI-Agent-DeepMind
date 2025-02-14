import 'dart:developer';

import 'package:dio/dio.dart';

import '../../../../core/error/exception.dart';
import '../../domain/entity/message.dart';

abstract interface class AsisstantRemoteDataSource {
  Future<Message> sendMessage({required Message message});
}

class AsisstantRemoteDataSourceImplementation
    implements AsisstantRemoteDataSource {
  final Dio dio;

  AsisstantRemoteDataSourceImplementation({required this.dio});

  @override
  Future<Message> sendMessage({required Message message}) async {
    try {
      log('message: ${message.content} sender id ${message.senderId} ');
      // final response = await dio.post(
      //   '',
      //   data: {'query': message.content, 'senderId': message.senderId},
      // );
      await Future.delayed(const Duration(seconds: 2));
      return message.copyWith(senderId: "18");
    } on DioException catch (e) {
      throw ServerException(e.message!);
    } catch (e) {
      throw ServerException('Failed to send message');
    }
  }
}
