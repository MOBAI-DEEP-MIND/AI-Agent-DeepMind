import 'package:fpdart/src/either.dart';

import '../../../../core/error/failure.dart';
import '../../domain/entity/message.dart';
import '../../domain/repository/assistant_repository.dart';
import '../datasources/asisstant_remote_data_source.dart';

class AssistantRepositoryImplementation implements AssistantRepository {
  final AsisstantRemoteDataSource asisstantRemoteDataSource;
  AssistantRepositoryImplementation({required this.asisstantRemoteDataSource });
  @override
  Future<Either<Failure, Message>> sendMessage({
    required Message message,
  }) async {
    try {
      final response = await asisstantRemoteDataSource.sendMessage(
        message: message,
      );
      return Right(response);
    } catch (e) {
      return Left(Failure(e.toString()));
    }
  }
}
